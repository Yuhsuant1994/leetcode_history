class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(list_current=[], list_result=[]):
            if len(list_current) == len(nums):
                list_result.append(list_current)
                return
            for num in nums:
                if num not in list_current:
                    backtracking(list_current + [num])
            return list_result
        return backtracking()
