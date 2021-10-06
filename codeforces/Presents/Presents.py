def present(arr):
    ans = []
    for i in range(1,len(arr)+1):
         try:
             ans.append(arr.index(i)+1)
         except:
             ans.append(i)    
    print(*ans)        
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split(" ")))
    present(arr)       