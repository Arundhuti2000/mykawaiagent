import os

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot execute  "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
             return f'Error: File not found or is not a regular file: "{file_path}"'
        if not target_path.endswith('py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", ]
