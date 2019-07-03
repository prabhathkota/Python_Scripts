"""
Task
Read an integer N. For all non-negative integers i < N, print i**2 (i-square). See the sample for details.

Input Format
The first and only line contains the integer, .

Constraints
1 <= N <= 20

Output Format
Print  lines, one corresponding to each .

"""

if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 20:
        for each in range(n):
            print(each**2)


