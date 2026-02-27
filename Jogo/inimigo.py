import random

class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        
class Asta(Inimigo):
    def __init__(self, nome, vida, ataque, espada):
        super().__init__(nome, vida, ataque)
        self.espada = espada
    
    def atacar_asta(self, personagem):
        dano_asta = random.randint(35, 55)
        personagem.vida -= dano_asta
        print(f"{self.nome} atacou {personagem.nome} com uma espada e causou {dano_asta} de dano!", end="\n\n")

class Gon(Inimigo):
    def __init__(self, nome, vida, ataque, pedra):
        super().__init__(nome, vida, ataque)
        self.pedra = pedra

    def atacar_gon(self, personagem):
        dano_gon = random.randint(20, 75)
        personagem.vida -= dano_gon
        print(f"{self.nome} atacou {personagem.nome} com uma pedra e causou {dano_gon} de dano!", end="\n\n")

class Kaneki(Inimigo):
    def __init__(self, nome, vida, ataque, kagune):
        super().__init__(nome, vida, ataque)
        self.kagune = kagune

    def atacar_kaneki(self, personagem):
        dano_kaneki = random.randint(30, 40)
        personagem.vida -= dano_kaneki
        print(f"{self.nome} atacou {personagem.nome} com seu kagune e causou {dano_kaneki} de dano!", end="\n\n")