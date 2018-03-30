#!/usr/bin/python3

#     Roman Numeral Generator; Given a decimal number the roman numeral
#     equivalent will be generated.
#     Copyright (C) 2018  Elliott Sobek
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

from os.path import basename
from sys import argv, exit
from getopt import getopt, GetoptError

num_lookup = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (5000, '\u2181'),
              (10000, '\u2182'), (50000, '\u2187'), (100000, '\u2188')]


def recurse_gn(num):
    if num == 0:
        return

    for f_i in range(1, len(num_lookup), 1):  # f_i: forward index

        for b_i in range(f_i - 1, -1, -1):  # b_i: backwards index
            prev_asoc = num_lookup[b_i]

            if (num == (num_lookup[f_i][0] - prev_asoc[0])) and (num != (num_lookup[f_i][0] // 2)):
                print("bob", end='')
                print(prev_asoc[1] + num_lookup[f_i][1], end='')
                num -= (num_lookup[f_i][0] - prev_asoc[0])
                recurse_gn(num)
                return
            elif num == (num_lookup[f_i][0] + prev_asoc[0]):
                print(num_lookup[f_i][1] + prev_asoc[1], end='')
                num -= (num_lookup[f_i][0] + prev_asoc[0])
                recurse_gn(num)
                return

    prev_asoc = (1, 'I')
    for num_asoc in num_lookup:

        if num < num_asoc[0]:
            print(prev_asoc[1], end='')
            num -= prev_asoc[0]
            recurse_gn(num)
            return
        prev_asoc = num_asoc


def generate_numeral(num):
    result = []

    while num != 0:

        for f_i in range(1, len(num_lookup), 1):  # f_i: forward index

            for b_i in range(f_i - 1, -1, -1):  # b_i: backwards index
                prev_asoc = num_lookup[b_i]

                if (num == (num_lookup[f_i][0] - prev_asoc[0])) and (num != (num_lookup[f_i][0] // 2)):
                    result.append(prev_asoc[1])
                    result.append(num_lookup[f_i][1])
                    num -= (num_lookup[f_i][0] - prev_asoc[0])
                    break
                elif num == (num_lookup[f_i][0] + prev_asoc[0]):
                    result.append(num_lookup[f_i][1])
                    result.append(prev_asoc[1])
                    num -= (num_lookup[f_i][0] + prev_asoc[0])
                    break

        if num == 0:
            break

        prev_asoc = (1, 'I')
        for num_asoc in num_lookup:

            if num < num_asoc[0]:
                result.append(prev_asoc[1])
                num -= prev_asoc[0]
                break
            prev_asoc = num_asoc

    return ''.join(result)


def main(argc=len(argv), argvs=argv):
    if argc < 2 or argc > 3:
        print("Usage: python3 " + basename(argvs[0]) + " [-hr] <unsigned int>")
        exit(1)
    opts = ''

    try:
        opts, args = getopt(argvs[1:], "hr")
    except GetoptError as e:
        print(e.msg)
        exit(1)
    recurse = False

    for opt, args in opts:
        if opt == "-h":
            print("Usage: python3 " + basename(argvs[0]) + " [-hr] <unsigned int>\n\n"
                                                           "\t-h\tHelp\n\n"
                                                           "\t-r\tRecursive")
            exit(1)
        elif opt == "-r":
            recurse = True
    usr_in = 0

    try:
        usr_in = int(argvs[-1])
    except ValueError as e:
        print(e)
        exit(1)

    if usr_in < 1:
        print("Error: Number is less than 1")
        exit(1)

    print("Roman Numeral Generator  Copyright (C) 2018  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.")

    if recurse:
        print(recurse_gn(usr_in))
    else:
        print(generate_numeral(usr_in))
    return


main()
