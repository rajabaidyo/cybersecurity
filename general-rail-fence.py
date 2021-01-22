file = open('plain.txt','w')
file.write('you are a nice person;\nstill fuck, you')
file.close()

#code for general railfence cipher(encryption)
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