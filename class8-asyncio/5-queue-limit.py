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
    print(f'{time.ctime()} Producer: Done')


async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queqe.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create the shared queqe
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many product
    product = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:23:16 2023 Consumer: Running
# Wed Aug 23 14:23:16 2023 Producer: Running
# Wed Aug 23 14:23:16 2023 Producer: Running
# Wed Aug 23 14:23:16 2023 Producer: Running
# Wed Aug 23 14:23:16 2023 Producer: Running
# Wed Aug 23 14:23:16 2023 Producer: Running
# Wed Aug 23 14:23:17 2023 >got 0.13571514200195767
# Wed Aug 23 14:23:17 2023 >got 0.22543208381346513
# Wed Aug 23 14:23:17 2023 >got 0.3491899552149734
# Wed Aug 23 14:23:17 2023 >got 0.3053076509623127
# Wed Aug 23 14:23:18 2023 >got 0.4577790163594835
# Wed Aug 23 14:23:18 2023 >got 0.257440614694049
# Wed Aug 23 14:23:18 2023 >got 0.7421572196630034
# Wed Aug 23 14:23:19 2023 >got 0.8612639650434949
# Wed Aug 23 14:23:20 2023 >got 0.5434109871066772
# Wed Aug 23 14:23:20 2023 >got 0.2791374039805533
# Wed Aug 23 14:23:21 2023 >got 0.66678459430161
# Wed Aug 23 14:23:21 2023 >got 0.9825119641814805
# Wed Aug 23 14:23:22 2023 >got 0.3445127183439365
# Wed Aug 23 14:23:23 2023 >got 0.6734038843287299
# Wed Aug 23 14:23:23 2023 >got 0.8461637004989622
# Wed Aug 23 14:23:24 2023 >got 0.7857602729607887
# Wed Aug 23 14:23:25 2023 >got 0.46426237933530856
# Wed Aug 23 14:23:26 2023 >got 0.9867785721847746
# Wed Aug 23 14:23:27 2023 >got 0.17302932765727308
# Wed Aug 23 14:23:27 2023 >got 0.5972601154010269
# Wed Aug 23 14:23:27 2023 >got 0.5044818475712711
# Wed Aug 23 14:23:28 2023 >got 0.6798108223537452
# Wed Aug 23 14:23:29 2023 >got 0.7524331678239022
# Wed Aug 23 14:23:29 2023 >got 0.5932712124755433
# Wed Aug 23 14:23:30 2023 >got 0.2715605477248103
# Wed Aug 23 14:23:30 2023 >got 0.24181133324726134
# Wed Aug 23 14:23:31 2023 >got 0.9098813164768019
# Wed Aug 23 14:23:31 2023 >got 0.6954048043404588
# Wed Aug 23 14:23:32 2023 >got 0.5202763362081545
# Wed Aug 23 14:23:33 2023 >got 0.0664766517762112
# Wed Aug 23 14:23:33 2023 >got 0.11011333638867893
# Wed Aug 23 14:23:33 2023 >got 0.376050858097582
# Wed Aug 23 14:23:33 2023 >got 0.18278765180574363
# Wed Aug 23 14:23:33 2023 >got 0.4722406344262192
# Wed Aug 23 14:23:34 2023 >got 0.8101685260552767
# Wed Aug 23 14:23:35 2023 >got 0.569452472905587
# Wed Aug 23 14:23:35 2023 >got 0.20573268876508632
# Wed Aug 23 14:23:36 2023 >got 0.4063115998478265
# Wed Aug 23 14:23:36 2023 >got 0.120324749781333
# Wed Aug 23 14:23:36 2023 >got 0.8458434767626536
# Wed Aug 23 14:23:37 2023 >got 0.9877115387252243
# Wed Aug 23 14:23:38 2023 >got 0.5490179432475454
# Wed Aug 23 14:23:38 2023 Producer: Done
# Wed Aug 23 14:23:38 2023 >got 0.028494951517093914
# Wed Aug 23 14:23:39 2023 >got 0.11940240620187048
# Wed Aug 23 14:23:39 2023 Producer: Done
# Wed Aug 23 14:23:39 2023 >got 0.36021240289452683
# Wed Aug 23 14:23:39 2023 >got 0.44186873807769245
# Wed Aug 23 14:23:39 2023 Producer: Done
# Wed Aug 23 14:23:39 2023 >got 0.7538942044439578
# Wed Aug 23 14:23:39 2023 Producer: Done
# Wed Aug 23 14:23:40 2023 >got 0.10144672027192847
# Wed Aug 23 14:23:40 2023 Producer: Done
# Wed Aug 23 14:23:40 2023 >got 0.9589954418031412
# Wed Aug 23 14:23:41 2023 >got 0.43978408432390825