import numpy as np


def input_integer():
        
    while True:
        
        try:
            n = int(input("Enter the number of coin tosses: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 1:
                print("Number must be positive.")
            else:
                return n
                break


def display_results(n):
    
    h = np.random.binomial(n,0.5)
    t = n - h
    
    print(f'Tosses: {n}')
    print(f'Heads:  {h}')
    print(f'Tails:  {t}')


def main():
    
    n = input_integer()
    
    display_results(n)


if __name__ == '__main__':
    
    main()