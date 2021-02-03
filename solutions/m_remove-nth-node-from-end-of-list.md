# Question
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
```

# initial solutions:

## S1: time limit exceeded
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #first we compute the length of head
        count,adjust,length=head,head,1
        while (count.next): #not none, start from 1 because last node's next is None
            length+=1
            count=count.next
        print(length)
        if length==1: return None #if length==1, n==1 then it mean become empty
        if length==n: return head.next #if length==1 then remove the first node
        #the node before nodetoremove, its next should be nodetoremove.next
        #ex: node(2) to remove than node(1).next =node(3), 
        #the same as node(1).next=node(2).next and  node(1).next=node(1).next.next
        #length-n is the node to remove, so we go one before to adjust the next
        for i in range(length-n-1):
            adjust=adjust.next
        adjust.next=adjust.next.next
        return head
            
        

```
