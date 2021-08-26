def mulOrDiv(n, total, memo=0):
    if n == 0 or (total < 1 and n % 6 != 1):
        return -1
    if n == 1:
        return memo
    elif n % 6 == 0:
        memo += 1
        return mulOrDiv(n / 6, total, memo=memo)
    else:
        total -= 1
        memo += 1
        return mulOrDiv(n * 2, total=total, memo=memo)


if __name__ == "__main__":
    total = int(input())
    for i in range(total):
        print(mulOrDiv(int(input()), 30, memo=0))
