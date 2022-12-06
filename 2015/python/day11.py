from utils import get_data


def increment_password(password):
    # Increment the password by one character, wrapping around from z to a
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == "z":
            password[i] = "a"
        else:
            password[i] = chr(ord(password[i]) + 1)
            break

    return "".join(password)


def is_valid_password(password):
    # Check if the password contains the letters i, o, or l
    if "i" in password or "o" in password or "l" in password:
        return False

    # Check if the password contains a straight of at least three letters
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            break
    else:
        return False

    # Check if the password contains at least two different, non-overlapping pairs of letters
    pair_count = 0
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and (i == 0 or password[i] != password[i - 1]):
            pair_count += 1
            i += 1
            if pair_count == 2:
                break
    else:
        return False

    # If the password passes all checks, it is valid
    return True


if __name__ == '__main__':
    # Read the puzzle input
    puzzle_input = get_data(11)

    # part one
    while not is_valid_password(puzzle_input):
        puzzle_input = increment_password(puzzle_input)

    print(puzzle_input)

    # part two
    puzzle_input = increment_password(puzzle_input)
    while not is_valid_password(puzzle_input):
        puzzle_input = increment_password(puzzle_input)

    print(puzzle_input)
