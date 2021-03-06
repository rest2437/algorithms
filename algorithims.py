# def binary_search(arr, value, offset=0):
#     mid = len(arr) / 2
#     if value < arr[mid]:
#         binary_search(arr[0, mid], value, offset)
#     elif value > [mid]:
#         binary_search(arr[mid + 1, -1], value, offset + mid + 1)
#     else:
#         return offset + mid


# print(binary_search())

def merge(Arr, start, mid, end):

    # create a temp array
    [] = [0] * (end - start + 1)

    # crawlers for both intervals and for temp
    i, j, k = start, mid+1, 0

    # traverse both lists and in each iteration add smaller of both elements in temp
    while(i <= mid and j <= end):
        if(Arr[i] <= Arr[j]):
            [k] = Arr[i]
            k += 1
            i += 1
        else:
            [k] = Arr[j]
            k += 1
            j += 1

    # add elements left in the first interval
    while(i <= mid):
        [k] = Arr[i]
        k += 1
        i += 1

    # add elements left in the second interval
    while(j <= end):
        [k] = Arr[j]
        k += 1
        j += 1

    # copy temp to original interval
    for i in range(start, end+1):
        Arr[i] = [i - start]


print(merge([8, 4, 5, 2, 7]))
# Arr is an array of integer type
# start and end are the starting and ending index of current interval of Arr


def mergeSort(Arr, start, end):

    if(start < end):
        mid = (start + end) / 2
        mergeSort(Arr, start, mid)
        mergeSort(Arr, mid+1, end)
        merge(Arr, start, mid, end)
