f = open('day8Input.txt','r')
data=[row.strip() for row in f.readlines()]


# data = []
# for i in f:
#     i = i[0:-1]
#     data.append([int(x) for x in i])
# print(data)
    
rows = len(data)
columns= len(data[0])
# edges=rows*2+((columns-2)*2)
# total =edges
# print(total)

# visible=total


for row in range(1,rows-1):
    for column in range(1, columns-1):
        tree=data[row][column]
        left=[data[row][column-i] for i in range(1,column)]
        right=[data[row][column+i] for i in range(1,columns-column)]
        top=[data[row-i][column] for i in range(1,row+1)]
        bottom=[data[row+i][column] for i in range(1,rows-row)]
        # if max(left)<tree or max(right)<tree or max(top)<tree or max(bottom)<tree:
            # visible+=1

        visible_tree_left=0
        for x in range(len(left)):
            visible_tree_left += 1
            if left[len(left)-1-x]>=tree:
                break
        visible_tree_right=0
        for x in range(len(right)):
            visible_tree_right +=1
            if right[x]>=tree:
                break
        visible_tree_top=0
        for x in range(len(top)):
            visible_tree_top+=1
            if top[len(top)-1-x]>=tree:
                break
        visible_tree_bottom=0
        for x in range(len(bottom)):
            visible_tree_bottom+=1
            if bottom[len(bottom)-1-x]>=tree:
                break
        best_score=0
        one_score=visible_tree_bottom*visible_tree_left*visible_tree_right*visible_tree_top
        if one_score>best_score:
            best_score = one_score
print(best_score)
# print(visible)

f.close()