# Question
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

# initial solutions:

## S1:
```python
class Solution:
    def maxSubArray(self, nums):
        result =min(nums)
        current_sum = 0        
        for num in nums:
            if num + current_sum > num:
                current_sum = num + current_sum
            else:
                current_sum = num
            
            if current_sum > result:
                result = current_sum
        
        return result

```


# explanation


