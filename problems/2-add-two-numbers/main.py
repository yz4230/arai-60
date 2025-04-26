from typing import Optional


class ListNode:
    def __init__(self, val=0, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            raise ValueError

        result: Optional[ListNode] = None
        first: Optional[ListNode] = None

        c = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + c
            c = s // 10
            s = s % 10
            if result:
                result.next = ListNode(s)
                result = result.next
            else:
                first = result = ListNode(s)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if result is None:
            raise ValueError

        if c > 0:
            result.next = ListNode(c)

        return first
