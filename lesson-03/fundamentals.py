import pprint
from collections import defaultdict
from itertools import zip_longest
from math import fsum

MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
]
NAMES = [
    x.strip()
    for x in """
        david betty susan mary darlene sandy davin
        shell becky beatrice tom michael wallace
    """.strip().split(
        " "
    )
    if x
]


def fsum_for_floating_point_arithmetic():
    xs = [0.1] * 10

    print(f"xs = {xs}\n")
    print(f"sum(xs)\n= {sum(xs)}\n")
    print(f"fsum(xs)\n= {fsum(xs)}")
    print()


def defaultdict_example():
    nd = {"joe": 1}
    dd = defaultdict(lambda: 1)

    print(f"nd['joe']: {nd['joe']}")
    print(f"dd['joe']: {dd['joe']}")
    print()


def defaultdict_set():
    d = defaultdict(set)

    # we use 'add' here, as the factory is a set
    d["t"].add("tom")
    d["m"].add("mary")
    d["t"].add("tim")
    d["t"].add("tom")
    d["m"].add("martin")

    pprint.pprint(d, width=60)
    print()


def defaultdict_list():
    d = defaultdict(list)

    # use 'append' because the factory is a list
    d["t"].append("tom")
    d["m"].append("mary")
    d["t"].append("tim")
    d["t"].append("tom")
    d["m"].append("martin")

    pprint.pprint(d, width=60)
    print()


def defaultdict_grouping():
    alphabetical_dict = defaultdict(list)

    # idiomatic grouping in Python
    for name in NAMES:
        feature = name[0]
        alphabetical_dict[feature].append(name)

    print("grouped by first char")
    pprint.pprint(alphabetical_dict, width=60)
    print()

    length_dict = defaultdict(list)

    for name in NAMES:
        feature = len(name)
        length_dict[feature].append(name)

    print("grouped by length")
    pprint.pprint(length_dict, width=70)
    print()


def key_function():
    # SELECT name FROM names ORDER BY len(name);
    sorted_names = sorted(NAMES, key=len)

    print("Names sorted alphabetically using a key function")
    pprint.pprint(sorted_names)
    print()


def zip_string_transpose():
    xs = "abcdef"
    ys = "ghijklm"

    print(f"xs: {xs}")
    print(f"ys: {ys}")
    print("transposed:")
    pprint.pprint(list(zip(xs, ys)), width=40)

    print()
    print("transposed without dropping:")
    pprint.pprint(list(zip_longest(xs, ys, fillvalue="ermagerd!")), width=40)
    print()


def zip_matrix_transpose():
    print("2-dimensional array:")
    pprint.pprint(MATRIX, width=20)

    print("\ntransposed:")
    transposed_xs = [list(row) for row in zip(*MATRIX)]
    pprint.pprint(transposed_xs, width=20)
    print()


def flattening_nested_lists():
    print("matrix:")
    pprint.pprint(MATRIX, width=15)

    # from the following, we can see how to flatten lists using a comprehension:

    # for row in MATRIX:
    #     for x in row:
    #         x

    flattened_xs = [x for row in MATRIX for x in row]
    #                     [     1     ] [     2     ]
    #              [               3                ]
    #
    # 1 - for each row in the matrix
    # 2 - for each item in the row
    # 3 - add x to the list

    print("flattened:")
    pprint.pprint(flattened_xs)


if __name__ == "__main__":
    fsum_for_floating_point_arithmetic()
    defaultdict_example()
    defaultdict_set()
    defaultdict_list()
    defaultdict_grouping()

    key_function()

    zip_string_transpose()
    zip_matrix_transpose()

    flattening_nested_lists()
