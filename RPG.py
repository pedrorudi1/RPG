import random


class Personagem:
    def __init__(self, Nome, Classe, level, HP, Atk, MagAtk, Def, MagDef, Spd):
        self.Nome = Nome
        self.Classe = Classe
        self.level = level
        self.HP = HP
        self.Atk = Atk
        self.MagAtk = MagAtk
        self.Def = Def
        self.MagDef = MagDef
        self.Spd = Spd

    def Equipar_arma(self, Armas):
        self.Atk = self.Atk + Armas.Atk
        self.MagAtk = self.MagAtk + Armas.MagAtk
        self.Spd = self.Spd + Armas.Spd
        print(f'Equipou {Armas.Nome}')

    def Equipar_armadura(self, Armaduras):
        self.Def = self.Def + Armaduras.Def
        self.MagDef = self.MagDef + Armaduras.MagDef
        self.Spd = self.Spd + Armaduras.Spd
        print(f'Equipou {Armaduras.Nome}')

    def Equipar_escudo(self, Escudos):
        self.Def = self.Def + Escudos.Def
        self.MagDef = self.MagDef + Escudos.MagDef
        self.Spd = self.Spd + Escudos.Spd
        print(f'Equipou {Escudos.Nome}')
    
    def Equipar_acessorio(self, Acessorios):
        self.HP = self.HP + Acessorios.HP
        self.Atk = self.Atk + Acessorios.Atk
        self.Def = self.Def + Acessorios.Def
        self.MagAtk = self.MagAtk + Acessorios.MagAtk
        self.MagDef = self.MagDef + Acessorios.MagDef
        self.Spd = self.Spd + Acessorios.Spd
        self.Efeito = Acessorios.Efeito

    def level_up(self, level):
        self.level = level + 1
        self.HP = self.HP + (2 * level)
        self.Atk = self.Atk + (2 * level)
        self.MagAtk = self.MagAtk + (1 * level)
        self.Def = self.Def + (1 * level)
        self.MagDef = self.MagDef + (1 * level)
        self.Spd = self.Spd + (1 * level)
        print(f'\n        Subiu {level} nível(eis)!')

    def __str__(self):
        return f'''
        Nome: {self.Nome}
        Classe: {self.Classe}
        Nível: {self.level}
        HP: {self.HP}
        Ataque: {self.Atk}
        Ataque Mágico: {self.MagAtk}
        Defesa Mágica: {self.MagDef}
        Defesa: {self.Def}
        Velocidade: {self.Spd}'''


class Inimigos:
    def __init__(self, Nome, HP, Atk, MagAtk, Def, MagDef, Spd, Xp):
        self.Nome = Nome
        self.HP = HP
        self.Atk = Atk
        self.MagAtk = MagAtk
        self.Def = Def
        self.MagDef = MagDef
        self.Spd = Spd
        self.Xp = Xp

    def __str__(self):
        return f'''
        Nome: {self.Nome}
        HP: {self.HP}
        Ataque: {self.Atk}
        Ataque Mágico: {self.MagAtk}
        Defesa: {self.Def}
        Defesa Mágica: {self.MagDef}
        Velocidade: {self.Spd}
        Experiência: {self.Xp}'''


class Armas:
    def __init__(self, Nome, Atk, MagAtk, Spd):
        self.Nome = Nome
        self.Atk = Atk
        self.MagAtk = MagAtk
        self.Spd = Spd

    def __str__(self):
        return f'''
        Nome da Espada: {self.Nome}
        Ataque: {self.Atk}
        Ataque Mágico: {self.MagAtk}
        Velocidade: {self.Spd}'''


class Armaduras:
    def __init__(self, Nome, Def, MagDef, Spd):
        self.Nome = Nome
        self.Def = Def
        self.MagDef = MagDef
        self.Spd = Spd
    
    def __str__(self):
        return f'''
        Nome da Armadura: {self.Nome}
        Defesa: {self.Def}
        Defesa Mágica: {self.MagDef}
        Velocidade: {self.Spd}'''


class Escudos:
    def __init__(self, Nome, Def, MagDef, Spd):
        self.Nome = Nome
        self.Def = Def
        self.MagDef = MagDef
        self.Spd = Spd
    
    def __str__(self):
        return f'''
        Nome do Escudo: {self.Nome}
        Defesa: {self.Def}
        Defesa Mágica: {self.MagDef}
        Velocidade: {self.Spd}'''
    

class Acessorios:
    def __init__(self, Nome, HP, Atk, Def, MagAtk, MagDef, Spd, Efeito):
        self.Nome = Nome
        self.HP = HP
        self.Atk = Atk
        self.Def = Def
        self.MagAtk = MagAtk
        self.MagDef = MagDef
        self.Spd = Spd
        self.Efeito = Efeito

    def __str__(self):
        return f'''
        Nome: {self.Nome}
        HP: {self.HP}
        Ataque: {self.Atk}
        Defesa: {self.Def}
        Ataque Mágico: {self.MagAtk}
        Defesa Mágica: {self.MagDef}
        Velocidade: {self.Spd}
        Efeito: {self.Efeito}'''


class Items:
    def __init__ (self, Nome, Efeito):
        self.Nome = Nome
        self.Efeito = Efeito

    def __str__(self):
        return f'{self.Efeito}'


def Menu():
    menu = '''
    ============ MENU PRINCIPAL ============
    
    1 - Criar Personagem
    
    2 - Criar Inimigos
    
    3 - Criar Armas
    
    4 - Criar Armaduras
    
    5 - Criar Escudos
    
    6 - Criar Acessórios
    
    7 - Criar Itens
    
    8 - Modo de Batalha
    
    Digite a opção desejada: '''

    return input(menu)

def Modo_de_batalha(Personagem, Inimigos):

    while Personagem.HP and Inimigos.HP > 0:
    
        if Personagem.Spd >= Inimigos.Spd:
            print(f'{Personagem.Nome} age primeiro.')
            opcao = input('''           1 - Atacar
            2 - Magia
            3 - Defender
            4 - Fugir
            Escolha a opção: ''')
            if opcao == 1:
                Dano = (random.randint(1, Personagem.Atk)) - Inimigos.Def
                return Dano
                if Dano > 0:
                    print(f'{Personagem.Nome} ataca, {Inimigos.Nome} perde {Dano} HP')
                    Inimigos.HP = Inimigos.HP - Dano
                    if Inimigos.HP <= 0:
                        print(f'{Inimigos.Nome} morreu.')
                        break
                    else:
                        Dano = (random.randint(1, Inimigos.Atk)) - Personagem.Def
                        return Dano
                    if Dano > 0:
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano} HP')
                        Personagem.HP = Personagem.HP - Dano
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
        else:
            print(f'{Inimigos.Nome} age primeiro.')
            Dano = (random.randint(1, Inimigos.Atk)) - Personagem.Def
            return Dano
            if Dano > 0:
                print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano} HP')
                Personagem.HP = Personagem.HP - Dano
                if Personagem.HP <= 0:
                    print(f'{Personagem.Nome} morreu.')
                    break
                else:
                    Dano = (random.randint(1, Personagem.Atk)) - Inimigos.Def
                    return Dano
                    if Dano > 0:
                        print(f'{Personagem.Nome} ataca, {Inimigos.Nome} perde {Dano} HP')
                        Inimigos.HP = Inimigos.HP - Dano
                        if Inimigos.HP <= 0:
                            print(f'{Inimigos.Nome} morreu.')
                            break

def main():
    barbaro1 = Personagem("Pedro", "Mago", 1, 12, 10, 2, 3, 5, 4)
    ragnarok = Armas("Ragnarok", 20, 15, 10)
    excalibur = Armas("Excalibur", 22, 20, 15)
    potion = Items("Poção", "Recupera 5 HP")
    armadura = Armaduras("Libra", 20, 20, 0)
    escudo = Escudos("Dragon Shield", 10, 8, 0)
    goblin = Inimigos("Goblin", 5, 3, 1, 2, 2, 3, 5)

    while True:

        opcao = Menu()

        if opcao == "8":
            Modo_de_batalha(barbaro1, goblin)


            

main()

# print(barbaro1)
# print(ragnarok)
# print(excalibur)
# print(armadura)
# print(escudo)
# barbaro1.Equipar_arma(excalibur)
# barbaro1.Equipar_armadura(armadura)
# barbaro1.Equipar_escudo(escudo)
# barbaro1.level_up(1)
# print(barbaro1)
# print(potion)
# print(goblin)