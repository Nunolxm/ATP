cinema=[]

def listar(cinema):
    print("Os filmes em exebição são:")
    for sala in cinema:
        print(sala[2])
    return

def disponivel(cinema, filmep, lugar):
    res=False
    for sala in cinema:
        lugares, vendidos, filme= sala
        if filmep==filme and lugar not in vendidos and lugar<lugares:
            res=True
    return res

def vendebilhete(cinema, filmep, lugar):
    if disponivel(cinema, filmep, lugar):
        for sala in cinema:
            filme=sala[2]
            if filmep==filme:
                sala[1].append(lugar)
                sala[1].sort
        print("O bilhete foi vendido.")
    else:
        print("O lugar não se encontra disponível.")
    return cinema

def listardisponibilidade(cinema):
    for sala in cinema:
        lugares, vendidos, filme= sala
        print("---------------------")
        print("Filme:", filme)
        print("Lugares disponíveis:", lugares-len(vendidos))

def inserirSala(cinema, sala):
    if sala not in cinema:
        cinema.append(sala)
    return cinema

def menu():
    print('''
    Menu:
    1 : Listar filmes em exebição;
    2 : Verificar disponibilidade de um lugar;
    3 : Vender bilhete;
    4 : Listar número de lugares disponíveis por filme;
    5 : Inserir sala;
    0 : Sair.''')

menu()
option=int(input("Selecione uma opção:"))

while option!=0:
    if option==1:
        listar(cinema)
    if option==2:
        filmep=str(input("Insira o filme:"))
        lugar=int(input("Insira o lugar:"))
        if disponivel(cinema,filmep,lugar):
            print("O lugar encontra-se disponível")
        else:
            print("O lugar não se encontra disponível")

    if option==3:
        filmep=str(input("Insira o filme:"))
        lugar=int(input("Insira o lugar:"))
        cinema=vendebilhete(cinema, filmep, lugar)
    if option==4:
        listardisponibilidade(cinema)
    if option==5:
        sala=[]
        sala.append(int(input("Insira o número de lugares da sala:")))
        sala.append([])
        sala.append(str(input("Insira o nome do filme em exebição:")))
        cinema=inserirSala(cinema, sala)
    menu()
    option=int(input("Selecione uma opção:"))

