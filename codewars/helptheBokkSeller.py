def stock_list(LA, LOC):
    if len(LA) == 0 or len(LOC) == 0:
        return ""
    print(LOC, LA)
    dic = {}
    for i in LOC:
        for j in LA:
            if i == j[0]:
                c = list(j.split(" "))
                print(c)
                if i in dic:
                    dic[i] += int(c[-1])
                else:
                    dic[i] = int(c[-1])
    ans = ""
    for i in LOC:
        if i not in dic:
            ans += f"({i} : 0) - "
            continue
        ans += f"({i} : {dic[i]}) - "
    ans = list(ans)
    ans.pop()
    ans.pop()
    ans.pop()
    return "".join(ans)
