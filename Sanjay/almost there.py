# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    n=int(n)
    if (n>100 and n<=110) or (n>=90 and n<100) or (n>200 and n<=210) or (n>=190 and n<200):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print(almost_there(50))
print(almost_there(249))



