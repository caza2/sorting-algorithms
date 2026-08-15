from typing import Optional

# Merge Sort. Time O(n log n). Space O(n)

def merge_sort(arr: Optional[list[int]]) -> Optional[list[int]]:

    if arr is None:
        return
    
    if len(arr) <= 1:
        return arr

    def merge(arr1: list[int], arr2: list[int]) -> list[int]:
        # Merges two sorted arrays
        new_arr: list[int] = []
        index_1, index_2 = 0, 0

        while index_1 < len(arr1) and index_2 < len(arr2):
            if arr1[index_1] < arr2[index_2]:
                new_arr.append(arr1[index_1])
                index_1 += 1
            else:
                new_arr.append(arr2[index_2])
                index_2 += 1

        while index_1 < len(arr1):
            new_arr.append(arr1[index_1])
            index_1 += 1

        while index_2 < len(arr2):
            new_arr.append(arr2[index_2])
            index_2 += 1

        return new_arr

    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))