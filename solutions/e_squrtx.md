# Question
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

 
Example :
```
Input: x = 4
Output: 2
Input: x = 8
Output: 2
```

# initial solutions:

## S1:correct but too long
```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1: 
            return 1
        elif x==0:
            return 0
        l,r=0,x
        while r>l:
            mid=(l+r)//2
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r=mid
            else:
                l=mid
```


explanation: sliding two point and taking the middle to find the right result 
```
50 answer should be 7
first check midle point [0,50] -> 25 
then check [0,25] -> 12
then check [0,12] -> 6
then check [6,12] -> 9
then [6,9] -> 7
```
