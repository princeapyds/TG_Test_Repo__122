#Function will return lesser of 2 evens or higher of odd number (if one of them or both are odd numbers
def lesser_of_evens(a,b):
    if int(a)%2==0  and int(b)%2==0:
        if a>b:
            return b
        else:
            return a
    else:
        if a>b:
            return a
        else:
            return b

print(lesser_of_evens(2,4))
print(lesser_of_evens(2,5))
