from collections import Counter
from random import choice, choices, sample, seed, shuffle


def choice_example():
    xs = ["red", "green", "blue", "orange"]
    seed(1)
    result = choice(xs)

    print(f"choice from {xs} is {result}")
    print()


def choices_example():
    xs = ["red", "green", "blue", "orange"]
    number_of_attempts = 10
    seed(1)
    results = choices(xs, k=number_of_attempts)
    counter = Counter(results)

    print(f"choices from {xs} are {results}")
    print(f"counts: {list(counter)}")
    print()


def sample_example():
    xs = ["red", "green", "blue", "orange"]
    results = sample(xs, 2)

    print(f"sample from {xs} is {results}")
    print()


def shuffle_example():
    xs = ["red", "green", "blue", "orange"]
    shuffle(xs)

    print(f"shuffling {xs} yields {xs}")
    print()


if __name__ == "__main__":
    choice_example()
    choices_example()
    sample_example()
    shuffle_example()
