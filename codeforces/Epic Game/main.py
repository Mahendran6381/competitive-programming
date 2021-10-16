import math

def findWin(a,b,n):
    print(a,b,n)
    c = True
    d = a    
    while True and n>=0:
        if c:
            c = False
            d = a    
        else:
            c = True
            d = b
        print(d,n)    
        gcd =  math.gcd(d,n)
        n =  n-gcd  
    if d == a:
        print("1")
    else:
        print('0')        
if __name__ == "__main__":
   l = list(map(int,input().split(" ")))
   findWin(l[0],l[1],l[2])