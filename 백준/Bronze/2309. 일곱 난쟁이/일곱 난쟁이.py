n = []
for i in range(9):
  n.append(int(input()))

for i in range(8):
  for j in range(i+1, 9):
    sumA = sum(n) - n[i] - n[j]
    #print(n[i], n[j])
    if sumA == 100:
      a = n[i]
      b = n[j]
      n.remove(a)
      n.remove(b)

      break
  if sumA == 100:
    break

n.sort()

for i in n: 
  print(i)