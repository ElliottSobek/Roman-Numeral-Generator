#     Roman Numeral Generator; Given a decimal number the roman numeral equivalent will be generated.
#     Copyright (C) 2017  Elliott Sobek
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

# test numbers: 3, 4, 6, 39, 73, 124, 578, 9999

numeral_lookup = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (5000, 'U+2181'),
                      (10000, 'U+2182'), (50000, 'U+2187'), (100000, 'U+2188')]


def place_rom_sym(symbol, value):
    result = []
    if result: # check if empty list; if so add right away
        result.append(symbol)
    # for item in numeral_lookup:
    #     if value < :
    #         result.append(symbol)
    result.append(symbol) # TMP
        # else result.insert(0, symbol) ?
    # or insert here?
    # check then append
    # check then insert index 0
    # rules for adding symbols
    return str(result)

# num
# num // lowest num but bigger, for example 400 is smaller than L but bigger or equal than C; C < 400 < L
# store result in var
# result * var for amount of symbols
# num %= current roman numeral
# if 0; Done


def decompose(integer):
    prev = -1
    pair = ()
    while integer != 0:
        for item in numeral_lookup:
            if item[0] > integer:
                break
            prev = item[0]
            pair = item
        result = integer // prev
        if result != 0:
            print(pair[1] * result) # place_roam_sym
            #place_rom_sym(pair[1] * result, integer)
            integer -= result
            result %= prev
    return


def long_decompose(integer):
    number = []
    prev = -1
    pair = ()
    while integer != 0:
        for item in numeral_lookup:
            if item[0] > integer:
                break
            prev = item[0]
            pair = item
        result = integer // prev
        if result != 0:
            print(pair[1] * result) # place_roam_sym
            #place_rom_sym(pair[1] * result, integer)
            integer -= prev * result
            result %= prev
    return


def main():
    print("Roman Numeral Generator  Copyright (C) 2017  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    # decompose(u_in)
    long_decompose(u_in)
    return

main()
