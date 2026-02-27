import os

def get_files_info(working_directory, directory="."):
    working_dir_abs=os.path.abspath(working_directory)
    target_dir=os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}"'
    try:
        listoftargetdiritems=os.listdir(target_dir)
        listofitemdetails = []
        for item in listoftargetdiritems:
            item_path = os.path.join(target_dir, item)
            is_dir= os.path.isdir(item_path)
            file_size= os.path.getsize(item_path)
            full_line = f'- {item}: file_size={file_size} bytes, is_dir={is_dir}\n'
            listofitemdetails.append(full_line)
        return "".join(listofitemdetails)
    except Exception as e:
        return (f'"Error: {e}"')