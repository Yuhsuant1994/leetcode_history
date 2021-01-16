"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
"""

import re

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output= False
        s=re.sub('[^\[\]\(\)\{\}]', '', s)
        if (len(s)<=10**4) & (1<=len(s)):
            while '()' in s or '[]' in s or '{}' in s :
                s=s.replace('()','')\
                    .replace('[]','')\
                    .replace('{}','')
            if s=='':
                output=True
        return output
            
#good solutions
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_par= []
        s=re.sub('[^\[\]\(\)\{\}]', '', s)
        par_map={'{':'}','(':')','[':']'}
        for char in s:
            if char in par_map: #if exist in the key
                open_par.append(char)
            else:
                if open_par:
                    #open_par[-1]=open_par.pop() and open_par remove that item
                    if char!=par_map[open_par.pop()]:
                        return False
                else:
                    return False
        return len(open_par)==0
        