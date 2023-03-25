f = open('day9Input.txt','r')
ropes=[rope.stripe() for rope in f.readlines()]
fins = open('day9Instruction.txt','r')
head = ropes[4][0]
tail = ropes[4][0]
dr=head[0]-tail[0]
dc=head[1]-tail[1]
row=len(f)
col=len(f)[0]
spots=set(row,col)
def adjust(head,tail):
    if abs(dr)<=1 and abs(dc)<=1:
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        tail(head[0]-1 if head[0]>tail[0] else head[0]+1, head[1]-1 if head[1]>tail[1] else head[1]+1)
    elif abs(dr)>=2:
        tail(head[0]-1 if head[0]>tail[0] else head[0]+1, head[1])
    elif abs(dc)>=2:
        tail(head[0], head[1]+1 if head[1]>tail[1] else head[1]-1)
for i in fins:
    i= i[1:]
    while i[2]>0 and head in range(col):
        while fins[i-1][0] != fins[i][0]:
            if i[0]=='R':
                head = head[col+1][row]
                int(i[2])-1
                tail = tail[col+1][row]
                spots.append(tail)
            if i[0]=='L':
                head = head[col-1][row]
                int(i[2])-1
                tail = tail[col+1][row]
                spots.append(tail)
        while i[2]>0 and head in range(row):
            if i[0]=='U':
                head = head[col][row-1]
                int(i[2])-1
                tail = tail[col][row-1]
                spots.append(tail)
            if i[0]=='D':
                head = head[col][row+1]
                int(i[2])-1
                tail = tail[col][row+1]
                spots.append(tail)
            tail = tail
        
print(spots.count())
        

f.close()
fins.close()