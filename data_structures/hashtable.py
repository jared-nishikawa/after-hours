import random

class LNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = None

    def __bool__(self):
        if self.head is None:
            return False
        return True

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.key, cur.value
            cur = cur.next

    def push(self, key, value):
        N = LNode(key, value)
        N.next = None
        cur = self.head

        if cur is None:
            self.head = N
            return 1

        if cur.key == N.key:
            N.next = cur.next
            self.head = N
            return 0

        while cur is not None:
            nxt = cur.next
            if nxt is None:
                cur.next = N
                return 0

            if nxt.key == key:
                cur.next = N
                N.next = nxt.next
                return 0
            cur = cur.next

    def lookup(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def __repr__(self):
        result = "["
        cur = self.head
        if not cur:
            return "[]"
        while cur.next is not None:
            result += str(cur.value) + ", "
            cur = cur.next
        result += str(cur.value) + "]"
        return result

class HashTable:
    def __init__(self, size=256, max_load=0.7):
        self.max_load = max_load
        self.size = size
        self.used_buckets = 0
        self.buckets = [LinkedList() for _ in range(self.size)]

    def __setitem__(self, key, value):
        h = hash(key) % self.size
        self.used_buckets += self.buckets[h].push(key, value)
        if self.used_buckets/self.size > self.max_load:
            self.resize()

    def __getitem__(self, key):
        h = hash(key) % self.size
        return self.buckets[h].lookup(key)

    def __repr__(self):
        layers = '\n'.join(bucket.__repr__() for bucket in self.buckets if bucket)
        return layers

    def resize(self):
        self.size = 2*self.size
        self.used_buckets = 0
        old = self.buckets
        self.buckets = [LinkedList() for _ in range(self.size)]
        for bucket in old:
            for k,v in bucket:
                self[k] = v

    def load(self):
        return self.used_buckets, self.size, self.used_buckets/self.size

if __name__ == '__main__':
    random.seed(0)
    H = HashTable(size=16, max_load=0.7)
    keys = set()
    for _ in range(24):
        k = random.randint(0,1024)
        v = random.randint(0,2**32)
        keys.add(k)
        H[k] = v
        print(H.load())
    print(keys)
    for k in keys:
        print(H[k])

