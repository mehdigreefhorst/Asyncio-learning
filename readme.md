# Asyncio running

We can run with async in helpful systems. I have until now worked frequently with async, while not properly understanding it. I only used it to not await things and just send things out when I did not want the return. 

But with asyncio you are actually creating a event loop, with multiple courantines, a function defined with async is a couratine. All courantines run on the same cpu core when using asyncio. It is not the same as multithreading. You are just working with quarantines. Which you can await other async process to make sure you are chaining them

aysncio.sleep is different from time.sleep. With time.sleep you will see that the whole thread is sleeping, so also other async operations, so never use time.sleep when you want that only a single quarantine is sleeping it will make the whole system stop. While with asyncio.sleep, only that specific quarantine is sleeping. 


### Queues
There is also a concept of queues in asyncio. It is a simple version of a queues unlike redis. With async queues, we have producers and consumers, and in between we have a queue. Producers do not know the status of the consumers and vice versa. When you create consumers who have a While True statement. Make sure to create a sentinel termination value. But you need as least the same number of sentinels (see asyncio_practice_queues.py), as you have possible running quarantine consumers. So this is very dangerous for production environments.


### Async iterators
You can also add async to other python systems. For example the iterator. You can do `async for i in range 5: print("do action")`


### Async schedule tasks
This is a super useful thing, you can create tasks to be executed, so they can be executed when there is time for it. But all you are doing is creating a new quarantine, as a block that is created as a sepeate subprocess that can be completed.
The create_task() function wraps an awaitable object into a higher-level Task object that’s scheduled to run concurrently on the event loop in the background. In contrast, awaiting a coroutine runs it immediately, pausing the execution of the caller until the awaited coroutine finishes.


### Gather

The gather() function is meant to neatly put a collection of coroutines into a single future object. This object represents a placeholder for a result that’s initially unknown but will be available at some point, typically as the result of asynchronous computations.

If you await gather() and specify multiple tasks or coroutines, then the loop will wait for all the tasks to complete. The result of gather() will be a list of the results across the inputs:


### as_completed
THis function allows to iterate over results when they come available, where the gather function waits until all tasks are done before going to the next step. As_completed goes to the next one as soon as one of the tasks is completed. So that you can already start processing the results in the meantime, e.g. process the gathered data after a network operation. The resulting order is dependent on when they complete and not when they start

### Exceptions
With the gather, you can also work with exceptions. You can gracefully handle exceptions all together. Since gather is a list when done. You can filter the exceptions of the same type as a group. Allowing you to have a clean software stack


### When to use ASYNC
Using async def for functions that perform blocking operations—such as standard file I/O or synchronous network requests—will block the entire event loop, negate the benefits of async I/O, and potentially reduce your program’s efficiency. Only use async def functions for non-blocking operations.

The battle between async I/O and multiprocessing isn’t a real battle. You can use both models in concert if you want. In practice, multiprocessing should be the right choice if you have multiple CPU-bound tasks.

The contest between async I/O and threading is more direct. Threading isn’t simple, and even in cases where threading seems easy to implement, it can still lead to hard-to-trace bugs due to race conditions and memory usage, among other things.

Threading also tends to scale less elegantly than async I/O because threads are a system resource with a finite availability. Creating thousands of threads will fail on many machines or can slow down your code. In contrast, creating thousands of async I/O tasks is completely feasible.

Async I/O shines when you have multiple I/O-bound tasks that would otherwise be dominated by blocking wait time, such as:

Network I/O, whether your program is acting as the server or the client
Serverless designs, such as a peer-to-peer, multi-user network like a group chat
Read/write operations where you want to mimic a fire-and-forget style approach without worrying about holding a lock on the resource
The biggest reason not to use async I/O is that await only supports a specific set of objects that define a particular set of methods. For example, if you want to do async read operations on a certain database management system (DBMS), then you’ll need to find a Python wrapper for that DBMS that supports the async and await syntax.