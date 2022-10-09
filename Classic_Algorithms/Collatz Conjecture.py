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


def collatz(n):
    
    collatz_list = [n]
    
    while n > 1:
        
        if n % 2 == 0:
            n //= 2
            
        else:
            n = n*3 + 1
            
        collatz_list.append(n)
        
    return(collatz_list)


def display(collatz_list):
    
    iterations = len(collatz_list) - 1
    
    print(f'It took {iterations} iterations to reach 1. Here is the sequence:')
    print(*collatz_list, sep = ', ')


def main():
    
    n = input_integer()
        
    collatz_list = collatz(n)
    
    display(collatz_list)


if __name__ == '__main__':
    
    main()