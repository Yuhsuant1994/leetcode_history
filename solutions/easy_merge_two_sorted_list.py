"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode()
        next_result=result
        while (l1 or l2):
            v1=l1.val if l1 else None
            v2=l2.val if l2 else None
            if (v1 is not None)&(v2 is not None):   
                next_result.next=(ListNode(v1) if v1<=v2 else ListNode(v2))
                l1=(l1.next if v1<=v2 else l1)
                l2=(l2.next if v1>v2 else l2)
                # if v1<=v2:
                #     next_result.next=ListNode(v1)
                #     l1=(l1.next if l1 else None)
                # else:
                #     next_result.next=ListNode(v2)
                #     l2=(l2.next if l2 else None)
            else:
                next_result.next=(ListNode(v1) if v2 is None else ListNode(v2))
                l1=(l1.next if v2 is None else l1)
                l2=(l2.next if v1 is None else l2)
            # if (v1 is not None) & (v2 is None):
            #     next_result.next=ListNode(v1)
            #     l1=(l1.next if l1 else None)
            # if (v1 is None)&(v2 is not None):
            #     next_result.next=ListNode(v2)
            #     l2=(l2.next if l2 else None)
            next_result=next_result.next
        return result.next
            
        