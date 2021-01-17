# Question
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
```

# initial solutions:

## S1:correct but too long
```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result=1
        if n<0:
            x=1/x
            n=abs(n)
        for i in range(n):
            result=result*x
        return result
        
        
```

## s2:better solution

```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
        n = abs(n)
        if n == 0:
            return 1
        temp = self.myPow(x,n//2)
        if n%2 == 0:
            return temp*temp
        else:
            return x*temp*temp

```

2^5: 2*p(2,2)*p(2,2) -> 2*p(2,1)*p(2,1)*p(2,1)*p(2,1)->2*2*2*2*2

# s3: even faster
```python
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = abs(n)
            
        c,val=1,x
        while n>2:
            if n%2!=0:
                c=c*val
            val=val*val
            n=n//2
                
        if n == 0:
            return 1
        elif n==1:
            return c*val
        else: #n==2:
            return c*val*val
```
explanation: 
```
2^11: 2*4^5 -> 2*4*16^2 -> 2*4*16*2
2^3: in the while loop (c==2, val=2*2, n==1) so stop return c*val=2*4
```
