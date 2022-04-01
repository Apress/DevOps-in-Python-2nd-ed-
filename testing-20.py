def put_httpbin(client):
    resp = client.put("https://httpbin.org/put", json=dict(a=1, b=2))
    resp.raise_for_status()
    resp_value = resp.json()
    print("debug", resp_value)
    data = json.loads(resp_value["data"])
    return data["a"] + data["b"]
