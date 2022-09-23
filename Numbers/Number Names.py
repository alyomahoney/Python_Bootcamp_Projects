import re


units = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}

ten_to_nineteen = {
    0:'',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
}

tens = {
    0:'',
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety',
}


def input_integer():
    
    print('This program takes an integer with an absolute value less than one million and prints it in English.')
    
    while True:
        
        try:
            n = int(input("Enter a number: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            
            if abs(n) >= 1000000:
                
                print('Absolute value must not exceed one million.')
                
            else:
            
                n_list = [0,0,0,0,0,0]
                n_list.extend([int(i) for i in str(abs(n))])
                
                return n_list, n


def last_three(n_list):

    if n_list[-2] == 1:

        last_three = ten_to_nineteen[n_list[-2]*10 + n_list[-1]]

    else:

        last_three = tens[n_list[-2]] + ' ' + units[n_list[-1]]

    if n_list[-3] != 0:
        
        if n_list[-2] == n_list[-1] == 0:
            
            last_three = units[n_list[-3]] + ' hundred' + last_three
            
        else:

            last_three = units[n_list[-3]] + ' hundred and ' + last_three
        
    return last_three


def first_three(n_list):
    
    first_three = last_three(n_list[:-3]) + ' thousand'
    
    if n_list[-3] == 0:
        
        if last_three(n_list) != ' ':
            
            first_three = first_three + ' and '
        
    else:
        
        first_three = first_three + ', '
        
    return first_three


def main():
        
    n_list, n = input_integer()
    
    first = ''
    
    if abs(n) >= 1000:
    
        first = first_three(n_list)
    
    last = last_three(n_list)
    
    if abs(n) == n:
        
        is_negative = ''
        
    else:
        
        is_negative = 'negative '
    
    print(is_negative + re.sub('\s{2,}',' ',(first + last).strip()))


if __name__ == '__main__':
    
    main()