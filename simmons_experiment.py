#code for Simmon's cipher
import string
import re
import operator

file = open('plain.txt','r')
open('cipher.txt','w').close()
fil = open('cipher.txt','a')
for each in file: 
  temp_string=""
  for val in each : 
    if val in (string.ascii_lowercase or string.ascii_uppercase):
      reverse=0
      if val in string.ascii_lowercase:
        reverse=122-(ord(val)-97)
      else :
        reverse=90-(ord(val)-65)
      temp_string=temp_string+chr(reverse)
    else : 
      temp_string=temp_string + val
  print(temp_string)
  fil.write(temp_string)
file.close()
fil.close()

# frequency analysis code

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

#graph plots

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
plt.bar(list(plain_list.keys()),list(plain_list.values()),color='red')
plt.xlabel('characters')
plt.ylabel('frequency')
plt.title('frequency of the plain-text characters')
plt.show()
plt.bar(list(cipher_list.keys()),list(cipher_list.values()),color='green')
plt.xlabel('characters')
plt.ylabel('frequency')
plt.title('frequency of the cipher-text characters')
plt.show()


