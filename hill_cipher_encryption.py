# 2x2 hill cipher encryption code
file = open('plain.txt','w')
file.write('abcd e efe abcd abc')
file.close()


print('the key values should be in english alphabets')
print('enter the 2x2 key for the hill cipher')
list=[]

#key entry
while True:
  for i in range(4):
    list.append(input())
  if ((ord(list[0])-97)*(ord(list[3])-97) - (ord(list[1])-97)*(ord(list[2])-97) )== 0:
    print('key is not invertible, enter new key')
  else:
    print('key entered')
    break
print(list)
mist = []
for i in range(4):
  print(i)
  mist.append(ord(list[i])-97)

#filler char
filler_char='z'
print('wanna change the filler character(default-z) ? 1 for yes ,0 for no')
check=input()
if check==1:
  filler_char=input()

print(mist)
file = open('plain.txt','r')
fil = open('cipher.txt','w').close()
fil = open('cipher.txt','a')

import string

def hill(first,second):
  first = ord(first)-97
  second = ord(second)-97
  one = chr((mist[0]*first + mist[1]*second )%26 + 97)
  two = chr((mist[2]*first + mist[3]*second) %26 + 97)
  return one+two


  
#encryption code
i=0
for each in file:
  # print(len(each))
  while i<len(each):
    if each[i] not in (string.ascii_lowercase or string.ascii_uppercase):
      fil.write(each[i])
    else:
      if (i+1)>=len(each):
        fil.write(hill(each[i],'z'))
      else:
        # print('reached here')
        if each[i+1] not in (string.ascii_lowercase or string.ascii_uppercase):
          fil.write(hill(each[i],'z'))
          fil.write(each[i+1])
        else :
          fil.write(hill(each[i],each[i+1]))
        i=i+1
    i=i+1

fil.close()
fil = open('cipher.txt','r')
for each in fil:
  print(each)