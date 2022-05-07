#  summer of 69

def summer_69(a):
    try:
        a=list(a)
        x = a.index(6)
        for i in a[x:]:
            a.remove(i)
            if i == 9: break
        print(f"{a}, sum is {sum(a)}")

    except:
        print(f"{a}, sum is {sum(a)}")



summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
summer_69([6, 9])
summer_69([])

