# url: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = ""
        node = head

        while node:
            num += str(node.val)
            node = node.next

        doubled_num = int(num) * 2
        num = str(doubled_num)
        return self.makeNewList(list(num))

    def makeNewList(self, values):
        head = ListNode(values[0])
        current = head

        # Agregar los nodos restantes
        for value in values[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = new_node
        return head


nodes = ListNode(9)
nodes.next = ListNode(9)
# nodes.next.next = ListNode(3)
nodes.next.next = None

solution = Solution()
a = solution.doubleIt(nodes)
while a:
    print(a.val)
    a = a.next

