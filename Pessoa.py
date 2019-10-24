from pokemon import *
import random

NOMES=["Dahaka", "Silverdick", "Trandor", "Alain", "Habbit", "Mirra", "Crystal",
           "Sharon", "Mia", "pifsa", "Anônimo", "Azog", "Meklan", "Phara"
    ]

POKEMONS =[
    PokemonFogo("charmander"),
    PokemonFogo("flarion"),
    PokemonFogo("charmilion"),
    PokemonFogo("charizard"),
    PokemonEletrico("pikachu"),
    PokemonEletrico("raichu"),
    PokemonAgua("squirtle"),
    PokemonAgua("magicarp"),
    PokemonAgua("bubasauro"),
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):#como podemos ter vários pokemons, então tem que ser uma lista
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print("{} não tem pokemons :(".format(self))

class Player(Pessoa):
    tipo="player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}:".format(self, pokemon))

class Inimigo(Pessoa):
    tipo="inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,3)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

meu_pokemon=PokemonEletrico("pakachu")
meu_pokemon2=PokemonFogo("charmander")
eu = Player(nome="Gabriel", pokemons=[meu_pokemon, meu_pokemon2])
pokemon_selvagem=PokemonAgua("bubasauro")
eu.mostrar_pokemons()
eu.capturar(pokemon_selvagem)
eu.mostrar_pokemons()

meu_inimigo=Inimigo()
print(meu_inimigo)
meu_inimigo.mostrar_pokemons()
