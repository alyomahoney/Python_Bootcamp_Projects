def input_integer():
    
    need_number = True
    
    while need_number:
        
        try:
            n = int(input("Enter a number: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 1:
                print("Number must be positive.")
            else:
                return n
            need_number = False
            break


def prime_factors(n):
    
    factors_list = []
    
    while True:
        
        start_length = len(factors_list)

        for i in range(2,int(n)+1):

            if n % i == 0:
                factors_list.append(i)
                n /= i
                break
                
        end_length = len(factors_list)
        
        if start_length == end_length:
            break
            
    return factors_list


import collections

def display_factors(f):
    
    factor_display = []
    
    if len(f) == 1:
        return f'{f[0]} is a prime number.'
    
    freq = collections.Counter(f)
    
    for i in set(f):
        
        if freq[i] == 1:
            factor_display.append(str(i))
            
        else:
            factor_display.append(str(i)+'^'+str(freq[i]))
    
    return ', '.join(factor_display)


def main():
    
    n = input_integer()
    
    factors = prime_factors(n)
    
    print(display_factors(factors))


if __name__ == '__main__':
    main()