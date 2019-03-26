import os

from src.system.exception import ServiceUnavailable

def service_discovery(local_key, k8s_service_name=""):
    k8s_value_host = os.getenv(k8s_service_name.upper() + "_SERVICE_HOST")
    k8s_value_port = os.getenv(k8s_service_name.upper() + "_SERVICE_PORT")
    
    if k8s_value_host:
        return k8s_value_host + ":" + k8s_value_port

    local_value = os.getenv(local_key)
    if local_value:
        return local_value
    raise ServiceUnavailable
