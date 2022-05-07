# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
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
