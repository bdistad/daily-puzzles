'''
Puzzle: Longest Common Prefix
Source: LeetCode

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longest_common_prefix(strings):

    first_string = strings[0]
    first_string_letters = [char for char in first_string]
    common_prefix_length = len(first_string)
    
    for string in strings[1:]:
        
        match_count = 0
        string_letters = [char for char in string]
        
        for i in range(0,len(first_string_letters)):
            if first_string_letters[i] == string_letters[i]:
                match_count = match_count + 1
            else:
                break

        if match_count < common_prefix_length:
            common_prefix_length = match_count

    return ''.join(first_string_letters[0:common_prefix_length])

#tests
test1 = ['recipe', 'resume', 'rest']
print(longest_common_prefix(test1))

test2 = ['red', 'green', 'blue']
print(longest_common_prefix(test2))














