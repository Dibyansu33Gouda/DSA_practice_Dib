def next_greater(arr):
    n=len(arr)
    result = [-1] * n
    stack=[]
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            j=stack.pop()
            result[j] = arr[i]
        stack.append(i)
    return result
arr = [4, 5, 2, 25, 7, 8, 3]
print(next_greater(arr))

        
