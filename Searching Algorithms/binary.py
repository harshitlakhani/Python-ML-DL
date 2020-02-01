
'''Binary Search'''

data = int(input('Enter the number:'))


''' the list data needs to be in sorted order'''

lst = [2, 7,8,9,14,23,48,80]

def binary_search(left,right):
    global lst
    global data
   
    if left <= right:
        print(left,right)
        middle = int((left + right) / 2)
        print(middle)
        
        if lst[middle] == data:
            return 'Available'
        elif data < lst[middle]:
            return binary_search(left,middle-1)
        elif data > lst[middle]:
            return binary_search(middle+1,right)
    else:
        return 'Not Available'
    
    
    
print(binary_search(0,len(lst)-1))
