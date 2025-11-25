import asyncio
import time

async def call_network(num: int):
    await asyncio.sleep(1)
    return num

async def main():
    total_cluster_units = 10 
    runs = 1
    result = await asyncio.gather(*(
        call_network(float(f"{val}.{_}")) for val in range(total_cluster_units) for _ in range(runs)
    ))
    nested_result = [result[i:runs+i] for i in range(0, total_cluster_units* runs, runs)]
    return nested_result


def start():
    
    start = time.perf_counter()
    print(asyncio.run(main()))
    end = time.perf_counter()

    print(f"total time = {end-start} seconds")


start()
