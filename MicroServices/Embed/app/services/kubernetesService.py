import kubernetes
import logging
import os

from kubernetes import client
from kubernetes import config


# Global Declaration

deployment_name = os.getenv("DEPLOYMENT_NAME")
namespace_name = os.getenv("NAMESPACE_NAME")

class Kubernetes:
    def __init__(self):

        # Init Kubernetes
        self.core_api = client.CoreV1Api()
        self.batch_api = client.BatchV1Api()

    def create_namespace(self, namespace):

        namespaces = self.core_api.list_namespace()
        all_namespaces = []
        for ns in namespaces.items:
            all_namespaces.append(ns.metadata.name)

        if namespace in all_namespaces:
            logging.info(f"Namespace {namespace} already exists. Reusing the same name Space.")
        else:
            namespace_metadata = client.V1ObjectMeta(name=namespace_name)
            self.core_api.create_namespace(
                client.V1Namespace(metadata=namespace_metadata)
            )
            logging.info(f"Created  new namespace {namespace}.")

        return namespace

    @staticmethod
    def create_container(image, name, pull_policy, args, command):

        container = client.V1Container(
            env_from=[{"configMapRef": {"name": "pdfembeddings-configmap"}},
                      {"secretRef": {"name": "pdfembeddings-secrets"}}],
            image=image,
            name=name,
            image_pull_policy=pull_policy,
            args=[args],
            command=["python3", "-u", command],
        )

        return container

    @staticmethod
    def create_pod_template(pod_name, container):
        pod_template = client.V1PodTemplateSpec(
            spec=client.V1PodSpec(restart_policy="Never", containers=[container]),
            metadata=client.V1ObjectMeta(name=pod_name, labels={"pod_name": pod_name}),
        )

        return pod_template

    @staticmethod
    def create_job(job_name, pod_template):
        metadata = client.V1ObjectMeta(name=job_name, labels={"job_name": job_name})

        job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=metadata,
            spec=client.V1JobSpec(backoff_limit=0, template=pod_template),
        )

        return job

    @staticmethod
    def get_image():
        api = client.AppsV1Api()
        image_json = api.read_namespaced_deployment(deployment_name, namespace_name)
        image=image_json.spec.template.spec.containers[0].image
        return image