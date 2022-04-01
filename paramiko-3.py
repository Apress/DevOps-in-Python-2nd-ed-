>>> import os
>>> with open("key.priv", "w") as fp:
...    os.chmod("key.priv", 0o600)
...    k.write_private_key(fp)
