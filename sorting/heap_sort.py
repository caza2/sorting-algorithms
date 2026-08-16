from typing import Optional
import heapq

# Heap sort with min heap built in class from heapq library. Time O(n log n), space O(n)
# TBC -> Own heapq library with heapify and heappop to code myself

def heap_sort(arr: Optional[list[int]]) -> Optional[list[int]]:

    if not arr or len(arr) <= 1:
        return arr

    sorted_arr: list[int] = []
    minHeap: list[int] = arr.copy()
    heapq.heapify(minHeap)

    for _ in range(len(arr)):
        sorted_arr.append(heapq.heappop(minHeap))

    return sorted_arr
