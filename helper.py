def find_index(s1, s2):
    result = None
    s2_len = len(s2)
    for i in range(len(s1) - len(s2) + 1):
        fragment = s1[i:i + s2_len]
        if fragment == s2:
            result = [i, i + s2_len]
            break
    return result


if __name__ == "__main__":
    exit(find_index())