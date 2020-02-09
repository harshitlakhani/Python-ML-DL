def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]

    return arr


lst = [8,3,99,12,45,32,53,9]

print(selection_sort(lst))