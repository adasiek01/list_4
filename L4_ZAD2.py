"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
import time
from L4_ZAD1 import QueueBaB, QueueBaE


def comparing(a, b):
    start_a = time.time()
    for i in range(1, 1000):
        a.enqueue("a")
        a.enqueue("b")
        a.enqueue("r")
        a.dequeue()
        a.is_empty()
        a.size()
    end_a = time.time()
    time_bab = end_a-start_a
    start_b = time.time()
    for i in range(1, 1000):
        b.enqueue("a")
        b.enqueue("b")
        b.enqueue("r")
        b.dequeue()
        b.is_empty()
        b.size()
    end_b = time.time()
    time_bae = end_b-start_b
    return time_bab, time_bae


if __name__ == "__main__":
    print(comparing(QueueBaB(), QueueBaE()))
