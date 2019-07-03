
"""
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry
"""
if __name__ == '__main__':
    n = int(input())
    student_list = []
    scores = []
    second_lowest_score = 0
    names_with_second_highest = []
    if 2 <= n <= 5:
        for _ in range(n):
            name = input()
            score = float(input())
            student_list.append([name, score])
            scores.append(score)

        if scores:
            scores = sorted(set(scores))
            second_lowest_score = scores[1]
        if student_list and second_lowest_score:
            for each in student_list:
                if second_lowest_score == each[1]:
                    names_with_second_highest.append(each[0])
        for each in sorted(names_with_second_highest):
            print(each)




