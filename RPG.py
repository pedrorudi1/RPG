import random


class Personagem:
    def __init__(self, Nome: str, Classe: str, level: int, HP: int, Atk: int, MagAtk: int, Def: int, MagDef: int,
                 Spd: int):
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
        self.Atk += Armas.Atk
        self.MagAtk += Armas.MagAtk
        self.Spd += Armas.Spd
        print(f'Equipou {Armas.Nome}')

    def Equipar_armadura(self, Armaduras):
        self.Def += Armaduras.Def
        self.MagDef += Armaduras.MagDef
        self.Spd += Armaduras.Spd
        print(f'Equipou {Armaduras.Nome}')

    def Equipar_escudo(self, Escudos):
        self.Def += Escudos.Def
        self.MagDef += Escudos.MagDef
        self.Spd += Escudos.Spd
        print(f'Equipou {Escudos.Nome}')

    def Equipar_acessorio(self, Acessorios):
        self.HP += Acessorios.HP
        self.Atk += Acessorios.Atk
        self.Def += Acessorios.Def
        self.MagAtk += Acessorios.MagAtk
        self.MagDef += Acessorios.MagDef
        self.Spd += Acessorios.Spd
        self.Efeito = Acessorios.Efeito

    def level_up(self, level):
        self.level = level + 1
        self.HP += (2 * level)
        self.Atk += (2 * level)
        self.MagAtk += (1 * level)
        self.Def += (1 * level)
        self.MagDef += (1 * level)
        self.Spd += (1 * level)
        print(f'\nSubiu {level} nível(eis)!')

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
    def __init__(self, Nome: str, HP: int, Atk: int, MagAtk: int, Def: int, MagDef: int, Spd: int, Xp: int):
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
    def __init__(self, Nome: str, Atk: int, MagAtk: int, Spd: int):
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
    def __init__(self, Nome: str, Def: int, MagDef: int, Spd: int):
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
    def __init__(self, Nome: str, Def: int, MagDef: int, Spd: int):
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
    def __init__(self, Nome: str, HP: int, Atk: int, Def: int, MagAtk: int, MagDef: int, Spd: int, Efeito: str):
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
    def __init__(self, Nome: str, Efeito: str):
        self.Nome = Nome
        self.Efeito = Efeito

    def __str__(self):
        return f'{self.Efeito}'


def MenuPrincipal():
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

    9 - Sair
    
    Digite a opção desejada: '''

    return input(menu)


def Modo_de_batalha(Personagem, Inimigos):
    while Personagem.HP and Inimigos.HP > 0:

        opcao = input('''
            1 - Atacar
            2 - Magia
            3 - Defender
            4 - Fugir
            Escolha a opção: ''')

        match opcao:
            case "1":
                Dano_inimigo = Ataque_Inimigo(Inimigos, Personagem)
                Dano_personagem = Ataque_Personagem(Personagem, Inimigos)
                if Inimigos.Spd > Personagem.Spd:
                    print(f'\n{Inimigos.Nome} age primeiro.')
                    if Dano_inimigo > 0:
                        Personagem.HP -= Dano_inimigo
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                        print(f'{Personagem.HP} restante.')
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
                    else:
                        print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')
                    if Dano_personagem > 0:
                        Inimigos.HP -= Dano_personagem
                        print(f'{Personagem.Nome} ataca, {Inimigos.Nome} perde {Dano_personagem} HP')
                        print(f'{Inimigos.HP} restante.')
                        if Inimigos.HP <= 0:
                            print(f'{Inimigos.Nome} morreu.')
                            break
                    else:
                        print(f'{Personagem.Nome} ataca... {Inimigos.Nome} defendeu.')
                else:
                    print(f'\n{Personagem.Nome} age primeiro.')
                    if Dano_personagem > 0:
                        Inimigos.HP -= Dano_personagem
                        print(f'{Personagem.Nome} ataca, {Inimigos.Nome} perde {Dano_personagem} HP')
                        print(f'{Inimigos.HP} restante.')
                        if Inimigos.HP <= 0:
                            print(f'{Inimigos.Nome} morreu.')
                            break
                    else:
                        print(f'{Personagem.Nome} ataca... {Inimigos.Nome} defendeu.')
                    if Dano_inimigo > 0:
                        Personagem.HP -= Dano_inimigo
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                        print(f'{Personagem.HP} restante.')
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
                    else:
                        print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')

            case "2":
                Dano_inimigo = Ataque_Inimigo(Inimigos, Personagem)
                Dano_personagem = Magia_Personagem(Personagem, Inimigos)
                if Inimigos.Spd > Personagem.Spd:
                    print(f'\n{Inimigos.Nome} age primeiro.')
                    if Dano_inimigo > 0:
                        Personagem.HP -= Dano_inimigo
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                        print(f'{Personagem.HP} restante.')
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
                    else:
                        print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')
                    if Dano_personagem > 0:
                        Inimigos.HP -= Dano_personagem
                        print(f'{Personagem.Nome} usa magia, {Inimigos.Nome} perde {Dano_personagem} HP')
                        print(f'{Inimigos.HP} restante.')
                        if Inimigos.HP <= 0:
                            print(f'{Inimigos.Nome} morreu.')
                            break
                    else:
                        print(f'{Personagem.Nome} usa magia... {Inimigos.Nome} desvia.')
                else:
                    print(f'\n{Personagem.Nome} age primeiro.')
                    if Dano_personagem > 0:
                        Inimigos.HP -= Dano_personagem
                        print(f'{Personagem.Nome} usa magia, {Inimigos.Nome} perde {Dano_personagem} HP')
                        print(f'{Inimigos.HP} restante.')
                        if Inimigos.HP <= 0:
                            print(f'{Inimigos.Nome} morreu.')
                            break
                    else:
                        print(f'{Personagem.Nome} usa magia... {Inimigos.Nome} desvia.')
                    if Dano_inimigo > 0:
                        Personagem.HP -= Dano_inimigo
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                        print(f'{Personagem.HP} restante.')
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
                    else:
                        print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')

            case "3":
                print(f'{Personagem.Nome} se defende.')
                Personagem.Def = int(Personagem.Def * 2)
                Personagem.MagDef = int(Personagem.MagDef * 2)
                Dano_inimigo = Ataque_Inimigo(Inimigos, Personagem)
                if Dano_inimigo > 0:
                    Personagem.HP -= Dano_inimigo
                    print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                    print(f'{Personagem.HP} restante.')
                    if Personagem.HP <= 0:
                        print(f'{Personagem.Nome} morreu.')
                        break
                else:
                    print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')
                Personagem.Def = int(Personagem.Def / 2)
                Personagem.MagDef = int(Personagem.MagDef / 2)

            case "4":
                fuga = random.randint(1, 5)
                if fuga >= 3:
                    print(f'{Personagem.Nome} fugiu.')
                    break
                else:
                    print(f'{Personagem.Nome} falhou na fuga.')
                    Dano_inimigo = Ataque_Inimigo(Inimigos, Personagem)
                    if Dano_inimigo > 0:
                        Personagem.HP -= Dano_inimigo
                        print(f'{Inimigos.Nome} ataca, {Personagem.Nome} perde {Dano_inimigo} HP')
                        print(f'{Personagem.HP} restante.')
                        if Personagem.HP <= 0:
                            print(f'{Personagem.Nome} morreu.')
                            break
                    else:
                        print(f'{Inimigos.Nome} ataca... {Personagem.Nome} defendeu.')

            case _:
                print(f'Opção inválida.')


def Ataque_Personagem(Personagem, Inimigos):
    Dano = random.randint(1, Personagem.Atk) - Inimigos.Def
    return Dano


def Magia_Personagem(Personagem, Inimigos):
    Dano = random.randint(1, Personagem.MagAtk) - Inimigos.MagDef
    return Dano


def Ataque_Inimigo(Inimigos, Personagem):
    acao_inimigo = random.randint(1, 2)
    if acao_inimigo == 1:
        Dano = random.randint(1, Inimigos.Atk) - Personagem.Def
        return Dano

    elif acao_inimigo == 2:
        Dano = random.randint(1, Inimigos.MagAtk) - Personagem.MagDef
        return Dano


def main():
    personagem = None
    inimigo = None

    while True:

        opcao = MenuPrincipal()

        match opcao:
            case "1":
                personagem = Personagem(Nome=str(input('Digite o nome do Personagem: ')),
                                        Classe=str(input('Digite a Classe do Personagem: ')),
                                        level=int(input('Digite o nível inicial do personagem: ')),
                                        HP=int(input('Digite o HP inicial do Personagem: ')),
                                        Atk=int(input('Digite o ataque inicial do Personagem: ')),
                                        MagAtk=int(input('Digite o Ataque Mágico do Personagem: ')),
                                        Def=int(input('Digite a defesa do personagem: ')),
                                        MagDef=int(input('Digite a Defesa Mágica do Personagem: ')),
                                        Spd=int(input('Digite a Velocidade do Personagem: ')))
                print(f'Personagem criado com sucesso.')
                print(personagem)

            case "2":
                inimigo = Inimigos(Nome=str(input('Digite o nome do Inimigo: ')),
                                   HP=int(input('Digite o HP inicial do Inimigo: ')),
                                   Atk=int(input('Digite o ataque inicial do Inimigo: ')),
                                   MagAtk=int(input('Digite o Ataque Mágico do Inimigo: ')),
                                   Def=int(input('Digite a defesa do Inimigo: ')),
                                   MagDef=int(input('Digite a Defesa Mágica do Inimigo: ')),
                                   Spd=int(input('Digite a Velocidade do Inimigo: ')),
                                   Xp=int(input('Digite a quantidade de Experiência que o Inimigo tem: ')))
                print(f'Inimigo criado com sucesso.')
                print(inimigo)

            case "3":
                arma = Armas(Nome=str(input('Digite o nome da arma: ')),
                             Atk=int(input('Digite a força de ataque da arma: ')),
                             MagAtk=int(input('Digite a força de ataque mágico da arma: ')),
                             Spd=int(input('Digite o bônus de velocidade da arma: ')))
                print(f'Arma criada com sucesso.')
                print(arma)

            case "4":
                armadura = Armaduras(Nome=str(input('Digite o nome da armadura: ')),
                                     Def=int(input('Digite a força de defesa da armadura: ')),
                                     MagDef=int(input('Digite a força de defesa mágica da armadura: ')),
                                     Spd=int(input('Digite o bônus de velocidade da armadura: ')))
                print(f'Armadura criada com sucesso.')
                print(armadura)

            case "5":
                escudo = Escudos(Nome=str(input('Digite o nome do escudo: ')),
                                 Def=int(input('Digite a força de defesa do escudo: ')),
                                 MagDef=int(input('Digite a força de defesa mágica do escudo: ')),
                                 Spd=int(input('Digite o bônus de velocidade do escudo: ')))
                print(f'Escudo criado com sucesso.')
                print(escudo)

            case "6":
                acessorio = Acessorios(Nome=str(input('Digite o nome do acessório: ')),
                                       HP=int(input('Digite o bônus de HP do acessório: ')),
                                       Atk=int(input('Digite o bônus de ataque do acessório: ')),
                                       Def=int(input('Digite o bônus de defesa do acessório: ')),
                                       MagAtk=int(input('Digite o bônus de ataque mágico do acessório: ')),
                                       MagDef=int(input('Digite o bônus de Defesa Mágica do acessório: ')),
                                       Spd=int(input('Digite o bônus de velocidade da arma: ')),
                                       Efeito=str(input('Digite o efeito do acessório: ')))
                print(f'Acessório criado com sucesso.')
                print(acessorio)

            case "7":
                item = Items(Nome=str(input('Digite o nome da arma: ')),
                             Efeito=str(input('Digite o efeito do item: ')))
                print(f'Item criado com sucesso.')
                print(item)

            case "8":
                if personagem is None:
                    print(f'Necessário criar personagem primeiro.')
                if inimigo is None:
                    print(f'Necessário criar inimigo primeiro.')
                else:
                    Modo_de_batalha(personagem, inimigo)

            case "9":
                break

            case _:
                print('Opção inválida.')


main()
