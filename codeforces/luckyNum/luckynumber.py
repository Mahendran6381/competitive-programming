def checkLucky(str):
    n = len(str)
    numList = list(map(int, str))
    mid = n // 2
    if set(numList) == set([7]) or set(numList) == set([4]) or set(numList) == set([4, 7]):
        if sum(numList[:mid]) == sum(numList[mid:]):
            print("YES")
        else:
            print("NO")    
    else:
        print("NO")


n = int(input())
str = input()
checkLucky(str)
