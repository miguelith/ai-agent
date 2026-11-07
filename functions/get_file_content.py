from os.path import abspath, commonpath, isfile, join, normpath

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = abspath(working_directory)
        target_file = normpath(join(working_dir_abs, file_path))

        if commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working file_path'

        if not isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file) as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

            return file_content_string

    except Exception as e:
        return f"Error: {e}"
