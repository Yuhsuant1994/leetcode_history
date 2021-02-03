# Question
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

# initial solutions:

## S1:correct but too long
```python
s=s[::-1]?        
```

as we are not returning, when we run this we realized that s didn't change "in-place",
in this case it can help already with the solution

## s2:solution

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i=0
        for char in s[::-1]:
            s[i]=char
            i+=1
```

