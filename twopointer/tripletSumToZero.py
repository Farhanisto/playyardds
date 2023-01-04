'''
Problem Statement 
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''


def triple_sum_to_zero(arr):
    arr.sort()
    result = []
    print(arr)

    for i in range(len(arr)):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            sum_here = arr[i]+arr[start]+arr[end]
            print(sum_here)
            # if sum_here == 0:
            #     result.append([arr[i], arr[start], arr[end]])
            #     continue
            # else:
            #     print(sum_here)
            #     if (sum_here > 0):
            #         end -= 1
            #     if sum_here < 0:
            #         start += 1
            if sum_here < 0:
                start += 1
            if sum_here > 0:
                end -= 1
            if sum_here == 0:
                result.append([arr[i], arr[start], arr[end]])
                start += 1
                end -= 1

    return result


print(triple_sum_to_zero([-5, 2, -1, -2, 3]))
