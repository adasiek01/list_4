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


if __name__ == "__main__":
    bae = QueueBaE()
    bae.enqueue(1)
    bae.enqueue(2)
    bae.enqueue(3)
    bae.enqueue(4)
    bae.enqueue(5)
    print(bae.dequeue())
    bae.enqueue(100)
    bab = QueueBaB()
    bab.enqueue(1)
    bab.enqueue(2)
    bab.enqueue(3)
    bab.enqueue(4)
    bab.enqueue(5)
    print(bab.dequeue())
    bab.enqueue(100)
