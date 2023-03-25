f = open("day2input.txt", 'r')

oneRoundScore = 0
totalScore = 0
#A = "rock"
#B = "paper"
#C = "scissors"

dicTIE = {"X":"A", "Y":"B", "Z":"C"}
dicLOSE = {"X":"C", "Y":"A", "Z":"B"}
dicScore = {"X":1,"Y":2,"Z":3}

dic = {"rock": "A", "paper": "B", "scissors": "C", "X" : ["rock", 1], "Y" : ["paper", 2], "Z" : ["scissors", 3]}
for i in f:
    print("i[0]: ",i[0] ,"i[2]: ", i[2], "dic[\"Y\"][0]: ", dic["Y"][0], " INPUT")
    if (i[0] == "A" and i[2] == "Y") or (i[0] == "B" and i[2] == "Z") or (i[0] == "C" and i[2] == "X"):
        oneRoundScore += 6
        print("PLUS 6")
    elif (i[0] == "A" and i[2] == "X") or (i[0] == "B" and i[2] == "Y") or (i[0] == "C" and i[2] == "Z"):
        oneRoundScore += 3
        print("PLUS 3")
   # print(oneRoundScore)
    print("PLUS : ", dic[i[2]][1])
    oneRoundScore += dic[i[2]][1]
   # print(oneRoundScore)
    totalScore += oneRoundScore
    oneRoundScore = 0
print("TOTAL SCORE: ", totalScore)

f.close()