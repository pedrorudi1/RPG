class Personagem:
    def __init__(self, Nome, Classe, level, HP, Atk, MagAtk, Def, MagDef, Spd):
        self.Nome = Nome
        self.Classe = Classe
        self.level = level
        self.HitPoints = HP
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
    
    def level_up(self, level):
        self.level = level + 1
        self.HitPoints = self.HitPoints + (2 * level)
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
        HP: {self.HitPoints}
        Ataque: {self.Atk}
        Ataque Mágico: {self.MagAtk}
        Defesa Mágica: {self.MagDef}
        Defesa: {self.Def}
        Velocidade: {self.Spd}'''


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
    

class Items:
    def __init__ (self, Nome, Efeito):
        self.Nome = Nome
        self.Efeito = Efeito

    def __str__(self):
        return f'{self.Efeito}'
        

barbaro1 = Personagem("Pedro", "Mago", 1, 12, 10, 2, 3, 5, 4)
ragnarok = Armas("Ragnarok", 20, 15, 10)
excalibur = Armas("Excalibur", 22, 20, 15)
potion = Items("Poção", "Recupera 5 HP")
armadura = Armaduras("Libra", 20, 20, 0)
escudo = Escudos("Dragon Shield", 10, 8, 0)

print(barbaro1)
# print(ragnarok)
# print(excalibur)
# print(armadura)
# print(escudo)
# barbaro1.Equipar_arma(excalibur)
# barbaro1.Equipar_armadura(armadura)
# barbaro1.Equipar_escudo(escudo)
barbaro1.level_up(99)
print(barbaro1)
# print(potion)