from operator import ge, le

import random
import math

class Heap(list):
    def __init__(self, arg, op=le):
        self.op = op
        super().__init__()
        for a in arg:
            self.push(a)

    def peek(self):
        return self[0]

    def pop(self):
        if not self:
            raise IndexError("pop from empty heap")
        result = self[0]
        last = self[-1]
        del self[-1]
        if not self:
            return result
        self[0] = last
        self.sift_down(0)
        return result

    def push(self, value):
        self.append(value)
        i = len(self) - 1
        self.sift_up(i)

    def replace(self, value):
        result = self[0]
        self.push(value)
        return result

    def replace_up(self, index, value):
        self[index] = value
        self.sift_up(index)

    def sift_up(self, index):
        if index == 0:
            return
        p = self.parent(index)
        if self.op(self[p], self[index]):
            self[index], self[p] = self[p], self[index]
            self.sift_up(p)

    def sift_down(self, index):
        a,b = self.children(index)
        if a + 1 >= len(self):
            return
        if b + 1 >= len(self):
            child = a
        else:
            if self[a] >= self[b]:
                child = a
            else:
                child = b
        if self.op(self[index], self[child]):
            self[index], self[child] = self[child], self[index]
            self.sift_down(child)

    def row(self, index):
        return int(math.log(index+1, 2))

    def parent(self, index):
        r = self.row(index)
        pos = index - (2**r - 1)
        return (2**(r-1)-1) + int(pos/2)

    def children(self, index):
        r = self.row(index)
        pos = index - (2**r - 1)

        return (2**(r+1)-1) + 2*pos, (2**(r+1)-1) + 2*pos+1

    def __repr__(self):
        if len(self) == 0:
            num_rows = 0
        else:
            num_rows = self.row(len(self)-1) + 1
        s = ""
        for row in range(num_rows):
            s += str(self[2**row-1:2**(row+1)-1]) + "\n"
        if not s:
            return "[]"
        return s.strip()

if __name__ == '__main__':
    random.seed(0)
    L = [random.randint(0,100) for _ in range(30)]

    H = Heap(arg=L, op=le)
    print(H)
    print("-"*20)
    for _ in range(8):
        print(H.pop())
        print(H)
        print("-"*20)
    
