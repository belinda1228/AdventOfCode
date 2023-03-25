f = open('day10Input.txt','r')
value=[i for i in f.stripe()]
cycleNum = 0
signalStrengths = 0
list=[20,60,100,140,180,220]
# value=i.split(' ')[0]

for i in f:
    value=i.split(' ')[1]
    print(value)
    for x in list:
        while cycleNum<=x:
            if i[0]=="a":
                cycleNum +=1
                if cycleNum%2 == 0:
                    signalStrengths+= int(value)
            if i[0]=='n':
                cycleNum+=1
                signalStrengths+=1
    
print(signalStrengths)

f.close()