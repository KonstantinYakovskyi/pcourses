from helper import find_index

def xfind():
    s1 = raw_input("Enter s1: ")
    s2 = raw_input("Enter s2: ")

    index = find_index(s1, s2)
    if index is not None:
        print "TRUE:  S1 is in S2"
    else:
        print "FALSE: S1 is not in S2"


if __name__ == "__main__":
    exit(xfind())