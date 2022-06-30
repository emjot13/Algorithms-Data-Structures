from timeit import default_timer as timer
import random
import math
import statistics

# Here I implemented HeapSort that can use two versions of Heapify function - recursive and iterative
# at the end there is a function to assess time needed to perform algorithm with different types of data as well.

def buildHeap(tab):
    heapSize = len(tab)
    k = int((len(tab) - 2) / 2) # parent node of the last node
    for i in range(k, -1, -1):
        heapify(tab, heapSize, i)
    return tab


def heapify(tab, heapSize, i):
    largest = i
    left_child = 2 * largest + 1
    right_child = 2 * largest + 2
    if left_child < heapSize and tab[left_child] < tab[i]:
        largest = left_child
    else:
        largest = i
    if right_child < heapSize and tab[right_child] < tab[largest]:
        largest = right_child
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, heapSize, largest)

    return tab


def heapify_recursive(tab, heapSize, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < heapSize and tab[left_child] < tab[i]:
        largest = left_child
    else:
        largest = i
    if right_child < heapSize and tab[right_child] < tab[largest]:
        largest = right_child
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify_recursive(tab, heapSize, largest)
    return tab


def heapSort_N_I_O(input_file, output_file):  #non-increasing order
    tab = []
    with open(input_file, 'r') as we:
        lines = we.readlines()
    for x in range(len(lines)):
        lines[x] = int(lines[x])
    for item in lines:
        tab.append(item)
    tab = buildHeap(tab)
    heapSize = len(tab)
    for i in range(len(tab) - 1, 0, -1):
        tab[0], tab[heapSize - 1] = tab[heapSize - 1], tab[0]
        heapSize -= 1
        heapify(tab, heapSize, 0)
    with open(output_file, 'w') as p:
        for num in tab:
            p.write('%s\n' % num)


def heapSort(tab):
    tab = buildHeap(tab)
    heapSize = len(tab)
    for i in range(len(tab) - 1, 0, -1):
        tab[0], tab[heapSize - 1] = tab[heapSize - 1], tab[0]
        heapSize -= 1
        heapify(tab, heapSize, 0)
    return tab

print("n \t\t ascending \t\t descending \t all the same \n")

def test():
    x = random.randint(0, 10000)
    asc_list = []
    desc_list = []
    same_list = []
    for n in range(800, 1001, 10):
        C = []
        A = []
        for m in range(n):
            A.append(random.randint(0, 10000))
            C.append(x)
        B = A.copy()
        A.sort()
        B.sort(reverse=True)
        start = timer()
        heapSort(A)
        stop = timer()
        start1 = timer()
        heapSort(B)
        stop1 = timer()
        start2 = timer()
        heapSort(C)
        stop2 = timer()
        Tn = stop - start
        Tn1 = stop1 - start1
        Tn2 = stop2 - start2
        Fn = n * math.log(n)
        one = int(Fn / Tn)
        two = int(Fn / Tn1)
        three = int(Fn / Tn2)
        asc_list.append(one)
        desc_list.append(two)
        same_list.append(three)
        print(n, '\t', format(Tn, '.8f'), '\t', format(Tn1, '.8f'), '\t', format(Tn2, '.8f'), '\t', one, '\t', two, '\t', three)
        print(int(statistics.stdev(asc_list)/statistics.mean(asc_list) * 100), "% ",
          int(statistics.stdev(desc_list)/statistics.mean(desc_list) * 100), "% ",
          int(statistics.stdev(same_list)/statistics.mean(same_list) * 100), "%", sep='')





