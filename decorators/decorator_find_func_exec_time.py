import functools
import time


def timer(f):
    @functools.wraps(f)
    def timer_wrap(*args, **kwargs):
        print('inside timer_wrap decorator')
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print('Total Time Taken : %4f secs' % (end_time - start_time))
    return timer_wrap


@timer
def test_timer_func(num_times):
    """ test_timer_func documentation """
    total_sum = 0
    for _ in range(num_times):
        total_sum += sum([i ** 2 for i in range(100000)])
    print('Total Sum: %f ' % total_sum)


if __name__ == '__main__':
    print('------------------------------------')
    test_timer_func(200)
    print('------------------------------------')


# Output:
#
# ------------------------------------
# inside timer_wrap decorator
# Total Sum: 66665666670000000.000000
# Total Time Taken : 6.213893 secs
# ------------------------------------




