"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.
"""
import time
import matplotlib.pyplot as plt


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if self.isEmpty():
            print("List already empty")
            return
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                if current == None:
                    print("Item not found")
                    return

        if previous == None:                  #jeśli usuwamy pierwszy element
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __str__(self):
        current = self.head
        li = []
        while current != None:
            li.append(current.getData())
            current = current.getNext()
        s = ("elements in the list are [" + ', '.join(['{}']*len(li))+"]")
        return s.format(*li)


def bi_list(a, n):
    """
    Funkcja porównuje czas wykonanych operacji dla implementacji
    Argument n - ilość operacji
    Argument a - lista wbudowana
    Zwraca ten czas * 10 dla czytelniejszego wykresu
    """
    start_a = time.time()
    for i in range(0, n):
        a.append(20)
        a.append("coś")
        a.remove(20)
        len(a)
        if not a:
            return True
        a.index("coś")
    end_a = time.time()
    return (end_a - start_a) * 10


def uo_list(b, n):
    """
    Funkcja porównuje czas wykonanych operacji dla implementacji
    Argument n - ilość operacji
    Argument b - lista jednokierunkowa
    Zwraca ten czas
    """
    start_b = time.time()
    for i in range(0, n):
        b.add(20)
        b.add("coś")
        b.remove(20)
        b.size()
        b.isEmpty()
        b.search(0)
    end_b = time.time()
    return end_b - start_b


uo_1 = uo_list(UnorderedList(), 500)
bi_1 = bi_list([], 500)
uo_2 = uo_list(UnorderedList(), 1000)
bi_2 = bi_list([], 1000)
uo_3 = uo_list(UnorderedList(), 2000)
bi_3 = bi_list([], 2000)

print([uo_1, bi_1])
print([uo_2, bi_2])
print([uo_3, bi_3])

l1 = [uo_1, uo_2, uo_3]
l2 = [bi_1, bi_2, bi_3]

x = [500, 1000, 2000]
plt.plot(x, l1)
plt.plot(x, l2)
plt.title("comparison")
plt.xlabel("steps")
plt.ylabel("time")
plt.legend(['UO', 'BI*10'])
plt.show()
