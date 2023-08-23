import asyncio
import time
from random import random

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue  
        await queue.put(value)  
    # send an all done signal
    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # Check for stop
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())