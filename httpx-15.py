import httpx, datetime
import asyncio

async def async_calls():
    before = datetime.datetime.now()
    async with httpx.AsyncClient() as async_client:
        fut1 = async_client.get("https://httpbin.org/delay/3?param=async-first")
        fut2 = async_client.get("https://httpbin.org/delay/3?param=async-second")
        responses = await asyncio.gather(fut1, fut2)
        delta = datetime.datetime.now() - before
    r1, r2 = responses
    results1 = r1.json()
    results2 = r2.json()
    print(delta // datetime.timedelta(seconds=1))
    print(results1["args"]["param"], results2["args"]["param"])

asyncio.run(async_calls())
