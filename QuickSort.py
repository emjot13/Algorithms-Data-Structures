from timeit import default_timer as timer
import random

# Here I implemented normal QuickSort and also a modified version, where for lists of a specific size, smaller than some
# value - the Partition procedure and recursion are not executed,
# but instead there is used simple sorting algorithm of choice - in this case it is BubbleSort.


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i - 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q + 1, r)


def modified_quickSort(A, p, r, c):
    if r - p + 1 < c:
        for i in range(r - p + 1):
            for j in range(p, r - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]

    elif p < r:
        q = partition(A, p, r)
        modified_quickSort(A, p, q, c)
        modified_quickSort(A, q + 1, r, c)


print(
    "Quicksort - normal               Modified quicksort               Quicksort with reversed lists     Modified quicksort with reversed lists \n\n ")



for n in range(1000, 10000, 100):
    a = []
    for m in range(n):
        a.append(random.randint(0, 10000))
    b = a.copy()
    start = timer()
    quickSort(a, 0, len(a) - 1)
    stop = timer()
    start1 = timer()
    modified_quickSort(b, 0, len(b) - 1, 500)
    stop1 = timer()
    Tn = stop - start
    Tn1 = stop1 - start1
    def whosfaster():
        if Tn < Tn1:
            return "QS is faster"
        return 'QS modified is faster'

    print(str(Tn) + "            " + str(Tn1) + "         " + whosfaster())
