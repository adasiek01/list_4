""" 
Rozważmy następującą sytuację.
W barze mlecznym klienci ustawiają się w kolejce. Przy długim blacie,na którym znajdują się różne potrawy 
nie może jednocześnie przebywać więcej niż jedna osoba. Dla uproszczenia załóżmy, że czas potrzebny na 
nałożenie porcji przez jednego klienta jest wprostproporcjonalny do ilości talerzy, które zamierza zapełnić 
(losowa liczba całkowita z przedziału [1,4]). Czas zapełnienia jednego talerza to 1 minuta. 
Gdy klient wchodzi do baru a miejsce przy blacie jest wolne, od razu przystępuje do nakładania jedzenia. 
W przeciwnym wypadku jest zmuszony do stania w kolejce. Gdy nakładający zakończy swoją czynność, jego miejsce 
zajmuje pierwsza osoba w kolejce.
Argumentami symulacji są liczba minut oraz szansa na przyjście w danej chwili klienta.
Przy pomocy poniższej symulacji obliczymy średni czas oczekiwania w kolejce.
"""

import random


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,
                          item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Client:
    def __init__(self, start_time):
        self.start_time = start_time
        self.empty_plates = random.randrange(1,4)

    def apply(self):
        self.empty_plates -= 1

    def ready(self):
        if self.empty_plates <= 0:
            return True
        else:
            return False
    
    def get_empty_plates(self):
        return self.empty_plates

    def wait_time(self, current_time):
        return current_time - self.start_time


class Milk_Bar:
    def __init__(self):
        self.current_client = None

    def tick(self):
        if self.current_client is None:
            return 
        self.current_client.apply()
        if self.current_client.ready():
            self.current_client = None

    def busy(self):
        if  self.current_client is not None:
            return True
        else: 
            return False

    def another_client(self, new_client):
        self.current_client = new_client


def milk_bar_simulation(minutes, probability):
    milk_bar = Milk_Bar()
    bar_queue = Queue()
    total_time = 0
    clients_quantity = 0

    for time in range(minutes):
        if random.random() < probability:
            new_client = Client(time)
            bar_queue.enqueue(new_client)

        if not milk_bar.busy() and not bar_queue.isEmpty():
            new_client = bar_queue.dequeue()
            milk_bar.another_client(new_client)
            clients_quantity = clients_quantity + 1
            total_time = total_time + new_client.wait_time(time)

        milk_bar.tick()
    print("averge waiting time: {}minutes".format(total_time/clients_quantity))


if __name__ == "__main__":
    milk_bar_simulation(30, 0.2)
