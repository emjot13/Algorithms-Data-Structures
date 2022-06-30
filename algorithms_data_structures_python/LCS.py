# Using the idea of dynamic programming I implemented Longest Common Subsequence algorithm.
# Function PrintLCS shows graphic representation of passing through next cells of table created using LCS algorithm.


def lcsLength(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n + 1)]  # creating lists
         for j in range(m + 1)]  # filling them with "i"
    b = [[0 for i in range(n + 1)]
         for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # x[i-1] == y[j-1] when indexing x,y starting at 0
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '\\'
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "|"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "-"
    return c, b


tab = []


def PrintLCS(x, b, i, j):
    global tab
    tab = []
    if i == 0 or j == 0:
        return
    if b[i][j] == "\\":

        PrintLCS(x, b, i - 1, j - 1)
        tab.append(x[i - 1])
        print(x[i - 1])
    elif b[i][j] == "|":
        PrintLCS(x, b, i - 1, j)
    else:
        PrintLCS(x, b, i, j - 1)


b = lcsLength("acbabbaba", "ba")[1]
print(b)
PrintLCS("acbabbaba", b, len("acbabbaba"), len("ba"))
print(tab)
