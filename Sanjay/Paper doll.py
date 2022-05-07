# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(a):
    a=str(a)
    b, c=" ", " "
    for i in range(len(a)):
        b=a[i]*3
        c = c+b
    return c


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))