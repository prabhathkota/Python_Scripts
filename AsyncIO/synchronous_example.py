import time


def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 500000 == 0:
            time.sleep(0.0001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


def main():
    divs1 = find_divisibles(508000, 34113)
    divs2 = find_divisibles(100052, 3210)
    divs3 = find_divisibles(500, 3)
    print('\nD1 result: {}'.format(divs1))
    print('\nD2 result: {}'.format(divs2))
    print('\nD3 result: {}'.format(divs3))


if __name__ == '__main__':
    main()

