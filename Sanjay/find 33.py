# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(a):
    a=list(a)
    x=a.index(3)
    try:
        y=a.index(3,x+1)
        if y==x+1:
            return True
        else:
            return False
    except:
        return "there is no repeat of 3"



print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([1,2,3,4,5,6]))
print(has_33([3, 3, 1]))
print(has_33([1,2,3,4,5,3,3,6])) # need help, this entry is failing... need to rework on the code
