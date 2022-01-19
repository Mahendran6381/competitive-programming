def tri_num(num: int):
    return "YES" if num % 3 == 0 or num == 1 else "NO"


if __name__ == "__main__":
    n = int(input())
    print(tri_num(n))
