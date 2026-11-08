from os.path import abspath, commonpath, isfile, join, normpath

from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gets the content of a file in a specified directory relative to the working directory. It truncates files that have more than 10,000 characters.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File to get contents from, relative to the working directory",
                },
            },
        },
        "required": ["file_path"],
    },
}


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
