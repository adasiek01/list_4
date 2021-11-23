"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
import time
import matplotlib.pyplot as plt
from L4_ZAD1 import QueueBaB, QueueBaE


def comparing(q, item):
    start_a = time.time()
    for i in range(1, 5000):
        q.enqueue(item)
    for i in range(1, 2500):
        q.dequeue()
    end_a = time.time()
    start_b = time.time()
    for i in range(1, 20000):
        q.enqueue(item)
    for i in range(1, 10000):
        q.dequeue()
    end_b = time.time()
    start_c = time.time()
    for i in range(1, 10000):
        q.enqueue(item)
    for i in range(1, 5000):
        q.dequeue()
    end_c = time.time()
    time_a = end_a - start_a
    time_b = end_b - start_b
    time_c = end_c - start_c
    return time_a, time_b, time_c


bab = comparing(QueueBaB(), 333)
bae = comparing(QueueBaE(), 333)

if __name__ == "__main__":
    print(bab)
    print(bae)

x = [5000, 10000, 20000]
plt.plot(x, bab)
plt.plot(x, bae)
plt.title("comparison")
plt.xlabel("steps")
plt.ylabel("time")
plt.show()
