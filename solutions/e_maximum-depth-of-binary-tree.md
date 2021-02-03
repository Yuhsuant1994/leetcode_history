# Question
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

# initial solutions:

## S1:correct but too long
```python
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level, current_max=0,0
        check_later=list()
        if root: 
            level+=1 #if it's not an empty tree
        else:
            return level
        #if (not root.left) & (not root.right) then stop
        #level==1 meaning only the first entrence
        #len(check_later)>0 meaning the loop to check is there
        if (not root.left) & ( not root.right ): return level #level 1
        while (len(check_later)>0)|(level==1): 
            if level!=1: #check loop
                check_ref=check_later.pop()
                level=check_ref[0]
                root=check_ref[1]
            while (root.left is not None) | (root.right is not None):
                level+=1
                if not root.left:
                    root=root.right
                elif not root.right:
                    root=root.left
                else:
                    check_later+=[[level,root.right]]
                    root=root.left
                    
            if level>current_max: current_max=level
        
        return current_max
p7=TreeNode(7)
p15=TreeNode(15)
p9=TreeNode(9)
p20=TreeNode(20,p15,p7)
p3=TreeNode(3,p9,p20)
s=Solution()
s.maxDepth(p3)
s.maxDepth(p7)     
```

