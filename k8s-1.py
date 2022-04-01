from kubernetes import client as k8client, config as k8config

client = k8config.new_client_from_config()
core = k8client.CoreV1Api(client)
