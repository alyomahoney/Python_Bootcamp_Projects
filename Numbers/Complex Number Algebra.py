import re


class ComplexNumber:
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f'{self.real} + {self.imaginary}i'
    
    def com_round(self, n):
        return f'{round(self.real,n)} + {round(self.imaginary,n)}i'


def initial_prompt():
    
    selection = input('This program performs basic complex number algebra.\nFirst, choose a complex number function:\n\nsubtraction, addition, multiplication, division, inversion or negation: ').lower()
    
    complex_functions = ('subtraction','addition','multiplication','division','inversion','negation')
    
    while selection not in complex_functions:
        
        selection = input('That is not a valid function.\n\nPlease choose either subtraction, addition, multiplication, division, inversion or negation: ').lower()
        
    return selection


def input_complex_number():
    
    pattern = r'^\s*(-?\d*)\s*(([\+-]\s*\d*)i)?\s*$'
    
    while True:
        
        n = input('Enter a complex number in the form x + yi: ')
        matched = re.match(pattern, n)
        
        imaginary_pattern = r'^(\s*-?\d)*i'
        imaginary_matched = re.match(imaginary_pattern, n)
        
        if bool(matched) and not (n.isspace() or n == ''):
            
            if matched.group(3) is None:
                imaginary = 0
                
            else:
            
                imaginary_temp = matched.group(3).replace(' ','')

                if imaginary_temp in ('+','-'):
                    imaginary = float(f'{imaginary_temp}1')

                else:
                    imaginary = float(matched.group(3).replace(' ',''))
            
            
            if matched.group(1) == '':
                real = 0

            else:
                real = float(matched.group(1).replace(' ',''))
            
            imaginary_pattern = r'^\s*-?\d*i'
            
            break
        
        elif bool(imaginary_matched):
            
            
            real = 0
            
            if imaginary_matched.group(1) is None:
                imaginary = 1
                
            elif imaginary_matched.group(1).replace(' ','') == '-':
                imaginary = -1
                
            else:
                imaginary = float(imaginary_matched.group(1))
                
            break
        
        else:
            
            print('That is not a valid  input. Complex numbers must be in the form x + iy')
            
    return ComplexNumber(real, imaginary)


def com_addition(com1, com2):
    
    x = com1.real + com2.real
    y = com1.imaginary + com2.imaginary
    
    return ComplexNumber(x,y)


def com_subtraction(com1, com2):
    
    x = com1.real - com2.real
    y = com1.imaginary - com2.imaginary
    
    return ComplexNumber(x,y)


def com_division(com1, com2):
    
    denominator = pow(com2.real,2) + pow(com2.imaginary,2)
    
    x = (com1.real * com2.real - com1.imaginary * com2.imaginary) / denominator
    y = (com1.imaginary * com2.real) - (com1.real * com2.imaginary) / denominator
    
    return ComplexNumber(x,y)


def com_multiplication(com1, com2):
    
    x = (com1.real * com2.real) - (com1.imaginary * com2.imaginary)
    y = (com1.real * com2.imaginary) + (com2.real * com1.imaginary)
    
    return ComplexNumber(x,y)


def com_inversion(com1):
    
    denominator = pow(com1.real,2) + pow(com1.imaginary,2)
    
    x =  com1.real/denominator
    y = -com1.imaginary/denominator
    
    return ComplexNumber(x,y)


def com_negation(com1):
    
    x =  com1.real
    y = -com1.imaginary
    
    return ComplexNumber(x,y)


def input_second_number(selection, com1):
    
    if selection == 'addition':
        print(f'Choose a number to add to {str(com1)}.')
        
    elif selection == 'subtraction':
        print(f'Choose a number to subtract from {str(com1)}.')
        
    elif selection == 'multiplication':
        print(f'Choose a second number to multiply {str(com1)} by.')
        
    else:
        print(f'Choose a number to divide {str(com1)} by.')
    
    com2 = input_complex_number()
    
    return com2


def calculate_answer(selection, com1, com2):
    
    if selection == 'addition':
        ans = com_addition(com1, com2)
        
    elif selection == 'subtraction':
        ans = com_subtraction(com1, com2)
        
    elif selection == 'multiplication':
        ans = com_multiplpication(com1, com2)
        
    elif selection == 'division':
        ans = com_division(com1, com2)
        
    elif selection == 'inversion':
        ans = com_inversion(com1)
        
    else:
        ans = com_negation(com1)
        
    return ans


def main():
    
    selection = initial_prompt()
    
    com1 = input_complex_number()
    
    if selection not in ('negation', 'inversion'):
        com2 = input_second_number(selection, com1)
        
    else:
        com2 = ComplexNumber(1,1)
        
    ans = calculate_answer(selection, com1, com2)
    
    print('Answer: ' + str(ans.com_round(3)))


if __name__ == '__main__':
    
    main()