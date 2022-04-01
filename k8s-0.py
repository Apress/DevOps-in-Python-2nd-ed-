from kubernetes import config as k8config

client = k8config.new_client_from_config()
