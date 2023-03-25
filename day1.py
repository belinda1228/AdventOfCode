f = open("day1Input.txt", "r")

canswer=0
fanswer=0
for i in f:
    if len(i)!= 1:
      canswer = canswer + int(i)
    if len(i) == 1:
      canswer = 0
    if fanswer < canswer:
      fanswer = canswer
print(fanswer) 

f.close()