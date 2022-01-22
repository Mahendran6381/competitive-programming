def is_similar_pairs(arr):
    if len(arr) % 2 != 0:
        return "No"
    a = 0
    b = a+1
    arr = sorted(arr)
    while len(arr) != 0 and b < len(arr) and a < len(arr):
        if arr[b] - arr[a] == 1 or arr[a] % 2 == arr[b] % 2:
            print(a, b)
            print(arr[a], arr[b])
            arr.remove(arr[a])
            arr.remove(arr[b])
            a = b+1
            b = a+1
        else:
            return "No"
    return "YES"


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(is_similar_pairs(arr))
