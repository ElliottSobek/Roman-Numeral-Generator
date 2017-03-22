def main():
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    numeral_lookup = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    print(numeral_lookup.get(1))
    print(u_in)
    return

main()
