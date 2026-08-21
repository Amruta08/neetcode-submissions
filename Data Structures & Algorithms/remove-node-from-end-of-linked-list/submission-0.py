# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # 1. Move fast pointer 'n' steps ahead
        while n > 0:
            fast = fast.next
            n -= 1
        
        # 2. Move slow and fast pointer, untill fast reaches null
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 3. Update pointers to delete node
        slow.next = slow.next.next
        return dummy.next
        