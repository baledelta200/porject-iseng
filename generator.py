import random

uppercase_letters = "ABCDEFGHIJKLMOPQRSTUVWYZ"
lowercase_letters =  uppercase_letters.lower()
digits = "123456789"
simbol = "!@#$%^&*()=+-_"

upper,lower,angka,syms = True,True,True,True

all= ""

if upper:
   all += uppercase_letters
if lower:   
   all += lowercase_letters
if angka:   
   all += digits
if syms:
   all += simbol   

panjang = 10
jumlah = 1

for x in range(jumlah):
    password = "".join(random.sample(all, panjang))
    print(password)