'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''
#create a python function that takes a list and return and int
import math
def fruits(fruits:list)-> int:
    obj_fruits = {}
    # map(lambda fruit: obj_fruits[fruit]= 0 if fruit not in obj_fruits.keys() else obj_fruits += 1,fruits)

    for fruit in fruits:
        if(fruit not in obj_fruits.keys()):
            obj_fruits[fruit]=1
        else:
            obj_fruits[fruit] += 1

    # now that we have that we will create a list of obj_fruits.values() and use sliding window to find the largest 2 sum
    # 
    values = list(obj_fruits.values()) 

    sum = 0
    start = 0
    maxSum = -float('inf') 

    if len(fruits) <2:
        return


    for c,value in enumerate(values):
        # print(value)
        sum += value

        if(c >= 1):
            maxSum = max(sum, maxSum)
            sum -= values[start]
            start = c+1
    return maxSum




    