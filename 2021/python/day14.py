from utils import get_data

from collections import Counter

data = get_data("14")

sequence, r = data.split("\n\n")

rules = {}
for line in r.strip().split("\n"):
    start, end = line.strip().split(" -> ")
    rules[start] = end

seq_counter = Counter()
for i in range(len(sequence) - 1):
    seq_counter[sequence[i] + sequence[i + 1]] += 1

for count in range(41):
    if count in [10, 40]:
        char_count = Counter()

        for key in seq_counter:
            char_count[key[0]] += seq_counter[key]

        char_count[sequence[-1]] += 1
        print(max(char_count.values()) - min(char_count.values()))

    new_seq_counter = Counter()
    for key in seq_counter:
        new_seq_counter[key[0] + rules[key]] += seq_counter[key]
        new_seq_counter[rules[key] + key[1]] += seq_counter[key]

    seq_counter = new_seq_counter
