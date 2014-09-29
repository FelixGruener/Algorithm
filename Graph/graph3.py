def countInversion(array):
  n = len(array)
  if n == 1:
    return 0
  else:
    left_array = array[:n/2]
    right_array = array[n/2:]
    countLeft = countInversion(left_array)
    countRight = countInversion(right_array)
    countMerge = merge(left_array,right_array,array)
    return countLeft+countRight+countMerge
  
def merge(left_array,right_array,array):
  count = 0
  p, q = len(left_array), len(right_array)
  i, j, k = 0, 0, 0
  while (i < p) and (j < q):
    if left_array[i] <= right_array[j]:
      array[k] = left_array[i]
      i += 1
    else:
      array[k] = right_array[j]
      j += 1
      count += (p - i)
    k += 1
  if i == p:
    array[k:] = right_array[j:]
  else:
    array[k:] = left_array[i:]
  return count
