def count_frequency(nums):
    frequency = {}

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency


nums = [1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 5, 5]
print(count_frequency(nums))
