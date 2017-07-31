PATH = 'C:\Projects\pcources\materials\DocToRead.txt'


def iter_lines(fd):
    with open(fd) as f:

        while True:
            data = f.readline()
            if not data:
                break
            yield data


def strip_spaces(path):
    for item in iter_lines(path):
        s = item
        print(s)

    a = iter


if __name__ == "__main__":
    exit(strip_spaces(PATH))
