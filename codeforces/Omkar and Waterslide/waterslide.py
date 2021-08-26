def waterslide(arr):
    large = max(arr)
    ans = 0
    i = 0
    arr = arr[::-1]
    while len(arr) != 0 and i < len(arr) - 1:
        print(len(arr))
        if arr[i] == large:
            arr.remove(arr[i])
        elif arr[i] == min(arr) and arr[i] != arr[i + 1]:
            arr[i] += 1
            ans += 1
        elif arr[i] == min(arr) and arr[i] == arr[i + 1]:
            arr[i] += 1
            arr[i + 1] += 1
            ans += 1
        i = i + 1
    return ans


n = int(input())
ans = []
for _ in range(n):
    m = int(input())
    lis = list(map(int, input().split(" ")))
    ans.append(waterslide(lis))
for i in ans:
    print("",i)
