class Barbaro:
    def __init__(self, Nome, HitPoints, Atk, MagAtk, MagDef, Def, Spd):
        self.Nome = Nome
        self.HitPoints = HitPoints
        self.Atk = Atk
        self.MagAtk = MagAtk
        self.MagDef = MagDef
        self.Def = Def
        self.Spd = Spd

    
    def Equipar_arma(self, Atk, Spd):
        self.Atk = self.Atk + ragnarok.Atk
        self.Spd = self.Spd + ragnarok.Spd
        print(f'Equipou {ragnarok.Nome}')
        
    
    def __str__(self):
        return f'''Nome: {self.Nome}
        HP: {self.HitPoints}
        Ataque: {self.Atk}
        Ataque Mágico: {self.MagAtk}
        Defesa Mágica: {self.MagDef}
        Defesa: {self.Def}
        Velocidade: {self.Spd}'''


class Armas:
    def __init__(self, Nome, Atk, Spd):
        self.Nome = Nome
        self.Atk = Atk
        self.Spd = Spd

    def __str__(self):
        return f'''Nome da Espada: {self.Nome}
        Ataque: {self.Atk}
        Velocidade: {self.Spd}'''



barbaro1 = Barbaro("Pedro", 12, 10, 2, 3, 5, 4)
ragnarok = Armas("Ragnarok", 20, 10)


print(barbaro1)
print(ragnarok)
barbaro1.Equipar_arma(20, 10)
print(barbaro1)
