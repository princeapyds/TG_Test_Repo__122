# To find if a number is  armstrong?
numb=9000
if numb == 0 or numb==1:
    print(f"{numb} is indeed an asrmstrong!")
else:
    #numb=str(numb)
    lista=list(str(numb))
    expon=(len(lista))
    suma=0
    for i in lista:
        i=int(i)**expon
        suma=suma+i

    if suma==int(numb):
        print(f"{numb} is indeed an armstrong number!")
    else:
        print(f"{numb} is not armstrong number")