import random
from timeit import default_timer as timer
import statistics

# Experimental analysis of time complexity. I analysed time complexity of two algorithms that were supposed to find
# the largest rectangle sub-matrix containing of only 1.


def make_square_matrix(size):
    matrix2 = []
    for i in range(0, size):
        matrix2.append([random.randint(0, 1)])
        for j in range(0, size - 1):
            matrix2[i].append(random.randint(0, 1))
    return matrix2


def method1(matrix):
    area = 0
    max_area = 0
    i1max = 0
    j1max = 0
    i2max = 0
    j2max = 0
    for i1 in range(0, len(matrix)):
        for j1 in range(0, len(matrix)):
            for i2 in range(i1, len(matrix)):
                for j2 in range(j1, len(matrix)):
                    area = ((j2 - j1) + 1) * ((i2 - i1) + 1)
                    for i3 in range(i1, i2 + 1):
                        for j3 in range(j1, j2 + 1):
                            if matrix[i3][j3] == 0:
                                area = 0
                    if area > max_area:
                        max_area = area
                        i1max = i1
                        j1max = j1
                        i2max = i2
                        j2max = j2
    return i1max, j1max, i2max, j2max


def method2(matrix):
    width = len(matrix)
    max_area = 0
    max_width = 0
    max_height = 0
    for i in range(0, width):
        for j in range(0, width):
            if matrix[i][j] == 1:
                new_max = width
                for x in range(i, width):
                    for y in range(j, new_max):
                        if matrix[x][y] == 0:
                            new_max = y
                            break
                    if (new_max - j) == 0:
                        break
                    pole = (x - i + 1) * (new_max - j)
                    if pole > max_area:
                        max_width = new_max - j
                        max_height = x - i + 1
                        max_area = (x - i + 1) * (new_max - j)
    return max_area, max_width, max_height


def test(starting_size, final_size, step, method, your_O_notation_Func):
    outcomes = []
    for n in range(starting_size, final_size, step):
        test_matrix = make_square_matrix(n)
        start = timer()
        method(test_matrix)
        stop = timer()
        Tn = stop - start
        Fn = your_O_notation_Func(n)
        rate_of_change = Fn / Tn
        print(rate_of_change)
        outcomes.append(rate_of_change)
    standard_deviation = int(statistics.stdev(outcomes)/statistics.mean(outcomes) * 100)
    print(str(standard_deviation) + "%")


test(1, 9, 1, method1, lambda x: x ** 2)


# You can interpret whether your assumption of O(n) is correct by comparing the following iterations
# and checking for changes, hence the use of standard deviation.
