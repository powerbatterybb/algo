n = int(input())
m = int(input())

item = []

for i in range(n,m+1):
  if (i**(1/2))%1 == 0:
    item.append(i)



#minItem = min(item)    

flag = 0
for i in item:
  flag = 1

if flag ==1:
  print(sum(item))
  print(min(item))
else:
  print(-1)

