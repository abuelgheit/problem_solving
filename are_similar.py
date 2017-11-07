def swp(i,a,b):
    s = 0
    item = a[i]
    if item in b:
        for j in range(len(b)):
            if b[j] == a[i] and b[j] != a[j]:
                indx = j
                s = b[i]
                b[i] = b[indx]
                b[indx] = s
                return -1
    else:
        return -2
    
    
def check(a,b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return i
    return -1

def areSimilar(a, b):
    if check(a,b) != -1:
        i = check(a,b)
        if swp(i,a,b) == -1:
            swp(i,a,b)
            if check(a,b) != -1:
                return False
        else:
            return False
    return True