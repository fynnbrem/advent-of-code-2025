import math
from typing import Literal


def do_chain_math(numbers: list[int], operator: Literal["*", "+"]) -> int:
    """Chains the `numbers` with the mathematical `operator`."""
    if operator == "*":
        return math.prod(numbers)
    elif operator == "+":
        return sum(numbers)
    else:
        raise ValueError("Invalid operator")
