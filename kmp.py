def build_lps(pat: str) -> list[int]:
    
    lps=[0]*len(pat)
    lenght=0
    i=1
    while i < len(pat) :
        if pat[i] == pat[lenght]:
            lenght+=1
            lps[i] = lenght
            i+=1
        elif lenght:
            lenght=lps[lenght-1]
        else:
            lps[i]=0
            i+=1
    return lps

def kmp_search(text:str , pat:str) ->list[int]:
    if not pat:
        return []
    
    lps=build_lps(pat)
    result=[]
    j=0
    for i , ch in enumerate(text):
        while j and ch!=pat[j]:
            j=lps[j-1]
        if ch==pat[j]:
            j+=1
        if j==len(pat):
            result.append(i-j+1)
            j=lps[j-1]
            
    return result

print(kmp_search("ABABABC", "ABABC"))