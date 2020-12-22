import pymorphy2
morph = pymorphy2.MorphAnalyzer()
f=open('boltun.txt','r',encoding='UTF-8')
f2=open('boltun.csv','w',encoding='UTF-8')
f2.write('index,Context,Response,NContext,NResponse'+'\n')
s=f.read()
mas=s.split('u:')
n=-1
vopros=''
otvet=''
vopros2=''
otvet2=''
for x in mas:
    mas2=x.split('\n')
    vopros=(mas2[0].strip())
    try:
        otvet=(mas2[1].strip())
        n=n+1
    except:
        continue
    vopros2 = ' '.join(morph.parse(word)[0].normal_form for word in vopros.split())
    otvet2 = ' '.join(morph.parse(word)[0].normal_form for word in otvet.split())
    f2.write(str(n)+',"'+vopros+'","'+otvet+'","'+vopros2+'","'+otvet2+'"'+'\n')
    
    
f.close()
f2.close()
