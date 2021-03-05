"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 
(note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, 
it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; 
There are 3 nodes before the intersected node in B.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Initial thought: too long

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        check = headA
        while check: # not None
            ref = headB
            while ref:
                if check == ref:
                    return check
                else:
                    ref = ref.next
            check = check.next
        return None
                
# Second thought: store value -> too long
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Second thought: store value
        listA, listB = list(), list()
        pointA, pointB = headA, headB
        while pointA or pointB:
            if pointA:
                if pointA.val in listB:
                    check = headB
                    for i in listB:
                        if check == pointA:
                            return pointA
                        check = check.next
                listA = listA + [pointA.val]
                pointA = pointA.next

            if pointB:
                if pointB.val in listA:
                    check = headA
                    for i in listA:
                        if check == pointB:
                            return pointB
                        check = check.next
                listB = listB + [pointB.val]
                pointB = pointB.next
        return None

# third: backward
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        # Second thought: store value
        listA, listB, inter = list(), list(), list()
        pointA, pointB = headA, headB
        i = 1
		
		# get full list of value
        while pointA:
            listA = listA + [pointA.val]
            pointA = pointA.next
        while pointB:
            listB = listB + [pointB.val]
            pointB = pointB.next
		
		# find value intersaction
        while i < min(len(listA), len(listB)):
            if listA[-i:] == listB[-i:]:
                i = i + 1
            else:
                i = i - 1
                break
        if i == 0: 
            return None
			
		# at least skip how many nodes
        skipA = len(listA) - i
        skipB = len(listB) - i
        pointA, pointB = headA, headB
        for s in range(skipA):
            pointA = pointA.next
        for s in range(skipB):
            pointB = pointB.next
        		
		# value the same don't means they are the same node    
        while pointA and pointB:
            if pointA == pointB:
                return pointA
            else:
                pointA = pointA.next
                pointB = pointB.next
        return None