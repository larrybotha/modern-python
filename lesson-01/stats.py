from statistics import mean, median, mode, pstdev, stdev

XS = [49, 50, 51]


def mean_example():
    result = mean(XS)

    print(f"mean: {result}")
    print()


def median_example():
    result = median([*XS, 52])

    print(f"median: {result}")
    print()


def mode_example():
    result = mode([*XS, 51, 51])

    print(f"mode: {result}")
    print()


def standard_deviation_example():
    result = stdev([*XS])

    print(f"standard deviation: {result}")
    print()


def population_standard_deviation_example():
    result = pstdev([*XS])

    print(f"population standard deviation: {result}")
    print()


if __name__ == "__main__":
    mean_example()
    median_example()
    mode_example()
    standard_deviation_example()
    population_standard_deviation_example()
