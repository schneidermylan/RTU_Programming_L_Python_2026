"""
Lab 2.1 – Simple Datasets and Aggregates
----------------------------------------
Practice lists, dictionaries and tuples by computing simple aggregates.

Write these functions:
- average(values)                -> float
    Average of a list of numbers. Return 0.0 if the list is empty.
- largest_city(populations)      -> tuple (name, population)
    The city with the LARGEST population.
- smallest_city(populations)    -> tuple (name, population)
    The city with the SMALLEST population.
- total_population(populations) -> int
    Sum of all populations. Return 0 if the dict is empty.

`populations` is a dictionary like {"Riga": 605000, "Daugavpils": 78000}.
For largest_city() and smallest_city():
- If two cities tie, return the one that comes FIRST in the dictionary.
- If the dictionary is empty, return ("", 0).
- Built-ins such as sum(), len(), max() and min() are allowed.
  Hint: max(populations, key=populations.get) gives the key with the
  largest value.

In the main block: create your OWN datasets (a list `temperatures` with
7 daily temperatures, and a dict `city_population` with at least 5 cities),
call the functions, and print the results. Print the average with
1 decimal place.
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    city = max(populations, key=populations.get)
    return (city, populations[city])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    city = min(populations, key=populations.get)
    return (city, populations[city])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    if not populations:
        return 0
    return sum(populations.values())


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.

    # Create your own datasets
    temperatures = [4.5, 3.8, 5.2, 4.1, 6.0, 3.5, 4.9]
    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Jurmala": 51000
    }

    # Call the functions and print the results
    avg_temp = average(temperatures)
    largest = largest_city(city_population)
    smallest = smallest_city(city_population)
    total_pop = total_population(city_population)

    print(f"Average temperature: {avg_temp:.1f}")
    print(f"Largest city: {largest[0]} - {largest[1]}")
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")
    print(f"Total population: {total_pop}")
