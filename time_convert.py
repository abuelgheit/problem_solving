def TimeConvert(num):
    num = int(num) 
    hours = int(num/60)
    mint = num%60
    time = "%d:%d" % (hours, mint)
    return time
    
# keep this function call here  
print(TimeConvert(input()))  
