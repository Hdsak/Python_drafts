def mySum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


print(mySum(1, 2, 3, 4, 5))
print(mySum(*[1, 2, 3, 4, 5]))
