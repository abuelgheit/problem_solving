def LongestWord(sen): 
    counter = 1
    word = ""
    the_word = word
    for i in sen:
        if i not in [" ", "^", "&", "!"]:
            word += i
            counter += 1
        else:
            counter = 0
            word = ""

        if counter > len(the_word):
            the_word = word
    sen = the_word                    
    return sen
    
# keep this function call here  
print(LongestWord(input()))