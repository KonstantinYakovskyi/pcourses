VALUE = 99


def get_simple_deviders(value):
    result = []
    for i in range(2, value - 1):
        if (value % i) == 0:
            if len(result) > 0:
                if i % result[-1] != 0:
                    result.append(i)
            else:
                result.append(i)
    return result


def factorize(value):
    results = get_simple_deviders(value)
    print(results)


# h1 = factorize(VALUE)
assert get_simple_deviders(14) == [2,7]
assert get_simple_deviders(15) == [3,5]
assert get_simple_deviders(99) == [3,11]

if __name__ == "__main__":
    exit(factorize(VALUE))
