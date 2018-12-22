import random, time
import matplotlib.pyplot as plt
class TreeNode(object):
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasleftChild(self):
        return self.leftChild

    def hasrightChild(self):
        return self.rightChild


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def get_min(self):
        current = self.root
        while current.hasleftChild():
            current = current.leftChild
        return current

    def get_max(self):
        current = self.root
        while current.hasrightChild():
            current = current.rightChild
        return current

    def add_node(self, key, node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = TreeNode(key)

        else:
            if key <= node.key:
                if node.leftChild is None:
                    node.leftChild = TreeNode(key)
                    node.leftChild.parent = node
                    return
                else:
                    return self.add_node(key, node=node.leftChild)
            else:
                if node.rightChild is None:
                    node.rightChild = TreeNode(key)
                    node.rightChild.parent = node
                    return
                else:
                    return self.add_node(key, node=node.rightChild)



def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add_node(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


repetitions = 3
max_operations = 20000
step = 1000
values_heap_add, values_heap_min, values_heap_max = [], [], []
for rounds in range(step, max_operations, step):
    this_list = []
    for r in range(rounds):
        this_list.append(random.randint(0, 5000))

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(3):
        a = BinarySearchTree()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= 3
    tot_time_min /= 3
    tot_time_max /= 3

    values_heap_add.append(tot_time_add * 1000)
    values_heap_min.append(tot_time_min * 1000)
    values_heap_max.append(tot_time_max * 1000)

xlabels = range(step, max_operations, step)
plt.plot(xlabels, values_heap_add, label='Add')
plt.plot(xlabels, values_heap_min, label='Get Min')
plt.plot(xlabels, values_heap_max, label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Execution time (msec)")
plt.title("Performance of Binary Tree Solution")
plt.show()
