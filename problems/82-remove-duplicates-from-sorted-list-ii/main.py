from typing import Optional


class ListNode:
    def __init__(self, val: int, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = orig = ListNode(0, head)
        while head and head.next:
            delete_next = False
            while head.next and head.next.next and head.next.val == head.next.next.val:
                delete_next = True
                head.next.next = head.next.next.next
            if delete_next:
                head.next = head.next.next
            else:
                head = head.next
        return orig.next
