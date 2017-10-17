def SimpleAdding(num):
    sum = 0
    for i in range(0, int(num)+1):
        sum += i
    return sum
    
# keep this function call here  
print(SimpleAdding(input()))  