class MyCircularQueue:

    def __init__(self, k: int):
        self._queue = []
        self._k = k

    def enQueue(self, value: int) -> bool:
        if len(self._queue) == self._k:
            return False
        else:
            self._queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self._queue.pop(0)
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._queue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._queue[-1]

    def isEmpty(self) -> bool:
        if len(self._queue) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self._queue) == self._k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

if __name__ == "__main__":
    mcqueue = MyCircularQueue(8)
    print(mcqueue.enQueue(3))
    print(mcqueue.enQueue(9))
    print(mcqueue.enQueue(5))
    print(mcqueue.enQueue(0))
    print(mcqueue.deQueue())
    print(mcqueue.deQueue())
    print(mcqueue.isEmpty())
    print(mcqueue.isEmpty())
    print(mcqueue.Rear())
    print(mcqueue.Rear())
    print(mcqueue.deQueue())