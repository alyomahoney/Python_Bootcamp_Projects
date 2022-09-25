import decimal as d


def input_integer():
        
    while True:
        
        try:
            n = int(input("Enter an integer: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 0:
                print("Number must not be negative.")
            else:
                return n
                break


def calculate_e(n):
    
    d.getcontext().prec = n+5

    factorial = 1
    e = 1

    for i in range(1, 1000):

        factorial *= i
        e += d.Decimal('1')/d.Decimal(str(factorial))
        
    return round(e,n)


def main():
    
    n = input_integer()
    
    result = calculate_e(n)
    
    plural = ''
    
    if n != 1:
        plural = 's'
    
    print(f'e rounded to {n} decimal place{plural} is:')
    print(result)


if __name__ == '__main__':
    
    main()
