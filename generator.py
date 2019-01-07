# Pratyusha Thundena
# November 17, 2017
# Collaborated with Matt Campbell and http://cs.umw.edu/~finlayson/class/fall12/cpsc110/notes/12-sorting.html

import time
import random

# creates a file and writes a series of random numbers in it
randfile = open("Random.txt", "w")
# gets the lower and upper limit for generating random numbers
start = int(input('Enter lower limit of random numbers: '))
end = int(input('Enter upper limit of random numbers: '))

# asks the user for the number of random generators to generate
for i in range(int(input('How many to generate?: '))):
    # generates ranodm integer between start and end & stores it as a string
    line = str(random.randint(start, end))
    # writes line to file and then prints the line
    randfile.write(line + '\n')
    print(line)

randfile.close()

def swap(a, i, j):
    """To swap elements i and j in array a for selection sort.
    Test data:
    input: N/A
    output: N/A
    Params: a,i,j (integers)
    returns: the value of swapped elements: i and j in array a; (integers)
    """
    (a[i], a[j]) = (a[j], a[i])



def selectionSort(a):
    """ To sort the list of generated random numbers using selection sort and record elapsed time .
    Test data:
    input: generated random numbers from 'Random.txt' file from range 1-100 & from range 1-1000
    output: selection sorted random numbers from lowest to highest in selectionSortResult.txt file from range 1-100 & from range 1-1000
    Params: a (integer)
    returns: selection sorted list of random numbers in increasing order (integers) with recorded elapsed time (in seconds)
    """
    n = len(a)
    for startIndex in range(n):
        # initializing minIndex with 1st element of array & then runs loop from 1 to n
        minIndex = startIndex
        for ind in range(startIndex+1, n):
            # updates the minIndex count and swaps the elements
            if a[ind] < a[minIndex]:
                minIndex = ind
        swap(a, startIndex, minIndex)

lst = []
# opens 'Random.txt' file
with open("Random.txt", "r") as f:
    for line in f:
        # strip the element of any spaces & then append it to the file
        lst.append(int(line.strip()))

# gets the time before & after execution
start_time = time.time()
selectionSort(lst)
end_time = time.time()

# writes the sorted array in the file and prints it
file = open("selectionSortResult","w")
for x in lst:
    file.write(str(x)+"\n")
file.close()
print('Sorted Selection Sort List: ', lst)
print('Elapsed time for Selection Sort: {:.20f} seconds'.format(end_time-start_time))




def merge_sort(A):
    """To merge sort list A into order(low to high , and return result.
    Test data:
    input: N/A
    output: N/A
    Params: A (integer)
    Returns: merge sorted list of random integers in increasing order (integers)
    """
    n = len(A)
    # partioning the elements from 0-mid and mid+1 to end & calls them recursively
    if n==1:
        return A
    mid = n//2   # floor division
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L,R)

def merge(L,R):
    """ To return merge when given two sorted sequences: L and R  with recorded elapsed time.
    Test data:
    input:  generated random numbers from 'Random.txt' file from 1-100 range & then from 1-1000 range
    output: merge sorted list of random numbers from lowest to highest in 'mergeSortResult.txt' file from 1-100 range & then from 1-1000 range
    Params: L, R (integers)
    returns: merge sorted list of random integers in increasing order(integers) with recorded elapsed time (in seconds)
    """
    i = 0
    j = 0
    answer = []
    # while index is less than length of 1st array & index j is less than length of 2nd array
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        # else put the element from 2nd array in resultant array
        else:
            answer.append(R[j])
            j += 1
    # after execution of loop check for any remaining elements in either array; if found add to resultant array
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

lst = []
# opens and reads 'Random.txt'
with open("Random.txt", "r") as f:
    for line in f:
        lst.append(int(line.strip()))
# gets time before and after execution
start_time = time.time()
lst = merge_sort(lst)
end_time = time.time()


# opens and writes to file 'mergeSortResult.txt'
file = open("mergeSortResult","w")
for x in lst:
    file.write(str(x)+"\n")
# closes 'mergeSortResult.txt'
file.close()
print('Sorted Merge Sort List: ', lst)
print('Elapsed time for Merge Sort: {:.20f} seconds'.format(end_time-start_time))


