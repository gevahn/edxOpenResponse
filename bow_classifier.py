def score(a,b):
    s = 0.0
    a_tot = 0.0
    b_tot = 0.0
    for k in a.keys():
        a_tot += a[k]
    for k in b.keys():
        b_tot += b[k]

    for k in a.keys():
        if k in b:
            s += 1#a[k]*b[k]
    
    return s#/(a_tot*b_tot)

