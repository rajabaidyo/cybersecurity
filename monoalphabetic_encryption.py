#code for the monoalphabetic substitution cipher

import string
print('Enter the mapping for the respective characters of the english alphabets')
list ={}
print('enter 1 to keep the default mapping')
flag = input()
if int(flag)==1:
  for i in range(26):
    list[chr(97+i)]=chr(97+((i+1)%26))
  print(list)
else:
  for i in range(26):
    while True:
      print('Enter the mapping for '+chr(97+i)+' :')
      key=input()
      if key in list.values():
        print('this key already exists, please enter another mapping for the character')
        continue
      else:
        list[chr(97+i)]=key
        break

print(list)
file = open('plain.txt','r')
fil = open('cipher.txt','w').close()
fil = open('cipher.txt','a')

#main monoalphabetic substitution 
for each in file:
  each = each.lower()
  for val in each:
    if val in string.ascii_lowercase:
      fil.write(list[val])
    else:
      fil.write(val)
    
fil.close()
fil=open('cipher.txt','r')
for each in fil:
  print(each,end='')
fil.close()
file.close()
