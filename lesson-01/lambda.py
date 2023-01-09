def immediately_invoked():
    print(f"immediately invoked: {(lambda x: x**2)(5)}")
    print()


def multiple_params():
    product = lambda x, y: x * y

    print(f"product of 4 and 5: {product(4,5)}")
    print()


def thunk():
    x = 5
    y = 6
    fn = lambda: x * y

    print(f"deferred execution: {fn()}")
    print()


def chained_comparisons():
    x = 6
    y = 5
    z = 10

    if y > x > z:
        print("x is between y and z")
    else:
        print("x is not between y and z")

    print()


if __name__ == "__main__":
    immediately_invoked()
    multiple_params()
    thunk()
    chained_comparisons()
