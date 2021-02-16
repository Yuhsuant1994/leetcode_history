# Question

Reverse a singly linked list.

```
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
``` 


# initial solutions:

## S1: iterated way
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        list_node = list()
        while head.next is not None:
            list_node.append(head)
            head = head.next
        current_node = head
        while list_node:
            current_node.next = list_node.pop()
            current_node = current_node.next
        current_node.next = None
        return head

```
