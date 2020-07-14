herolist = {
    '1':{'p1':'a',
         'p2':'b'
         },
    '2':{'p1':'c',
         'p2':'d'
         },
    '3':{'p1':'e',
         'p2':'a'
         },
    '4':{'p1':'b',
         'p2':'d'
         },
    '5':{'p1':'e',
         'p2':'c'
         },
    '6':{'p1':'b',
         'p2':'d'
         },
    '7':{'p1':'b'
         }
}

jiban={'a':0,'b':0,'c':0,'d':0,'e':0}

def addp(xp):
    jiban[xp] += 1
    return

# addp('a')
# addp('a')
# addp('a')
# print(jiban['a'])





n = int(input("Hero number: ").strip())
for i in range(n):
    x = input("Hero{} name: ".format((str(i+1))))
    pn = len(herolist[x])    #p number
    for o in range(pn):
        p = 'p' + str(o + 1)
        addp(herolist[x][p])





print(jiban)

# while jiban[x] == 0

for i in ['a','b','c','d','e']:
    if jiban[i] == 0:
        del jiban[i]


print(jiban)















#     print("For now: {},{}".format(ap1,ap2))
#     i += 1