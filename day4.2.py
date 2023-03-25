f = open('day4.2Input.txt','r')

pairs = 0
for i in f:
    j= i.split(',')[0]
    jNum1= j.split('-')[0]
    jNum2= j.split('-')[1]
    x= i.split(',')[1]
    xNum1= x.split('-')[0]
    xNum2= x.split('-')[1]
    if (int(xNum1)>=int(jNum1) and int(xNum1)<=int(jNum2)) or (int(jNum1)>=int(xNum1)and int(jNum1)<=int(xNum2)) or (int(xNum2)>=int(jNum1)and int(xNum2)<=int(jNum2)) or(int(jNum2)>=int(xNum1)and int(jNum2)<=int(xNum2)):
        pairs +=1
   # elif (int(xNum1)<=int(jNum2) and int(xNum1)>=int(jNum1))or (int(jNum1)<=int(xNum2)and int(jNum1)>=int(jNum1)) or (int(xNum2)<=int(jNum2)and int(xNum2)>=int(jNum1))or(int(jNum2)<=int(xNum2)and int(jNum2)>=int(xNum1)):
   #     pairs +=1
    #elif(int(jNum1)>int(xNum1)and int(jNum1)>int(xNum2) and int(jNum2)>int(jNum1)):
    #    pairs +=0
print(pairs)

f.close()