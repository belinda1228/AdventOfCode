f= open('day8Input.txt','r')
data=[]
for i in f:
    i=i[0:-1]
    data.append([int(x) for x in i])

rows=len(data)
cols=len(data[0])
oneScore=0
score=0
scores=[]

for x in range(0,rows-1):
    for y in range(0,cols-1):
        tree=data[x][y]
        left=[data[x][y-i] for i in range(0,y-i)]
        right=[data[x][y+i] for i in range(1,y)]
        print('meow')
        top=[data[x-i][y] for i in range(0,x+1)]
        bottom=[data[x+i][y] for i in range(1,x)]
        while left<=tree:
            oneScore+=1
        score = oneScore
        oneScore=0
        while right<=tree:
            oneScore+=1
        score = score*oneScore
        oneScore=0
        while top<=tree:
            oneScore+=1
        score = score*oneScore
        oneScore=0
        while bottom<=tree:
            oneScore+=1
        score = score*oneScore
        oneScore=0
    scores.append(score)
    print(score)

print(max(scores))

f.close()