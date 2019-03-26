import os

from src.system.exception import ServiceUnavailable

def service_discovery(local_key, k8s_service_name=""):
    if os.getenv("KUBERNETES_SERVICE_HOST"):
        return f"{k8s_service_name}.default.svc.cluster.local"  # XXX
    elif os.getenv(local_key):
        return os.getenv(local_key)
    raise ServiceUnavailable
