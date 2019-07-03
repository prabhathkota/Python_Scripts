"""
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, a. The second line contains the second integer, b.
"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    limitn = 10**10
    if 1 <= a <= limitn and 1 <= b <= limitn:
        print(a + b)
        print(a - b)
        print(a * b)
