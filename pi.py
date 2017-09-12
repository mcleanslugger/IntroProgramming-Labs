import math
def main():
    pi = 0
    sign = 1
    n = int(input("Enter the nth number you want to find: "))
    for denominator in range(1, n*2, 2):
        pi = pi + sign * 4 / denominator
        sign = sign * -1
    print(pi)
    print(math.pi - pi)
main()
