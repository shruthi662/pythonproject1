def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input("Enter a positive integer: "))
    while num != 1:
        print(num, end=' ')
        num = collatz(num)
    print(1)  # Print the final 1 in the sequence
except ValueError:
    print("Please enter a valid integer.")
