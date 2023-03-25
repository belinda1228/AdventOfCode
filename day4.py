f = open('day4Input.txt','r')
pairs = 0
for i in f:
    j= i.split(',')[0]
    jNum1= j.split('-')[0]
    jNum2= j.split('-')[1]
    x= i.split(',')[1]
    xNum1= x.split('-')[0]
    xNum2= x.split('-')[1]
    if int(jNum1)<=int(xNum1)and int(jNum2)>=int(xNum2):
        pairs +=1
    elif int(jNum1)>=int(xNum1)and int(jNum2)<=int(xNum2):
        pairs +=1
print(pairs)

#print(jEnd,xStart)

f.close()