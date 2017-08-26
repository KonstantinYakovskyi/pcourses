from helper import find_index

def xsplit():
    # s1 = raw_input("Enter s1: ")
    # s2 = raw_input("Enter s2: ")

    s1 = 'here some text'
    s2 = 'some'

    indexes = find_index(s1, s2)
    result = [s1[:indexes[0]], s1[indexes[1]:]]
    print(result)


if __name__ == "__main__":
    exit(xsplit())
