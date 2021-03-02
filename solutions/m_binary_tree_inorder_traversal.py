"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

video: different between preorder, inorder, postorder traversal
https://www.youtube.com/watch?v=WLvU5EQVZqY
preorder: root, left, right
inorder: left root right
postorder: left right root
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive way
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return list()

# initial iterative result
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_unused_node, list_result_value = list(), list()
        while root:
            if root in list_unused_node:
                list_result_value = list_result_value + [root.val]
                list_unused_node.pop()
                if root.right:
                    root = root.right
                elif list_unused_node:
                    root = list_unused_node[-1]
                else:
                    root = None
            elif root.left:
                list_unused_node = list_unused_node + [root]
                root = root.left
            elif root.right:
                list_result_value = list_result_value + [root.val]
                root = root.right
            elif root.left is None and root.right is None:
                list_result_value = list_result_value + [root.val]
                if list_unused_node:
                    root = list_unused_node[-1]
                else: 
                    root = None
        return list_result_value
        


    

    
