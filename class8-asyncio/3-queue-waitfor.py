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

#Wed Aug 23 14:52:20 2023 Consumer: Running
#Wed Aug 23 14:52:20 2023 Consumer: gave up waiting...
#Wed Aug 23 14:52:20 2023 > got 0.6979160828360244
#Wed Aug 23 14:52:21 2023 Consumer: gave up waiting...
#Wed Aug 23 14:52:21 2023 > got 0.6684853453183232
#Wed Aug 23 14:52:21 2023 > got 0.04171156022336764
#Wed Aug 23 14:52:21 2023 Consumer: gave up waiting...
#Wed Aug 23 14:52:22 2023 > got 0.7359489422411067
#Wed Aug 23 14:52:22 2023 > got 0.06297639366321761
#Wed Aug 23 14:52:22 2023 Consumer: gave up waiting...
#Wed Aug 23 14:52:23 2023 > got 0.8385736767680743
#Wed Aug 23 14:52:23 2023 > got 0.4762368878335991
#Wed Aug 23 14:52:23 2023 > got 0.10472784708506533
#Wed Aug 23 14:52:24 2023 > got 0.4361227353267213
#Wed Aug 23 14:52:24 2023 Producer: Done
#Wed Aug 23 14:52:24 2023 > got 0.047314279375334056
