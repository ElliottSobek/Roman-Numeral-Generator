def place_rom_sym():
    result = []
    # rules for adding symbols
    return result

# num
# num // lowest num but bigger, for example 400 is smaller than L but bigger or equal than C; C < 400 < L
# store result in var
# result * var for amount of symbols
# num %= current roman numeral
# if 0; Done


def decompose_once(integer):
    numeral_lookup = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (5000, 'U+2181'),
                      (10000, 'U+2182'), (50000, 'U+2187'), (100000, 'U+2188')]
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
            print(pair[1] * result)
            integer -= result
            result %= prev
    return


def main():
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    decompose_once(u_in)
    return

main()
