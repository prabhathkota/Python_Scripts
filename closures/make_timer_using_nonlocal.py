import time


def make_timer():
    last_called = None

    def time_elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called = now
            return None
        result = now - last_called
        last_called = now
        return result

    return time_elapsed


if __name__ == '__main__':
    t1 = make_timer()
    t2 = make_timer()
    print(t1())
    print(t2())
    time.sleep(1)
    print('T1 called after', t1(), 'secs sleep')
    time.sleep(2)
    print('T2 called after', t2(), 'secs sleep')
    time.sleep(1)
    print('T2 called again after', t2(), 'secs sleep')
    time.sleep(1)
    print('T1 called again after', t1(), 'secs sleep')


"""
Output:
None
None
T1 called after 1.0040202140808105 secs sleep
T2 called after 3.0084831714630127 secs sleep
T2 called again after 1.0050411224365234 secs sleep
T1 called again after 4.010027170181274 secs sleep
"""