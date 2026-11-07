from os import listdir
from os.path import abspath, commonpath, getsize, isdir, join, normpath

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = abspath(working_directory)
        target_dir = normpath(join(working_dir_abs, directory))

        if commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        contents = [
            f"- {content}: file_size={getsize(join(target_dir, content))} bytes, is_dir={isdir(join(target_dir, content))}"
            for content in listdir(target_dir)
        ]

        return "\n".join(contents)

    except Exception as e:
        return f"Error: {e}"
