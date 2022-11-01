def input_integer():
        
    while True:
        
        try:
            n = int(input("Enter an integer: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n <= 1:
                print("Number must be greater than one.")
            else:
                return n
                break


def get_primes(n):

    primes = list(range(2,n))
    p = 2

    while p <= pow(n, 0.5):

        for i in range(2*p, n, p):
            primes[i-2] = 0

        count = 1

        while primes[p - count] == 0:

            count -= 1

            if count < -n:
                break

        p = primes[p - count]

    return [i for i in primes if i != 0]


def display_result(n, primes):
    
    print(f'\nThe list of prime numbers smaller than {n} is:\n')
    print(*primes, sep = ', ')


def main():
    
    print('This program generates the prime numbers smaller than a given integer.')
    
    n = input_integer()
    
    if n == 2:
        print('There are no prime numbers smaller than 2.')
        return
    
    primes = get_primes(n)
    
    display_result(n, primes)


if __name__ == '__main__':

    main()