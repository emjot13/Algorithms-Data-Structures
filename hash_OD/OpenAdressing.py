# Using OOP I implemented another Hash procedure, this time using open addressing with procedure of double hashing.
# I also programmed procedure of deleting specific part of previously added elements only
# after filling the mixing table to specific point, then again filling the table to the same point with another keys.
# At the end I again tested the algorithms with regards to different table sizes.
from timeit import default_timer as timer


class Surname:
    def __init__(self, surname, frequency):
        self.key = surname
        self.freq = frequency


class ToArray:
    def __init__(self, filename, arraySize):
        self.filename = filename
        self.arraySize = arraySize
        self.array = []
        with open(filename, "r") as f:
            lines = f.readlines()
            for k in lines[:int(0.8 * arraySize)]:
                i = k.strip().split(' ')
                toAdd = Surname(i[1], i[0])
                self.array.append([toAdd.key, int(toAdd.freq)])

        self.hashedArray = []
        for k in range(arraySize):
            self.hashedArray.append([])

        def goodHash(word, factor=111):
            hashKey = 0
            for i in range(len(word)):
                hashKey *= factor
                hashKey += ord(word[i])
            return hashKey

        def hashh():
            for k in self.array:
                i = 0
                index = ((goodHash(k[0]) % self.arraySize) + (
                        i * (1 + goodHash(k[0]) % (self.arraySize - 2)))) % self.arraySize
                while self.hashedArray[index] != []:
                    i += 1
                    index = ((goodHash(k[0]) % self.arraySize) + (i * (
                            1 + goodHash(k[0]) % (self.arraySize - 2)))) % self.arraySize
                self.hashedArray[index] = k

        def delete():
            for k in range(0, int(0.8 * arraySize), 2):
                counter = -1
                for j in self.hashedArray:
                    counter += 1
                    if self.array[k] == j:
                        self.hashedArray[counter] = "DEL"

        def fillAgain():
            new_list = []
            with open("surnames.txt", "r") as f:
                lines = f.readlines()
                for x in lines[len(self.array):len(self.array) + int(0.5 * arraySize)]:
                    j = x.strip().split(' ')
                    toAdd = Surname(j[1], j[0])
                    new_list.append([toAdd.key, int(toAdd.freq)])

            for x in new_list:
                j = 0
                index = ((goodHash(x[0]) % self.arraySize) + (
                        j * (1 + goodHash(x[0]) % (self.arraySize - 2)))) % self.arraySize
                while self.hashedArray[index] != [] and self.hashedArray[index] != "DEL":
                    j += 1
                    index = ((goodHash(x[0]) % self.arraySize) + (
                                j * (1 + goodHash(x[0]) % (self.arraySize - 2)))) % self.arraySize

                self.hashedArray[index] = x

        hashh()
        delete()
        fillAgain()
        if self.arraySize == 17:
            print(self.hashedArray, self.arraySize, "\n")


def tests(size):
    start = timer()
    obj = ToArray("surnames.txt", size)
    stop = timer()
    time = stop - start
    blanks = 0
    dels = 0
    for each in obj.hashedArray:
        if each == []:
            blanks += 1
        elif each == "DEL":
            dels += 1
    print(
        f"SIZE: {size} ==>    number of blanks: {blanks}      number of \"DEL\": {dels}       "
        f"time taken:  {time}     \n(blanks, \"DEL\", time taken) to size ratio:      "
        f"{round(blanks / size * 100, 2)}%,     {round(dels / size * 100, 2)}%,      {round(time / size * 100, 2)}%\n\n")


tests(17)
tests(127)
tests(607)
tests(4073)
tests(7243)
tests(10009)
