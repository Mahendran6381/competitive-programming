print("HI")


def prefill(n, v, memo=[]):
    if type(n) is str:
        try:
            arr = []
            int(n)
            arr.append(v)
            return arr
        except Exception as e:
            print(e)
            print(f"{n} is invalid")
    else:
        if n == 0:
            arr = memo.copy()
            memo = []
            return arr
        else:
            memo.append(v)
            return prefill(n - 1, v, memo=memo.copy())


print("hlo")

print(prefill(3, 1))
print(prefill(2, "abc"))
print(prefill(3, prefill(2, "2d")))
