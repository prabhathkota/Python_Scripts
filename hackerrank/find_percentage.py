"""
Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Output:
56.00  (52+56+60/3)
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if 2 <= n <= 10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        scores_of_student = student_marks[query_name]
        avg = sum(scores_of_student)/len(scores_of_student)
        print(format(avg, '.2f'))

