f = open('day6Input.txt','r')

for i in f:
    #list=[]
    for j in range(4,len(i)):
        #list.append(i[j])
        s =set(i[(j-4):j])
        if len(s)==4:
            print(j)
            break
        #for z,x in enumerate(i[j+1],i[j+3]):
            #if i[x] ==i[j] or i[x]==i[x-1] or i[x]==i[x-2]:
                #break
            #if i[x] !=i[j] and i[x]!=i[x-1] and i[x]!=i[x-2]:
               # break
            #else:
              #  x+=1       
        #j+=1
        #break
   # print(z+1)

        #j+=1
        #j=i[0]
#print i[x]

#if the last char didnt repeat then index of that last char

f.close()