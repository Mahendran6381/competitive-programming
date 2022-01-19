def find_capacity(inArr, outArr):
    capacity = 0
    Ele = inArr[0]
    temp = 0
    for i in range(len(inArr)):
        print(" temp ", temp, " cap ", capacity)
        temp = (Ele-outArr[i])+inArr[i]
        if temp > capacity:
            capacity = temp
        Ele = temp
    return capacity


if __name__ == "__main__":
    a = b = list()
    for i in range(int(input())):
        t1, t2 = map(int, input().split(" "))
        a.append(t1)
        b.append(t2)
    print(find_capacity(b, a))
