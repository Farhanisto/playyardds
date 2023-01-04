'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''


def remove_duplicates(arr):
    '''
    Time complexity: O(n)
    Space complexity: O(1)
    '''
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    start = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[start]:
            arr[start+1] = arr[i]
            start += 1
    return start+1


# print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
