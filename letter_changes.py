def LetterChanges(st):
    index = 0
    new_word = ""
    alphapet = "abcdefghijklmnopqrstuvwxyzacd"
    
    for i in st.lower():
        if i.islower():
            index = alphapet.index(i) + 1
            if alphapet[index] in {"a", "e", "i", "o", "u"}:
                new_word += alphapet[index].upper()
            else:
                new_word += alphapet[index]    
        else:
            new_word += i    
    return new_word
    
# keep this function call here  
print(LetterChanges(input()))  

