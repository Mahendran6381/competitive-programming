def removeSTr(oriStr, popStr):
    for i in popStr:
        if i in oriStr:
            popStr.remove(i)
            oriStr.remove(i)
        elif i not in oriStr:
            return "Fuck No"
    return "NO"


firname = input()
secname = input()
oriname = input()
print(removeSTr(list(sorted(firname + secname)), list(sorted(oriname))))
