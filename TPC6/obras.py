#Modelo: [[nome, desc, anoCriação, periodo, compositor, duração, id],...]

import csv
from fileinput import filename
import matplotlib.pyplot as plt

def lerObras(filename):
    file=open(filename, encoding="UTF8")
    file.readline()
    csv_file=csv.reader(file,delimiter=";")

    lista=[]
    for obra in csv_file:
        lista.append(tuple(obra))

    file.close()
    return lista

def contarObras(lista):
    return len(lista)

def imprime(obras):
    print(f"| {'Nome':^20} | {'Descrição':^25} | {'Ano':^8} | {'Compositor':^15} |")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:^8} | {comp[:15]:15} |")

def ordem(tuplo):
    return(tuplo[0])

def titAno(obras):
    lista=[]
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))

    lista.sort(key=ordem)
    return lista

def ordem2(tuplo):
    return(tuplo[1])

def titAno_2(obras):
    lista=[]
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=ordem2)
    return lista

def titporAno(obras):
    dici={}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano]=[nome]
    return dici

def titporPeriodo(obras):
    dici={}
    for nome, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo].append(nome)
        else:
            dici[periodo]=[nome]
    return dici


def titporCompositor(obras):
    dict={}
    for nome, _, _, _,compositor, *_ in obras:
        if compositor in dict.keys():
            dict[compositor].append(nome)
        else:
            dict[compositor]=[nome]
    return dict

def grafico(obras,criterio):
    distrib=criterio(obras)
    height=[]
    for list in distrib.values():
        height.append(len(list))
    plt.bar(distrib.keys(), height)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.show()
    return

def novaDistrib(obras):
    res= []
    listaComp= []
    for obra in obras:
        nome, desc, ano, periodo, comp, duracao, id = obra
        if comp not in listaComp:
            listaComp.append(comp)
    for compositor in listaComp:
        listaObras= []
        for obra in obras:
            nome, desc, ano, periodo, comp, duracao, id = obra
            if  comp == compositor:
                listaObras.append(nome)
        res.append((compositor, listaObras))
    return res

def lernovaDistrib(lista):
    for tuplo in lista:
        autor, obras = tuplo
        i = 1
        branco = ""
        print(f"\n{autor:<30}|{obras[0]:<20}")
        while i != len(obras):
            print(f"{branco:<30}|{obras[i]:<20}")
            i += 1
    return