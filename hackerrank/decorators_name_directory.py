"""
Sort by Age

Input:
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Output:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""

import operator


def person_lister(f):
    def inner(people):
        sorted_by_age = sorted(people, key=lambda x: int(x[2]))
        print(sorted_by_age)
        print(f)
        return map(f, sorted_by_age)
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

