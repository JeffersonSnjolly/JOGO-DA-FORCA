import random
import os
from time import sleep
print( """
========================================
            JOGO DA FORCA
========================================
ADIVINHE A PALAVRA ABAIXO.
APERTE 1 PARA SAIR.
""")


tentivas = 8
letrasErradas = []
lista = []
palavras =  ["CASA","CARRO","MOUSE","BANANA","MATRIX"]
pc = random.choice(palavras)
tamanho = len(pc)

for i in range(0, tamanho):
    lista.append("-")
match pc:
    case "CASA":
        dica = "MORADIA."
    case "CARRO":
        dica = "MEIO DE TRANPORTE."
    case "MOUSE": 
        dica = "HARDWARE DE COMPUTADOR."   
    case "BANANA":
        dica = "FRUTA AMARELA."
    case "MATRIX":
        dica = "FILME, AÇÃO E FUTO DISTÓPICO."
    case _:
        dica = "NÃO TEMOS DICA."

try:
    while tentivas > 0:
        print("="*40)
        print(f"DICA: {dica}")
        print(f"NUMERO DE TENTATIVAS: {tentivas}")
        if letrasErradas:
            print("LETRAS ERRADAS: ", end=" ")
            for i in letrasErradas:
                print(i, end=" ")
            print("\n")
        for i in range(0,len(lista)):
            print(lista[i], end=" ")
            
        print("\n")
        print("="*40)
        user = input("DIGITE UMA LETRA: ").upper()
        if user in pc and user != "1":
            posiçao = [i for i,c in enumerate(pc) if c == user]
            for l in range(0, len(posiçao)):
                lista[posiçao[l]] = user
            tentivas -= 1
            aux = "".join(lista)
            sleep(0.5)
            if aux == pc:
                os.system('cls')
                print("="*40)
                for i in range(0,len(lista)):
                    print(lista[i], end=" ")
            
                print("\n")
                print(f"NUMERO DE TENTATIVAS RESTANTES: {tentivas}")
                
                if letrasErradas:
                    print("LETRAS ERRADAS: ", end=" ")
                    for i in letrasErradas:
                        print(i, end=" ")
                    print("\n")
                print(f"PARABÉNS! VOÇÊ É O GANHADOR")
                print("="*40)
                print("GOODBY!")
                break
            os.system('cls')
            
        elif user == "1":
            sleep(1)
            print("GOODBY!")
            break     
            
        else:
            
            print(f"{user} ESTÁ ERRADA!")
            tentivas -=1
            letrasErradas.append(user)
            sleep(2)
            os.system('cls')


    print("FIM FO JOGO")
except:
    print("Não foi possivel rodar a aplicação.")