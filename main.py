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


def generate_numeral(num):
    numeral_lookup = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (5000, '\u2181'),
                      (10000, '\u2182'), (50000, '\u2187'), (100000, '\u2188')]
    result = []
    while num != 0:

        for i in range(1, len(numeral_lookup), 1):
            for j in range(i - 1, -1, -1):
                prev2 = numeral_lookup[j]
                if (num == (numeral_lookup[i][0] - prev2[0])) and (num != (numeral_lookup[i][0] // 2)):
                    result.append(prev2[1])
                    result.append(numeral_lookup[i][1])
                    num -= (numeral_lookup[i][0] - prev2[0])
                    break
                elif num == (numeral_lookup[i][0] + prev2[0]):
                    result.append(numeral_lookup[i][1])
                    result.append(prev2[1])
                    num -= (numeral_lookup[i][0] + prev2[0])
                    break

        if num == 0:
            break

        prev = (1, 'I')
        for item in numeral_lookup:
            if num < item[0]:
                result.append(prev[1])
                num -= prev[0]
                break
            prev = item

    return ''.join(result)


def main():
    print("Roman Numeral Generator  Copyright (C) 2017  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    print(generate_numeral(u_in))
    return

main()
