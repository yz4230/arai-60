from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        orig = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next

        return orig
