# Question
backtracking

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
```
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]```

[reference video](https://www.youtube.com/watch?v=sz1qaKt0KGQ&feature=emb_logo)


## S1: 
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def inner(curr,l,r):
            
            # if current string hit n*2
            # thats when you back out!
            if len(curr) == n*2:
                res.append(curr)
                return
            
            # keep adding left parens until no more remaining
            if l>0:
                inner(curr+"(",l-1,r)
                
            # keep adding right parens if a left matches it
            # and there are remaining
            if r>0 and l<r:
                inner(curr+")",l,r-1)
                    
        inner("",n,n)
        return res
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