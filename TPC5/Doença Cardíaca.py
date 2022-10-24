def ler(file):
    f=open(str(file),"r")
    lista=[]

    for line in f:     
        paciente=line[:-1].split(",")
        lista.append(paciente)
    f.close
    return lista

def sexo(list):
    m=0
    f=0
    for p in list:
        if p[-1]=="1":
            if p[1]=="M":
                m+=1
            if p[1]=="F":
                f+=1
    distrib=[("M",m),("F",f)]
    return distrib

def idade(list):
    distrib=[]
    e=30
    while e<85:
        escalão=[e,e+5]
        n=0
        for p in list:
            if p[-1]=="1" and escalão[0]<=int(p[0])<escalão[1]:
                n+=1
        distrib.append((escalão,n))
        e+=5
    return distrib

def colesterol(list):
    distrib=[]
    e=0
    while e<540:
        escalão=[e,e+10]
        n=0
        for p in list:
            if p[-1]=="1" and escalão[0]<=int(p[3])<escalão[1]:
                    n+=1
        distrib.append((escalão,n))
        e+=10
    return distrib

def tabela(dados,criterio):
    if criterio==sexo:
        print("Sexo  | Nº de Doentes")
    if criterio==idade:
        print("Idade | Nº de Doentes")
    if criterio==colesterol:
        print("Colesterol | Nº de Doentes")
    for i in criterio(dados):
        print(i[0],"|",i[1])
    print("\n")
dados=ler("myheart.csv")

tabela(dados,sexo)
tabela(dados,idade)
tabela(dados,colesterol)