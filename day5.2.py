f = open('day5.2Input.txt','r')
dic={"1": ["V","C","D","R","Z","G",'B','W'], "2":['G','W','F','C','B','S','T','V'], "3":['C','B','S','N','W'],
"4":['Q','G','M','N','J','V','C','P'], "5":['T','S','L','F','D','H','B'], "6":['J','V','T','W','M','N'],
"7":['P','F','L','C','S','T','G'],"8":['B','D','Z'],"9":['M','N','Z','W']}

for x in f:
        list=[]
        #print(list)
        #print("a"+x)
        move = x.split(' ')[1]
        begFrom = x.split(' ')[3]
        to = x.split(' ')[5]
        while int(move)>=1 and dic[begFrom]:
            list.append(dic[begFrom][-1])
            del dic[begFrom][-1]
            move =int(move)-1
        #print(list)
        while list:
            temp = list[-1]
            dic[to].append(temp)
            del list[-1]
            #print(list)
         #   print(temp)
        #print(dic)
            
print(dic)
for key in dic:
        print(dic[key][-1])
f.close()