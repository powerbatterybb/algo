#입력
n, goal = map(int,input().split())
numList = list(map(int, input().split()))
sumList = []

#for 
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1, n):
      sum = numList[i]+numList[j]+numList[k]
      if sum <= goal:
        sumList.append(sum)
        
print(max(sumList))