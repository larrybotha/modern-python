X = "my string"

if __name__ == "__main__":
    print(f"{X!r} is the repr of {X}")

    print(f"'{type(X).__name__}' is the name of the type of X")
