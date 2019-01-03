import random

class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, v):
        N = Node(v)
        N.prev = self.tail
        N.next = None
        if self.head is None:
            self.head = N
        else:
            self.tail.next = N
        self.tail = N
        self.length += 1

    def pop(self):
        if self.head is None:
            raise EmptyQueueError
        result = self.head
        self.head = result.next
        self.length -= 1
        return result.value

    def __bool__(self):
        if self.head is None:
            return False
        return True

    def __repr__(self):
        return '<Queue, len={}, head={}, tail={}>'.format(self.length, self.head.value, self.tail.value)

if __name__ == '__main__':
    random.seed(0)
    Q = Queue()
    for _ in range(20):
        Q.push(random.randint(0,100))

    print(Q)
    while Q:
        print(Q.pop())





