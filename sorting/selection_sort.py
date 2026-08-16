from typing import Optional

# Selection sort. Time O(n^2), space O(1)

def selection_sort(arr: Optional[list[int]]) -> Optional[list[int]]:

    if not arr or len(arr) <= 1:
        return arr

    for i in range(len(arr)-1):
        curr_min_index: int = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[curr_min_index]:
                curr_min_index = j

        arr[i], arr[curr_min_index] = arr[curr_min_index], arr[i]

    return arr