def SimpleSymbols(st): 
    stat = "true"
    for i in range(0, len(st)):
        if st[0].isalpha():
            stat = "false"
            break
        if st[i].isalpha():
            if (st[i-1] != "+") or (st[i+1] != "+"):
                stat = "false"
                break
    return stat
    
# keep this function call here  
print(SimpleSymbols(input()))