def has_pair_with_sum(arr, x):
    seen_numbers = set()

    for num in arr:
        target = x - num

        if target in seen_numbers:
            return True

        seen_numbers.add(num)

    return False
