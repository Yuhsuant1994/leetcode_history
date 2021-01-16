"""
Given a string s, find the length of the longest substring without repeating characters. 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


# import numpy as np
# def find(s, searchch):
#     result=[0]+[i for i, char in enumerate(s) if searchch == char]+[len(s)]
#     return np.array(result)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        lookup_index={}
        if len(set(s))==1:
            max_len=1
        start_index=0
        for i in range(len(s)):
            if s[i] in lookup_index:
                start_index=max(lookup_index[s[i]],start_index)
            max_len=max(i-start_index+1,max_len)
            lookup_index[s[i]]=i+1
        return max_len
        