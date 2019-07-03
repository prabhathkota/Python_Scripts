"""
X Y Z - 3 integers

representing the dimensions of a cuboid along with an integer N

possible coordinates (i, j, k)
sum of i + j + k is not equal to N

0 <= i <= X
0 <= j <= Y
0 <= k <= Z

Sample Input
1
1
1
2

Sample Output
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

x = int ( input())
y = int ( input())
z = int ( input())
n = int ( input())


print([ [ i, j, k ] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k) != n )])





