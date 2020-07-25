def separate(arr, arr_size):
    j = 0
    for i in range(arr_size):
        if(arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j


def find_missing_positive(arr, arr_size):
    for i in range(arr_size):
        if (abs(arr[i]) - 1 < arr_size and arr[abs(arr[i]) - 1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    for i in range(arr_size):
        if (arr[i] > 0):
            return i + 1
    return arr_size + 1


def solution(A):
    arr_len = len(A)
    count_of_positive = separate(A, arr_len)

    return find_missing_positive(A[count_of_positive:], arr_len - count_of_positive)
