
f1 = open('day5InputInstruction.txt','r')


dic={"1": ["V","C","D","R","Z","G",'B','W'], "2":['G','W','F','C','B','S','T','V'], "3":['C','B','S','N','W'],
"4":['Q','G','M','N','J','V','C','P'], "5":['T','S','L','F','D','H','B'], "6":['J','V','T','W','M','N'],
"7":['P','F','L','C','S','T','G'],"8":['B','D','Z'],"9":['M','N','Z','W']}
#print(dic)
for x in f1:
        #print("a"+x)
        move = x.split(' ')[1]
        begFrom = x.split(' ')[3]
        to = x.split(' ')[5]
        #print(to)
        while int(move)>=1 and dic[begFrom]:
            temp = dic[begFrom][-1]
            #print(temp)
            #print(dic[to])
            dic[to].append(temp)
            del dic[begFrom][-1]
            temp = ''
            move= int(move)-1
print(dic)
for key in dic:
        print(dic[key][-1])
#print(dic[begFrom])
#columnFrom = i.split(' ')[int(begFrom-1)]
#columnTo = i.split(' ')[int(to-1)]

        #print(move)

f1.close()