# herolist = {
#     '1': {'p1': 'a',
#           'p2': 'b'
#           },
#     '2': {'p1': 'c',
#           'p2': 'd'
#           },
#     '3': {'p1': 'e',
#           'p2': 'a'
#           },
#     '4': {'p1': 'b',
#           'p2': 'd'
#           },
#     '5': {'p1': 'e',
#           'p2': 'c'
#           },
#     '6': {'p1': 'b',
#           'p2': 'd'
#           },
#     '7': {'p1': 'b'
#           }
# }


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
