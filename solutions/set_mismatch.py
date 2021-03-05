"""
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in 
the form of an array.
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        for i in range(len(nums)):
            # missing
            if i+1 not in nums:
                result = result + [i+1]
            # check duplicated
            if nums[i] in nums[i+1:]:
                result = [nums[i]] + result 
            # stop if found
            if len(result) == 2:
                return result
        