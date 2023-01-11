from collections import OrderedDict, deque
from typing import Deque, List, Optional, Tuple

x: int = 10


def f(x: int, y: Optional[int] = None) -> int:
    return x + y if y else 20


y: OrderedDict = OrderedDict()


def g(xs: List[int]) -> None:
    print(len(xs))
    print(xs[2])

    for x in xs:
        print(x)

    print()


g([10, 20, 30])

hts: List[float] = [97.1, 102.5, 97.5]
person: Tuple[str, int] = ("Joe", 5 * 12 + 11)
info: Tuple[str, ...] = ("a", "b", "c")
fifo: Deque = deque()

print(f"answer is {x} today")
