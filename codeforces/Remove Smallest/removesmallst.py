def Removesmallest(arr):
    i = 0
    while(len(arr) != 1):
        if(arr[i+1] == arr[i]):
            arr.remove(arr[i])
        elif(arr[i+1]-arr[i] <= 1 and arr[i] != arr[i+1]):
            arr.remove(min(arr[i+1],arr[i]))
        elif(arr[i+1]-arr[i] > 1):
            return "NO"
    return   "YES"     
if __name__ == "__main__":
    n = int(input())
    ans = []
    for _ in range(n):
        m = int(input())
        ans.append(Removesmallest(sorted(list(map(int,input().split(" "))))))
    for i in ans:
        print(i)    
