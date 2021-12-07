""" Na zlocie bohaterów filmów animowanych wyprodukowanych przez DreamWorks, Pixar oraz Walt Disney Pictures 
pojawiło się 10 postaci. W programie zaplanowano wyścig, do którego zawodnicy przystępują stojąc jeden za drugim. Postaci są ustawiane
na linii startu zgodnie z wyliczanką "N" (n to dowolna liczba naturalna). Postać "first" bardzo chciałaby ruszać do biegu tuż za 
postacią "second".
Za pomocą zapisanej poniżej funkcji sprawdzimy, czy dla danej wyliczanki marzenie postaci "first" się spełni. """


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def counting_rhyme(names, n, first, second):
    """
    Funkcja wyznaczająca kolejnośc w jakiej zawodnicy ustawiają się na linii startu.
    Jako argumenty przyjmuje listę imion zawodników 'names', liczbę do której chcemy wyliczać 'n',
    imiona postaci z przodu 'first' i z tyłu 'secdond'.
    """
    start_list = []
    characters_queue = Queue()
    for character in names:
        characters_queue.enqueue(character)

    while characters_queue.size() > 0:

        for i in range(n):
            characters_queue.enqueue(characters_queue.dequeue())

        choose = characters_queue.dequeue()
        start_list.append(choose)

    first_index = start_list.index(first)
    second_index = start_list.index(second)
    if second_index == first_index+1:
        return True, start_list
    else: 
        return False, start_list


if __name__ == "__main__":
    participants = ['Shrek', 'Elsa', 'Mulan', 'Mushu', 'Osioł', 'Nemo', 'Król Julian', 'Fiona', 'Olaf', 'Mort' ]
    for i in range(0, 20):
        print(counting_rhyme(participants, i, "Mulan", "Fiona"))

