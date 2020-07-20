
from herolist import *
from combo import *

##################################
#需要将羁绊统一归零
def clear(n):
    fnow = {}
    for i in range(len(n)):
        fnow[n[i]] = 0
        i += 1
    return fnow

jiban = clear(nlist)
##################################


##############
#输入数字
n = int(input("Hero number: ").strip())

#遍历所有英雄
nowhero = []
for i in range(n):
    x = input("Hero{} name: ".format(str(i + 1)))     #输入英雄名称
    nowhero.append(x)
    #将英雄身上所有羁绊记录
    def addp(xp):
        jiban[xp] += 1
        return
    #pn 羁绊数(三项属性-第一项)
    pn = len(herolist[x]) - 1
    for o in range(pn):
        p = 'p' + str(o + 1)
        addp(herolist[x][p])


#检索剔除羁绊数为0
for i in nlist:
    if jiban[i] == 0:
        del jiban[i]
##################################
print(jiban)

for i in jiban:
    print("羁绊\"{}\":{}".format(i,jiban[i]))


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
#         print(x,lev) 

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

print("Need hero name: ",needhero)
print('权重: ',needheroweigh)

print("Now hero: ",nowhero)
herostar = []
for i in needhero:
    herostar.append(herolist[i]['star'])
print("Need hero's Star: ",herostar)



















