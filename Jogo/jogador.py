import random

import Jogo.inimigo as inimigo
class Jogador:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

class mago(Jogador):
    def __init__(self, nome, vida, ataque, cura, bola_de_fogo):
        super().__init__(nome, vida, ataque)
        self.cura = cura
        self.bola_de_fogo = bola_de_fogo

    def ataca_mago(self, inimigo):
        dano_mago = random.randint(45 , 65)
        inimigo.vida -= dano_mago
        print(f"{self.nome} atacou {inimigo.nome} com uma bola de fogo e causou {dano_mago} de dano!", end="\n\n")
        

class ninja(Jogador):
    def __init__(self, nome, vida, ataque, adagada, furtividade):
        super().__init__(nome, vida, ataque)
        self.adagada = adagada
        self.furtividade = furtividade

    def ataca_ninja(self, inimigo):
        dano_ninja = random.randint(35 , 50)
        inimigo.vida -= dano_ninja
        print(f"{self.nome} atacou {inimigo.nome} com uma adaga e causou {dano_ninja} de dano!", end="\n\n")
        
class arqueiro(Jogador):
    def __init__(self, nome, vida, ataque, flecha, fumaca):
        super().__init__(nome, vida, ataque)
        self.flecha = flecha
        self.fumaca = fumaca

    def ataca_arqueiro(self, inimigo):
        dano_arqueiro = random.randint(30 , 65)
        inimigo.vida -= dano_arqueiro
        print(f"{self.nome} atacou {inimigo.nome} com uma flecha e causou {dano_arqueiro} de dano!", end="\n\n")



