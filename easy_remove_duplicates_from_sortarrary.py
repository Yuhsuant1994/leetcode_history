"""
Given a sorted array nums, remove the duplicates in-place such that each element appears 
only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input 
array in-place with O(1) extra memory.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums 
being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set 
beyond the returned length.
"""





"""
delete an element from the array is O(n) complexity
the goal is not to remove the elements, but to swap 
to the end and then return the length of the array 
so that you could take a slice of it and get all unique elems
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while (i+1<len(nums)):
            if nums[i]==nums[i+1]:
                del nums[i+1]
            else: 
                i+=1
        return len(nums)
#much faster switch result
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        to_replace=0
        for i in range(len(nums)):
            if (i!=to_replace)&(nums[to_replace]!=nums[i]):
                to_replace+=1
                nums[to_replace]=nums[i]
        return to_replace+1