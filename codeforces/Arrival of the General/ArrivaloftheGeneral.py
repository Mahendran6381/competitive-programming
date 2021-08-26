def Lineup(arr, n):
    m = arr[::-1]
    indexOfMin = m.index(min(m))
    indexOfMax = arr.index(max(arr))
    print(indexOfMin, indexOfMax)
    if indexOfMax > indexOfMin:
        print((indexOfMax + indexOfMin) - 1)
    else:
        print(indexOfMax + indexOfMin)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(" ")))
    Lineup(arr, n)
