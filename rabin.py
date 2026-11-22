def rabin_krap(text:str , pat:str , base:int = 256 , mod:int =1_000_000_007) -> list[int]:
    n,m = len(text) , len(pat)
    if m==0 or m > n :
        return []
    
    high=pow(base ,m-1,mod)
    p_hash = t_hash= 0
    for k in range(m):
        p_hash=(p_hash*base + ord(pat[k])) % mod
        t_hash=(t_hash * base + ord(text[k])) % mod
        
    result=[]
    
    for i in range(n-m+1):
        if p_hash == t_hash and text[i:i + m] == pat:
            result.append(i)
            
        if i < n-m:
            t_hash=((t_hash - ord(text[i]) *high)*base + ord(text[i+m])) % mod
    return result

print(rabin_krap("ABABDABACDABABCABAB", "ABABCABAB"))
    