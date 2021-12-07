class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):
    """
    Tutaj skopiuj swoją implementację klasy UnorderedList,
    wykonaną jako rezultat Zadania 5.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:  # jeśli usuwamy pierwszy element
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def remove_2(self, item, start_place):
        """
        Funkcja która usuwa wybrany element, ale szuka od wskazanego miejsca
        Argument item - element
        Argument start_place - początkowe miejsce szukania
        """
        current = self.head
        previous = None
        found = False
        position = 0

        while not found:
            if current.get_data() == item and position >= start_place:
                found = True
            else:
                previous = current
                current = current.get_next()
                position += 1

        if previous == None:  # jeśli usuwamy pierwszy element
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        """
        Metoda dodająca element na koniec listy.
        Przyjmuje jako argument obiekt, który ma zostać dodany.
        Niczego nie zwraca.
        """
        current = self.head
        last = False

        if self.is_empty() == True:
            self.add(item)
            return
        while last == False:
            if current.get_next() == None:
                last = True
            else:
                current = current.get_next()
        new_item = Node(item)
        current.set_next(new_item)

    def index(self, item):
        """
        Metoda podaje miejsce na liście,
        na którym znajduje się określony element -
        element pod self.head ma indeks 0.
        Przyjmuje jako argument element,
        którego pozycja ma zostać określona.
        Zwraca pozycję elementu na liście lub None w przypadku,
        gdy wskazanego elementu na liście nie ma.
        """
        current = self.head
        ind = 0
        while current != None:
            if current.get_data() != item:
                ind += 1
                current = current.get_next()
            else:
                return ind

    def insert(self, pos, item):
        """
        Metoda umieszcza na wskazanej pozycji zadany element.
        Przyjmuje jako argumenty pozycję,
        na której ma umiescić element oraz ten element.
        Niczego nie zwraca.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy nie jest możliwe umieszczenie elementu
        na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
        """
        current = self.head
        length = self.size()
        if pos > length:
            raise IndexError("ERROR")
        if pos == 0:
            self.add(item)
        else:
            for i in range(0, pos - 1):
                current = current.get_next()
                if current.get_next() == current:
                    return IndexError
            new_item = Node(item)
            next = current.get_next()
            current.set_next(new_item)
            new_item.set_next(next)

    def pop(self, pos=-1):
        """
        Metoda usuwa z listy element na zadaniej pozycji.
        Przyjmuje jako opcjonalny argument pozycję,
        z której ma zostać usunięty element.
        Jeśli pozycja nie zostanie podana,
        metoda usuwa (odłącza) ostatni element z listy.
        Zwraca wartość usuniętego elementu.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy usunięcie elementu z danej pozycji jest niemożliwe."""

        current = self.head
        if pos == -1:
            while current.get_next() != None:
                current = current.get_next()
            removing = current.get_data()
            self.remove_2(removing, self.size() - 1)

        elif self.is_empty():
            return

        elif pos > self.size() - 1:
            raise IndexError("Too large index")

        else:
            for i in range(0, pos):
                current = current.get_next()
            to_remove = current.get_data()
            self.remove_2(to_remove, pos)
            return to_remove

    def __str__(self):
        current = self.head
        li = []
        while current != None:
            li.append(current.get_data())
            current = current.get_next()
        s = ("elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)


class StackUsingUL(object):
    def __init__(self):
        self.items = UnorderedList()

    def is_empty(self):
        """
        Metoda sprawdzajacą, czy stos jest pusty.
        Nie pobiera argumentów.
        Zwraca True lub False.
        """
        return self.items.is_empty()

    def push(self, item):
        """
        Metoda umieszcza nowy element na stosie.
        Pobiera element, który ma zostać umieszczony.
        Niczego nie zwraca.
        """
        self.items.append(item)

    def pop(self):
        """
        Metoda ściąga element ze stosu.
        Nie przyjmuje żadnych argumentów.
        Zwraca ściągnięty element.
        Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
        """
        if self.items.is_empty():
            raise IndexError("This stack is empty")
        else:
            return self.items.pop()

    def peek(self):
        """
        Metoda podaje wartość elementu na wierzchu stosu
        nie ściągajac go.
        Nie pobiera argumentów.
        Zwraca wierzchni element stosu.
        Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
        """
        if self.items.is_empty():
            raise IndexError("This stack is empty")
        else:
            current = self.items.head
            while current.get_next() != None:
                current = current.get_next()
            return current.get_data()

    def size(self):
        """
        Metoda zwraca liczę elementów na stosie.
        Nie pobiera argumentów.
        Zwraca liczbę elementów na stosie.
        """
        return self.items.size()

    def __str__(self):
        current = self.items.head
        li = []
        while current != None:
            li.append(current.get_data())
            current = current.get_next()
        s = ("elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)


if __name__ == "__main__":
    mylist = StackUsingUL()
    mylist.push(4)
    print(mylist.peek())
    mylist.pop()
    print(mylist)

