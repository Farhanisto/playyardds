'''
Problem Statement 
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

def longest_subarray(arr, k):
    max_len= -float('inf')
    start = 0
    sum = 0
    replace = 0
    arr_copy = arr[:]
    
    for count,val in enumerate(arr):
        if val != 0 :
            sum += 1
        else:
            # do a replace

            while replace < k:
                # arr_copy[count] = 1
                sum +=1
                replace +=1
            if val != 0:
                start += 1
                max_len = max(max_len, sum)


            
        #do a replace check here
        # while replace < k:
        #     #if replace count is less than k, just add it to the sum
        #     if val == 0:
        #         arr_copy[count] = 1
        #         replace += 1
                
    return max_len


    