class MyAuth(httpx.Auth):

     def auth_flow(self, request: httpx.Request):
        ....
