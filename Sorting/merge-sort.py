


import math


def divide(list):
    l = math.ceil(len(list) /2)
    return (list[:l], list[l:])


def merge(left, right):
    l, r = 0 , 0
    merged = []
    for h in range(len(left) + len(right)):
        
        if l == len(left):
            merged.extend(right[r:])
            break
        elif r == len(right):
            merged.extend(left[l:])
            break
        
        if left[l] == right[r]:
            merged.append(left[l])
            l+=1
            merged.append(right[r])
            r+=1
        elif left[l] > right[r]:
            merged.append(right[r])
            r+=1
        else:
            merged.append(left[l])
            l+=1
        h+= 1
    print(merged)
    return merged

def merge_sort(list):
    if len(list) == 1:
        return list
    divided = divide(list)
    print(divided[0],divided[1])
    
    
    sorted_left = merge_sort(divided[0])
    sorted_right = merge_sort(divided[1])
    
    return merge(sorted_left, sorted_right)
    
    


list = [5,1,4,2,3]
print(merge_sort(list))