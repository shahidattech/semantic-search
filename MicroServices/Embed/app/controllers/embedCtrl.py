from fastapi.responses import JSONResponse
from fastapi import UploadFile, File, Depends, status
from typing import List
from pydantic import Field
from sqlalchemy.orm import Session
import app.validator.skill as skill_validator
import app.services.dbService as dbService
from app.responses.response_model import create_skill_resp
from app.utils.utility import save_files_on_disk
import logging
import os


def create_embedding(db:Session, topic_name: str, files: List[UploadFile] = File()):
    try:
        created_by = 1 # to be resolved from Auth Token
        tenant_id = 1 # to be resolved from Auth Token
        if topic_name:
            logging.info("===Skill Name===", topic_name)
            if dbService.isTopicExistsByName(topic_name.strip(), db):
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                    content="Skill Name already Exists in our Records, Pelase Choose a Different Skill")
         
        if not files:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                    content="Atleast one file is rerquired to be supplied to create knowledgebase")

        # Save Files on Disk Temporarily--> To be Replaced with S3 
        # This is going to use Kubernetes POD storage temporarily
        file_lists = save_files_on_disk(created_by, tenant_id, files)
        # Keep track of the files beings used by the embedding uniquely for further modification
        embedding_id = dbService.create_embedding(topic_name, ",".join(file_lists), created_by, tenant_id, db)
        print(",".join(file_lists))

        # # Trigger Kubernetes Batch JOB for Extraction
        # command = os.getenv("COMMAND_PDF_EMBEDDING", "")
        # triggerKuberNetesBatch(tenant_id, created_by, skill_id, command, file_lists)
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=create_skill_resp(
                                skill_id= embedding_id,
                                message="Embedding Created Successfully, Embedding process is in progress, We will notofy once completed"
                            ))

    # Upload Files using Kubernetes Batch 1
    # Embed file using Kubernetes Batch 2
    except Exception as Err:
        print("Errr=", Err)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# def triggerKuberNetesBatch(tenant_id:str, created_by:str, skill_id: int, command, file_lists):
#     try:
#         kuber_object = custom_kuber.Kubernetes()
#         image = kuber_object.get_image()
#         container_name = os.getenv("EMBED_CONTAINER_NAME")
#         pull_policy = os.getenv("KUBERNETI_PULL_POLICY")
#         job_id = str(skill_id)
#         pod_id = job_id
#         pod_name = f"{container_name}-pod-{pod_id}"
#         job_name = f"{container_name}-job-{job_id}"
#         namespace = os.getenv("NAMESPACE")
#         script_path = os.getenv("SCRIPT_PATH")
#         args = {
#             'tenant_id':tenant_id,
#             'user_id': created_by,
#             'skill_id': skill_id,
#             'file_lists': file_lists
#         }
#         container = kuber_object.create_container(image, container_name, pull_policy, args, script_path)
#         pod_template = kuber_object.create_pod_template(pod_name, container)
#         job = kuber_object.create_job(job_name, pod_template)
#         api_instance= kubernetes.client.BatchV1Api()
#         api_instance.create_namespaced_job(body=job,namespace=namespace)
#         return True
#     except Exception as Err:
#         logging.error("===Error in triggerKuberNetesBatch:: " + str(Err))
#         raise Err


