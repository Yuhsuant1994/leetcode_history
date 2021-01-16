"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""

#solution 1: initial solution too slow
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=s[0]
        for index, char in enumerate(s):
            charlist= [i for i,c in enumerate(s) if (c==char)&(i>index)]
            if charlist:
                for checki in charlist[::-1]:
                    subs=s[index:checki+1]
                    if (subs==subs[::-1])&(len(subs)>len(result)):
                        result=subs

        return result

#solution 2: try slice window, fix start move end
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=''
        if len(s) <= 1 or s == s[::-1]:
            return s
        for start in range(len(s)):
            end=start+len(result) #this part is saving time already
            while end<len(s):
                substring=s[start:end+1]
                end+=1
                if (substring==substring[::-1]):
                    result=substring
        return result
    
#solution 3 two way slice window:
"""
Runtime: 5364 ms, faster than 19.09% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 13.9 MB, less than 24.43% of Python online submissions for Longest Palindromic Substring.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=s[0]
        for i in range(len(s)):
            #check for even case 'bb'
            l, r=i, i+1
            while (l>=0)&(r<=len(s)-1)&(s[l:r+1]==s[l:r+1][::-1]):
                if len(s[l:r+1])>len(result):
                    result=s[l:r+1]
                l,r=l-1,r+1
                
            #check for odd case 'bab'
            l, r=i, i+2
            while (l>=0)&(r<=len(s)-1)&(s[l:r+1]==s[l:r+1][::-1]):
                if len(s[l:r+1])>len(result):
                    result=s[l:r+1]
                l,r=l-1,r+1
                
        return result
    
##avoid duplication:
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=s[0]
        for i in range(len(s)):
            #check for even case 'bb'
            result=self.getReplaceResult(i,i+1,s,result)
            #check for odd case 'bab'
            result=self.getReplaceResult(i,i+2,s,result)         
        return result
    
    def getReplaceResult(self,l,r,s,result):
        while (l>=0)&(r<=len(s)-1)&(s[l:r+1]==s[l:r+1][::-1]):
                if len(s[l:r+1])>len(result):
                    result=s[l:r+1]
                l,r=l-1,r+1
        return result
        
        
    

    

    
