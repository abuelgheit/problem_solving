def FirstFactorial(num): 
    f = 1
    for i in range(1, int(num)+1):
        f *= i
    return f
    
# keep this function call here  
print(FirstFactorial(input()))  


