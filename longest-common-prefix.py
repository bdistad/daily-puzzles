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
from typing import List
def longest_common_prefix(strings):
    prefix_length = dict()
    for i in range(0,len(strings)):
        for x in range(i, len(strings)):
            print('i: ' + str(i) + ' x: ' + str(x))
            if x+1 < len(strings):
                string_1_letters = [char for char in strings[i]] 
                string_2_letters = [char for char in strings[x+1]]
                
                #compare each letter 
     
    return None

string1 = ['recipe', 'resume', 'rest']
string2 = ['red', 'green', 'blue']
print(longest_common_prefix(string1))
#print(longest_common_prefix(string2))














