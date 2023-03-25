f = open('day7Input.txt','r')
datas=[data.strip() for data in f.readlines()]
# print(datas)
# datas = []
# for i in f:
#     i = i[0:-1]
#     datas.append([x for x in i])
# print(datas)
path = '/home'
dirs = {'/home':0}

for j in datas:
    if j[0]=='$':
        if j[2:4] =='ls':
            pass
        elif j[2:4]== 'cd':
            if j[5:6] =='/':
                path = '/home'
            elif j[5:7] =='..':
                path=path[:path.rfind('/')]
            else:
                dir_name = j[5:]
                path = path+'/'+dir_name
                dirs.update({path:0})
    elif j[0:3]=='dir':
        pass
    else:
        size = int(j[:j.find(' ')])
        dir = path
        for i in range(path.count('/')):
            dirs[dir]+=size
            dir = dir[:dir.rfind('/')]

total = 0
limit = 30000000-(70000000-dirs['/home'])
valid_dirs = []
for dir in dirs:
    # print(dir,dirs[dir])
    if dirs[dir]>=100000:
        total+=dirs[dir]
    if limit<=dirs[dir]:
        valid_dirs.append(dirs[dir])
    smallest=min(valid_dirs)


print(valid_dirs)
print(total)
print(smallest)
f.close()