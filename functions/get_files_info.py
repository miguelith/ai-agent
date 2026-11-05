from os.path import abspath, commonpath, isdir, join, normpath


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = abspath(working_directory)
        target_dir = normpath(join(working_dir_abs, directory))

        if commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"
