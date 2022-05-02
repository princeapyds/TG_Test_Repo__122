# A function that takes  two-word string and returns True if both words begin with same letter
def animal_crackers(a):
    a=a.lower()
    if a[0]==a[a.find(" ",0)+1]:
        print(True)
    else:
        print(False)

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
animal_crackers("Cute cat")
