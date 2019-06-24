"""
Asyncio is a beautiful symphony between an Event loop, Tasks and Co-routines all coming together so perfectly

Tasks:
    - Event loop runs tasks one after the other. At any given time, only one of the tasks is running

Event loop:
    - When the active task makes a blocking call, say a network request, and cannot make further progress it gives the
        control back to the event loop realising that some other task could possibly better utilise the event loop’s time.
    - The event loop time is precious. If you are not making progress, you should step off the loop, so that someone
        else can. Event loop is the measure of progress.

Co-routine:
    - Subroutine/Method/Function is state-less
    - Co-routines is a stateful widget, it maintains state in between executions.
    - They have co-operative nature, that enables giving up control of the event loop, when the co-routine
        gets blocked and has nothing useful to do (real world scenario like a network request, db query etc.)
    - Co-routines look like a normal function, but in their behaviour they are stateful objects with
        resume() and pause() — like methods.
"""

import asyncio


# definition of a co-routine
async def coroutine_1():
    print('coroutine_1 is active on the event loop')

    print('coroutine_1 yielding control. Going to be blocked for 4 seconds')
    await asyncio.sleep(4)

    print('coroutine_1 resumed. coroutine_1 exiting')


# definition of a co-routine
async def coroutine_2():
    print('coroutine_2 is active on the event loop')

    print('coroutine_2 yielding control. Going to be blocked for 5 seconds')
    await asyncio.sleep(5)

    print('coroutine_2 resumed. coroutine_2 exiting')


# this is the event loop
loop = asyncio.get_event_loop()

# schedule both the coroutines to run on the event loop
loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))

