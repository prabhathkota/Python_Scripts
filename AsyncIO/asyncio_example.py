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


# this is a co-routine definition
async def fake_network_request(request):
    print('making network call for request:  ' + request)
    # simulate network delay
    await asyncio.sleep(1)

    return 'got network response for request: ' + request


# this is a co-routine definition
async def web_server_handler():
    # schedule both the network calls in a non-blocking way.

    # ensure_future creates a task from the co-routine object, and schedules it on the event loop
    task1 = asyncio.ensure_future(fake_network_request('one'))

    # another way to do the scheduling
    task2 = asyncio.get_event_loop().create_task(fake_network_request('two'))

    # simulate a blocking task. This gives a chance to the network requests scheduled above to be executed.
    await asyncio.sleep(0.5)

    print('doing useful work while network calls are in progress...')

    # wait for the network calls to complete. Time to step off the event loop using await!
    await asyncio.wait([task1, task2])

    print(task1.result())
    print(task2.result())

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(web_server_handler()))

