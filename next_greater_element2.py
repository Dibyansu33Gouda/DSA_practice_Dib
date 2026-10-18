def next_greater_element(nums:list[int])->list[int]:
    n=len(nums)
    res=[-1]*n
    stack=[]
    
    for i in range(n):
        while stack and nums[i] > stack[-1]:
            idx=stack.pop()
            res[idx]=nums[i]
            
        stack.append(i)
        
    return res
print(next_greater_element([2,1,2,4,3]))
    