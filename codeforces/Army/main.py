n = input()
_n = input().strip(" ")
_n, d = _n[0], _n[-1]
_n, d = int(_n), int(d)
a, b = map(int, input().split())
print(((b-a)*d)-a)
