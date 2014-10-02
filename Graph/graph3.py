from alg_cluster import Cluster
import math


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
    

# load the data for PA3
  
def load_data(data_file):
  '''
  load the data
  '''
  clusters = []
  data = open(data_file)
  data_text = data.read()
  data_lines = data_text.split('\n')
  for line in data_lines:
    content = line.split(',')
    clusters.append(Cluster(int(content[0]),float(content[1]),float(content[2]),int(content[3]),float(content[4])))
  return clusters

# slow

def slow_closest_pair(cluster_list):
  '''
  Takes a list of Cluster objects and returns the set of all closest pairs where each pair is represented by
  the tuple (dist, idx1, idx2) with idx1 < idx2 where 
  dist is the distance between the closest pair cluster_list[idx1] and cluster_list[idx2]. 
  This function should implement the brute-force closest pair method described in BFClosestPair from Homework 3 
  with the two differences: 
      a set of all closest pairs is returned consisting of all pairs that share the same minimal distance 
      and the returned indices are ordered.
  '''
  smallest_distance = cluster_list[0].distance(cluster_list[1])
  smallest_pairs = {(smallest_distance, cluster_list[0].fips_codes(), cluster_list[1].fips_codes())}
  for i in range(len(cluster_list)-1):
    for j in range(i+1,len(cluster_list)):
      current_distance = cluster_list[i].distance(cluster_list[j])
      if current_distance < smallest_distance:
        smallest_distance = current_distance
        smallest_pairs = {(smallest_distance, cluster_list[i].fips_codes(), cluster_list[j].fips_codes())}
      elif current_distance == smallest_distance:
        smallest_pairs.add((smallest_distance, cluster_list[i].fips_codes(), cluster_list[j].fips_codes()))
  return  smallest_pairs
      
def fast_closest_pair(cluster_list):
  '''
  Takes a list of Cluster objects and and returns a closest pair where the pair is represented by
  the tuple (dist, idx1, idx2) with idx1 < idx2 where
  dist is the distance between the closest pair cluster_list[idx1] and cluster_list[idx2]. 
  This function should implement the fast divide-and-conquer closest pair method described in Homework 3
  with the exception that the returned indices are ordered. 
  Note this method should compute horizontal and vertical orderings of the clusters 
      and call a recursive helper function that will do the majority of the work.
  '''
  
  
if __name__ == "__main__":
  #A = [5,4,3,2,1,0]
  #print countInversion(A)
  #print A

  #A = [5,4,6,3,7,1]
  #print mystery(A, 0, 6)

  #points = {0:(1,1),1:(1,-0.8),2:(-0.5,-0.5),3:(-0.3,1.2)}
  #p1 = (1,2)
  #p2 = (2,3)
  #print euclidianDistance(p1,p2)
  file111 = 'unifiedCancerData_111.csv'
  file290 = 'unifiedCancerData_290.csv'
  file896 = 'unifiedCancerData_896.csv'
  file3108 = 'unifiedCancerData_3108.csv'
  cluster_list111 = load_data(file111)
  cluster_list290 = load_data(file290)
  cluster_list896 = load_data(file896)
  cluster_list3108 = load_data(file3108)
  print slow_closest_pair(cluster_list111)
  print slow_closest_pair(cluster_list290)
  print slow_closest_pair(cluster_list896)
  print slow_closest_pair(cluster_list3108)
  
  
