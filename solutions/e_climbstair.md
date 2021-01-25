# Question
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
```

# initial solutions:

## S1:fibonacci sequence
```python
class Solution(object):        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #fibonacci sequence
        a,b=0,1 #result=a+b
        for i in range(n):
            a,b=b,a+b
        return b
```

## s2:brutal solution
```
first calculate set number
then calculate the combination C(v,v1)-> 
v is the length of 1 and 2
v1 is the number of 1
idea is that for example v=6 and v1=2, so it means in the length of 6 chose 2 of the number to be 1
```
```python
class Solution(object):        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        if n==1: return 1
        def fac(num): #we can use also math function
            fac=1
            for i in range(1,num+1):
                fac=fac*i
            return fac

        number_set=list()
        x,result=1,0
        
        while 2*x<=n:
            y=n-2*x
            number_set+=[[x+y,x]] 
            x+=1
            
        for c in number_set:
            result+=fac(c[0])/(fac(c[1])*fac(c[0]-c[1]))
        return result+1 #plus there's always a step of all 1

```
