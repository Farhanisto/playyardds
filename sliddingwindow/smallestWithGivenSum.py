'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

def smallest_subarray_with_given_sum(arr, s):
   smallest, sum, start = float('inf'), 0, 0
   for i in range(len(arr)):
        if arr[i] >= s:
            return 1
        sum += arr[i]
       
        # if sum >= s:
        #     smallest = min(i+ 1 - start , smallest)
        #     sum -= arr[start]
        #     start += 1

        while sum >= s and i< len(arr):
            smallest = min(i - start + 1, smallest)
            sum -= arr[start]
            start += 1
  
   return 0 if smallest == float('inf') else smallest

