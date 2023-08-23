from random import random
import asyncio 
import time

# coroutine to generate work
async def producer(queqe):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
    # send an all done signal
    await queqe.put(None)
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queqe):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queqe.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waitting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
    # report
    print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queqe
    queqe = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queqe), consumer(queqe))

# start the asyncio program
asyncio.run(main())

#Wed Aug 23 14:51:32 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:33 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:33 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:34 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:34 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:35 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:35 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:36 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:36 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:37 2023 Consumer: got nothing, waitting a while...
#Wed Aug 23 14:51:37 2023 Producer: Done
#Wed Aug 23 14:51:37 2023 >got None
#Wed Aug 23 14:51:37 2023 Consumer: Done
