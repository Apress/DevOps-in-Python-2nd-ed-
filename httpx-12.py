client = httpx.Client(
    auth=AWSv4Auth(
        aws_session=botocore.session.get_session(),
        region='us-east-1',
        service='es',
    ),
)
