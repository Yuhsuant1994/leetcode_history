"""
Description:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up: Could you solve it without converting the integer to a string?
Example:
Input: x = 121
Output: true
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x>=0)&(str(x)==str(x)[::-1]):
            return True
        else:
            return False

#without converting to string

class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            num_digit=0
            while (x/(10**(num_digit)))>=1:
                num_digit=num_digit+1
            result=True
            for i in range(num_digit//2+1):
                if result==True: 
                    first=x//(10**(num_digit-i-1))
                    if first>9:
                        first=first%10
                    second=int((x/(10**(i)))%10)
                    while second>9:
                        second=second//10
                    if first != second:
                        result=False
        else: 
            result=False
        return result
    
