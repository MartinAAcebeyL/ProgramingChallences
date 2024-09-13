# https://leetcode.com/problems/merge-in-between-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        current = list1

        count = 0
        before_a, after_b = None, None

        while current and current.next:
            if count == a - 1:
                before_a = current
            if count == b:
                after_b = current.next
                break
            current = current.next
            count += 1
        before_a.next = list2
        current = list2

        while current and current.next:
            current = current.next

        current.next = after_b

        return list1
[10, 1, 13, 6, 9, 5]
3
4
[1000000, 1000001, 1000002]
[0, 1, 2, 3, 4, 5, 6]
2
5
[1000000, 1000001, 1000002, 1000003, 1000004]
[0, 1, 2, 3, 4, 5, 6]
2
3
[1000000, 1000001, 1000002, 1000003, 1000004]
