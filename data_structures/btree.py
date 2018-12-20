import random

def pad(n):
    return sum(2**i for i in range(1,n))

def print_tree(n, ons):
    for i in range(2**(n-1)):
        space = (pad(n)-i)*' '
        on = '/' + ' '*2*i + '\\'
        off = len(on)*' '
        group = [on if num else off for num in ons]
        print(space + ((pad(n+1)-2*i)*' ').join(group))

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def sort(self):
        nums = []
        if self.left:
            nums += self.left.sort()
        nums.append(self.value)

        if self.right:
            nums += self.right.sort()

        return nums

    def push(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.push(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.push(value)

    def display(self, indent=0, char='\t'):
        cur = self
        curlayer = [cur]
        vallayers = []
        while any(curlayer):
            layer = []
            for node in curlayer:
                if node:
                    layer.append(node.value)
                else:
                    layer.append(None)
            vallayers.append(layer)

            nextlayer = []
            for node in curlayer:
                if not node:
                    nextlayer.append(None)
                    nextlayer.append(None)
                else:
                    nextlayer.append(node.left)
                    nextlayer.append(node.right)
            curlayer = nextlayer

        for ind,layer in enumerate(vallayers):
            s_layer = []
            for i,v in enumerate(layer):
                if ind == 0:
                    parent = None
                else:
                    parent = vallayers[ind-1][i//2]
                if v is not None:
                    s_layer.append('%02d' % v)
                elif parent is not None:
                    s_layer.append('--')
                else:
                    s_layer.append('  ')
            o_layer = [1 if v is not None else 0 for v in layer]
            r = len(vallayers)-ind
            print(pad(r)*' ' + (pad(r+1)*' ').join(s_layer))
            if r == 1:
                break
            print_tree(r, o_layer)


random.seed(0)

root = Node(50)
for _ in range(9):
    val = random.randint(0,99)
    root.push(val)

root.display()

print(root.sort())
