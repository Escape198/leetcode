from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        if not self.queue1 and not self.queue2:
            self.queue1.append(value)
        elif self.queue1:
            self.queue1.append(value)
        else:
            self.queue2.append(value)

    def pop(self):
        if not self.queue1 and not self.queue2:
            raise IndexError("pop from empty stack")

        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()

    def top(self):
        if not self.queue1 and not self.queue2:
            raise IndexError("top from empty stack")

        if self.queue1:
            return self.queue1[-1]
        else:
            return self.queue2[-1]

    def is_empty(self):
        return not self.queue1 and not self.queue2


stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element:", stack.top())
print("Popped element:", stack.pop())
stack.push(4)
print("Top element:", stack.top())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())
