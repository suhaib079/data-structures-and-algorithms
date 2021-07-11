def insertion_sort(arr): 
  
    if len(arr)==0:
        return f'This list is empty'

    for i in range(1,len(arr)):
        j = i - 1
        temp = arr[i]
        while j>= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1]= temp
    return arr     


x = [8,4,23,42,16,15]

print(insertion_sort(x))