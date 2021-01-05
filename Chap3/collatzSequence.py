def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print( 3 * number + 1)
        return 3 * number + 1

n = input('Enter any number: ')
while n !=1:
    n = collatz(int(n))

# print('Enter a number')
# try:
#     number = int(input())
#     collatz(number)
# except ValueError:
#     print('You must type a number.')