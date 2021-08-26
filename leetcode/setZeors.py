a = [[0, 2, 0], [1, 3, 3], [1, 2, 3]]
print(a)


def change_arr(col, ele):
    if col < 0 or ele < 0:
        pass
    else:
        for i in range(len(a)):
            if i == col:
                for j in range(i):
                    arr[i][j] = 0
            else:
                a[i][ele] = 0


col, ele = 0, 0
arr = a.copy()
for i in arr:
    for j in i:
        if j == 0:
            change_arr(arr.index(i), i.index(j))
print(a)
