
import asyncio
import time

from asyncio_practice_tasks import coro


async def main():
    task1 = asyncio.create_task(coro([10, 5, 2]))
    task2 = asyncio.create_task(coro([3, 2, 1]))
    start = time.perf_counter()
    for task in asyncio.as_completed([task1, task2]):
      result = await task
      end = time.perf_counter()
      print(f'result: {result} completed in {end-start} seconds')
      print(f"Both tasks done: {all((task1.done(), task2.done()))}")


asyncio.run(main())