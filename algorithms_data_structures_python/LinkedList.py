
# Here I implemented Linked List using OOP, apart from the most basic operations, I added function to create Linked List
# with no duplicates and function to merge 2 lists without copying them,
# but rather by using nodes from L1 and L2 to create L3.



class Element:
    def __init__(self, k):
        self.key = k
        if k is not None:
            self.length = len(self.key)
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.sentinel = Element(None)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel

    def search(self, k):

        self.sentinel.key = k
        next = self.sentinel.next
        while next is not None and next.key is not k:
            next = next.next
        self.sentinel.key = None
        if next == self.sentinel:
            return None
        else:
            return next

    def insert(self, key):
        newElement = Element(key)
        newElement.prev = self.sentinel
        newElement.next = self.sentinel.next
        self.sentinel.next = newElement
        newElement.next.prev = newElement

    def delete(self, x):

        x.prev.next = x.next
        x.next.prev = x.prev

    def print(self):
        tab = []
        to_print = self.sentinel.next
        while to_print.key is not None:
            tab.append([to_print.key, to_print.length])
            to_print = to_print.next
        print(tab)




def no_duplicates(L):
    ND_list = LinkedList()
    to_print = L.sentinel.next
    while to_print.key is not None:
        if ND_list.search(to_print.key) is None:
            ND_list.insert(str(to_print.key))
        to_print = to_print.next
    return ND_list


def merge(L1, L2):
    L3 = LinkedList()
    L1.sentinel.prev.next = L2.sentinel.next
    L2.sentinel.prev.next = L3.sentinel
    L2.sentinel.next.prev = L1.sentinel.prev
    L3.sentinel.next = L1.sentinel.next
    L3.sentinel.prev = L2.sentinel.prev
    L1.sentinel.next.prev = L3.sentinel
    L1.sentinel.next = L1.sentinel
    L1.sentinel.prev = L1.sentinel
    L2.sentinel.next = L2.sentinel
    L2.sentinel.prev = L2.sentinel
    return L3


myList = LinkedList()
myList.insert("")
myList.insert("-23")
myList.insert("12aa")
myList.insert("!@#$")
myList.insert("!@#$")
