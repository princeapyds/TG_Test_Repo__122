# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(b):
   x=[]
   for a in range(b+1):
      if a>1:
         for i in range(2,a):
            if a%i==0: break
         else: x.append(a)
   print(x)
   print(len(x))

count_primes(100)
count_primes(11)
count_primes(1)
count_primes(0)
count_primes(200)
