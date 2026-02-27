from Jogo.jogador import mago, arqueiro, ninja
from Jogo.inimigo import Asta, Gon, Kaneki
import random

print("Bem vindo ao jogo de RPG!")
nome = input("Digite o nome do seu personagem: ")
print("Escolha a classe do seu personagem:")
print("1 - Mago")
print("2 - Ninja") 
print("3 - Arqueiro")
classe = int(input("Digite o número da classe escolhida: "))

if classe == 1:
    personagem =mago(nome, 125, 45, 15, 25)
    print(f"Pessima escolha, {personagem.nome}! Você escolheu a classe Mago que tem {personagem.vida} de vida e 45 à 65 de ataque.", end="\n\n")
if classe == 2:
    personagem = ninja(nome, 160, random.randint(25, 40), 0, 25)
    print(f"Pessima escolha, {personagem.nome}! Você escolheu a classe Ninja que tem {personagem.vida} de vida e 35 à 50 de ataque.", end="\n\n")
        
if classe == 3:
    personagem = arqueiro(nome, 140, random.randint(20, 55), 0, 50)
    print(f"Pessima escolha, {personagem.nome}! Você escolheu a classe Arqueiro que tem {personagem.vida} de vida e 30 à 65 de ataque.", end="\n\n")

Asta_obj = Asta("Asta", 145, random.randint(35, 55), 20)
Gon_obj = Gon("Gon", 155, random.randint(20, 75), 15)
Kaneki_obj = Kaneki("Kaneki", 120, random.randint(30, 40), 30)

inimigos = [Asta_obj, Gon_obj, Kaneki_obj]
inimigo = random.choice(inimigos)

if isinstance(inimigo, Asta):
    print(f"O {inimigo.nome} viu que você é BETA! e veio te mogar, ele tem {inimigo.vida} de vida e tem 35 à 55 de ataque.", end="\n\n")
elif isinstance(inimigo, Gon):
    print(f"O {inimigo.nome} viu que você é BETA! e veio te mogar, ele tem {inimigo.vida} de vida e tem 20 à 75 de ataque.", end="\n\n")
elif isinstance(inimigo, Kaneki):
    print(f"O {inimigo.nome} viu que você é BETA! e veio te mogar, ele tem {inimigo.vida} de vida e tem 30 à 40 de ataque.", end="\n\n")

while personagem.vida > 0 and inimigo.vida > 0:
    print("O que você vai fazer?")
    print("1 - Atacar")
    print("2 - ")
    acao = int(input("Digite o número da ação escolhida: "))
    if acao == 1:
        if isinstance(personagem, mago):
            personagem.ataca_mago(inimigo)
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.", end="\n\n")
        elif isinstance(personagem, ninja):
            personagem.ataca_ninja(inimigo)
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.", end="\n\n")
        elif isinstance(personagem, arqueiro):
            personagem.ataca_arqueiro(inimigo)
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.", end="\n\n")

    acao_inimigo = 1 # Inimigo sempre ataca
    if acao_inimigo == 1:
        if isinstance(inimigo, Asta):
            inimigo.atacar_asta(personagem)
            print(f"{personagem.nome} tem {personagem.vida} de vida restante.", end="\n\n")
        elif isinstance(inimigo, Gon):
            inimigo.atacar_gon(personagem)
            print(f"{personagem.nome} tem {personagem.vida} de vida restante.", end="\n\n")
        elif isinstance(inimigo, Kaneki):
            inimigo.atacar_kaneki(personagem)
            print(f"{personagem.nome} tem {personagem.vida} de vida restante.", end="\n\n")

    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado por {inimigo.nome}!")
    elif inimigo.vida <= 0:
        print(f"{personagem.nome} derrotou {inimigo.nome}!")
    elif personagem.vida <= 0 and inimigo.vida <= 0:
        print(f"{personagem.nome} e {inimigo.nome} se derrotaram mutuamente!")