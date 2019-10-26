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
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index,pokemon))
        else:
            print("{} não tem pokemons :(\n".format(self))


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}\n".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Inimigo não tem pokemon")



    def batalhar(self, inimigo):
        print("{} iniciou uma batalha com {}\n".format(self, inimigo))

        inimigo.mostrar_pokemons()
        pokemon_inimigo = inimigo.escolher_pokemon()
        nosso_pokemon = self.escolher_pokemon()

        if nosso_pokemon and pokemon_inimigo:
            while True:
                vitoria = nosso_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    break

                vitoria_inimigo = pokemon_inimigo.atacar(nosso_pokemon)
                if vitoria_inimigo:
                    print("{} ganhou a batalha".format(inimigo))
                    break

        else:
            print("Essa batalha não pôde ocorrer\n")

class Player(Pessoa):
    tipo="player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}\n".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha= int(input("Escolha seu pokemon que irá pra rinha"))
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida\n")
        else:
            print("Você não tem pokemons\n")

class Inimigo(Pessoa):
    tipo="inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,3)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)


