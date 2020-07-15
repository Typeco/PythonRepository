herolist = {
    '1': {'star':1,
          'p1': 'a',
          'p2': 'b'
          },
    '2': {'star':1,
          'p1': 'c',
          'p2': 'd'
          },
    '3': {'star':2,
          'p1': 'a',
          'p2': 'd'
          },
    '4': {'star':3,
          'p1': 'b',
          'p2': 'e'
          },
    '5': {'star':4,
          'p1': 'c',
          'p2': 'd',
          'p3': 'a'
          }
}

nlist = ['a','b','c','d','e']   #测试用 羁绊列表

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
##################################

#输入数字
n = int(input("Hero number: ").strip())

#遍历所有英雄
for i in range(n):
    x = input("Hero{} name: ".format(str(i + 1)))     #输入英雄名称

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
    
    
    
    
    

combonum = {
    'a':{
        "cb1":3,
        "cb2":6
    },
    'b':{
        "cb1":3,
        "cb2":6,
        "cb3":9
    },
    'c': {
        "cb1": 2,
        "cb2": 4
    },
    'd': {
        "cb1": 4
    },
    'e': {
        "cb1": 3,
        "cb2": 6
    }
}






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
        




print("还差羁绊{}，当前羁绊等级{}".format(closenum(jiban,combonum)[0],closenum(jiban,combonum)[1]))




























