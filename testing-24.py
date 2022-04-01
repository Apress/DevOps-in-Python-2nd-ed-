def test_put_httpbin_fake():
    with httpx.Client(app=make_app()) as client:
        value = put_httpbin(client)
    assert value == 4
