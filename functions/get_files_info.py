import os


def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    if not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    try:
        tgtpath = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_tgt_dir = os.path.commonpath([working_dir_abs, tgtpath]) == working_dir_abs
    except OSError as e:
        return f'Error: OSError "{str(e)}"'
    if not valid_tgt_dir:
        return f'Error: Cannot list "{directory}" as it outside the permitted working directory'

