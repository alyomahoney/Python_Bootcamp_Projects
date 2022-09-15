def fib_seq(n):

    fib = [1,1]
    for i in range(n):
        fib.append(fib[-1]+fib[-2])

    del fib[-2:]

    for i in range(len(fib)):
        fib[i] = str(fib[i])

    return ', '.join(fib)


def input_integer():
        
    while True:
        
        try:
            n = int(input("Enter a number: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 1:
                print("Number must be positive.")
            else:
                return n
                break


def main():
    
    n = input_integer()
    
    sequence = fib_seq(n)
    
    print(sequence)


if __name__ == '__main__':
    main()