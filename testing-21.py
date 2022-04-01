def test_put_httpbin_real():
    with httpx.Client() as client:
        value = put_httpbin(client)
    assert value == 4
