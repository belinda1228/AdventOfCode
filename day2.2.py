f = open("day2.2Input.txt",'r')

drawDicY = {"A":"A", "B":"B", "C":"C"}
winDicZ = {"A":"B", "B":"C", "C":"A"}
lostDicX = {"A":"C", "B":"A", "C":"B"}
valueDic = {"A": 1, "B":2, "C":3}
fscore = 0
cscore = 0
for i in f:
    if i[2] =="Y":
        cscore = cscore +3 + valueDic[drawDicY[i[0]]]
        fscore += cscore
        cscore = 0


    if i[2] == "Z":
        cscore = cscore +6 + valueDic[winDicZ[i[0]]]
        fscore += cscore
        cscore = 0

    if i[2] == "X":
        cscore = cscore +0 + valueDic[lostDicX[i[0]]]
        fscore += cscore
        cscore = 0

    
print(fscore)
f.close()