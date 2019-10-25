from pokemon import *
from Pessoa import *
nome=input("Seja bem vindo, Player! Qual o seu nome?")

def escolher_pokemon_inicial(player):
    print("Olá {}, escolha um pokemon para iniciar sua jornada".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possue 3 esxolhas")
    print("1 - ",pikachu)
    print("2 - ",charmander)
    print("3 - ",squirtle)

    while True:
        escolha = input("Escolha seu pokemon")

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida")

player = Player(nome=nome)
player.capturar(PokemonFogo("Charmander", level=1))
#escolher_pokemon_inicial(player)
inimigo1 = Inimigo(nome="gary sonolento", pokemons=[PokemonAgua("Golduck", level=1)] )
player.batalhar(inimigo1)
