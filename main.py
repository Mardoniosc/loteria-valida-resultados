import os
from loteria import resultados

RESULTADO_LOTOFACIL = []
RESULTADO_MEGASENA = [2, 5, 10, 29, 34, 44]
RESULTADO_LOTOMANIA = []


class Principal():
    def __init__(self):
        self.menuSistema()

    def menuSistema(self):
        os.system('clear') or None
        # Apresentação
        print("\n\n ## Olá meu nome é bigLoteria, sou um aplicativo de validação de resultado de jogos. ##\n\n")

        def optionGames():
            print("""
          Essas são minhas Opções até o momento:
          (1) = Resultados Jogos Lotofacil 
          (2) = Resultados Jogos LotoMania
          (3) = Resultados Jogos MegaSena
          (0) = Para SAIR
      """)

        optionGames()

        first_choice = input("Qual a função desejada? ")

        if first_choice == "0":
            print("\n\n *** Agradeço sua companhia e espero que tenha ajudado. ***")
            exit()

        elif first_choice == "1":
            self.validGamesLotofacil()

        elif first_choice == "2":
            self.validGamesLotoMania()

        elif first_choice == "3":
            self.validGamesMegaSena()

        else:
            self.menuSistema()

    def validGamesLotofacil(self):
        os.system('clear') or None
        print('\n\n ##### RESULTADO LOTOFACIL  ##### \n\n')
        tipo = 'lotofacil'
        nomeArquivo = 'Lotofacil'
        resultados(tipo, RESULTADO_LOTOFACIL, nomeArquivo)
        print('\n\n ########## LOTOFACIL  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuSistema()

    def validGamesLotoMania(self):
        os.system('clear') or None
        print('\n\n ##### RESULTADO LOTOMANIA  ##### \n\n')
        tipo = 'lotomania'
        nomeArquivo = 'Lotomania'
        resultados(tipo, RESULTADO_LOTOMANIA, nomeArquivo)
        print('\n\n ########## LOTOMANIA  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuSistema()

    def validGamesMegaSena(self):
        os.system('clear') or None
        print('\n\n ##### RESULTADO MEGA SENA  ##### \n\n')
        tipo = 'megasena'
        nomeArquivo = 'Megasena'
        resultados(tipo, RESULTADO_MEGASENA, nomeArquivo)
        print('\n\n ########## MEGA SENA  ########## \n\n')
        input('Pressione ENTER para continuar...')
        self.menuSistema()


if __name__ == "__main__":
    Principal()
