    #1. BST (Binary Search Tree) 
    # adalah struktur data pohon biner yang memiliki sifat khusus, yaitu setiap node memiliki nilai yang lebih besar dari nilai 
    # di subtree kiri dan lebih kecil dari nilai di subtree kanan. BST digunakan untuk menyimpan data secara terurut dan memungkinkan 
    # pencarian, penyisipan, dan penghapusan elemen dengan efisiensi yang baik.

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        
    def insert(root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root
        
    def preorder(node):
        if node:
            print(node.value, end=" ")
            preorder(node.left)
            preorder(node.right)

    def inorder(node):
        if node:
            inorder(node.left)
            print(node.value, end=" ")
            inorder(node.right)
        
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.value, end=" ")

    data = [50, 30, 70, 20, 40]
    root = None
    for x in data:
        root = insert(root, x)
        
    print("preorder:")
    preorder(root)
    print("\ninorder(urut):")
    inorder(root)
    print("\npostorder:")
    postorder(root)
    print()