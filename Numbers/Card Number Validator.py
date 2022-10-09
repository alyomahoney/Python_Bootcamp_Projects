import re


def input_card_number():
    
    card_number_raw = input("Please enter your card number: ")
    
    card_number_clean = re.sub(r'[\D]', '', card_number_raw)
    
    return card_number_clean


def check_visa(card_number):
    
    pattern = r'^4\d{15}$'
    
    match = re.match(pattern, card_number)
    
    if match is None:
        return False
    
    else:
        return True


def check_amex(card_number):
    
    pattern = r'^3[47]\d{13}'
    
    match = re.match(pattern, card_number)
    
    if match is None:
        return False
    
    else:
        return True


def check_mastercard(card_number):
    
    pattern = r'^5[1-5]\d{14}$|^2((22[1-9]|2[3-9]\d)|[3-6]\d{2}|(720|7[01]\d))$'
    
    match = re.match(pattern, card_number)
    
    if match is None:
        return False
    
    else:
        return True


def check_luhn(card_number):
    
    total = 0
    double = False
    
    for i in card_number[::-1]:
        
        i = int(i)
        
        if double:
            i *= 2
            
            if i >= 10:
                i -= 9
        
        total += i
        double = not double
                
    return total % 10 == 0


def get_issuer(card_number):
    
    if check_visa(card_number):
        return 'Visa'
    
    elif check_amex(card_number):
        return 'AMEX'
    
    elif check_mastercard(card_number):
        return 'Mastercard'
    
    else:
        return False


def display(issuer):
    
    if bool(issuer):
        print(f'That is a valid {issuer} card number.')
        
    else:
        print('That is not a valid card number')


def main():
    
    card_number = input_card_number()
    
    if not check_luhn(card_number):
        print('That is not a valid card number.')
        return
        
    issuer = get_issuer(card_number)
        
    display(issuer)


if __name__ == '__main__':
    
    main()