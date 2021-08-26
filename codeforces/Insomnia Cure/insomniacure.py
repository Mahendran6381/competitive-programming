def findDamage(k,l,m,n,d):
    c = 0
    for i in range(d):
        if(d%k==0 | d%l==0 |d%m==0 |d%n==0):
            c +=1

    return c        