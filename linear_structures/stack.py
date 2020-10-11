class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Lista:
    pass


class Pila(Lista):
    def __init__(self):
        self.head = None
        self.tail = None

    def dequeue(self):
        temp = self.head
        item_to_remove = None
        if temp.next == None:
            item_to_remove = temp
            self.head = None
        while temp:
            temp = temp.next
            if temp.next.next == None:
                item_to_remove = temp.next
                temp.next = None
        return item_to_remove

    def enqueue(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp_head = self.head
            self.head = Node(value)
            self.head.next = temp_head

    def peek(self):
        return self.head.value
