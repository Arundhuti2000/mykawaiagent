import os
import sys
from config import MAX_CHARS
# Add the project root to sys.path to allow importing config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_dir_abs, file_path))
        
        
        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
             return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
             return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, 'r') as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                 content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
            
    except Exception as e:
        return f"Error: {str(e)}"