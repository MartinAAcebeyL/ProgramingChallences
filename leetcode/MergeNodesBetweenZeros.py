# url: https://leetcode.com/problems/merge-nodes-in-between-zeros/description/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    head = head.next
    aux = head
    while head and head.next:
        print(head)
        _next = head.next
        head.val += _next.val
        if _next.val == 0:
            head.next = _next.next
            head = _next.next
        else:
            head.next = _next.next
    return aux

[0, 3, 1, 0, 4, 5, 2, 0]
[0, 1, 0, 3, 0, 2, 2, 0]
