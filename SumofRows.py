x = [[5, 7, 1],
     [9, 7, 17],
     [4, 7, 10]]

answer = 0

for i in range(len(x)):
    for j in range(len(x[0])):
        answer = answer + x[i][j]

    print(answer, end = " ")
    answer = 0