def LetterCapitalize(st): 
    ls = []
    ls = st.split(" ")
    ls2 = ""
    for i in ls:
        ls2 += i[0].upper() + i[1:] + " "
    return ls2
    
# keep this function call here  
print(LetterCapitalize(input()))  

