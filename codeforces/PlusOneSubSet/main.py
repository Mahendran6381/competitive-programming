def plus_one_subset(arr):
    maxElem = max(arr)
    j = 0
    while arr.count(maxElem) != len(arr):
        for i in range(len(arr)):
            if arr[i] != maxElem:
                arr[i] += 1
        print(arr)
        j = j+1
    return j


if __name__ == "__main__":
    for _ in range(int(input())):
        c = int(input())
        arr = list(map(int, input().split(" ")))
        print(plus_one_subset(arr))
