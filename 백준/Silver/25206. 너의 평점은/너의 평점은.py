item = []
for i in range(20):
  a= input().split()
  item.append(a)

  #print(item)

sum = 0.0
cnt = 0.0

for i in range(20):

  if item[i][2] == "P":
    pass

  else:
    if item[i][2] == "A+":
      sum = sum+ 4.5*float(item[i][1])
    elif item[i][2] == "A0":
      sum = sum+ 4.0*float(item[i][1])
    elif item[i][2] == "B+":
      sum = sum+ 3.5*float(item[i][1])
    elif item[i][2] == "B0":
      sum = sum+ 3.0*float(item[i][1])
    elif item[i][2] == "C+":
      sum = sum+ 2.5*float(item[i][1])
    elif item[i][2] == "C0":
      sum = sum+ 2.0*float(item[i][1])
    elif item[i][2] == "D+":
      sum = sum+ 1.5*float(item[i][1])
    elif item[i][2] == "D0":
      sum = sum+ 1.0*float(item[i][1])
    elif item[i][2] == "F":
      sum = sum+ 0*float(item[i][1])

    cnt = cnt + float(item[i][1])

print(sum/cnt)