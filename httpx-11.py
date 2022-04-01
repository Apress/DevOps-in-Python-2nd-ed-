from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

import httpx

class AWSv4Auth(httpx.Auth):
    def __init__(self, aws_session, region, service):
        self.aws_session = aws_session
        self.region = region
        self.service = service

    def sign(self, request):
        aws_request = AWSRequest(
            method=request.method.upper(),
            url=to_canonical_url(request.url),
            data=request.body,
        )
        credentials = aws_session.get_credentials()
        SigV4Auth(credentials, service, region).add_auth(request)
        request.headers.update(**aws_request.headers.items())
        yield request
