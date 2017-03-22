# dictionary of numbers to symbols
def main():
    try:
        u_in = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
    print(u_in)
    return

main()
