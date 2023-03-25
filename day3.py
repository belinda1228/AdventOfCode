f = open('day3Input.txt', 'r')


#dic = {'a':1, 'b':2,'c':3, 'd':4,'e':5, 'f':6, 'g':7, 
#'h':8,'i':9,'j':10,'k':11, 'l':12, 'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,
#'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,
#'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,}
csum = 0
csumY = 0
tempList=[]

print(tempList)
print(fList)
for i in f:
        for j in range(0, len(i)//2):
            for x in range(len(i)//2, len(i)-1):
                if i[j]==i[x]:
                    tempList.append(i[j])
                    if ord(str(i[j]))>=97:
                        csumY = csumY + (ord(i[j])-96)
                    elif ord(str(i[j]))>=65:
                        csumY = csumY +(ord(i[j])-38)
                    print(csumY, " ", i[j] ," ***")
                    break
            else:
                continue
            break
        
for rucksack in data:
    half = len(rucksack)//2
    left = set(rucksack[:half])
    right = set(rucksack[half:])
    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalsum+=priority +1
        #fList.append(tempList)
print(tempList)

            
print(csum)
print(csumY)


f.close()

