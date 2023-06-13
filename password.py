import string

sandi = "akusukabapak2#$"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in sandi])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in sandi])
special = any([1 if c in string.punctuation else 0 for c in sandi])
digits = any([1 if c in string.digits else 0 for c in sandi])

karakter = [upper_case,lower_case,special,digits]

length = len(sandi)

skor = 0

with open('biasa.txt', 'r') as f:
    biasa = f.read().splitlines()

if sandi in biasa:
    print("ganti sandi udh biasa score 0")
    exit()


if length > 9:
    skor += 1
if length > 12:
    skor += 1
if length > 20:
    skor += 1    
print(f"panjang sandi {str(length)}, tambah {str(skor)} point")

if sum(karakter) > 1:
    skor += 1
if sum(karakter) > 2:
    skor += 1
if sum(karakter) > 3:
    skor += 1        
print(f"perbedaan karakter {str(sum(karakter))}, tambah {str(sum(karakter) -1 )} point")

if skor < 3:
    print(f"lemah kali: {str(skor)} / 6")
elif skor == 3:
    print(f"lumayan: {str(skor)} / 6 ")
elif skor > 3:
    print(f"anak pintar: {str(skor)} /6 ")    
   