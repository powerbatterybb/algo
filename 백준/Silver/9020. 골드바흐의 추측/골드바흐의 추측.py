import sys
n = int(sys.stdin.readline())

sosu = []
for i in range(2, 10000):
  temp = 0
  for j in range(1,int(i**(1/2))+1):
    if i % j ==0:
      temp =  temp+1
    
    if temp>2:
      break
  
  if temp == 1:
    sosu.append(i)

#print(sosu)

for i in range(n):
  num = int(sys.stdin.readline())

  # solution= []
  # for j in range(len(sosu)):
  #   for k in range(len(sosu)):
  #     if sosu[j]+sosu[k] ==num:
  #       solution.append([sosu[j],sosu[k]])
      
  #     if sosu[k]>num:
  #       break
  #   if sosu[j]>num:
  #     break

  val = int(num/2)
  #print(t)

  for j in range(val):
    if (val-j in sosu) and (val+j in sosu) :
      print(val-j,val+j)
      break
  