def max_sub_array_of_size_k(k: int, nums: list[int]) -> int:
    n = len(nums)
    if n < k or k <= 0:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum



arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sub_array_of_size_k(k, arr))  # Output: 9