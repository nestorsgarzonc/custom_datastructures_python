class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        if self.head:
            return self.head.value
        return None


class Cola(Lista):
    def __init__(self):
        super().__init__()

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node.value

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


# constaints = input().split(' ')
# elements = input().split(' ')
cola = Cola()
cola.enqueue(10)
cola.enqueue(8)
cola.enqueue(80)
print(cola.dequeue())
print(cola.dequeue())
print(cola.dequeue())
print(cola.peek())
