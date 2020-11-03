"""
UNIVERSIDAD NACIONAL DE COLOMBIA
IMPLEMENTACION BST
GRUPO 7
INTEGRANTES:
    - Nestor Sebastián Garzón Contreras
    - Jaider Andrés Pinto Pinto
    - Juan Andrés Moreno Sánchez
    - David Alexander Zambrano Bohórquez
"""


class Node():
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class Tree:
    def __init__(self, arr=None):
        if(not arr):
            self.root = None
            return
        self.build_tree(arr)

    def previous(self, node: Node):
        if node.left == None:
            #TODO: implementar
            return

    def build_tree(self, arr: list):
        if len(arr) == 0:
            return
        if len(arr) == 1:
            self.root = Node(arr[0])
            return
        new_arr = sorted(arr)
        mid = (len(arr)) // 2
        self.root = Node(new_arr[mid])
        self.root.left = self.build_tree(new_arr[:mid])
        self.root.right = self.build_tree(new_arr[mid+1:])

    def insert(self, value):
        pass

    def __str__(self) -> str:
        self.print_helper(self.root)
        return ''

    def print_helper(self, tree):
        if tree:
            self.print_tree(tree.left)
            print(tree.value)
            self.print_tree(tree.right)
            return
        print('No hay elementos')

if __name__ == "__main__":
    tree = Tree()
    tree.build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
