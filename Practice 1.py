def xfind():
    s1 = raw_input("Enter s1: ")
    s2 = raw_input("Enter s2: ")
    # s1 = 'abcdef'
    # s2 = 'cd'
    result = False
    s2_len = len(s2)
    for i in range(len(s1) - len(s2)):
        fragment = s1[i:i + s2_len]
        if fragment == s2:
            result = True
            break
    print(result)


if __name__ == "__main__":
    exit(xfind())