# Question
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

```
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

# initial solutions:

## S1: backtracking

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(list_current=list(), list_result=list()):
            if len(list_current) == len(nums):
                list_result.append(list_current)
                return
            for num in nums:
                if num not in list_current:
                    backtracking(list_current + [num])
            return list_result
        return backtracking()
```
