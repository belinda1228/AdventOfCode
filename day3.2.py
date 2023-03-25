from string import ascii_letters
f = open('day3.2Input.txt', 'r')
data = [i for i in f.read().strip().split('/n')]
csum = 0
csumY = 0
tempList=[]

print(tempList)
# for i in f:
#         for j in range(0, len(i)//2):
#             for x in range(len(i)//2, len(i)-1):
#                 if i[j]==i[x]:
#                     tempList.append(i[j])
#                     if ord(str(i[j]))>=97:
#                         csumY = csumY + (ord(i[j])-96)
#                     elif ord(str(i[j]))>=65:
#                         csumY = csumY +(ord(i[j])-38)
#                     print(csumY, " ", i[j] ," ***")
#                     break
#             else:
#                 continue
#             break
j=3
totalsum =0
for x in range(0,len(data),3):
    i = data[x:j]
    j+=3
    print(i[j])
    for priority, char in enumerate(ascii_letters):
        if char in i[0] and char in i[1] and char in i[2]:
            totalsum+= priority +1
print(totalsum)
        #print(i[j])
   


# print(sum)

f.close()