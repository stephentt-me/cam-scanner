import logging

import etcd

def make_heartbeat(value):
    client = etcd.Client(host="127.0.0.1", port=2379)  # XXX
    client.write("/nodes/image_processing", value, ttl=5, append=True)
    logging.debug("A heartbeat sent.")
