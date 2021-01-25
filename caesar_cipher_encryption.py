#Caesar cipher encryption
import string
print('Enter the monoalphabetic key for the caesar cipher')
while True:
  key=input()
  if len(key)>1 or key not in string.ascii_lowercase :
    print('Key Error')
  else : 
    break

file = open('test.txt','r')
fil = open('cipher.txt','w').close()
fil = open('cipher.txt','a')

for each in file :
  for val in each :
    if val in string.ascii_lowercase:
      fil.write(chr ((ord(val)-97+ord(key)-96)%26 + 97) )
    elif val in string.ascii_uppercase:
      fil.write(chr ((ord(val)-65+ord(key)-96)%26 + 65) )
    else:
      fil.write(val)
fil.close()

fil=open('cipher.txt','r')
for each in fil:
  print(each)
fil.close()