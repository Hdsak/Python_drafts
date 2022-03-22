import sys


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i - 1][j] == 0 and a[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and a[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and a[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and a[i][j + 1] == 0:
                    m[i][j + 1] = k + 1


def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(str(m[i][j]).ljust(2), end=" ")
        print()


def load_a():
    map_ = []
    a = None
    b = None
    size = None
    with open('advent_16.test.txt', 'r') as file:
        for y, line in enumerate(file.readlines()):
            parts = line.split()
            if size is None:
                size = len(parts)
            row = []
            for x, p in enumerate(parts):
                if p == "A":
                    assert a is None
                    a = (y, x)
                    row.append(0)
                elif p == "B":
                    assert b is None
                    b = (y, x)
                    row.append(0)
                elif p == ".":
                    row.append(0)
                elif p == "#":
                    row.append(1)
                else:
                    raise ValueError("unexpected part", p)
            assert len(row) == size
            map_.append(row)
        return map_, a, b


images = []
a, start, end = load_a()
zoom = 20
borders = 6
m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i, j = start
m[i][j] = 1
k = 0
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
i, j = end
k = m[i][j]
the_path = [(i, j)]
while k > 1:
    if i > 0 and m[i - 1][j] == k - 1:
        i, j = i - 1, j
        the_path.append((i, j))
        k -= 1
    elif j > 0 and m[i][j - 1] == k - 1:
        i, j = i, j - 1
        the_path.append((i, j))
        k -= 1
    elif i < len(m) - 1 and m[i + 1][j] == k - 1:
        i, j = i + 1, j
        the_path.append((i, j))
        k -= 1
    elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
        i, j = i, j + 1
        the_path.append((i, j))
        k -= 1
print(len(the_path))
