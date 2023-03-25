f = open("day1.2Input.txt", "r")

canswer=0
fanswer=[]
total = 0
for i in f:
    if len(i)!= 1:
      canswer = canswer + int(i)
    if len(i) == 1:
        fanswer.append(canswer)
        canswer = 0
    
fanswer.sort(reverse=True)
for x in range(0, 3):
    total += fanswer[x]
print(total)

f.close()