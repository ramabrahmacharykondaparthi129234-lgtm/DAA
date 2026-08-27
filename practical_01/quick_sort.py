def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quicksort(left) + [pivot] + quicksort(right)


numbers = [5, 3, 8, 4, 2]

print("Before:", numbers)
print("After :", quicksort(numbers))
