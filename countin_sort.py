def counting_sort(arr):
    max_val=max(arr)
    count=[0]*(max_val+1)
    for nums in arr:
        count[nums]+=1
    sorted_array=[]
    for i in range(len(count)):
        if count[i]>0:
            sorted_array.append(i)
            count[i]-=1
    return sorted_array
array=[87,21,63,22,14,98,32]
print(array)
print(counting_sort(array))
     