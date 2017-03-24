numeral_lookup = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: 'U+2181', 10000: 'U+2182'
    , 50000: 'U+2187', 100000: 'U+2188'}

# num
# num // lowest num but bigger, for example 400 is smaller than L but bigger or equal than C; C < 400 < L
# store result in var
# result * var for ammount of symbols
# num %= current roman numeral
# if 0; Done


def decompose(integer):
    prev = -1
    while integer != 0:
        for key, rom_num in numeral_lookup.items():
            if key >= integer:
                break
            prev = key
        result = integer // prev
        if result != 0:
            print(numeral_lookup.get(prev) * result)
            result %= prev
    return


def main():
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    decompose(u_in)
    return

main()
