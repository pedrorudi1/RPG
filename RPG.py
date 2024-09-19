class Personagem:
    def __init__(self, Nome, Classe, HP, Atk, MagAtk, Def, MagDef, Spd):
        self.Nome = Nome
        self.Classe = Classe
        self.HitPoints = HP
        self.Atk = Atk
        self.MagAtk = MagAtk
        self.Def = Def
        self.MagDef = MagDef
        self.Spd = Spd

    
    def Equipar_arma(self, Armas):
        self.Atk = self.Atk + ragnarok.Atk
        self.MagAtk = self.MagAtk + ragnarok.MagAtk
        self.Spd = self.Spd + ragnarok.Spd
        print(f'Equipou {ragnarok.Nome}')
        
    
    def __str__(self):
        return f'''
        Nome: {self.Nome}
        Classe: {self.Classe}
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
        

barbaro1 = Personagem("Pedro", "Mago", 12, 10, 2, 3, 5, 4)
ragnarok = Armas("Ragnarok", 20, 15, 10)
potion = Items("Poção", "Recupera 5 HP")


print(barbaro1)
print(ragnarok)
barbaro1.Equipar_arma(ragnarok)
print(barbaro1)
print(potion)