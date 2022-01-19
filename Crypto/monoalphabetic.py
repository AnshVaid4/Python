#Some changes in function to be done
text=input("Enter the string: ")
ran=int(input("Enter randomization: "))
ciphertext=""
orig=""
for i in text:
    if i == " ":
        ciphertext=ciphertext+" "
        continue
    if ord(i) >=65 and ord(i) <= 90:
        val=(ord(i)+ran)%26
        if (ord(i)+val) > 90:
            remainder=val%90
            ciphertext=ciphertext+chr(65+remainder)
        else:
            ciphertext=ciphertext+chr(ord(i)+val)
    if ord(i) >=97 and ord(i) <= 122:
        val=(ord(i)+ran)%26
        if ord(i)+val > 122:
            remainder=val%122
            ciphertext=ciphertext+chr(97+remainder)
        else:
            ciphertext=ciphertext+chr(ord(i)+val)

print(ciphertext)
    

