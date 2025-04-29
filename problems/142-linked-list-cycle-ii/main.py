from typing import Optional


class ListNode:
    def __init__(self, val: int, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while slow and fast:
            if fast.next is None:
                return None
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        slow = head
        while slow and fast:
            if fast.next is None:
                return None
            if slow == fast:
                return slow
            slow, fast = slow.next, fast.next
        return None
