# Question
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

# initial solutions:

## S1: time limit exceeded
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i=0
        result=list()
        if len(nums)<3:return result
        nums=sorted(nums,reverse=True)
        while (i<len(nums)-2) &(nums[i]!=0):
            #stop until the nums is through or until 0
            l=i+1
            r=len(nums)-1
            while r>l: #try to make nums[i] to 0
                if nums[i]+nums[r]+nums[l]==0:
                    if [nums[i],nums[l],nums[r]] not in result: 
                        result+=[[nums[i],nums[l],nums[r]]]
                    l+=1
                elif nums[i]+nums[r]+nums[l]>0:
                    l+=1
                else:
                    r-=1
            i+=1
        if nums.count(0)>=3: result=result+[[0,0,0]]
        return result      
```

# explanation
example [-1,0,1,2,-1,-4] first I want to sort the list from large to small, 
so that we only need to iterate one by one. [2, 1, 0, -1, -1, -4].
then we should check [2,1].
start checking from 2, then the 2 number in the list after the checknum [1, 0, -1, -1, -4]
should be adding up to -2. for the subset I use 2 pointers one from the left one from the 
right. if adding up is too big then the left should be moving one step to go smaller, 
if too small then right should be moving to left to go bigger. iterate until two pointer meets.


exception: 
1. len<3 -> []
2. more than 3 0 in the list then need to add [0,0,0]