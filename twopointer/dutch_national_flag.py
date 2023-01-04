"""
This is an algorithm for partitioning an array into various sections, in
place.
The sections depend on the actual problem. It can be:
[True: False]
[evens:odds]
[smaller:equal:larger]
PS: Use lomuto partitioning scheme when partitioning into 2 sides (e.g. for
quick sort we partition as [equal or less than pivot: greater than pivot]).
To partition into more than 2 sides, use dutch national flag
"""


def dutch_national_flag(arr, pivot_idx):
    start, equal, end = 0, 0, len(arr) - 1
    pivot = arr[pivot_idx]
    while equal < end:
        if arr[equal] < pivot:
            arr[start], arr[equal] = arr[equal], arr[start]
            start += 1
            equal += 1
        elif pivot == arr[equal]:
            equal += 1
        else:
            arr[equal], arr[end] = arr[end], arr[equal]
            end -= 1

    return arr
