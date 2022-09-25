def input_integer():
        
    while True:
        
        try:
            n = int(input("Enter an integer: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 1:
                print("Number must be positive.")
            else:
                return n
                break


def is_happy(n):
    
    results = [n]
    
    while True:
        
        total = 0
        
        for i in str(n):
            
            total += pow(int(i),2)
            
        results.append(total)
        n = total
        
        if results.count(total) > 1:
            
            if total != 1:
                
                return results, False
        
            else:
                
                results.pop()
                return results, True


def display_output(is_happy):
    
    if is_happy[1]:
        
        print(f'{is_happy[0][0]} is a happy number. Here is the sequence.')
        
    else:
        print(f'{is_happy[0][0]} is not a happy number. Here is the sequence, which enters an infinite cycle at {is_happy[0][-1]}.')
    
    print(*is_happy[0], sep = ', ')


def main():
    
    n = input_integer()
    
    is_happy_res = is_happy(n)
    
    display_output(is_happy_res)


if __name__ == '__main__':
    
    main()