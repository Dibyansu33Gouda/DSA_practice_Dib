def two_sum_sorted(nums:list[int],target:int)->list[int]:
    left=0
    right=len(nums)-1
    
    while left < right:
        current_sum=nums[left]+nums[right]
        
        if current_sum==target:
            return[left,right]
        
        elif current_sum > target:
            right-=1
            
        else:
            left+=1
            
    return [-1,-1]
print(two_sum_sorted([1, 3, 4, 6, 8, 11], 10))
    
    