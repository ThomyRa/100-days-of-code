
def prime_checker(number):
    for num in range(2, number // 2 + 1):
        if (number % num == 0):
            print('Not prime')
    print('Is Prime')

n = int(input("Check this number: "))
prime_checker(number=n)