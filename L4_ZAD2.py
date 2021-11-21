"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
import time
from L4_ZAD1 import QueueBaB, QueueBaE


def comparing(a, b):
    start_a = time.time()
    a.enqueue(i for i in range(1, 1000))
    a.dequeue()
    end_a = time.time()
    time_bab = end_a-start_a
    start_b = time.time()
    b.enqueue(i for i in range(1, 1000))
    b.dequeue()
    end_b = time.time()
    time_bae = end_b-start_b
    return time_bab, time_bae


if __name__ == "__main__":
    print(comparing(QueueBaB(), QueueBaE()))
