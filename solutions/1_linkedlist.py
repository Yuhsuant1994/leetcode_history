class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next



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
p3=ListNode(3)
p2=ListNode(2,p3)
p1=ListNode(1,p2) #head


head = p1
list_node = list() 
list_v = list()
while head.next is not None:
    list_node.append(head)
    list_v.append(head.val)
    head = head.next
    
current_node = head
while list_node:
    current_node.next = list_node.pop()
    current_node = current_node.next
cu