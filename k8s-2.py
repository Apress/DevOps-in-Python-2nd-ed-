from kubernetes import client as k8client, config as k8config

client = k8config.new_client_from_config()
core = k8client.CoreV1Api(client)

res = core.list_pod_for_all_namespaces()
for pod in res.items:
    for container in pod.spec.containers:
        print(container.image)
