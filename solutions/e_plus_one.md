# Question
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 


```
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [9,9]
Output: [1,0,0]
Explanation: The array represents the integer 123.
```

# initial solutions:

## S1:
```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i,carry=1,1
        while (carry==1) & (i<=len(digits)):
            if digits[-i]+carry == 10:
                digits[-i]=0
                i+=1
            else:
                digits[-i]+=1
                carry=0

            if (carry==1) &(i==len(digits)+1):
                digits=[1]+digits
                i+=1
        return digits
```


# explanation

