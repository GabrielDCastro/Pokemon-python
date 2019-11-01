from pokemon import *
from Pessoa import *
from loja import *


def escolher_pokemon_inicial(player):
    print("Olá {}, escolha um pokemon para iniciar sua jornada\n".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possue 3 escolhas")
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
        else:            print("Escolha inválida")



if __name__ == "__main__":
    print("Bem vindo ao Pokemon RPG de texto")
    nome = input("Qual vai ser seu nome?")
    player = Player(nome)
    print("Objetivo é ser um mestre pokemon e lutar com geral")

    if player.pokemons:
        print("Já vi que possui Pokemon")
    else:
        escolher_pokemon_inicial(player)

    print("Vamos fazer uma primeira luta para se abtuar. Seu oponente sera o gary")
    gary = Inimigo(nome="Gary sonolento", pokemons=[PokemonAgua("squirtle", level=1)])
    player.batalhar(gary)
    while True:
        print("____________________________________________")
        print("O que deseja fazer?")
        print("1 - Explorar a procura de novos pokemons")
        print("2 - Lutar com um inimigo")
        print("3 - Mostrar sues pokemons")
        print("4 - Mostrar dineiro")
        print("5 - Ir a loja")
        print("0 - Sair do jogo")
        escolha = input("")
        print("____________________________________________")

        if escolha == '0':
            print("Saindo do jogo...")
            break
        elif escolha == '1':
            player.explorar()
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
        elif escolha == '3':
            player.mostrar_pokemons()
        elif escolha == "4":
            player.mostrar_dinheiro()
        elif escolha == "5":
            while True:
                lista= []
                pokemon1 = random.choice(POKEMONS)
                valor1 = pokemon1.level * 500
                pokemon2 = random.choice(POKEMONS)
                valor2 = pokemon2.level * 500
                pokemon3 = random.choice(POKEMONS)
                valor3 = pokemon3.level * 500
                print("1 - {} ${}\n2- {} ${}\n3 - {} ${}".format(pokemon1, valor1 , pokemon2, valor2, pokemon3, valor3))
                print("Deseja comprar algum? (s/n)")
                escolha_compra = input()
                if escolha_compra == 'n':
                    break
                elif escolha_compra == 's':
                    compra= input("Qual deseja comprar?")
                    if compra == "1" and player.dinheiro >= valor1:
                        player.capturar(pokemon1)
                        player.dinheiro -= valor1
                    if compra == "2" and player.dinheiro >= valor2:
                        player.capturar(pokemon2)
                        player.dinheiro -= valor2
                    if compra == "3" and player.dinheiro >= valor3:
                        player.capturar(pokemon3)
                        player.dinheiro -= valor3
                    else:
                        print("Dinheiro insuficiente")


