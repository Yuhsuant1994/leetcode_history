"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
"""
#inital try good result
"""
Runtime: 12 ms, faster than 99.34% of Python online submissions for String to Integer (atoi).
Memory Usage: 13.9 MB, less than 6.55% of Python online submissions for String to Integer (atoi).
"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result,i=0, 0 
        s=s.lstrip()
        if len(s)==0:
            return 0 
        mini, maxi=-2**31, 2**31-1
        det= -1 if s[0]=='-' else 1
        s=s[1:] if s[0] in ['-','+'] else s
        
        while i < len(s):
            if s[:i+1].isdigit():
                i+=1
                result=int(s[:i])*det
            else:
                i=len(s)
        result=mini if result<mini else result
        result=maxi if result>maxi else result            
        return result

"""
Runtime: 16 ms, faster than 96.72% of Python online submissions for String to Integer (atoi).
Memory Usage: 13.5 MB, less than 53.58% of Python online submissions for String to Integer (atoi).
"""
#try to optimize memory-> reduce variable
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0 
        s=s.strip() 
        if len(s)==0:
            return 0 
        start=1 if s[0] in ['-','+'] else 0
        i=start
        while i < len(s):
            if s[start:i+1].isdigit():
                i+=1
                result=int(s[:i])
            else:
                i=len(s)
        result=-2**31 if result<-2**31 else result
        result=2**31-1 if result>2**31-1 else result            
        return result