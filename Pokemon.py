import random
class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie
        if level:
            self.level=level
        else:
            self.level=random.randint(1,10)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = (20 + (self.level + 5))
        self.vida = (50 + (self.level + 15))


    def __str__(self):
        return "{} ({})".format(self.nome, self.level)

    def atacar(self, pokemon):
        dano = int((self.ataque * random.random() * 1.3))
        if self.tipo == 'fogo' and pokemon.tipo == 'eletrico':
            dano = int(dano * 1.5)
            print('ataque especial fogo')
        elif self.tipo == 'água' and pokemon.tipo == 'fogo':
            dano = int(dano * 1.5)
            print('ataque especial agua')
        elif self.tipo == 'elétrico' and pokemon.tipo == 'água':
            dano = int(dano * 1.5)
            print('ataque especial eletrico')

        pokemon.vida -= dano
        print("{} perdeu {} pontos de vida!".format(pokemon, dano))

        if pokemon.vida <= 0:
            print("{} foi derrotado".format(pokemon))
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = "elétrico"
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = "fogo"
    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo em {}".format(self, pokemon))
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = "água"
    def atacar(self, pokemon):
        print("{} lançou um jato d'água em {}".format(self, pokemon))
        return super().atacar(pokemon)
