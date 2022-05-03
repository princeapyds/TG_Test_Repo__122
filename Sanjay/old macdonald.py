#function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    name=str(name)
    if len(name)>=4 and name[3]!=0 and name[3]!=" ":
        m=name[3:]
        x=name[:3]
        print(x.capitalize() + m.capitalize())
    else:
        print("enter a string longer than 4 characters and there should not be space in 4th place")

old_macdonald("sanjay")
old_macdonald("sanj")
old_macdonald("san")
old_macdonald("san yy")
old_macdonald("SanJay")
old_macdonald("macdonald")