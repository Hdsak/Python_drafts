def hex_output():
    dec = 0
    hex = input('Hex number to convert: ')
    for power, digit in enumerate(reversed(hex)):
        dec += int(digit, 16) * (16 ** power)
    print(dec)
hex_output()