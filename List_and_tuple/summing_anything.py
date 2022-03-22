def sum_anything(*items):
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(sum_anything(10, 20, 30, 40))
print(sum_anything('a', 'b', 'c', 'd'))
print(sum_anything([10, 20, 30], [40, 50, 60], [70, 80]))
