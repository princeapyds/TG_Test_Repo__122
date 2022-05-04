# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

b=" "
c=" "
for i in range(len(a)):
    #print(i)
    b=a[i]*3
    c = c+b
print(c)