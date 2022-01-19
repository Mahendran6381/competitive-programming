
def have_find(string: str):
    string = string.strip(" ?!")
    print(string[-1])
    if string[-1] in "aeiouAEIOU":
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    string = input()
    print(have_find(string))
