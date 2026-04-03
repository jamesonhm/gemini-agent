import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        tgtpath = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_tgt_dir = os.path.commonpath([working_dir_abs, tgtpath]) == working_dir_abs
    except OSError as e:
        return f'Error: OSError "{str(e)}"'
    if not os.path.isdir(tgtpath):
        return f'Error: "{directory}" is not a directory'
    if not valid_tgt_dir:
        return f'Error: Cannot list "{directory}" as it outside the permitted working directory'
    
    items = os.listdir(tgtpath)
    contents = ''
    try:
        for i in items:
            item_path = os.path.join(tgtpath, i)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            contents += f'- {i}: file_size={size} bytes, is_dir={is_dir}\n'
        return contents
    except OSError as e:
        return f'Error: OSError "{str(e)}"'
    
