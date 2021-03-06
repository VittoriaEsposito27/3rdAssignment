import random, time, heapq
import matplotlib.pyplot as plt
class MinMaxHeap(object):
    def __init__(self):
        self.content_min = []
        self.content_max = []

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]

    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]



def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


repetitions = 3
max_operations = 200000
step = 10000
values_heap_add, values_heap_min, values_heap_max = [], [], []
for rounds in range(step, max_operations, step):
    this_list = []
    for r in range(rounds):
        this_list.append(random.randint(0, 50000))

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for repetition in range(3):
        a = MinMaxHeap()
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
plt.title("Performance of Heap Solution")
plt.show()

