def find_missing_number(arr, N):
    total_sum = N * (N + 1) // 2

    arr_sum = sum(arr)

    missing_number = total_sum - arr_sum

    return missing_number


arr = [1, 2, 4, 6, 3, 7, 8]
N = 8
print(find_missing_number(arr, N))
