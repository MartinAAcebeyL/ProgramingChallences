# url: https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
