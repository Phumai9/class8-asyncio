# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.


from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queqe):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queqe
        await queqe.put(value)
        #print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queqe.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # check for stop signal
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

#Wed Aug 23 14:50:20 2023 Producer: Running
#Wed Aug 23 14:50:20 2023 Consumer: Running
#Wed Aug 23 14:50:21 2023 >got 0.6749485067820122
#Wed Aug 23 14:50:21 2023 >got 0.584160924671123
#Wed Aug 23 14:50:22 2023 >got 0.9565908530460696
#Wed Aug 23 14:50:23 2023 >got 0.18521223709512646
#Wed Aug 23 14:50:23 2023 >got 0.3367991038165442
#Wed Aug 23 14:50:23 2023 >got 0.37651114058578206
#Wed Aug 23 14:50:24 2023 >got 0.8884777545808717
#Wed Aug 23 14:50:24 2023 >got 0.1771594501511916
#Wed Aug 23 14:50:25 2023 >got 0.5885975988041554
#Wed Aug 23 14:50:26 2023 Producer: Done
#Wed Aug 23 14:50:26 2023 >got 0.6497389921716039
#Wed Aug 23 14:50:26 2023 Consumer: Done
