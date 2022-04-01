____________________________ test_put_httpbin_real _____________________________

    def test_put_httpbin_real():
        with httpx.Client() as client:
            value = put_httpbin(client)
>       assert value == 4
E       assert 3 == 4

httpbin_httpx.py:36: AssertionError
----------------------------- Captured stdout call -----------------------------
debug {'args': {}, 'data': '{"a": 1, "b": 2}', ...
