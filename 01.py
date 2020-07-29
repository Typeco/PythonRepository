#################################
import csv
#################################

##################################
combonum = {}
with open("cbn.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['id'], row['c1'], row['c2'], row['c3'], row['c4'])
        cbndict = {}
        for i in ['c1', 'c2', 'c3', 'c4']:
            if row[i] != '':
                row[i]=int(row[i])
                cbndict[i] = row[i]
        combonum[row["id"]] = cbndict
######################################
herolist = {}
with open("hdb.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['id'], row['star'], row['p1'], row['p2'], row['p3'])
        hpdict = {}
        for i in ['star','p1', 'p2', 'p3']:
            if row[i] != None:
                hpdict[i] = row[i]
        herolist[row["id"]] = hpdict
######################################
nlist = []
for k in herolist.keys():
    for i in range(len(herolist[k])-1):
        if nlist.count(herolist[k]['p'+str(i+1)]) == 0:
            nlist.append(herolist[k]['p'+str(i+1)])
######################################
#需要将羁绊统一归零
def clear(n):
    fnow = {}
    for i in range(len(n)):
        fnow[n[i]] = 0
        i += 1
    return fnow

jiban = clear(nlist)
##################################


#################################

# #输入数字
# n = int(input("Hero number: ").strip())
# #遍历所有英雄
# nowhero = []
# for i in range(n):
#     x = input("Hero{} name: ".format(str(i + 1)))     #输入英雄名称
#     nowhero.append(x)
#     #将英雄身上所有羁绊记录
#     def addp(xp):
#         jiban[xp] += 1
#         return
#     #pn 羁绊数(三项属性-第一项)
#     pn = len(herolist[x]) - 1
#     for o in range(pn):
#         p = 'p' + str(o + 1)
#         addp(herolist[x][p])
#################################
#2修改findhero文件:
with open("findhero.conf","r",encoding='UTF-8') as f:
    info = f.read()
list_info = eval(info)
# nowhero = ['佐伊','崔斯特']
nowhero = list_info

#################################
for i in nowhero:
    #将英雄身上所有羁绊记录
    def addp(xp):
        jiban[xp] += 1
        return
    #pn 羁绊数(三项属性-第一项)
    pn = len(herolist[i]) - 1
    for o in range(pn):
        p = 'p' + str(o + 1)
        addp(herolist[i][p])


#################################
#检索剔除羁绊数为0
for i in nlist:
    if jiban[i] == 0:
        del jiban[i]
##################################
print(jiban)


def closenum(jiban,combonum):
    f = []
    weig = []
    for key in jiban:
        x = []
        lev = 0
        #########
        #计算差值
        for i in combonum[key]:
            x.extend([combonum[key][i] - jiban[key]])
        #判断x中的负数
        for o in range(len(x)):
            if x[o] <= 0:
                x[o] = 100
                #计算权重
                lev += 1
        #寻找x中最小值
        weig.append(lev)
        f.extend([min(x)])
        print(key,lev)

    return f,weig

www = closenum(jiban,combonum)
print("还差羁绊{}，当前羁绊等级{}".format(www[0],www[1]))

#查找羁绊
def findHeroPro(dict,x):
    dictlist = list(dict.values())
    a = []
    for i in dictlist:
        for key, value in i.items():
            if value == x :
                a.append(list(dict.keys())[list(dict.values()).index(i)])
    return a

needhero = []
for i in jiban.keys():
    needhero.extend(findHeroPro(herolist,i))

print("查找羁绊:", list(jiban.keys()))


needheroweigh = {}
for i in needhero:
    needherotime = needhero.count(i)
    needheroweigh[i] = needherotime
print(needheroweigh)
needhero =list(needheroweigh.keys())

#删除重名英雄
for i in nowhero:
    if i in needhero:
        needhero.remove(i)
        needheroweigh.pop(i)

herostar = []
for i in needhero:
    herostar.append(herolist[i]['star'])





push = open("push.txt","w")
line0 = ("#"*45)
line1 = ("Now hero: {}".format(nowhero))
line2 = ("Need hero name: {}".format(needhero))
line3 = ("Need hero's Star: {}".format(herostar))
line4 = ('Hero weigh: {}'.format(needheroweigh))
line5 = ('Hero\'s 羁绊: {}'.format(jiban))


push.write(line1+'\n'+line5+'\n'+line2+'\n'+line3+'\n'+line4+'\n')
push.write("#"*45)
for i in needhero:
    push.write('\n'+"Hero's name: ")
    push.write(i+'\n')
    n = len(herolist[i])-1
    for o in range(n):
        p = 'p' + str(o+1)
        push.write("Hero's 羁绊{}: {}".format(o+1,herolist[i][p])+'\n')
    push.write('#'*45)

push.close()








