import math
import decimal as d


def input_integer():
        
    while True:
        
        try:
            n = int(input("How many decimal places would you like the number displayed to?: "))
            
        except:
            print("That is not an integer. Please try again.")
            
        else:
            if n < 0:
                print("Number must not be negative.")
            else:
                return n
                break


def input_decimal():
    
    while True:
        
        try:
            d_raw = input("Enter a number: ")
            d_float = float(d_raw)
            
        except:
            print("That is not a number")
            
        else:
            return d_raw


def input_binary():
    
    b_raw = input("Enter a binary number: ")
    
    while len(set(b_raw).difference(set('01.'))) or b_raw.count('.') > 1:
        
        print("A binary number must contain only zeroes and ones. Please try again.")
        b_raw = input("Enter a binary number: ")
        
    return b_raw


def decimal_to_binary_integer(d_raw):
    
    integer_portion = int(d.Decimal(d_raw))
    
    return bin(integer_portion)[2:]


def decimal_to_binary_fraction(d_raw, p):
    
    d_decimal = d.Decimal(d_raw)
    d_fraction = d_decimal - int(d_decimal)
    b_fraction = ''
    
    if d_fraction == 0:
        
        return b_fraction
    
    for i in range(1,p+1):
        
        if d_fraction < 1/pow(d.Decimal('2'),i):
            
            b_fraction = b_fraction + '0'
            
        else:
            
            b_fraction = b_fraction + '1'
            d_fraction -= 1/pow(d.Decimal('2'),i)
            
    return b_fraction


def decimal_to_binary(d_raw, p):
    
    d_integer = decimal_to_binary_integer(d_raw)
    d_fraction = decimal_to_binary_fraction(d_raw, p)
    
    return d_integer + '.' + d_fraction


def binary_to_decimal_integer(b_raw):
    
    if '.' not in b_raw:
        
        integer_portion = b_raw
        
    else:
    
        integer_portion = b_raw[:b_raw.index('.')]
    
    if '1' not in integer_portion:
        
        return 0
    
    decimal_int = 0
    
    for i in range(len(integer_portion)):
        
        decimal_int += int(integer_portion[-i-1])*2**i
    
    return decimal_int


def binary_to_decimal_fraction(b_raw):
    
    dot_position = b_raw.find('.')
    
    if dot_position in [-1, len(b_raw)-1]:
        
        return 0
    
    fraction_portion = b_raw[dot_position + 1:]
    
    decimal_frac = 0
    
    for i in range(len(fraction_portion)):
        
        decimal_frac += 1/pow(2, i+1)*int(fraction_portion[i])
        
    return decimal_frac


def binary_to_decimal(b_raw):
    
    decimal_int = binary_to_decimal_integer(b_raw)
    decimal_frac = binary_to_decimal_fraction(b_raw)
    
    return decimal_int + decimal_frac


def main():
    
    print('This program converts decimal numbers into binary nubers and vice versa.')
    
    dec_or_bin = input('Would you like to enter a decimal (d) or binary (b) number?: ')
    
    while dec_or_bin.lower() not in ['d','b','decimal','binary','dec','bin']:
        
        dec_or_bin = input('That is not a valid input.\nWould you like to enter a decimal (d) or binary (b) number?: ')
        
    if dec_or_bin in ['d','decimal','dec']:
        
        user_dec = input_decimal()
        
        if int(d.Decimal(user_dec)) == float(user_dec):
            
            output_bin = decimal_to_binary_integer(user_dec)
            print('Your number in binary form is ' + output_bin)
        
        else:
            
            precision = input_integer()
            output_bin = decimal_to_binary(user_dec, precision)
            print('Your number in binary form is ' + output_bin)
            
    else:
        
        user_bin = input_binary()
        output_dec = binary_to_decimal(user_bin)
        print('Your number in decimal form is ' + str(output_dec))


if __name__ == '__main__':
    
    main()