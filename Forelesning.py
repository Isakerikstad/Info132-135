def insertion_sort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr[j + 1] = key


x = [3,4,5,1,2,66,44,22,324,425,24]
insertion_sort(x)
print(x)


