class Node:
    def __init__(self, item, priority):
        """
        Clase elemento en el cual se almacena la prioridad y el elemento
        item: Dynamic 
        priority: Int  
        """
        self.item = item
        self.priority = priority


class PriorityQueue():
    def __init__(self):
        """
            Iniciamos el PriorityQueue usando una pila implementada por medio de un arrreglo
        """
        self.head = []
        self.counter = 0

    def append(self, value, priority):
        """
            Se inserta un nuevo elemento, se reordena según la prioridad de los elementos 
        """
        self.head.append(Node(value, priority))
        self.counter += 1

    def extract_max(self):
        """ Se otiene el valor de mayor prioridad en la cola """
        max_index = -1
        max_element = None
        for i in self.head:
            if i.priority > max_index:
                max_index = i.priority
                max_element = i
        self.head = [i for i in self.head if i != max_element]
        return f'Priority: {max_element.priority} Element: {max_element.item}'


myList = PriorityQueue()
myList.append('Sebastian Garzon', 2)
myList.append('Jaider Pinto', 7)
myList.append('David Zambrano', 5)
myList.append('Juan Andrés', 1)

print(myList.extract_max())
print(myList.extract_max())
print(myList.extract_max())
print(myList.extract_max())
