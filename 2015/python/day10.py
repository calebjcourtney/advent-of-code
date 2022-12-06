from utils import get_data


def apply_steps(s):
    # Initialize an empty result string
    result = ""

    # Iterate over the string, keeping track of the current digit and the
    # number of times it appears in a row
    current_digit = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_digit:
            # If the current digit is the same as the previous one,
            # increase the count
            count += 1
        else:
            # If the current digit is different from the previous one,
            # add the count and the digit to the result string
            result += str(count) + current_digit
            current_digit = s[i]
            count = 1

    # Add the last count and digit to the result string
    result += str(count) + current_digit

    # Return the result string
    return result


if __name__ == '__main__':
    data = get_data(10)

    for i in range(40):
        data = apply_steps(data)

    print(len(data))

    for i in range(10):
        data = apply_steps(data)

    print(len(data))
