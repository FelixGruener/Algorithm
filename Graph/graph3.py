def countInversion(array):
  '''
  count number of inversions in the array, and perform sorting with smallest first
  input: array
  output: number of inversions in the array, the original array will be sorted
  '''
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
  '''
  merge function for countInversion(array)
  '''
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


def mystery(array,left_boundary,right_boundary):
  '''
  return i if there exists an i such that array[i] == i, and -1 otherwise
  '''
  if left_boundary > right_boundary:
    return -1
  middle = (left_boundary + right_boundary)/2
  if array[middle] == middle:
    return middle
  else:
    if array[middle] < middle:
      return mystery(array, middle + 1, right_boundary)
    else:
      return mystery(array, left_boundary, middle - 1)

    
def hierarchicalClustering(points, k):
  '''
  input: points whose ith point pi is a pair(xi,yi), and k, the desired number of cluster
  output: k clusters
  '''
  n = len(points)
  clusters = [{i} for i in points.keys()]
  while len(clusters) > k:
    i, j = closestPair(clusters)
    clusters.append(i.union(j))
    clusters.remove(i)
    clusters.remove(j)
  return clusters


def euclidianDistance(p1, p2):
  '''
  input: two points
  output: euclidian distance between the two points
  '''
  return sum([(p1[i] - p2[i])**2 for i in range(len(p1))])**0.5
  

def BFClosestPair(points):
  '''
  brute-force algorithm for solving the closest pair problem
  input: a set p of more than 2 points
  output: a tuple(d,i,j) where d is the smallest pairwise distance of points in p and i,j are the indices of two points
  '''
  smallestDistance = euclidianDistance(points[0],points[1])
  smallestI = 0
  smallestJ = 1
  for i in range(len(points)-1):
    for j in range(i+1, len(points)):
      if euclidianDistance(points[i],points[j]) < smallestDistance:
        smallestDistance = euclidianDistance(points[i],points[j])
        smallestI = i
        smallestJ = j
  return (smallestDistance, smallestI, smallestJ)
  

def SlowDCClosestPair(points):
  '''
  a divide-and-conquer algorithm solving the closest pair problem
  input: a set p of more than 2 points
  output: a tuple(d,i,j) where d is the smallest pairwise distance of points in p and i,j are the indices of two points
  '''
  n = len(points)
  if n <= 3:
    return BFClosestPair(points)
  else:
    return 0
    
  
#A = [5,4,3,2,1,0]
#print countInversion(A)
#print A

#A = [5,4,6,3,7,1]
#print mystery(A, 0, 6)

#points = {0:(1,1),1:(1,-0.8),2:(-0.5,-0.5),3:(-0.3,1.2)}
#p1 = (1,2)
#p2 = (2,3)
#print euclidianDistance(p1,p2)
