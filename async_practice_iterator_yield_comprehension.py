import asyncio
import time 


async def powers_of_two(stop=10):
    exponent = 0
    while exponent < stop:
        yield 2**exponent
        exponent += 1
        await asyncio.sleep(0.2)  # Simulate some asynchronous work

async def main():
    g = []
    print("generator based")
    async for i in powers_of_two(5):
        g.append(i)
    print(g)
    f = [j async for j in powers_of_two(5) if not (j // 3 % 5)]
    print(f)


start = time.perf_counter()


asyncio.run(main())
[1, 2, 4, 8, 16]
[1, 2, 16]

end = time.perf_counter()
print(f"\n==> Total time: {end - start:.2f} seconds")

#  -----------------------------------------------------


async def powers_of_two_list(stop=10):
    total_list = []
    exponent = 0
    while exponent < stop:
        total_list.append(2**exponent)
        exponent += 1
        await asyncio.sleep(0.2)  # Simulate some asynchronous work
    return total_list

async def main_list():
    g = []
    print("List based")
    for i in await powers_of_two_list(5):
        g.append(i)
    print(g)
    f = [j for j in await powers_of_two_list(5) if not (j // 3 % 5)]
    print(f)


start = time.perf_counter()


asyncio.run(main_list())
[1, 2, 4, 8, 16]
[1, 2, 16]

end = time.perf_counter()
print(f"\n==> Total time: {end - start:.2f} seconds")

#  -----------------------------------------------------


async def powers_of_two_gather(stop=10):
    exponent = 0
    while exponent < stop:
        yield 2**exponent
        exponent += 1
        await asyncio.sleep(0.2)  # Simulate some asynchronous work

async def main_gather():
    g = []
    print("generator based")
    g = await asyncio.gather(powers_of_two_list(5))

    print(g)
    f = [j async for j in powers_of_two_gather(5) if not (j // 3 % 5)]
    print(f)


start = time.perf_counter()


asyncio.run(main_gather())
[1, 2, 4, 8, 16]
[1, 2, 16]

end = time.perf_counter()
print(f"\n==> Total time: {end - start:.2f} seconds")

