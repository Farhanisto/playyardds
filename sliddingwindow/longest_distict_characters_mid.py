'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''


def longest_distict_characters(str, k):
    max_len = 0
    curr_len = 0
    start_idx = 0
    chars = set()
    for end_idx in range(len(str)):
        curr_len += 1
        if (end_idx - start_idx + 1 - len(chars)) >= k:
            chars.clear()
            curr_len -= 1
            start_idx += 1
        chars.add(str[end_idx])
        max_len = max(max_len, end_idx - start_idx + 1)
    return max_len


print(longest_distict_characters("araaci", 2))
print(longest_distict_characters("cbbebi", 3))
print(longest_distict_characters("cbbebi", 1))
print(longest_distict_characters("cbbebi", 3))
print(longest_distict_characters("", 1))
