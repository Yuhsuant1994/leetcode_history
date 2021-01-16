"""
Given a 32-bit signed integer, reverse digits of an integer.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 0 when the reversed integer overflows.

Example:
Input: x = 120
Output: 21
"""

"""
Runtime: 32 ms, faster than 6.09% of Python online submissions for Reverse Integer.
Memory Usage: 13.7 MB, less than 13.80% of Python online submissions for Reverse Integer.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result=int(str(abs(x))[::-1])
        if x<0:
            result=result*-1
        if (-2**31<=result) & (2**31-1>=result):
            return result
        else:
            return 0