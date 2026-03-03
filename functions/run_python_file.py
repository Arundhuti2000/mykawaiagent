import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, target_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
             return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith('py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_path]
        if args:
            command.extend(args)
        CWD= working_directory
        CompletedProcess = subprocess.run(command,cwd=CWD, text=True,capture_output=True,timeout=30)
        
        output_parts=[]
        if CompletedProcess.returncode!=0:
            output_parts.append(f"Process exited with code X")
        if not CompletedProcess.stderr and not CompletedProcess.stdout:
            output_parts.append("No output produced")
        else:
            if CompletedProcess.stdout:
                output_parts.append(f"STDOUT: {CompletedProcess.stdout}")
            if CompletedProcess.stderr:
                output_parts.append(f"STDERR:  + {CompletedProcess.stderr}")
        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"
