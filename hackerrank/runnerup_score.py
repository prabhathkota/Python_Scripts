"""
Get the runner up score

Input Format
The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in list .

Output Format
Get the runner up score

"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if 2 <= n <= 10:
        sarr = sorted(set(arr))
        print(sarr[-2])

