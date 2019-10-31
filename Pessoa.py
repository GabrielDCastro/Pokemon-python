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
    PokemonFogo("blaziken"),
    PokemonFogo("houndoom"),
    PokemonEletrico("pikachu"),
    PokemonEletrico("helioptile"),
    PokemonEletrico("raichu"),
    PokemonEletrico("elekid"),
    PokemonEletrico("electrike"),
    PokemonEletrico("pichu"),
    PokemonAgua("squirtle"),
    PokemonAgua("magicarp"),
    PokemonAgua("bubasauro"),
    PokemonAgua("totodile"),
    PokemonAgua("gyarados"),
    PokemonAgua("empoleon"),
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):#como podemos ter vários pokemons, então tem que ser uma lista
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index,pokemon))
            print("")
        else:
            print("{} não tem pokemons :(\n".format(self))


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}\n".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Inimigo não tem pokemon")


    def mostrar_dinheiro(self):
        print("Você possui ${}".format(self.dinheiro))
        print("")

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, inimigo):
        print("{} iniciou uma batalha com {}\n".format(self, inimigo))

        inimigo.mostrar_pokemons()
        pokemon_inimigo = inimigo.escolher_pokemon()
        nosso_pokemon = self.escolher_pokemon()

        if nosso_pokemon and pokemon_inimigo:
            while True:
                vitoria = nosso_pokemon.atacar(pokemon_inimigo)
                print("")
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level *100)
                    nosso_pokemon.level += 1
                    if nosso_pokemon.level >=100:
                        nosso_pokemon.level = 100
                    break

                vitoria_inimigo = pokemon_inimigo.atacar(nosso_pokemon)
                if vitoria_inimigo:
                    print("{} ganhou a batalha".format(inimigo))
                    break

        else:
            print("Essa batalha não pôde ocorrer\n")

    def batalhar_pokemon(self, inimigo):
        print("{} iniciou uma batalha com {}\n".format(self, inimigo))

        pokemon_inimigo = inimigo
        nosso_pokemon = self.escolher_pokemon()

        if nosso_pokemon and pokemon_inimigo:
            while True:
                vitoria = nosso_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.capturar(inimigo)
                    nosso_pokemon.level +=1
                    break

                vitoria_inimigo = pokemon_inimigo.atacar(nosso_pokemon)
                if vitoria_inimigo:
                    print("{} ganhou a batalha. Não foi possível captura-lo".format(inimigo))
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
                    escolha= int(input("Escolha seu pokemon que irá para a luta"))
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida\n")
        else:
            print("Você não tem pokemons\n")

    def explorar(self):
        if random.random() <=0.65:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu: {}".format(pokemon))

            escolha = input("Deseja lutar ? (s/n): ")
            if escolha == "s":
                self.batalhar_pokemon(pokemon)
        else:
            print("Essa exploração não deu em nada")

class Inimigo(Pessoa):
    tipo="inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemon_aleatorio = []
            for i in range(random.randint(1,3)):
                pokemon_aleatorio.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemon_aleatorio)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
