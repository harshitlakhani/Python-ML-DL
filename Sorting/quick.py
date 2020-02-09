lst = [3,22,7,2,1,5,4]


def quick_sort(l,r):
    if l<r:
        pi = partition(l,r)
        
        quick_sort(l,pi-1)
        quick_sort(pi+1,r)

def partition(left,right):
    pivot = lst[right]
    i = left-1
    
    for j in range(left,right):
        if lst[j]<pivot:
            i = i+1
            lst[i],lst[j] = lst[j],lst[i]
    lst[i+1],lst[right] = lst[right],lst[i+1]
    return i+1
    

length = len(lst)
quick_sort(0,length-1)
print(lst)
