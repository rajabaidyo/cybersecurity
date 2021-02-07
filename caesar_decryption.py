#Caesar cipher decryption
import string
print('Enter the monoalphabetic key for the caesar cipher')
while True:
  key=input()
  if len(key)>1 or key not in string.ascii_lowercase :
    print('Key Error')
  else : 
    break

file = open('cipher.txt','r')
fil = open('test.txt','w').close()
fil = open('test.txt','a')

for each in file :
  for val in each :
    if val in string.ascii_lowercase:
      fil.write(chr ((ord(val)-97-ord(key)+96)%26 + 97) )
    elif val in string.ascii_uppercase:
      fil.write(chr ((ord(val)-65-ord(key)+96)%26 + 65) )
    else:
      fil.write(val)
fil.close()

fil=open('test.txt','r')
for each in fil:
  print(each)
fil.close()