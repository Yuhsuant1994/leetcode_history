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
p6 = TreeNode(6)
p5 = TreeNode(7)
p4 = TreeNode(15)
p3 = TreeNode(20)#, p6, None)
p2 = TreeNode(9, p4, p5)
p1 = TreeNode(3, p2, p3)
#s = Solution()
#s.maxDepth(p3)
#s.maxDepth(p7)  
p10 = TreeNode(1)  
p30 = TreeNode(3, p10, None)
p20 = TreeNode(2, p30, None)

treeDict = dict()
def createTreeDict(treeDict, i, node):
    if node:
        if i in treeDict:
            treeDict[i] = treeDict[i] + [node.val]
        else:
            treeDict[i] = [node.val]
        return createTreeDict(treeDict, i+1, node.left), createTreeDict(treeDict, i+1, node.right)
    else:
       return

createTreeDict(treeDict, 0, p1)
result = list()
for level in range(len(treeDict)):
    result = result + [sum(treeDict[level]) / len(treeDict[level])]
    print(result)




# iterative
root = p20
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
        root = list_unused_node[-1]

print('hi')


