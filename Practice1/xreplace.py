from helper import find_index

def xreplace():
    s1 = raw_input("Enter s1: ")
    s2 = raw_input("Enter s2: ")
    s3 = raw_input("Enter s3: ")

    # s1 = 'here you haNNve soNNme text'
    # s2 = 'NN'
    # s3 = ''

    is_present = True
    while is_present:
        indexes = find_index(s1, s2)
        if indexes is not None:
            start_index = indexes[0]
            end_index = indexes[1]
            s1 = s1[:start_index] + s3 + s1[end_index:]
        else:
            is_present = False
    print('Result is: ' + s1)

if __name__ == "__main__":
    exit(xreplace())
