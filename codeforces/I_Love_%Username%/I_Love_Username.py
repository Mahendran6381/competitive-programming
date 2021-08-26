def amazing_performence(arr):
    high = low = arr[0]
    ans = 0
    for i in arr:
        if i >high:
            high = i
            ans +=1
        elif i<low:
            low = i
            ans+=1
    return ans 
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split(' ')))
    print(amazing_performence(arr))

