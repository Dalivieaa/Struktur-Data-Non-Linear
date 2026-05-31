# 2. AVL (Adelson Velsky Landis) 
# Tree adalah jenis pohon biner yang seimbang secara otomatis. Setiap node dalam AVL Tree memiliki faktor keseimbangan yang dihitung 
# sebagai selisih antara tinggi subpohon kiri dan subpohon kanan. AVL Tree memastikan bahwa faktor keseimbangan setiap node berada dalam 
# rentang -1, 0, atau 1, sehingga menjaga pohon tetap seimbang.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def balance(n):
    return height(n.left) - height(n.right) if n else 0

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    root.height = 1 + max(height(root.left), height(root.right))
    balance_factor = balance(root)

    if balance_factor > 1 and key < root.left.key: 
        return rotate_right(root)
    if balance_factor < -1 and key > root.right.key:
        return left_rotate(root)
    if balance_factor > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return rotate_right(root)
    if balance_factor < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return left_rotate(root)

    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

data = [30, 10, 20]
root = None

for x in data:
    root = insert(root, x)

print("Hasil inorder traversal setelah insert 30, 10, 20:")
inorder(root)
print()