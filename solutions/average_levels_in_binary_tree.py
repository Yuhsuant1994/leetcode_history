"""
Given a non-empty binary tree, return the average value of the nodes on 
each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on 
level 2 is 11. Hence return [3, 14.5, 11].
"""
# Recursive Create a dictionary for the tree values, then to everage the result.
# note that we need to convert len to a float to get float division

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def createTreeDict(self, treeDict, i, node):
        if node:
            if i in treeDict:
                treeDict[i] = treeDict[i] + [node.val]
            else:
                treeDict[i] = [node.val]
            return self.createTreeDict(treeDict, i+1, node.left),\
                   self.createTreeDict(treeDict, i+1, node.right)
        else:
            return

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = list()
        treeDict = dict()
        self.createTreeDict(treeDict, 0, root)
        for l in range(len(treeDict)):
            result = result + [sum(treeDict[l]) / float(len(treeDict[l]))]
        return result