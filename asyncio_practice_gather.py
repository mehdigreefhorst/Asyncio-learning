import time
import asyncio
async def coro(numbers):
   await asyncio.sleep(min(numbers))
   return list(reversed(numbers))


async def main():
    task1 = asyncio.create_task(coro([i for i in range(1000)]))
    task2 = asyncio.create_task(coro([i for i in range(2, 10000)]))
    start = time.perf_counter()
    result = await asyncio.gather(task1, task2)
    end = time.perf_counter()
    print(f"it took {end-start} seconds")
    print(f"Both tasks done: {all((task1.done(), task2.done()))}")
    return result


result = asyncio.run(main())




#print(f"result: {result}")

