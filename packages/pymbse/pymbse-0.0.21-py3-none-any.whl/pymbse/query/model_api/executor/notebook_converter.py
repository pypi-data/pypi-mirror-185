import os

import nbformat  # type: ignore
from nbconvert import HTMLExporter  # type: ignore

import pymbse.commons.json_file as json_file  # type: ignore
import pymbse.commons.text_file as text_file  # type: ignore

IMPORT_KEYWORD = "import"
FROM_KEYWORD = "from"
PARAMETERS_KEYWORD = "parameters"
TAGS_KEYWORD = "tags"
METADATA_CELL_KEYWORD = "metadata"
SB_GLUE_OUTPUT_KEYWORD = "sb.glue"
SOURCE_CELL_KEYWORD = "source"
CODE_KEYWORD = "code"
CELLS_KEYWORD = "cells"
CELL_TYPE_KEYWORD = "cell_type"


def convert_ipynb_to_html(ipynb_abs_path: str, html_abs_path: str) -> None:
    """Function converting an ipynb file executed with papermill (containing the outputs) to an html file

    :param ipynb_abs_path: an absolute path to an ipynb output notebook
    :param html_abs_path: an absolute path to an html report
    """
    with open(ipynb_abs_path) as f:
        nb = nbformat.read(f, as_version=4)

    config = {
        "TemplateExporter": {"exclude_input": True},
        "TagRemovePreprocessor": {"remove_all_outputs_tags": ["skip_output"]},
    }
    html_exporter = HTMLExporter(config)
    body, _ = html_exporter.from_notebook_node(nb)
    decoded_body = body.encode("ascii", "ignore").decode()
    with open(html_abs_path, "w") as f:
        f.write(decoded_body)


def create_script_if_missing_or_outdated(
    notebook_abs_path: str, script_abs_path: str, model_name_without_ext: str
) -> None:
    """Function creating a script from a notebook if the script is either missing or outdated (notebook was updated
    after the script creation).

    :param notebook_abs_path: an absolute path to the model notebook
    :param script_abs_path: an absolute path to the script
    :param model_name_without_ext: name of a model without an extension
    """
    if is_script_missing_or_outdated(notebook_abs_path, script_abs_path):
        convert_notebook_to_script(
            notebook_abs_path, model_name_without_ext, script_abs_path
        )


def is_script_missing_or_outdated(notebook_abs_path: str, script_abs_path: str) -> bool:
    """Function checking whether a script is either missing or outdated

    :param notebook_abs_path: an absolute path to a model notebook
    :param script_abs_path: an absolute path to a script created from model notebook
    :return: True if script is either missing or outdated, otherwise True
    """
    if is_script_missing(script_abs_path):
        return True
    elif is_script_outdated(notebook_abs_path, script_abs_path):
        os.remove(script_abs_path)
        return True
    else:
        return False


def is_script_missing(script_abs_path: str) -> bool:
    """Function checking whether a script is missing

    :param script_abs_path: an absolute path to a script created from model notebook
    :return: True if a script is missing, otherwise False
    """
    return not os.path.isfile(script_abs_path)


def is_script_outdated(notebook_abs_path: str, script_abs_path: str) -> bool:
    """Function checking whether a script is outdated w.r.t. a notebook.
    This happens if the model last modification time is greater or equal to the one of a notebook.
    The equality of the modification time may occur if an outdated script and the model were moved at the same time.
    e.g., while cloning a repository containing mis-synchronized model and script, or copying the two.
    It is assumed that the copying should happen in less then a second. Thus the comparison is carried out on integer
    modification times.

    :param notebook_abs_path: an absolute path to a model notebook
    :param script_abs_path: an absolute path to a script created from model notebook
    :return: True if script is outdated, otherwise False
    """
    model_last_modification_time = os.path.getmtime(notebook_abs_path)
    script_last_modification_time = os.path.getmtime(script_abs_path)

    return int(model_last_modification_time) >= int(script_last_modification_time)


def convert_notebook_to_script(
    notebook_abs_path: str, notebook_name: str, script_abs_path: str
) -> None:
    """Function converting a notebook into a script equivalent. The notebook is executed as a function.
    The function name is given by as run_<notebook_name>. The input arguments are taken from cells with `parameters`
    tags. The return value is taken from the sb.glue code.

    :param notebook_abs_path: an absolute path to a model notebook
    :param notebook_name: name of a notebook without extension
    :param script_abs_path: an absolute path to a script created from model notebook
    """
    # Parse notebook
    notebook = json_file.read(notebook_abs_path)
    cells_with_parameters, cells_with_code = separate_parameters_and_code_cells(
        notebook
    )
    parameter_lines = extract_parameter_lines(cells_with_parameters)
    code_lines = extract_code_lines(cells_with_code)
    output_variable = extract_output_variable(cells_with_code)
    cleaned_code_lines = remove_ipython_magic_and_sys_path_apppend(code_lines)

    # Construct script
    function_parameters = ", ".join(parameter_lines)
    output_lines = []
    output_lines.append("\n")
    output_lines.append("def run_%s_script(%s):" % (notebook_name, function_parameters))

    for cleaned_code_line in cleaned_code_lines:
        output_lines.append("\t" + cleaned_code_line)

    output_lines.append("\t" + "return " + output_variable)

    text_file.writelines(script_abs_path, output_lines)


def separate_parameters_and_code_cells(notebook: dict) -> tuple:
    """Function separating cells with parameters from those with code

    :param notebook: a dictionary witho notebook contents
    :return: a two-element tuple containing a list of cells with parameters and list of cells with code
    """
    cells_with_all_code = [
        cell
        for cell in notebook[CELLS_KEYWORD]
        if cell[CELL_TYPE_KEYWORD] == CODE_KEYWORD
    ]
    cells_with_parameters = []
    cells_with_code = []

    for cell in cells_with_all_code:
        if TAGS_KEYWORD in cell[METADATA_CELL_KEYWORD] and (
            PARAMETERS_KEYWORD in cell[METADATA_CELL_KEYWORD][TAGS_KEYWORD]
        ):
            cells_with_parameters.append(cell)
        else:
            cells_with_code.append(cell)

    return cells_with_parameters, cells_with_code


def extract_parameter_lines(cells_with_parameters: list) -> list:
    """Function extracting parameter lines from a list of cells with parameters. In case there is a comment in a
    parameter line, an AttributeError is raised.

    :param cells_with_parameters: a list of cells with parameters
    :return: a list of lines with parameters
    """

    # extract parameter code lines
    param_code_lines = []
    for cell in cells_with_parameters:
        for line in cell[SOURCE_CELL_KEYWORD]:
            param_code_lines.append(line.replace("\n", ""))

    # remove comments
    param_code_lines = _remove_comments_from_lines(param_code_lines)

    # strip trailing whitespace characters
    param_code_lines = [param_code_line.strip() for param_code_line in param_code_lines]

    # remove empty code lines
    param_code_lines = [
        param_code_line
        for param_code_line in param_code_lines
        if param_code_line.strip()
    ]

    return param_code_lines


def _remove_comments_from_lines(code_lines: list[str]) -> list[str]:
    return [_remove_comment(code_line) for code_line in code_lines]


def _remove_comment(code_line):
    if "#" in code_line:
        comment_to_remove = code_line[code_line.index("#") :]
        return code_line.replace(comment_to_remove, "")
    else:
        return code_line


def extract_code_lines(cells_with_code: list) -> list:
    """Function extracting code lines from lines with code

    :param cells_with_code: a list of cells with code
    :return: a list of code lines
    """
    code_lines = []
    for cell in cells_with_code:
        for line in cell[SOURCE_CELL_KEYWORD]:
            if SB_GLUE_OUTPUT_KEYWORD not in line:
                code_lines.append(line.replace("\n", ""))
    return code_lines


def extract_output_variable(cells_with_code: list) -> str:
    """Function extracting an output variable name from cells with code

    :param cells_with_code: a list of cells with code
    :return: an output variable name
    """
    output_line = ""
    for cell in cells_with_code:
        for line in cell[SOURCE_CELL_KEYWORD]:
            if SB_GLUE_OUTPUT_KEYWORD in line:
                output_line = line

    output_variable = output_line.split(",")[1]
    if "=" in output_variable:
        output_variable = output_variable.split("=")[-1]

    return output_variable


def remove_ipython_magic_and_sys_path_apppend(code_lines: list) -> list:
    """Function separating code lines into those with import statements and those with remaining code

    :param code_lines: a list of code lines for separation
    :return: a two-element tuple containing a list of import lines and a list of remaining code lines
    """
    cleaned_code_lines = []

    for code_line in code_lines:
        if not (code_line.startswith("%") or ("sys.path.append" in code_line)):
            cleaned_code_lines.append(code_line)

    return cleaned_code_lines
