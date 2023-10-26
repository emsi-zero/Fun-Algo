import math


def divide(unsorted_list):
    l = math.ceil(len(unsorted_list) / 2)
    return unsorted_list[:l], unsorted_list[l:]


def merge(left, right):
    l, r = 0, 0
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
            l += 1
            merged.append(right[r])
            r += 1
        elif left[l] > right[r]:
            merged.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            l += 1
        h += 1
    print(merged)
    return merged


def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    divided = divide(unsorted_list)
    print(divided[0], divided[1])

    sorted_left = merge_sort(divided[0])
    sorted_right = merge_sort(divided[1])

    return merge(sorted_left, sorted_right)


input_list = [5, 1, 4, 2, 3]
print(merge_sort(input_list))
