with open('advent_7.test.txt', 'r') as file:
    files = file.readlines()
x = [[int(x__) for x__ in x_.split()] for x_ in files]
iterator = 0

indices = []
for i in x:
    iterator += 1
    if i[0] == 0:
        indices.append(iterator)
cells = []
answers = []
for i in x[1:]:
    length = len(i[1:])
    for j in i:
        if j in indices:
            cells.append(j)
    if len(cells) == length:
        if len(cells) != 0:
            answers.append(cells.copy())
    else:
        cells.clear()
print(answers)

with open('advent_10.test.txt', 'r') as file:
    files = file.readline()
x = [int(i) for i in files.split()]


def largest_rect(n, a_list):
    all_sums = []
    for index, element in enumerate(a_list):
        for i in range(index + 1, n):
            s = a_list[index: i + 1]
            all_sums.append(len(s) * min(s))
    return max(all_sums)


print(largest_rect(1000, x))

with open('advent_13.test.txt', 'r') as file:
    files = file.readlines()
x = [int((i.strip()[-10:])) for i in files]
x.sort()
my = str(x[7492])
with open('advent_13.test (2).txt', 'r') as file:
    files = file.readlines()
y = [i.strip() for i in files]
for i in y:
    ex = []
    for j in i:
        if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            ex.append(j)
        answer = ''.join(ex)
        if my in answer:
            print(i)
