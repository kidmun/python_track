def swap_case(s):
    ans = ""
    for c in s:
        if c.islower():
            ans += c.upper()
        else:
            ans += c.lower()
    return ans


if __name__ == '__main__':