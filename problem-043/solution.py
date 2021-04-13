class Stack:
    def __init__(self):
        self.stack: List[int] = []
        self.max_stack: List[int] = []

    def push(self, val: int):
        self.stack.append(val)
        if not self.max_stack:
            self.max_stack.append(val)
        elif val > self.max_stack[-1]:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self) -> int:
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()

    def max(self) -> int:
        return self.max_stack[-1]


stack = Stack()
nums = [4, 2, 3, 5, 1]
for num in nums:
    stack.push(num)

assert stack.max() == 5
assert stack.pop() == 1
assert stack.max() == 5
assert stack.pop() == 5
assert stack.max() == 4