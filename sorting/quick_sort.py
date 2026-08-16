from typing import Optional
from random import randint

# Quick sort. Time O(n log n). Space: O(1) in-place

def quick_sort(arr: Optional[list[int]]) -> Optional[list[int]]:

    if not arr or len(arr) <= 1:
        return arr

    def partition(left: int, right: int) -> None:

        if left >= right:
            return
        random_pivot: int = randint(left, right)
        pivot_val, pivot_index = arr[random_pivot], left
        arr[left], arr[random_pivot] = arr[random_pivot], arr[left]
        for curr in range(left+1, right+1):
            if arr[curr] < pivot_val:
                pivot_index += 1
                arr[curr], arr[pivot_index] = arr[pivot_index], arr[curr]
                
        arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
        
        partition(left, pivot_index-1)
        partition(pivot_index+1, right)

    partition(0, len(arr)-1)
    return arr
