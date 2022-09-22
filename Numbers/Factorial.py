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


def factorial(n):
    
    if n in [0,1]:
        
        return 1
    
    else:
        
        return n * factorial(n-1)


def main():
    
    print('This program calculates the factorial of a given integer.')
    
    n = input_integer()
    
    res = factorial(n)
    
    print(f'{n}! = {res}')


if __name__ == '__main__':
    
    main()