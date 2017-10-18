def CorrectPath(st): 
    n_r = 0
    n_l = 0
    n_u = 0
    n_d = 0
    n_q = 0

    n_r2 = 0
    n_l2 = 0
    n_u2 = 0
    n_d2 = 0

    new_word = ""
    st = list(st)
    for i in st:
        if i == "r":
            n_r += 1
        elif i == "l":
            n_l += 1
        elif i == "d":
            n_d += 1
        elif i == "u":
            n_u += 1
        elif i == "?":
            n_q += 1

    for i in range(0, len(st)):
        
        if st[i] == "r":
            n_r2 += 1
        if st[i] == "l":
            n_l2 += 1
        if st[i] == "d":
            n_d2 += 1
        if st[i] == "u":
            n_u2 += 1



        if (st[i] == "?") and ((n_r - n_l) < 4):
            st[i] = "r"
            n_r += 1
            n_q -= 1
        elif (st[i] == "?") and ((n_r - n_l) > 4):
            st[i] = "l"
            n_l += 1
            n_q -= 1
        elif (st[i] == "?") and ((n_d - n_u) < 4):
            st[i] = "d"
            n_d += 1
            n_q -= 1
        elif (st[i] == "?") and ((n_d - n_u) > 4):
            st[i] = "u"
            n_u += 1
            n_q -= 1
        elif (st[i] == "?") and ((n_d - n_u) == 4) and ((n_r - n_l) == 4) and ((n_d2 - n_u2) > 1):
            st[i] = "u"
            n_u += 1
            n_q -= 1
        elif (st[i] == "?") and ((n_d - n_u) == 4) and ((n_r - n_l) == 4) and ((n_d2 - n_u2) < 1):
            st[i] = "d"
            n_d += 1
            n_q -= 1
    st = ''.join(st)
    return st
    
# keep this function call here  
print(CorrectPath(input()))  
