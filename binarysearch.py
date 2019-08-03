def BinarySearch_iter(a, value):
    """searches given value in the array a
    which values have to be sorted in ascending order (iterative way)"""
    minimum = 0
    maximum = len(a)-1
    while minimum <= maximum:
        middle = int((minimum + maximum)/2)
        if a[middle] == value:
            return "Value {} is at the {} position of the array".format(value, middle)
        elif a[middle] > value:
            maximum = middle-1
            continue
        elif a[middle] < value:
            minimum = middle+1
            continue
    return "Value {} is not in the array".format(value)

def BinarySearch_rec(a, value, minimum, maximum):
    """searches given value in the array a
    which values have to be sorted in ascending order (recursive way)"""
    if minimum > maximum:
        return "Value {} is not in the array".format(value)
    middle = int((minimum + maximum)/2)
    if a[middle] == value:
        return "Value {} is at the {} position of the array".format(value, middle)
    elif a[middle] > value:
        return BinarySearch_rec(a, value, minimum, middle-1)
    elif a[middle] < value:
        return BinarySearch_rec(a, value, middle+1, maximum)

if __name__ == '__main__':
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                     29, 31, 37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113]
    
    # **************************************************************
    # ITERATIVE WAY
    # **************************************************************
    # searching value that's in the array
    print(BinarySearch_iter(prime_numbers, 73))
    
    # searching value that isn't in the array
    print(BinarySearch_iter(prime_numbers, 4))
    
    
    # **************************************************************
    # RECURSIVE WAY
    # **************************************************************
    # searching value that's in the array
    print(BinarySearch_rec(prime_numbers, 73, 0, len(prime_numbers)-1))
    
    # searching value that isn't in the array
    print(BinarySearch_rec(prime_numbers, 4, 0, len(prime_numbers)-1))