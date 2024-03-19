a, b ,V = map(int,input().split())

cnt = 0
val = 0

#반복문 시간초과
'''
while True:
  cnt = cnt+1
  val = val+a
  if val >= V:
    break
  val = val-b

print(cnt)
'''

#수학적으로 접근
day = ((V-a) / (a-b)) +1

if day % 1 == 0:
  day = day
  cnt = int(day)
else:
  day = day + 1
  cnt = int(day)

print(cnt)