# Question
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

# initial solutions:

## S1:
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        to_replace=0
        if 0 not in nums: return nums
        for i in range(len(nums)):
            if (nums[i]!=0):
                inter=nums[to_replace]
                nums[to_replace]=nums[i]
                nums[i]=inter
                to_replace+=1

```

## s2: 
adding an `if` statement adding runtime
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        to_replace=0
        if 0 not in nums: return nums
        for i in range(len(nums)):
            if (nums[i]!=0):
                if i!=to_replace:
                    inter=nums[to_replace]
                    nums[to_replace]=nums[i]
                    nums[i]=inter
                to_replace+=1

```

# explanation
* `if 0 not in nums: return nums`: for case if there's no 0 in the list then nothing needs to be done
* to_replace is the index for the index for the first 0, later to be replace by non 0
	to_replace is added to the next one when to_replace is not 0

* iterate over all the index, if we find to_replace!=i meaning that there's 0 so we can switch 2 number. 
solution 2 we check if i==to_replace. however, solution one without anycheck is faster but switching the 
same index pointer would not affect the result.