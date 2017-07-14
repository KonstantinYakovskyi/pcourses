def decode():
    # row = raw_input("Enter row to decode: ")
    rows = ['', '1', '11', '11111', '11#', '11##', '11122234###55']

    def func(rows):
        actual_result = []
        for row in rows:
            result = ''
            previous_symbol = ''

            for current_symbol in row:
                last_symbol_in_result = result[-1:]
                penultimate_symbol_in_result = result[-2:-1]

                if previous_symbol == '':
                    previous_symbol = current_symbol
                    continue

                elif current_symbol == previous_symbol:
                    # check if '#' is already executed
                    if current_symbol == '#':
                        if penultimate_symbol_in_result == last_symbol_in_result:
                            continue
                        else:
                            result += last_symbol_in_result

                    elif last_symbol_in_result != current_symbol:
                        result += current_symbol
                previous_symbol = current_symbol

            actual_result.append(result)
        return actual_result

    expected_results = ['', '', '1', '1', '1', '11', '1225']
    actual_results = func(rows)

    print(actual_results == expected_results)
    print('Expected results: ' + str(expected_results))
    print('Actual results: ' + str(actual_results))


if __name__ == "__main__":
    exit(decode())
