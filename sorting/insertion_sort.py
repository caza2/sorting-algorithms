from typing import Optional

# Insert sort. Time O(n^2), O(1) space

def insertion_sort(arr: Optional[list[int]]) -> Optional[list[int]]: 

    if not arr or len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):

        j: int = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr