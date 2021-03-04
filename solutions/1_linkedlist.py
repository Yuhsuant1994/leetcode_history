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
p5=ListNode(5)
p4=ListNode(4,p5)
p21=ListNode(2,p4)
p22=ListNode(2,p4)
headB=ListNode(1,p21)
headA=ListNode(1,p22)
#head

# Second thought: store value
if not headA or not headB:
    print( None)
# Second thought: store value
listA, listB, inter = list(), list(), list()
pointA, pointB = headA, headB
i = 1
while pointA:
    listA = listA + [pointA.val]
    pointA = pointA.next
while pointB:
    listB = listB + [pointB.val]
    pointB = pointB.next
while i < min(len(listA), len(listB)):
    if listA[-i:] == listB[-i:]:
        i = i + 1
    else:
        i = i - 1
        break
if i == 0: 
    print(  None)
skipA = len(listA) - i
skipB = len(listB) - i
pointA, pointB = headA, headB
for s in range(skipA):
    pointA = pointA.next
for s in range(skipB):
    pointB = pointB.next
            
while pointA and pointB:
    if pointA == pointB:
        print(  pointA)
    else:
        pointA = pointA.next
        pointB = pointB.next
print(  None)