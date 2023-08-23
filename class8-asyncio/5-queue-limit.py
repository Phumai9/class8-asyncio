from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queqe,id):
    print(f'{time.ctime()} Producer {id}: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(id*0.1)
        # add to the queqe
        await queqe.put(value)
    print(f'{time.ctime()} Producer {id}: Done')


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
    product = [producer(queue,_) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())

# Wed Aug 23 15:28:14 2023 Consumer: Running
# Wed Aug 23 15:28:14 2023 Producer 0: Running
# Wed Aug 23 15:28:14 2023 Producer 1: Running
# Wed Aug 23 15:28:14 2023 Producer 2: Running
# Wed Aug 23 15:28:14 2023 Producer 3: Running
# Wed Aug 23 15:28:14 2023 Producer 4: Running
# Wed Aug 23 15:28:14 2023 >got 0.34918175046828737
# Wed Aug 23 15:28:14 2023 >got 0.7412029495528796
# Wed Aug 23 15:28:15 2023 >got 0.6792699679114664
# Wed Aug 23 15:28:16 2023 >got 0.11349235443581762
# Wed Aug 23 15:28:16 2023 >got 0.41967090899850457
# Wed Aug 23 15:28:16 2023 >got 0.0024106001384078812
# Wed Aug 23 15:28:16 2023 >got 0.6740042732117232
# Wed Aug 23 15:28:17 2023 >got 0.10039601033386325
# Wed Aug 23 15:28:17 2023 >got 0.532098798290322
# Wed Aug 23 15:28:17 2023 >got 0.36123811411566764
# Wed Aug 23 15:28:18 2023 >got 0.942587307520024
# Wed Aug 23 15:28:19 2023 >got 0.9284617894588845
# Wed Aug 23 15:28:20 2023 >got 0.5785673613876454
# Wed Aug 23 15:28:20 2023 >got 0.6219870239388249
# Wed Aug 23 15:28:21 2023 >got 0.6512689380273414
# Wed Aug 23 15:28:22 2023 >got 0.7839029373509936
# Wed Aug 23 15:28:22 2023 >got 0.5741062312699778
# Wed Aug 23 15:28:23 2023 >got 0.6929295256861919
# Wed Aug 23 15:28:24 2023 >got 0.35394912705828296
# Wed Aug 23 15:28:24 2023 >got 0.7467404201514625
# Wed Aug 23 15:28:25 2023 >got 0.8369501967479789
# Wed Aug 23 15:28:26 2023 >got 0.1628600717047587
# Wed Aug 23 15:28:26 2023 >got 0.2317972304347189
# Wed Aug 23 15:28:26 2023 >got 0.6807800839971467
# Wed Aug 23 15:28:27 2023 >got 0.13255616652094293
# Wed Aug 23 15:28:27 2023 >got 0.44970595034189464
# Wed Aug 23 15:28:27 2023 >got 0.1730327912474786
# Wed Aug 23 15:28:27 2023 >got 0.1655063385129497
# Wed Aug 23 15:28:28 2023 >got 0.13785183755297725
# Wed Aug 23 15:28:28 2023 >got 0.3730382161747682
# Wed Aug 23 15:28:28 2023 Producer 0: Done
# Wed Aug 23 15:28:28 2023 >got 0.5848636778615874
# Wed Aug 23 15:28:29 2023 >got 0.008868006662082983
# Wed Aug 23 15:28:29 2023 >got 0.22729228445064664
# Wed Aug 23 15:28:29 2023 >got 0.2330135602880865
# Wed Aug 23 15:28:29 2023 >got 0.5481398431384414
# Wed Aug 23 15:28:30 2023 >got 0.2576529407468089
# Wed Aug 23 15:28:30 2023 >got 0.5939812112795966
# Wed Aug 23 15:28:31 2023 >got 0.7074736734434152
# Wed Aug 23 15:28:31 2023 >got 0.9253111274828175
# Wed Aug 23 15:28:32 2023 >got 0.024737854972857076
# Wed Aug 23 15:28:32 2023 >got 0.25672895380267724
# Wed Aug 23 15:28:33 2023 >got 0.3535996803254645
# Wed Aug 23 15:28:33 2023 >got 0.4443602891598162
# Wed Aug 23 15:28:33 2023 >got 0.783381297500696
# Wed Aug 23 15:28:33 2023 Producer 1: Done
# Wed Aug 23 15:28:34 2023 >got 0.4210393532723581
# Wed Aug 23 15:28:34 2023 Producer 2: Done
# Wed Aug 23 15:28:35 2023 >got 0.17680110399028526
# Wed Aug 23 15:28:35 2023 >got 0.38240968947406384
# Wed Aug 23 15:28:35 2023 Producer 3: Done
# Wed Aug 23 15:28:35 2023 >got 0.047872407175054144
# Wed Aug 23 15:28:35 2023 Producer 4: Done
# Wed Aug 23 15:28:35 2023 >got 0.8480507389083315
# Wed Aug 23 15:28:36 2023 >got 0.4626056384454953
