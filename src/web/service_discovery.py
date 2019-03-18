import etcd

from src.web.system.exception import ServiceUnavailable


def discovery(name):
    # TODO: sort by ttl
    client = etcd.Client(host="127.0.0.1", port=2379)  # XXX
    try:
        values = []
        res = client.read(f"/nodes/{name}", recursive=True, dir=True, sorted=True)
        for item in res.children:
            values.append(item.value)
        values = [i for i in values if i is not None]
    except etcd.EtcdKeyNotFound:
        raise ServiceUnavailable
    if not values:
        raise ServiceUnavailable
    return values[0]
