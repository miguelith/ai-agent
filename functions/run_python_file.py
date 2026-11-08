from os.path import abspath, commonpath, isfile, join, normpath
from subprocess import run

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File to overwrite, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Extra CLI flags",
                },
            },
        },
        "required": ["file_path"],
    },
}


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = abspath(working_directory)
        target_file = normpath(join(working_dir_abs, file_path))

        if commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", target_file]

        if args:
            command.extend(args)

        completed_process = run(
            command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30
        )
        output = []
        process_output = completed_process.stdout
        process_error = completed_process.stderr
        process_returncode = completed_process.returncode

        if process_returncode != 0:
            output.append(f"Process exited with code {process_returncode}")

        if not process_output and not process_error:
            output.append("No output produced")

        if process_output:
            output.append(f"STDOUT: {process_output}")

        if process_error:
            output.append(f"STDERR: {process_error}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
