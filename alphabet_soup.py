def AlphabetSoup(st): 
    lst = list(st)
    final = ""
    for i in sorted(lst):
        final += i
    return final

    
# keep this function call here  
print(AlphabetSoup(input())) 