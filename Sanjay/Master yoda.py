# Given a sentence, return a sentence with the words reversed
def master_yoda(a):
    a = str(a)
    b = a.split()
    c = b[::-1]
    x = " ".join(c)
    return(x)

x = master_yoda('I am home')
print(x)
x= master_yoda('We are ready')
print(x)
x= master_yoda("Tiger are biggest cat's in the family")
print(x)