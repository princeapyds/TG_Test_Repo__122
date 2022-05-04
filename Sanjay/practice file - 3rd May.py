'''
# checking map fuction

def squares(num):
    return num**2

my_list=[1,2,3,4,5]

#a=list(map(squares,my_list))
#print(a)


""""
def num_check(a):
    if type(a)==list or type(a)==tuple or type(a)==set:
        x=3
        count=0
        for i in a:
            if x==i:
                count=count+1
                if count==2: break
                    #print(i)
            #else:
                #print("nothing")
    if count==2:
        print(" 3  is getting repeated  ")
    else:
        print("nothing")

"""



"""
def num_check(a):
    if type(a)==list or type(a)==tuple or type(a)==set:
        count=0
        for i in a:
            if i==3:
                  x=i

                    count=count+1
                    if count==2 and : break
    if count==2:
        print("great")
    else:
        print("not great")


a=[1,2,3,3,5]
num_check(a)

a=[1,3,3]
num_check(a)

a=[1,3,1,3]
num_check(a)

a=[3,1,3]
num_check(a)

a=[3,1,3]
print(a.index(3))
print(a.index(3,1))
"""

# print(dir (list))
#print(help( list.index))




a='Mississippi'
b=" "
c=" "
for i in range(len(a)):
    #print(i)
    b=a[i]*3
    c = c+b
print(c)
'''

def black_jack(a,b,c):
    sum=int(a)+int(b)+int(c)
    if sum <=21:
        print(sum)
    else:
        if a==11 or b==11 or c==11:
            sum=sum-10
            print(sum)
        else:
            print("Bust")

black_jack(1,2,3)
black_jack(5,6,7)
black_jack(9,9,9)
black_jack(9,9,11)
black_jack(11,6,7)
black_jack(0,0,0)
black_jack(11,11,0)
black_jack(8,11,0)

