#code for railfence cipher(encryption)
from array import array
fil = open('cipher.txt','w').close()
file = open('plain.txt','r')
fil = open('cipher.txt','a')
print('enter the number of rails')
while(True) : 
  inp = input()
  try :
    inp = int(inp)
    break
  except:
    print("your input is not of correct")
count=1
flag = True
list=[]
for i in range(inp) : 
  list.append([])
# print(list)
for each in file:
  # print(each)
  for val in each: 
    if val!='\n':
      list[count-1].append(val)
      # print(list)
      if count==1 :
        flag=True
        count=count+1
      elif count == inp :
        flag=False
        count=count-1
      else :
        if flag==True :
          count=count+1
        else :
          count=count-1
  ans=""
  str=""
  # print(str.join(list[0]))
  for i in range(inp):
    # print(str.join(list[i]))
    ans=ans+str.join(list[i])
    list[i].clear()
  ans=ans+'\n'
  fil.write(ans)


# print(ans)
fil.close()
fil=open('cipher.txt','r')
for each in fil:
  print(each)
  print(len(each))
fil.close()

# frequency analysis code

import re
import string
import operator
file = open('plain.txt','r')
cipher = open('cipher.txt','r')
plain_list = {}
cipher_list = {}
count=0
for each in file : 
  print(each)
  for val in each :
    if val in (string.ascii_lowercase or string.ascii_uppercase):
      count+=1
      if val in plain_list:
        plain_list[val]+=1
      else:
        plain_list[val]=1
for key in plain_list:
  plain_list[key]=(plain_list[key]/count)*100
plain_list=dict(sorted(plain_list.items(), key=operator.itemgetter(1),reverse=True))
print(plain_list)



for each in cipher : 
  print(each)
  for val in each :
    if val in (string.ascii_lowercase or string.ascii_uppercase):
      if val in cipher_list:
        cipher_list[val]+=1
      else:
        cipher_list[val]=1
for key in cipher_list:
  cipher_list[key]=(cipher_list[key]/count)*100
cipher_list=dict(sorted(cipher_list.items(), key=operator.itemgetter(1),reverse=True))
print(cipher_list)

import matplotlib.pyplot as plt
#plot for the plain txt
plt.plot(tuple(plain_list.keys()),tuple(plain_list.values()),label='plain-text-frequency')
plt.plot(tuple(cipher_list.keys()),tuple(cipher_list.values()),label = 'cipher-text-frequency')
plt.legend()
plt.show()

#plot for the ciphered txt
plt.plot(tuple(cipher_list.keys()),tuple(cipher_list.values()),label='cipher-text-frequency')
plt.plot(tuple(plain_list.keys()),tuple(plain_list.values()),label='plain-text-frequency')
plt.legend()
plt.show()

#bar-graph plot for the frequency analysis
plt.bar(tuple(plain_list.keys()),tuple(plain_list.values()),color='red')
plt.xlabel('characters')
plt.ylabel('frequency')
plt.title('frequency of the plain-text characters')
plt.show()
plt.bar(tuple(cipher_list.keys()),tuple(cipher_list.values()),color='green')
plt.xlabel('characters')
plt.ylabel('frequency')
plt.title('frequency of the cipher-text characters')
plt.show()