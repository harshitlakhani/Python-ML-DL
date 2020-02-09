def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i-1,0,-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]

    return arr


lst = [22,31,45,74,89,33,64,46]

print(insertion_sort(lst))