____________________________ test_put_httpbin_fake _____________________________

    def test_put_httpbin_fake():
        with httpx.Client(app=make_app()) as client:
            value = put_httpbin(client)
>       assert value == 4
E       assert 3 == 4

httpbin_httpx.py:30: AssertionError
----------------------------- Captured stdout call -----------------------------
debug {'data': '{"a": 1, "b": 2}'}
