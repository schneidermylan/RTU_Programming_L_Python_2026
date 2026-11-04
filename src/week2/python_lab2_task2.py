"""
Lab 2.2 – Comprehensions and Transformations
--------------------------------------------
Practice list, set and dictionary comprehensions.

Write these functions. Each one should return a SINGLE comprehension
(one line after `return`), not a for loop that appends:
- squares(numbers)      -> list : the square of each number, same order
- positives(numbers)    -> list : only the numbers greater than 0
                                (0 is NOT positive), same order
- even_squares(numbers) -> set  : the squares of the EVEN numbers only
                                (0 and negative even numbers count too)
- cubes(numbers)        -> dict : maps each number to its cube

In the main block: use the list NUMBERS below, call each function and
print the results.
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return a list with the square of each number (list comprehension)."""
    return [n ** 2 for n in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only the numbers greater than 0 (list comprehension)."""
    return [n for n in numbers if n > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return a set of the squares of the even numbers (set comprehension)."""
    return {n ** 2 for n in numbers if n % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dict mapping each number to its cube (dict comprehension)."""
    return {n: n ** 3 for n in numbers}


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")
