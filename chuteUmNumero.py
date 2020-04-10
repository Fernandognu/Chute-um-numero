## Criação de um jogo interativo entre usuario e maquina, com o objetivo de adivinhar um numero aleatorio ##
## o programa deve dar dicas ao usuario ##

import random
import time
import os


numeroSorteado = random.randint(0, 100)

def frase():
    print("Vou Pensar em um numero entre 0 e 100!")

def chute():
    chuteUsuario = int(input("Tente adivinhar o numero!"))
    if chuteUsuario == numeroSorteado:
        print("Voce acertou!")
        time.sleep(10)
        print("\n" * os.get_terminal_size().lines)
        frase()
        time.sleep(5)
        chute()

    elif chuteUsuario > numeroSorteado:
        print("Chute um numero mais baixo!")
        chute()

    elif chuteUsuario < numeroSorteado:
        print("Chute um numero mais alto!")
        chute()

frase()
time.sleep(5)
chute()