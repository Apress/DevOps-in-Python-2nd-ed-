import contextlib, paramiko, sys

with contextlib.context(paramiko.SSHClient()) as client:
    client.connect(sys.argv[1])
    ## Do things with client
