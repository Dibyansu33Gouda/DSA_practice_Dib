def lenght_of_longest_subtr(s:str)->int:
    window_Set=set()
    left=0
    max_lenght=0
    for right in  range(len(s)):
        if s[right] in window_Set:
            window_Set.remove(s[left])
            left+=1
            
        window_Set.add(s[right])
        
        max_lenght=max(max_lenght,right-left+1)
        
    return max_lenght
print(lenght_of_longest_subtr("abcabcbb")) 
print(lenght_of_longest_subtr("pwwkew"))
