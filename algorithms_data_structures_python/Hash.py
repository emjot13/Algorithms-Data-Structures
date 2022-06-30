# Using OOP I implemented a few versions of hash functions and tested them by criteria like: number of indexes at which
# the elements are empty lists, max number of words that are elements of the same list,
# and the average length of non-empty lists.


class Hash:
    def __init__(self, filename, method, arraySize):
        self.array = []
        self.filename = filename
        self.method = method
        self.arraySize = arraySize
        self.clearArray()

    def clearArray(self):
        self.array = []
        for _ in range(self.arraySize):
            self.array.append([])

    def toArray(self):
        arr = []
        with open(self.filename, "r") as filein:
            for k in range(2 * self.arraySize):
                line = filein.readline()
                line = line.strip()
                arr.append(line)
        return arr

    def goodHash(self, word, factor):
        hashKey = 0
        for i in range(len(word)):
            hashKey *= factor
            hashKey += ord(word[i])
        return hashKey % self.arraySize

    def built_in(self, word):
        hashkey = hash(word)
        return hashkey % self.arraySize

    def badHash(self, word):
        hashkey = ord(word[0])
        return hashkey % self.arraySize

    def main(self):
        self.clearArray()
        array1 = self.toArray()
        if self.method == "goodHash":
            for each in array1:
                self.array[self.goodHash(each, 111)].append(each)
        elif self.method == "built_in":
            for each in array1:
                self.array[self.built_in(each)].append(each)
        elif self.method == "badHash":
            for each in array1:
                self.array[self.badHash(each)].append(each)
        print(self.array)
        return self.array

    def tests(self):
        counted_array = self.main()

        blanks = 0
        for each in counted_array:
            if not each:
                blanks += 1

        max_len = 0
        for each in counted_array:
            if len(each) > max_len:
                max_len = len(each)

        avg = 0
        for each in counted_array:
            if len(each) > 0:
                avg += len(each)

        avg = round(avg / blanks, 2)

        print(self.method + ", " + str(self.arraySize) + "       blanks: " + str(blanks) + "   max length: "
              + str(max_len) + "    average length: " + str(avg).format())
