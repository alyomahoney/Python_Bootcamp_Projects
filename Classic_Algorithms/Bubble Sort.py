def input_list():
    
    response = []
    valid_response = False
    
    while not len(response) or not valid_response:
        
        try:
            response = list(map(float,input('\nEnter the numbers of the list you wish to sort, separated by spaces: ').strip().split()))
            
        except:
            print('\nThat is not a valid numerical list. Please enter the numbers of a list separated by spaces.')
        
        else:
            valid_response = True
            
    return response


def bubble_sort(s):
    
    n = len(s)
    
    while True:
    
        swap = False
        
        for i in range(n-1):

            if s[i] > s[i+1]:

                s[i], s[i+1] = s[i+1], s[i]
                swap = True
                last_swap = i

        if not swap:
            break
            
        n = last_swap + 1
        
    return s


def display_sorted_list(s):
    
    formatted_list = [('%f' % i).rstrip('0').rstrip('.') for i in s]

    print('\nThe sorted list is:')
    print(*formatted_list, sep = ', ')


def main():
    
    print('This program uses a Bubble Sort to sort a numerical list.')
    
    s = input_list()
    
    s_sorted = bubble_sort(s)
    
    display_sorted_list(s_sorted)


if __name__ == '__main__':
    
    main()