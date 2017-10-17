def FirstReverse(str): 
    s = ""
    for i in range(len(str) - 1, -1, -1):
        s += str[i]
    # code goes here 
    return s
    
# keep this function call here  
print(FirstReverse(input()))