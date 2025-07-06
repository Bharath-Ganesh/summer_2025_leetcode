class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.arr = [-1] * k
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.arr[self.front] = -1
        self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        # one slot of “distinction”: full when advancing rear would hit front
        return (self.rear + 1) % self.size == self.front


if __name__ == '__main__':
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(1)
    myCircularQueue.enQueue(2)
    myCircularQueue.enQueue(3)
    myCircularQueue.enQueue(4)
    myCircularQueue.Rear()
    myCircularQueue.isFull()
    myCircularQueue.deQueue()
    myCircularQueue.enQueue(4)
    myCircularQueue.Rear()