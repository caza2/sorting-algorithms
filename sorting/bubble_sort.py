from typing import Optional

# Bubble Sort. Time O(n^2), space O(1)

def bubble_sort(arr: Optional[list[int]]) -> Optional[list[int]]:

    if not arr or len(arr) <= 1:
        return arr

    max_swapped: int = 0
    made_swap: bool = True

    while made_swap:
        made_swap = False

        for i in range(len(arr) - 1 - max_swapped):
            if arr[i] > arr[i+1]:
                made_swap = True
                arr[i], arr[i+1] = arr[i+1], arr[i]

        max_swapped += 1

    return arr