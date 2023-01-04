'''
Triplet Sum Close to Target (medium)
Problem Statement 
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''


def find_closest_sum(arr, target):
    arr.sort()
    result = sum(arr[:3])

    for i in range(len(arr)-2):
        s = i+1
        e = len(arr) - 1

        while s < e:
            sum_here = arr[i] + arr[s] + arr[e]

            if (abs(sum_here - target) < abs(result - target)):
                result = sum_here
            if sum_here < target:
                s += 1
            else:
                e -= 1
    return result


print(find_closest_sum([-3, -1, 1, 2], 1))
