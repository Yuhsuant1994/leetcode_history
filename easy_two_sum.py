"""
Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
Runtime: 28 ms, faster than 93.63% of Python online submissions for Two Sum.
Memory Usage: 13.5 MB, less than 81.47% of Python online submissions for Two Sum.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            rest=target-nums[i]
            if rest in nums:
                i1=nums.index(rest)
                if i!=i1:
                    return [i,i1]
                else:
                    continue

"""
Runtime: 56 ms, faster than 18.37% of Python online submissions for Two Sum.
Memory Usage: 13.7 MB, less than 16.35% of Python online submissions for Two Sum.
"""                    
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if (i1!=i2)&(nums[i1]+nums[i2]==target):
                    return [i1,i2]

        