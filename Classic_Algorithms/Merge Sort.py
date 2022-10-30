def input_list():
    
    response = []
    valid_response = False
    
    while not len(response) or not valid_response:
        
        try:
            response = list(map(int,input('\nEnter the numbers of the list you wish to sort, separated by spaces: ').strip().split()))
            
        except:
            print('\nThat is not a valid numerical list. Please enter the numbers of a list separated by spaces.')
        
        else:
            valid_response = True
            
    return response


def merge_lists(a, b):
    
    merged_list = []
    
    while len(a) and len(b):
        merged_list.append(min(a[0], b[0]))
        
        if a[0] < b[0]:
            a.pop(0)
            
        else:
            b.pop(0)
        
    if len(a):
        merged_list.extend(a)
        
    else:
        merged_list.extend(b)
    
    return merged_list


def split_list(a):
    
    a1 = a[0:int(len(a)/2)]
    a2 = a[int(len(a)/2):len(a)]
    
    return a1,a2


def merge_sort(s):
    
    if len(s) == 1:
        return s
    
    a,b = split_list(s)
    
    a_sorted = merge_sort(a)
    b_sorted = merge_sort(b)
    
    return merge_lists(a_sorted,b_sorted)


def display_sorted_list(s):
    
    print('\nThe sorted list is:')
    print(*s, sep = ', ')


def main():
    
    print('This program uses a Merge Sort to sort a numerical list.')
    
    s = input_list()
    
    s_sorted = merge_sort(s)
    
    display_sorted_list(s_sorted)


if __name__ == '__main__':
    
    main()