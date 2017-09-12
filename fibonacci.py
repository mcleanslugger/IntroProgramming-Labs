def main():
    previous = 1
    current = 1
    n = int(input("Enter the nth place you want to find in the fibonacci sequence: "))
    for i in range(0, n-2):
        previous, current = current, previous + current
    print(current)


main()
