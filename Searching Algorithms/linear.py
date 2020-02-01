
'''Linear Search'''

data = int(input('Enter the number:'))

lst = [2, 9, 33, 72, 21, 23,54]

def linear_search(num, arr):
    
    ''' Checks the elements one by one '''
    
    for i in arr:
        if i == num:
            return 'Available'
    return 'Not Available'
    
    
print(linear_search(data, lst))
