def longest_consec(strarr, k):
    if (k == 0 or len(strarr) == 0) or (k > len(strarr) or k < 0):
        return ""
    else:
        ans = ["".join(strarr[i : i + k]) for i in range(len(strarr))]
        return max(ans, key=lambda x: len(x))
