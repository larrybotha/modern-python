xs = [1, 2, 3]
ys = [4, 5, 6]
zs = "abracadabra"


def concat_with_slices():
    zs = xs[:2] + ys[:2]

    print(f"zs: {zs}")
    print()


def counting_in_lists():
    print(f"count of 'a' in {zs}: {zs.count('a')}")
    print()


def sorting_via_coercion():
    print(f"sorting {zs}: {sorted(zs)}")
    print()


if __name__ == "__main__":
    concat_with_slices()
    counting_in_lists()
    sorting_via_coercion()
