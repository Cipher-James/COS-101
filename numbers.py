numbers = [10, 20, 30, 40, 20, 50, 60, 20, 70, 80]


def find_sum(values):
    total = 0
    for value in values:
        total += value
    return total


def find_mean(values):
    return sum(values) / len(values)


def find_median_mode(values):
    ordered = sorted(values)
    size = len(ordered)

    if size % 2 == 0:
        median = (ordered[size // 2 - 1] + ordered[size // 2]) / 2
    else:
        median = ordered[size // 2]

    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1

    highest = max(counts.values())
    mode = [value for value, count in counts.items() if count == highest]

    return median, mode


print("Sum:", find_sum(numbers))
print("Mean:", find_mean(numbers))
print("Median and Mode:", find_median_mode(numbers))
