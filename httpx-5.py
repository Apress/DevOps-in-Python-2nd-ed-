import httpx
import ssl

ssl_context = ssl.create_default_context()
ssl_context.options |= ssl.OP_NO_TLSv1_3
client = httpx.Client(verify=ssl_context)
