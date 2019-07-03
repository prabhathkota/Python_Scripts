"""
Input:
3
07895462130
919875641230
9195969878

Output:
+91 78954 62130
+91 91959 69878
+91 98756 41230
"""


def wrapper(f):
    def fun(ll):
        nlist = ["+91 "+c[-10:-5]+" "+c[-5:] for c in ll]
        f(nlist)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    n = int(input())
    l = [input() for _ in range(n)]
    sort_phone(l)


