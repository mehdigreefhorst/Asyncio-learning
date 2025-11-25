import asyncio
import aiohttp
import time

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")

async def main():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.python.org",
    ]
    await asyncio.gather(*(check(url) for url in websites))

async def main_simple():
    websites = [
        "https://realpython.com",
        "https://pycoders.com",
        "https://www.python.org",
    ]
    for url in websites:
        await check(url)

# Run multiple times to see the pattern
for i in range(3):
    print(f"\n--- Run {i+1} ---")
    
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Concurrent time: {end - start:.2f}s")
    
    start = time.perf_counter()
    asyncio.run(main_simple())
    end = time.perf_counter()
    print(f"Sequential time: {end - start:.2f}s")
    
    # Add a delay to let connections close
    # time.sleep(5)