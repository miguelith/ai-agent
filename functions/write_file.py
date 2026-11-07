from os import makedirs
from os.path import abspath, commonpath, dirname, isdir, join, normpath


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = abspath(working_directory)
        target_file = normpath(join(working_dir_abs, file_path))

        if commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        makedirs(dirname(target_file), exist_ok=True)

        with open(target_file, mode="w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
