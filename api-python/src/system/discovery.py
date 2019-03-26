import logging
import os

from src.system.exception import ServiceUnavailable

def service_discovery(local_key, k8s_service_name="", k8s_service_port=""):
    if os.getenv("KUBERNETES_SERVICE_HOST"):
        domain_name = f"{k8s_service_name}.default.svc.cluster.local:{k8s_service_port}"  # XXX
        logging.info("Call external " + domain_name)
        return domain_name
    elif os.getenv(local_key):
        return os.getenv(local_key)
    raise ServiceUnavailable
