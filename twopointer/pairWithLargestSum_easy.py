'''
Problem Statement 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''


def pair_with_largest_sum(arr, target):
    start = 0
    end = len(arr) - 1
    # print(start, end)
    while start < end:
        current_sum = arr[start] + arr[end]
        if current_sum == target:
            return [start, end]
        elif current_sum > target:
            end -= 1
        else:
            start += 1
    return [-1, -1]


print(pair_with_largest_sum([1, 2, 3, 4, 6], 6))
print(pair_with_largest_sum([2, 5, 9, 11], 11))
# print(pair_with_largest_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 50))
