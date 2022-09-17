tax_bands = {
    '0':1,
    '12570':1,
    '50270':0.8,
    '150000':0.6,
    'Inf':0.55
}

tax_bands_sco = {
    '0':1,
    '12570':1,
    '14732':0.81,
    '25688':0.80,
    '43662':0.79,
    '150000':0.59,
    'Inf':0.54
}


def input_gross_salary():
        
    while True:
        
        try:
            n = round(float(input("Enter your gross salary (before tax) in GBP: ")),2)
            
        except:
            print("That is not a number. Please try again.")
            
        else:
            if n <= 0:
                print("Number must be positive.")
            else:
                return n
                break


def live_in_scotland():
    
    response = input("Do you live in Scotland? (Y/N): ")    
    
    while response.lower() not in ['y','n','yes','no',]:
        
        response = input("That is not a valid answer.\nDo you live in Scotland? (Y/N): ")
        
    return response.lower() in ['y','yes']


def calculate_net(g, s = False, tax_bands = tax_bands, tax_bands_sco = tax_bands_sco):
    
    g_str = str(g)
    
    if g_str < min(list(tax_bands)):
        return g
    
    if s:
        
        tax_bands = tax_bands_sco
    
    bands_and_gross = [float(i) for i in tax_bands]
    bands_and_gross.append(g)
    bands_and_gross.sort()
        
    tax_index = bands_and_gross.index(g)
    
    n = 0

    for i in range(1,tax_index):
        
        cur_band = float(list(tax_bands.keys())[i])
        low_band = float(list(tax_bands.keys())[i-1])
        multiplier = tax_bands[list(tax_bands.keys())[i]]
                
        n += (cur_band - low_band) * multiplier
        
    actual_band = float(list(tax_bands.keys())[tax_index-1])
    actual_rate = tax_bands[list(tax_bands.keys())[tax_index]]

    n += (g - actual_band) * actual_rate
    
    return n


def display_net(n, g):
    
    net_display = "£{:0,.2f}".format(n)
    tax_paid_display = "£{:0,.2f}".format(g-n)
    
    net_income_statement = f'Your annual net income is {net_display}.'
    tax_paid_statement = f'You will pay {tax_paid_display} income tax.'
    
    print(net_income_statement)
    print(tax_paid_statement)


def main():
    
    g = input_gross_salary()
    
    s = live_in_scotland()
    
    n = calculate_net(g, s = s)
    
    display_net(n, g)


if __name__ == '__main__':
    
    main()