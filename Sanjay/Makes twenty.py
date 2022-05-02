# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    a=int(a)
    b=int(b)
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False

x=makes_twenty(20,10)
print(x)

y=makes_twenty(12,8)
print(y)

j=makes_twenty(2,3)
print(j)