from helper import find_index
def decode():
    row = raw_input("Enter row to decode: ")

    result = ''
    for i in range(len(row)):
        counter = 0
        if row[i] == row[i+1] and row[i] != '#':
            while row[i] == row[i+1] and row[i] != '#':
                counter +=1
                i +=1
                result += row[i]
                i = i + counter -1

    if len(find_index(row, '#')) > 1:
        result = result + result[-1:]
    print('Result is: ' + result)


if __name__ == "__main__":
    exit(decode())
