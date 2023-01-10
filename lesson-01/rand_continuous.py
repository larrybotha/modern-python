from random import expovariate, gauss, random, seed, triangular, uniform
from statistics import mean, stdev


def seeding():
    seed_value = 1

    seed(seed_value)
    xs = [random() for _ in range(10)]

    seed(seed_value)
    ys = [random() for _ in range(10)]

    seed(seed_value)
    zs = [random() for _ in range(10)]

    assert all([x == y for x, y in zip(xs, ys)]), "nope"
    assert all([x == z for x, z in zip(xs, zs)]), "nope"

    def join(vs):
        return "\n".join([str(v) for v in vs])

    print(f"xs: {join(xs)}\n")
    print(f"ys: {join(ys)}\n")
    print(f"zs: {join(zs)}")
    print()


def uniform_distribution_example():
    seed(1)
    xs = [uniform(0, 100) for _ in range(1000)]

    print(f"uniformly distributed mean:\n{mean(xs)}")
    print(f"uniformly distributed stdev:\n{stdev(xs)}")
    print()


def triangular_distribution_example():
    seed(1)
    xs = [triangular(0, 100) for _ in range(1000)]

    print(f"triangular distributed mean:\n{mean(xs)}")
    print(f"triangular distributed stdev:\n{stdev(xs)}")
    print()


def gaussian_distribution_example():
    seed(1)
    xs = [gauss(100, 15) for _ in range(1000)]

    print(f"gaussian distributed mean:\n{mean(xs)}")
    print(f"gaussian distributed stdev:\n{stdev(xs)}")
    print()


def expovariate_distribution_example():
    seed(1)
    xs = [expovariate(50) for _ in range(1000)]

    print(f"expovariate distributed mean:\n{mean(xs)}")
    print(f"expovariate distributed stdev:\n{stdev(xs)}")
    print()


if __name__ == "__main__":
    seeding()
    triangular_distribution_example()
    uniform_distribution_example()
    gaussian_distribution_example()
    expovariate_distribution_example()
