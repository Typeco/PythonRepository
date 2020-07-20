#################################
# from herolist import *
# from combo import *
import pprint
#################################
nlist = ['星之守护者',
         '银河魔装机神',
         '星神',
         '奥德赛',
         '未来战士',
         '太空海盗',
         '源计划',
         '暗星',
         '战地机甲',
         '宇航员',
         '剑士',
         '爆破专家',
         '刺客',
         '斗士',
         '法师',
         '圣盾使',
         '狙神',
         '秘术师',
         '破法战士',
         '强袭枪手',
         '星舰龙神',
         '佣兵',
         '重装战士',
         '大魔法使']

combonum = {
    '星之守护者': {
        'c1': 3,
        'c2': 6,
        'c3': 9
    },
    '银河魔装机神': {
        'c1': 3
    },
    '星神': {
        'c1': 2,
        'c2': 4,
        'c3': 6
    },
    '奥德赛': {
        'c1': 3,
        'c2': 6,
        'c3': 9
    },
    '未来战士': {
        'c1': 2,
        'c2': 4,
        'c3': 6,
        'c4': 8
    },
    '太空海盗': {
        'c1': 2,
        'c2': 4
    },
    '源计划': {
        'c1': 3,
        'c2': 6
    },
    '暗星': {
        'c1': 2,
        'c2': 4,
        'c3': 6,
        'c4': 8
    },
    '战地机甲': {
        'c1': 2,
        'c2': 4,
        'c3': 6,
        'c4': 8
    },
    '宇航员': {
        'c1': 3
    },
    '剑士': {
        'c1': 3,
        'c2': 6,
        'c3': 9
    },
    '爆破专家': {
        'c1': 2
    },
    '刺客': {
        'c1': 2,
        'c2': 4,
        'c3': 6
    },
    '斗士': {
        'c1': 2,
        'c2': 4
    },
    '法师': {
        'c1': 2,
        'c2': 4,
        'c3': 6
    },
    '圣盾使': {
        'c1': 2,
        'c2': 4,
        'c3': 6
    },
    '狙神': {
        'c1': 2,
        'c2': 4
    },
    '秘术师': {
        'c1': 2,
        'c2': 4
    },
    '破法战士': {
        'c1': 2
    },
    '强袭枪手': {
        'c1': 2,
        'c2': 4
    },
    '星舰龙神': {
        'c1': 1
    },
    '佣兵': {
        'c1': 1
    },
    '重装战士': {
        'c1': 2,
        'c2': 4,
        'c3': 6
    },
    '大魔法使': {
        'c1': 1
    }
}

herolist = {
    '波比': {'star':1,
          'p1': '星之守护者',
          'p2': '重装战士'
          },
    '崔斯特': {'star':1,
          'p1': '未来战士',
          'p2': '法师'
          },
    '俄洛伊': {'star':1,
          'p1': '战地机甲',
          'p2': '斗士'
          },
    '菲奥娜': {'star':1,
          'p1': '源计划',
          'p2': '剑士'
          },
    '格雷福斯': {'star':1,
          'p1': '太空海盗',
          'p2': '强袭枪手'
          },
    '吉格斯': {'star':1,
          'p1': '奥德赛',
          'p2': '爆破专家'
          },
    '嘉文四世': {'star':1,
          'p1': '暗星',
          'p2': '圣盾使'
          },
    '凯特琳': {'star':1,
          'p1': '未来战士',
          'p2': '狙神'
          },
    '蕾欧娜': {'star':1,
          'p1': '源计划',
          'p2': '重装战士'
          },
    '魔腾': {'star':1,
          'p1': '战地机甲',
          'p2': '刺客'
          },
    '墨菲特': {'star':1,
          'p1': '奥德赛',
          'p2': '斗士'
          },
    '霞': {'star':1,
          'p1': '星神',
          'p2': '剑士'
          },
    '佐伊': {'star':1,
          'p1': '星之守护者',
          'p2': '法师'
          },
    '安妮': {'star':2,
          'p1': '银河魔装机神',
          'p2': '法师'
          },
    '赵信': {'star':2,
          'p1': '星神',
          'p2': '圣盾使'
          },
    '布里茨': {'star':2,
          'p1': '未来战士',
          'p2': '斗士'
          },
    '莫德凯撒': {'star':2,
          'p1': '暗星',
          'p2': '重装战士'
          },
    '克格莫': {'star':2,
          'p1': '战地机甲',
          'p2': '强袭枪手'
          },
    '慎': {'star':2,
          'p1': '未来战士',
          'p2': '剑士'
          },
    '阿狸': {'star':2,
          'p1': '星之守护者',
          'p2': '法师'
          },
    '诺提勒斯': {'star':2,
          'p1': '宇航员',
          'p2': '重装战士'
          },
    '德莱厄斯': {'star':2,
          'p1': '太空海盗',
          'p2': '破法战士'
          },
    '亚索': {'star':2,
          'p1': '奥德赛',
          'p2': '剑士'
          },
    '卢锡安': {'star':2,
          'p1': '源计划',
          'p2': '强袭枪手'
          },
    '劫': {'star':2,
          'p1': '奥德赛',
          'p2': '刺客'
          },
    '洛': {'star':2,
          'p1': '星神',
          'p2': '圣盾使'
          },
    '易': {'star':3,
          'p1': '奥德赛',
          'p2': '剑士'
          },
    '艾希': {'star':3,
          'p1': '星神',
          'p2': '狙神'
          },
    '萨克': {'star':3,
          'p1': '暗星',
          'p2': '刺客'
          },
    '卡尔玛': {'star':3,
          'p1': '暗星',
          'p2': '秘术师'
          },
    '薇恩': {'star':3,
          'p1': '源计划',
          'p2': '狙神'
          },
    '兰博': {'star':3,
          'p1': '银河魔装机神',
          'p2': '爆破专家'
          },
    '卡西奥佩娅': {'star':3,
          'p1': '战地机甲',
          'p2': '秘术师'
          },
    '伊泽瑞尔': {'star':3,
          'p1': '未来战士',
          'p2': '强袭枪手'
          },
    '杰斯': {'star':3,
          'p1': '太空海盗',
          'p2': '重装战士'
          },
    '辛德拉': {'star':3,
          'p1': '星之守护者',
          'p2': '法师'
          },
    '蔚': {'star':3,
          'p1': '源计划',
          'p2': '斗士'
          },
    '巴德': {'star':3,
          'p1': '宇航员',
          'p2': '秘术师'
          },
    '妮蔻': {'star':3,
          'p1': '星之守护者',
          'p2': '圣盾使'
          },
    '菲兹': {'star':4,
          'p1': '银河魔装机神',
          'p2': '刺客'
          },
    '维克托': {'star':4,
          'p1': '战地机甲',
          'p2': '法师'
          },
    '纳尔': {'star':4,
          'p1': '宇航员',
          'p2': '斗士'
          },
    '烬': {'star':4,
          'p1': '暗星',
          'p2': '狙神'
          },
    '金克丝': {'star':4,
          'p1': '奥德赛',
          'p2': '强袭枪手'
          },
    '泽拉斯': {'star':5,
          'p1': '暗星',
          'p2': '法师'
          },
    '璐璐': {'star':5,
          'p1': '星神',
          'p2': '秘术师'
          },
    '索尔': {'star':5,
          'p1': '奥德赛',
          'p2': '星舰龙神'
          },
    '艾克': {'star':5,
          'p1': '源计划',
          'p2': '刺客'
          },
    '锤石': {'star':5,
          'p1': '未来战士',
          'p2': '破法战士'
          }
}
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
        print(x,lev)

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


# print("#"*45)
# print("Now hero: {}".format(nowhero))
# print("Need hero name: {}".format(needhero))
# print("Need hero's Star: {}".format(herostar))
# print('Hero weigh: {}'.format(needheroweigh))












