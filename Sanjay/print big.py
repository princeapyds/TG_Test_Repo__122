# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

def print_big(x):
    shapes=dict()
    shapes['a']= '''
  *
*   *
*****
*   *
*   *
'''

    shapes['b']='''
***
*   *
***
*   *
***
'''

    shapes['c']='''
 ****
*
*
*
 ****
'''

    shapes['d']='''
***
*  *
*   *
*  *
***
'''

    shapes['e']='''
*****
*
***
*
*****
'''
    if x == 'a': print(shapes['a'])
    if x == 'b': print(shapes['b'])
    if x == 'c': print(shapes['c'])
    if x == 'd': print(shapes['d'])
    if x == 'e': print(shapes['e'])


print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')





