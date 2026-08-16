import random
from typing import Optional, Callable
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.bubble_sort import bubble_sort

def run_tests(sort_function: Callable[[Optional[list[int]]], Optional[list[int]]]):

    test_cases: list[tuple[Optional[list[int]], Optional[list[int]]]] = [
        ([3, 1, 2], [1, 2, 3]),
        ([], []),
        (None, None),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2, 2, 1], [1, 2, 2]),
        ([-3, 2, -1, 0], [-3, -1, 0, 2]),
    ]
    # Add 100 random test cases
    for _ in range(100):
        size: int = random.randint(0, 100)
        nums: list[int] = [random.randint(-1000, 1000) for _ in range(size)]

        test_cases.append((nums, sorted(nums)))

    for i, (input_list, expected) in enumerate(test_cases, start=1):

        test_input = input_list.copy() if input_list is not None else None
        result = sort_function(test_input)

        assert result == expected, (
            f"Function: {sort_function.__name__}"
            f"Test {i} failed\n"
            f"Input:    {input_list}\n"
            f"Expected: {expected}\n"
            f"Got:      {result}"
        )

    print(f"{sort_function.__name__}: all {len(test_cases)} tests passed!")


if __name__ == "__main__":
    run_tests(sort_function=merge_sort)
    run_tests(sort_function=quick_sort)
    run_tests(sort_function=bubble_sort)