class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sum_count = 0
        sum_dict = {0: 1}

        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            if complement in sum_dict:
                sum_count += sum_dict[complement]
            sum_dict[prefix_sum] = sum_dict.get(prefix_sum, 0) + 1

        return sum_count



prefix_sum_count = defaultdict(int)
prefix_sum_count[0] = 1

current_sum = 0
count = 0

for num in nums:
    current_sum += num
    count += prefix_sum_count[current_sum - k]
    prefix_sum_count[current_sum] += 1

return count



prefix_sums = [0] * (len(nums) + 1)
count = 0
current_sum = 0

for i in range(len(nums)):
    current_sum += nums[i]
    prefix_sums[i + 1] = current_sum

prefix_sum_count = defaultdict(int)

for i in range(len(prefix_sums)):
    count += prefix_sum_count[prefix_sums[i] - k]
    prefix_sum_count[prefix_sums[i]] += 1

return count