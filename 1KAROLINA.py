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
    #return self.list_of_items
    
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
    self.list_of_items.reverse()
    self.list_of_items.append(item)
    self.list_of_items.reverse()
    return self.list_of_items

  def dequeue(self):
    """
    Metoda służąca do ściągania obiektu do kolejki.
    Nie pobiera argumentów.
    Zwraca ściągnięty obiekt.
    """
    removed = self.list_of_items.pop(-1)
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
    list = QueueBaE()
    print(list.enqueue(1))
    print(list.enqueue(2))
    print(list.enqueue(3))
    print(list.enqueue(4))
    print(list.enqueue(5))
    print(list.dequeue())
    print(list.dequeue())
    print(list.enqueue(80))
    print(list.dequeue())
    print(list.dequeue())
    print(list.dequeue())

    