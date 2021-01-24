''' Additional Information for this version of playfair code 
-> If there are more than one characters of same type then only the first char is taken into
the key. Eg - key 'jokker' becomes 'joker'

-> The filler character is 'z' for odd situations
eg : "monarch" -> mo,na,rc,hz

-> The left-out character is 'j' and is filled by 'i'
eg: The words like 'job' in plain-text gets modified into 'iob'

-> If there is 'j' in secret key then choose the left-out character and the substitute
character for it.
eg: key = "joker" , then we can chose the left-out as 't' and replacement as 'q'
so the words like 'take' in the plain text gets modified to 'qake'
'''
import re
import string
from collections import OrderedDict 

def removeDupWithOrder(str):  
    return "".join(OrderedDict.fromkeys(str)) 


print('Enter the secret key')
key = input()
key = removeDupWithOrder(key)
print(key)
leftout = "j"
char_filler ="z"
if 'j' in key:
  while(True):
    print('Enter the leftout character')
    leftout=input()
    print('Enter the filler character')
    char_filler=input()
    regex = '['+leftout+char_filler+']'
    # print(regex)
    if re.findall(regex, key) or len(leftout)>1 or len(char_filler)>1:
      print('Matching characters in key and input provided or invalid length')      
    else :
      print('Inputs are okay')
      break

#making the encryption - decryption matrix
seq = 'abcdefghijklmnopqrstuvwxyz'
list = {}
row = 0
col =0 
for i in key:
  list[i]=(str(row)+str(col))
  list[str(row)+str(col)]=i
  col=col+1
  if col == 5 : 
    row = row+1
    col=0
check = key + leftout
for i in seq :
  if i not in check:
    list[i]=(str(row)+str(col))
    list[str(row)+str(col)]=i
    col=col+1
    if col==5:
      row=row+1
      col=0
print(list)

# encryption - decryption matrix
for i in range(5):
  for j in range(5):
    print(list[str(i)+str(j)], end = " ")
    print(list[list[str(i)+str(j)]],end = " ")
  print('\n')



# print(list['q'][1])
fil=open('cipher.txt','w').close()
file=open('plain.txt','w')
file.write('monarch \n monarch\nmon;archy\nmonarch y')
file.close()


#code for the encryption
def check(x):
  if x in string.ascii_lowercase:
    return True
  else:
    return False

def filling(first,second):
  print(first+second)
  # print(list[first])
  # print(list[second])
  if list[first][0]==list[second][0] and list[first][1]!=list[second][1]:
    return (list[ list[first][0] + str( (int(list[first][1]) + 1)%5) ]
            +list[list[second][0] + str( (int(list[second][1]) + 1)%5)] )
  elif list[first][1]==list[second][1] and list[first][0]!=list[second][0]:
    return (list[str( (int(list[first][0]) + 1)%5 ) + list[first][1]]
            +list[str( (int(list[second][0]) + 1)%5) + list[second][1] ] )
  elif first==second:
    return (first+first)
  else:
    return (list[list[first][0]+list[second][1]] + list[list[second][0]+list[first][1]])



first = None
second = None
file = open('plain.txt','r')
fil = open('cipher.txt','w').close()
fil = open('cipher.txt','a')
for each in file:
  each = each.lower()
  print(each)
  i=0
  while(i<len(each)) :
    print(i)
    first = each[i]
    state_first = check(first)
    if state_first==True:
      if i==len(each)-1:
        second = char_filler
      else :
        second = each[i+1]
    else:
      fil.write(first)
      i+=1
      # print('====',i)
      continue
    state_second = check(second)
    if state_second == True:
      # print(filling(first,second))
      fil.write(filling(first,second))
    else :
      temp=second
      second = char_filler
      # print(filling(first,second))
      fil.write(filling(first,second))
      fil.write(temp)
    i+=2



fil.close()
fil=open('cipher.txt','r')
for each in fil : 
  print(each)
  print(len(each))
fil.close()

