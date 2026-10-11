nums=[215132]
k=3

win_sum=sum(nums[:k])
max_sum=win_sum

left=0
for right in range(0,len(nums)):
    win_sum+=nums[right]-nums[left]
    max_sum=max(max_sum,win_sum)
    
    left+=1
    
print(max_sum,end=" ")