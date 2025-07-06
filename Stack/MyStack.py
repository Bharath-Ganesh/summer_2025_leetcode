from collections import deque


class MyStack:
    """
    Stack Operation : push(3), push(4), push(5), pop(), push(7), peek()
    Queue 1 : []
    Queue 2 : [5, 4, 3]
    """

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.appendleft(x)

    def pop_all_elements(self):
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp

    def pop(self) -> int:
        if self.empty():
            return -1
        self.pop_all_elements()
        return self.queue1.popleft()

    def top(self) -> int:
        if self.empty():
            return -1
        self.pop_all_elements()
        return self.queue1[0]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_3 = obj.top()
    print(param_3)
    param_2 = obj.pop()
    print(param_2)
    param_4 = obj.empty()
    print(param_4)