# Question
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

# initial solutions:

## S1:creating extra memory
```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = list()
        for num in nums:
            if num in ls:
                ls.remove(num)
            else:
                ls = ls + [num]
        return ls.pop()
```

## s2:without creating extra list object

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums:
            num = nums[0]
            count = 0
            while num in nums:
                nums.remove(num)
                count = count + 1
            if count == 1: return(num) 
        
```
