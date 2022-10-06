def merge(array, byfunc, p,q,r):
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]

    left_index = 0
    right_index = 0
    dest = p
    
    len_left = q-p + 1
    len_right = r-q


    #print("left array:", left_array, "right array:", right_array, len_left, len_right)
    while left_index < len_left and right_index < len_right:
        
        if byfunc == None:
            if left_array[left_index] <= right_array[right_index]:
                array[dest] = left_array[left_index]
                left_index += 1
            
            else:
                array[dest] = right_array[right_index]
                right_index += 1
            
            dest += 1            
        
        else:
            #print("case 1", left_index, right_index, dest)
            #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]) )
            if byfunc(left_array[left_index]) <= byfunc(right_array[right_index]):
                array[dest] = left_array[left_index]
                left_index += 1
                
            
            else:
                #print(byfunc(left_array[left_index]),byfunc(right_array[right_index]) )
                array[dest] = right_array[right_index]
                right_index += 1
        
            dest += 1
    
    while left_index < len_left:
        #print(dest, len_left)
        array[dest] = left_array[left_index]
        left_index += 1
        dest += 1

    while right_index < len_right:
        #print(dest, right_index, len_right)
        array[dest] = right_array[right_index]
        right_index += 1
        dest += 1
    
    return array

def mergesort_recursive(array, byfunc, p, r):
    if r-p > 0:
        q = (r+p)//2
        mergesort_recursive(array,byfunc, p, q)
        mergesort_recursive(array,byfunc, q+1, r)
        merge(array,byfunc, p, q, r)
        

def mergesort(array, byfunc=None):
    mergesort_recursive(array, byfunc, 0, len(array)-1)
        

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





