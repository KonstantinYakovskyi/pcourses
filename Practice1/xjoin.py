def xjoin():
    # array = raw_input("Enter array: ")
    # s = raw_input("Enter s: ")

    array = ['is', 'the', 'capital', 'of', 'GB']
    s = 'London'

    for i in array:
        s += '-' + str(i)
    print(s)


if __name__ == "__main__":
    exit(xjoin())
