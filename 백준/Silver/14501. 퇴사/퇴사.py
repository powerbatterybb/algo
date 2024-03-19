n = int(input())
item = []
for i in range(n):
  item.append(list(map(int,input().split())))

#print(item)

result = [0]

def bf(start, r):
  for i in range(start, n):
    if i+item[i][0] <= n:
      #print(item[i][0], item[i][1])
      temp = bf(i+item[i][0],r+item[i][1])
      #print(temp)
      result.append(temp)
  return r

bf(0,0)
print(max(result))