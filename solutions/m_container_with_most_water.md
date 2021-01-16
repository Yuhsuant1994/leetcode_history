# Question
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
```

# initial solutions:

## S1: time limit exceeded
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(height)):
            #for j in range(i,len(height)):
            for j in range(i,len(height)):
                w=j-i
                contain=w*min(height[i],height[j])
                result=contain if contain>result else result       
        return result
```

## s2: move from two side (no need to iterate all of the points)
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result,l,r=0,0, len(height)-1
        while (r>l):#stop when right is more than left
            contain=(r-l)*min(height[l],height[r])
            result=contain if contain>result else result
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return result

```

# explanation
2nd result is to have 2 pointers from both end, then move the smaller height point forward