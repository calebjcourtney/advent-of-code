from utils import get_line_data


def solve(time, record):
    num_wins = 0
    for hold_time in range(time + 1):
        total_distance = hold_time * (time - hold_time)
        if total_distance > record:
            num_wins += 1

    return num_wins


def part_one(data):
    times = list(map(int, data[0].split(":")[1].split()))
    distances = list(map(int, data[1].split(":")[1].split()))

    output = 1

    for time, dist in zip(times, distances):
        output *= solve(time, dist)

    return output


def part_two(data):
    time = int("".join(data[0].split(":")[1].strip().split()))
    distance = int("".join(data[1].split(":")[1].strip().split()))

    return solve(time, distance)


if __name__ == '__main__':
    data = get_line_data("06")

    p1_result = part_one(data)
    print(p1_result)

    p2_result = part_two(data)
    print(p2_result)
