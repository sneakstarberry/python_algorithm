def max_c(exam_a) :
    current_a = 0
    max_a = exam_a[0]
    for i in range(0,len(exam_a)):
        current_a = max(current_a + exam_a[i], exam_a[i])
        max_a = max(max_a, current_a)

    return max_a


a_array = [-1, 3, -1, 5]
print(max_c(a_array))