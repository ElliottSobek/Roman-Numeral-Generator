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

numeral_lookup = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (5000, '\u2181'),
                  (10000, '\u2182'), (50000, '\u2187'), (100000, '\u2188')]


def is_subtraction(num):
    result = []
    item = numeral_lookup

    for i in range(1, len(item), 1):
        for j in range(i - 1, -1, -1):
            prev2 = item[j]
            if (num == (item[i][0] - prev2[0])) and (num != (item[i][0] // 2)):
                result.append(prev2[1])
                result.append(item[i][1])
                num -= (item[i][0] - prev2[0])
                return True
    return False


def is_addition(num):
    result = []
    item = numeral_lookup
    
    for i in range(1, len(item), 1):
        for j in range(i - 1, -1, -1):
            prev2 = item[j]
            if num == (item[i][0] + prev2[0]):
                result.append(item[i][1])
                result.append(prev2[1])
                num -= (item[i][0] + prev2[0])
                return True
    return False


def generate_numeral(num):
    result = []
    while num != 0:
        if num == 1:
            result.append('I')
            break
        prev = (0, 'Q')
        for item in numeral_lookup:
            if (num == (item[0] - prev[0])) and (num != (item[0] // 2)):  # Subtraction
                result.append(prev[1])
                result.append(item[1])
                num -= (item[0] - prev[0])
                break
            elif num == (item[0] + prev[0]):  # Addition
                result.append(item[1])
                result.append(prev[1])
                num -= (item[0] + prev[0])
                break
            prev = item
        if num == 0:
            break
        newPrev = (1, 'I')
        for newitem in numeral_lookup:
            if num < newitem[0]:
                result.append(newPrev[1])
                num -= newPrev[0]
                break
            newPrev = newitem
    return ''.join(result)


def main():
    print("Roman Numeral Generator  Copyright (C) 2017  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")
    # try:
    #     u_in = int(input("Enter a number: "))
    # except ValueError:
    #     print("Invalid input")
    #     return
    # print(decompose(u_in))
    # print(generate_numeral(3))
    # print(generate_numeral(4))
    # print(generate_numeral(5))
    # print(generate_numeral(6))
    # print(generate_numeral(8))
    # print(generate_numeral(39))
    # print(generate_numeral(73))
    # print(generate_numeral(124))
    # print(generate_numeral(578))
    # print(generate_numeral(9999))
    print(is_addition(60))
    return


main()
