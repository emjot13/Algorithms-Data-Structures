# Using OOP I implemented some of Binary Search Tree procedures like: printing, deleting, searching
# and inserting (with possibility of adding the same key a few times)

class Node:
    def __init__(self, x):
        self.key = x
        self.left = None  # left child
        self.right = None  # right child
        self.p = None  # parent node
        self.amount = 1

    def left_child(self, z):
        self.left = z

    def right_child(self, z):
        self.right = z


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print(self, x):
        if x == None: return
        self.print(x.left)
        print(x.key)
        self.print(x.right)

    def insert(self, z):
        x = self.root
        y = None
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key == x.key:
                x.amount += 1
                return
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left_child(z)
            else:
                y.right_child(z)

    def search(self, x, k):
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def delete(self, z):
        if z.amount == 1:
            if z.left is None and z.right is None:
                if z == self.root:
                    self.root = None
                else:
                    if z == z.p.left:
                        z.p.left = None
                    else:
                        z.p.right = None
            elif z.left is not None and z.right is not None:
                y = self.bstMinimum(z.right)
                z.key = y.key
                self.bstDelete(y)  #
            else:
                if z.left is not None:
                    z.left.p = z.p
                    if z == self.root:
                        self.root = z.left
                    else:
                        if z == z.p.left:
                            z.p.left = z.left
                        else:
                            z.p.right = z.left
                else:
                    z.right.p = z.p
                    if z == self.root:
                        self.root = z.right
                    else:
                        if z == z.p.left:
                            z.p.left = z.left
                        else:
                            z.p.right = z.left
        else:
            z.amount -= 1


tree = BinarySearchTree()
tree.insert(Node("a"))
tree.insert(Node("b"))
tree.insert(Node("c"))
tree.insert(Node("d"))
tree.insert(Node("y"))
tree.insert(Node("z"))
print("search right child of word: \"a\"")
print(tree.search(tree.root, "a").right.key)
print("print node \"d\"")
tree.print(tree.search(tree.root, "d"))
print("the entire tree")
tree.print(tree.root)
print("number of 'y'")
print(tree.search(tree.root, "y").amount)
print("tree after deleting 'c'")
tree.delete(tree.search(tree.root, "c"))
tree.print(tree.root)
print("number of 'a'")
print(tree.search(tree.root, "a").amount)
print("ilosc 'r'")
print(tree.search(tree.root, "r"))
tree.print(tree.root)
