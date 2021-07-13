def quicksort(arr, L, R):
  if L < R:
      position = Partition(arr, L, R)
      quicksort(arr, L, position - 1)
      quicksort(arr, position + 1, R)
  return arr

def Partition(arr, L, R):
  pivot = arr[R]
  low = L - 1
  for i in range(L,R):
    if arr[i] <= pivot:
      low+= 1
      Swap(arr, i, low)
  Swap(arr, R, low + 1)
  return low + 1

def Swap(arr, i, low):
  temp = arr[i]
  arr[i] = arr[low]
  arr[low] = temp