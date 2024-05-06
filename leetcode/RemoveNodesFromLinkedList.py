# https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        stack = []
        current = head
        while current:
            while stack and current.val > stack[-1].val:
                stack.pop()

            stack.append(current)
            current = current.next

        dummy = ListNode(0)
        prev = dummy
        for node in stack:
            prev.next = node
            prev = prev.next
        prev.next = None

        return dummy.next
