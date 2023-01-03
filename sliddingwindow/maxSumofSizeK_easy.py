'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''


def max_sub_array_k_size(arr, k):
    '''
    Time Complexity - O(n)
    Space Complexity - O(1)
    '''
    curr_sum, max_sum, start = 0, -float('inf'), 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if i >= k-1 and i < len(arr)-1:
            max_sum = max(max_sum, curr_sum)
            # print(start)
            curr_sum -= arr[start]
            start += 1
    return max_sum
