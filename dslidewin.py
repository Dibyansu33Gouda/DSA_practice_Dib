def min_array(target:int ,num:list[int])->int:
    left=0
    current_sum=0
    min_len=float("inf")
    
    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)

            current_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))  # Output: 2
    