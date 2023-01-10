from collections import Counter


def dict_like_counting():
    counter = Counter()
    num_things = counter["things"]

    print(f"num_things: {num_things}")

    num_things += 1

    print(f"num_things: {num_things}")
    print()


def counting_at_init():
    x = "red green blue red blue red"
    counter = Counter(x.split(" "))

    print(f"items in counter: {counter.items()}")
    print()


def most_common():
    counter = Counter([1, 2, 3, 1])

    print(f"most common value in counter: {counter.most_common(1)}")
    print()


def elements():
    counter = Counter("red green blue red green red".split(" "))

    print(f"elements: {list(counter.elements())}")
    print(f"items: {list(counter.items())}")
    print(f"keys: {list(counter.keys())}")
    print(f"values: {list(counter.values())}")
    print()


if __name__ == "__main__":
    dict_like_counting()
    counting_at_init()
    most_common()
    elements()
