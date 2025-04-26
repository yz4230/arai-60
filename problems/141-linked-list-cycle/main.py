# Definition for singly-linked list.
from typing import Optional


class ListNode:
    # val: int
    # next: Optional["ListNode"]
    def __init__(self, val: int, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        if head == head.next:
            return True
        curr = head
        while curr:
            if curr.next == head:
                return True
            curr.next, curr = head, curr.next
        return False
