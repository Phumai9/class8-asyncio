from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queue.put(value)
        #print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

 # entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:52:20 2023 Consumer: Running
# Wed Aug 23 14:52:20 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:20 2023 > got 0.6979160828360244
# Wed Aug 23 14:52:21 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:21 2023 > got 0.6684853453183232
# Wed Aug 23 14:52:21 2023 > got 0.04171156022336764
# Wed Aug 23 14:52:21 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:22 2023 > got 0.7359489422411067
# Wed Aug 23 14:52:22 2023 > got 0.06297639366321761
# Wed Aug 23 14:52:22 2023 Consumer: gave up waiting...
# Wed Aug 23 14:52:23 2023 > got 0.8385736767680743
# Wed Aug 23 14:52:23 2023 > got 0.4762368878335991
# Wed Aug 23 14:52:23 2023 > got 0.10472784708506533
# Wed Aug 23 14:52:24 2023 > got 0.4361227353267213
# Wed Aug 23 14:52:24 2023 Producer: Done
# Wed Aug 23 14:52:24 2023 > got 0.047314279375334056
