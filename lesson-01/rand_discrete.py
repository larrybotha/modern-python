from collections import Counter
from random import choice, choices, sample, shuffle


def choice_example():
    xs = ["red", "green", "blue", "orange"]
    result = choice(xs)

    print(f"choice from {xs} is {result}")
    print()


def choices_example():
    xs = ["red", "green", "blue", "orange"]
    number_of_attempts = 10
    results = choices(xs, k=number_of_attempts)
    counter = Counter(results)

    print(f"choices from {xs} are {results}")
    print(f"counts: {list(counter)}")
    print()


def choices_counter_even_distribution():
    xs = "draw win lose play-again".split(" ")
    counter = Counter(choices(xs, k=1000))

    print(f"counter:\n{counter}")
    print()


def choices_counter_weighted_distribution():
    xs = sorted("draw win lose play-again".split(" "))
    weights = [1, 2, 3, 4]
    counter = Counter(choices(xs, weights, k=1000))
    sorted_result = sorted(list(counter.items()), key=lambda x: x[0])

    print(f"counter:\n{sorted_result}")
    print()


def sample_example():
    xs = ["red", "green", "blue", "orange"]
    zs = choices(xs, k=8)
    # sample 2 unique values from zs
    results = sample(zs, 2)
    text = "\n".join(["sample from", str(zs), "is", str(results)])

    print(text)
    print()


def sample_example_lottery():
    xs = list(range(1, 57))
    result = sorted(sample(xs, k=6))

    print(f"lottery result: {result}")
    print()


def shuffle_example():
    xs = ["red", "green", "blue", "orange"]

    print(f"xs before:\n{xs}")

    shuffle(xs)

    print(f"xs after shuffling:\n{xs}")
    print()


def sample_choice_equivalence():
    xs = ["draw", "win", "lose"]
    sampled_value = sample(xs, 1)[0]
    # 'choice' is a special case of 'sample'
    chosen_value = choice(xs)
    text = "\n".join(
        [
            f"sampled value: {sampled_value}",
            f"chosen value: {chosen_value}",
        ]
    )
    print(text)


if __name__ == "__main__":
    choice_example()
    choices_example()
    choices_counter_even_distribution()
    choices_counter_weighted_distribution()
    sample_example()
    sample_example_lottery()
    shuffle_example()
    sample_choice_equivalence()
