import sys
n = int(input())

for i in range(n):
  k = int(input())

  item =[]
  result = []
  cnt = 1
  for j in range(k):
    x = list(map(int,sys.stdin.readline().split()))
    item.append(x)

  item.sort()

  #print(item)

  #result.append(item[0])
  max_val = item[0][1]

  for y in range(1,k):
    if max_val>= item[y][1]:
      #result.append(item[y])
      cnt = cnt+1
      max_val=item[y][1]

  #print(len(result))
  #print(len(result))
  print(cnt)