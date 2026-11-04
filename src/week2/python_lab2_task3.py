"""
Lab 2.3 – Operator Frequency Counter
------------------------------------
Practice strings and dictionaries by counting characters.

Write a function `count_operators(expression)` that returns a dictionary
with how many times each operator character appears in the expression.

Rules:
- The dictionary ALWAYS has all six keys from OPERATORS, in that order,
  even when a count is 0. Hint: start with {op: 0 for op in OPERATORS}.
- Count character by character: the minus in "-5" counts as "-",
  and "**" counts as two "*".
- Every other character (digits, spaces, letters) is ignored.

In the main block: ask the user for an arithmetic expression, call
count_operators() and print the result.
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
    """Return a dict with the count of each operator in expression."""
    counts = {op: 0 for op in OPERATORS}
    for char in expression:
        if char in counts:
            counts[char] += 1
    return counts


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    expression = input("Enter an arithmetic expression: ")
    result = count_operators(expression)
    print(f"Operator counts: {result}")
