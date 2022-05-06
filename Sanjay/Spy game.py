# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order


def spy_game(a):
    try:
        if a.index(0,0):
            x= a.index(0)
            if a.index(0,x+1):
                y=a.index(0,x+1)
                if a.index(7,y+1):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))