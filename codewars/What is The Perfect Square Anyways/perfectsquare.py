from math import ceil,log,sqrt
def perfect_square(n):
    for i in range(2,int(sqrt(n))+1):
        exp = int(round(log(i)))
        if i**exp == n:
            return [i,exp] 