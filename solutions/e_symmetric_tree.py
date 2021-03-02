# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkSym(self, node1, node2):
        # if one of the node is none we can check
        if not node1 or not node2:
            return node1 == node2
        else:
            # check the same, and continue next node
            # here 2 nodes might be different so we are checking the value
            return node1.val == node2.val and self.checkSym(node1.left, node2.right) and self.checkSym(node1.right, node2.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkSym(root, root)


a = TreeNode(2)
b = TreeNode(2)
a == b # return false