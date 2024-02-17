from typing import List
import uuid, os
import logging
def save_files_on_disk(user_id: str, tenant_id:str, files: List):
    try:
        FOLDER_BASE = os.getenv("FOLDER_BASE", "") if os.getenv("FOLDER_BASE", "") else "/"
        print("FOLDER_BASE",FOLDER_BASE)
        file_list = []
        # If Folder not present then Create one


        for file in files:
            gen_file_id = uuid.uuid4()
            gen_file_name = f"{str(gen_file_id)}_{file.filename}"
            abs_file_path = f"{FOLDER_BASE}/{str(user_id)}/{str(tenant_id)}/"
            if not os.path.exists(abs_file_path):
                os.makedirs(abs_file_path)
            final_file_abs_file_path = f"{abs_file_path }{gen_file_name}"
            with open(final_file_abs_file_path, 'wb') as file_obj:
                file_obj.write(file.file.read())
                file_list.append(final_file_abs_file_path)
        
        return file_list

    except IOError as Err:
        logging.error("====IOError Error while Saving the files on Disk====" + str(Err))
        raise Err
    
    except Exception as Err:
        logging.error("====Error while Saving the files on Disk====" + str(Err))
        raise Err






