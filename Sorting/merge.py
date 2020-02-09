def merge_list(left_sublist, right_sublist):
    i, j = 0, 0
    result = []
    while i < len(left_sublist) and j < len(right_sublist):

        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            result.append(right_sublist[j])
            j += 1

    result += left_sublist[i:]
    result += right_sublist[j:]
    return result


def merge_sort(ilist):
    if len(ilist) <= 1:
        return ilist
    else:
        midpoint = int(len(ilist) / 2)
        left_sublist = merge_sort(ilist[:midpoint])
        right_sublist = merge_sort(ilist[midpoint:])
        return merge_list(left_sublist, right_sublist)


lst = [2, 6, 3, 9, 55, 12, 1, 13]
print(merge_sort(lst))