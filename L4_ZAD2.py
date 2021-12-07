"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność implementacji kolejek QueueBaB i QueueBaE.
"""
import time
import matplotlib.pyplot as plt


class QueueBaB(object):
    """
       Klasa implementująca kolejkę za pomocą pythonowej listy tak,
       że początek kolejki jest przechowywany na początku listy.
       """

    def __init__(self):
        self.list_of_items = []

    def enqueue(self, item):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items.append(item)

    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        removed = self.list_of_items.pop(0)
        return removed

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if len(self.list_of_items) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.list_of_items)


class QueueBaE(object):
    """
    Klasa implementująca kolejkę za pomocą pythonowej listy tak,
    że początek kolejki jest przechowywany na końcu listy.
    """

    def __init__(self):
        self.list_of_items = []

    def enqueue(self, item):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items.insert(0, item)

    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        removed = self.list_of_items.pop()
        return removed

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if len(self.list_of_items) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.list_of_items)


def comparing(n):
    """
    Funkcja porównuje czasy wykonanych operacji dla obu zaimplementowanych kolejek
    Argument n - ilość operacji
    Zwraca te czasy
    """

    bab = QueueBaB()
    bae = QueueBaE()
    start_a = time.time()
    for i in range(1, n):
        bab.enqueue(20)
    for i in range(1, n):
        bab.dequeue()
    end_a = time.time()
    start_b = time.time()
    for i in range(1, n):
        bae.enqueue(20)
    for i in range(1, n):
        bae.dequeue()
    end_b = time.time()
    time_bab = end_a - start_a
    time_bae = end_b - start_b
    return time_bab, time_bae


x = [5000, 7500, 10000]
list_bab = [comparing(5000)[0], comparing(7500)[0], comparing(10000)[0]]
list_bae = [comparing(5000)[1], comparing(7500)[1], comparing(10000)[1]]
plt.plot(x, list_bab)
plt.plot(x, list_bae)
plt.title("comparison")
plt.xlabel("steps")
plt.ylabel("time")
plt.legend(["bab", "bae"])
plt.show()

if __name__ == "__main__":
    print(list_bab, list_bae)




















































































































































































































































































































































































































































































