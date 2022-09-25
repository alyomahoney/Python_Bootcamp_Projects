money_items = {
    '£50':50,
    '£20':20,
    '£10':10,
    '£5 ':5,
    '£2 ':2,
    '£1 ':1,
    '50p':.5,
    '20p':.2,
    '10p':.1,
    '5p ':.05,
    '2p ':.02,
    '1p ':.01
}


def input_cost_given():
    
    while True:
        
        try:
            c = float(input("Enter the cost: "))
            
        except:
            print("That is not a number. Please try again.")
            
        else:
            if c <= 0:
                print("Cost must be positive.")
                
            elif round(c, 2) != c:
                print("Must not be to more than two decimal places.")
                
            else:
                cost = c
                break
                
    while True:
        
        try:
            g = float(input("Enter the amount given: "))
            
        except:
            print("That is not a number. Please try again.")
            
        else:
            if g <= 0:
                print("Amount given must be positive.")
                
            elif round(g, 2) != g:
                print("Must not be to more than two decimal places.")
                
            elif g < c:
                print(f"The amount given cannot be less than the cost which is £{c}")
                
            else:
                given = c
                break
                
    return c, g


def calculate_items_given(c, g):
    
    change = round(g - c, 2)
    
    number_of_each_item = []

    for i in list(money_items.values()):

        number_this_instance = change//i

        change -= number_this_instance * i
        change = round(change, 2)

        number_of_each_item.append(number_this_instance)

        if change == 0:

            break
            
    return number_of_each_item


def display_change(number_of_each_item):
    
    for i in range(len(number_of_each_item)):
    
        if number_of_each_item[i] != 0:

            print(list(money_items.keys())[i] + ': ' + str(int(number_of_each_item[i])))


def main():
    
    c, g = input_cost_given()
    
    number_of_each_item = calculate_items_given(c, g)
    
    display_change(number_of_each_item)


if __name__ == '__main__':
        
        main()