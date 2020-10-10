"""
Implementacion de Priority Queue
Grupo 7 estructuras de datos
Universidad Nacional de Colombia
"""


class Node:
    def __init__(self, data, priority):
        """
        Clase elemento en el cual se almacena la prioridad y el elemento
        data: Dynamic 
        priority: Int  
        """
        self.data = data
        self.priority = priority
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def append(self, data, priority: int):
        if self.head == None:
            self.head = Node(data, priority)
        else:
            temp = self.head
            self.head = Node(data, priority)
            self.head.next = temp

    def pop(self):
        if self.head == None:
            return None
        if self.head.next == None:
            temp = self.head
            self.head = None
            return temp
        temp = self.head
        self.head = self.head.next
        return temp


class PriorityQueue:
    def __init__(self):
        """
            Iniciamos el PriorityQueue usando una pila implementada por medio de un arrreglo
        """
        self.node = Stack()

    def append(self, value, priority: int):
        """
            Se inserta un nuevo elemento, se reordena según la prioridad de los elementos 
        """
        
        self.node.append(value, priority)

    def extract_max(self) -> str:
        """ Se otiene el valor de mayor prioridad en la cola """
        max_index = -1
        max_element = None

        temp = self.node.head
        while temp != None:
            prior = temp.priority
            if prior > max_index:
                max_index = prior
                max_element = temp
            temp = temp.next
        temp_queue = Stack()
        temp = self.node.head
        while temp != None:
            if temp != max_element:
                temp_queue.append(temp.data, temp.priority)
            temp = temp.next
        self.node = temp_queue
        return f'Priority: {max_element.priority} Element: {max_element.data}'


myList = PriorityQueue()
myList.append('Sebastian Garzon', 2)
myList.append('Jaider Pinto', 7)
myList.append('David Zambrano', 5)
myList.append('Juan Andrés', 1)

print(myList.extract_max())
print(myList.extract_max())
print(myList.extract_max())
print(myList.extract_max())
