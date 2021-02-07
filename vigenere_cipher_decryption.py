#code for vigenere decryption part

import string
def cc(val,str_key,count):
  key=str_key[count]
  if val in string.ascii_lowercase:
    return(chr ((ord(val)-97-ord(key)+96)%26 + 97) )
  elif val in string.ascii_uppercase:
    return(chr ((ord(val)-65-ord(key)+96)%26 + 65) )
  else:
    return(val)

print('Enter the key')
key = input()
key=key.lower()
file=open('cipher.txt','r')
fil = open('test.txt','w').close()
fil=open('test.txt','a')
count=0
for each in file:
  for val in each:
    if val in (string.ascii_lowercase or string.ascii_uppercase):
      count+=1
      count%=len(key)
    fil.write(cc(val,key,count-1))
fil.close()

fil=open('test.txt','r')
for each in fil:
  print(each)
fil.close()