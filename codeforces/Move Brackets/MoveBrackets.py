def moveBracket(arr):
    char = {")": "(", "(": ")"}
    stack = []
    move = 0
    i = 0
    while len(arr) != 0:
        if i not in stack:
            stack.append(i)
            i = i + 1
            print(stack)
        elif char[i] in stack:
            print(stack)
            print(stack, arr, move)
            arr.remove(char[stack[-1]])
            move += 1
            stack.pop()
        i = i + 1
        print(stack)
    print(move)


moveBracket(["(", ")"])
