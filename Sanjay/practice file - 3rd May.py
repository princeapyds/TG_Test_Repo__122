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
"""
a=[3,1,3]
print(a.index(3))
print(a.index(3,1))

# print(dir (list))
#print(help( list.index))

