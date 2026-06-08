def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[0]
    rest_num = numbers[1:]
    left_part = []

    for i in rest_num:
        if i <= pivot:
            left_part.append(i)
    
    right_part = []

    for i in rest_num:
        if i > pivot:
            right_part.append(i)
            
    sorted_left = quick_sort(left_part)
    sorted_right = quick_sort(right_part)
    
    return  sorted_left + [pivot] + sorted_right
print(quick_sort([5,654, 54,4, 3, 2543, 2, 65,203]))