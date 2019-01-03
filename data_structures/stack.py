import random

class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, v):
        N = Node(v)
        N.prev = self.head
        self.head = N
        self.length += 1

    def pop(self):
        if self.head is None:
            raise EmptyStackError
        result = self.head
        self.head = result.prev
        self.length -= 1
        return result.value

    def __bool__(self):
        if self.head is None:
            return False
        return True

    def __repr__(self):
        return '<Stack, len={}, head={}>'.format(self.length, self.head.value)

if __name__ == '__main__':
    random.seed(0)
    s = Stack()
    for _ in range(20):
        s.push(random.randint(0,100))

    print(s)
    while s:
        print(s.pop())





