"""
Nome: Jhonathan Alexandre Bueno
Curso: Análise e Desenvolvimento de Sistemas
"""


import random

# Selecionar os jogadores

jogadores = []

while True:
  nome_jogador = str(input("Digite seu nome (digite Start para começar o jogo): ")).upper()
  if nome_jogador != 'START':
    jogadores.append({"nome": nome_jogador, "cerebro": 0, "tiro": 0, "passo": 0})
  
  elif len(jogadores) < 2 and nome_jogador == 'START':
      print('ERRO! É necessário no mínimo 2 jogadores para iniciar.')

  else:
    break

# Variaveis

dado = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde', 'amarelo', 'amarelo', 'amarelo', 'amarelo', 'vermelho', 'vermelho', 'vermelho']
dado_verde = ('cerebro', 'passo', 'cerebro', 'tiro', 'passo', 'cerebro')
dado_amarelo = ('tiro', 'passo', 'cerebro', 'tiro', 'passo', 'cerebro')
dado_vermelho = ('tiro', 'passo', 'tiro', 'cerebro', 'passo', 'tiro')
jogador_atual_indice = 0

# Funções

def sortear_dado(dado):
    sortear = random.choice(dado)
    return sortear


def mostrar_menu():
    print('-'* 15)
    print("1. Jogar dados")
    print("2. Parar")
    print('-'* 15)

def comecar_rodada():
    return int(input("Escolha uma das opções: "))


def remover(dado):
    sortear = sortear_dado(dado)
    dado.remove(sortear)

# Sortear o lado dos dados

def dado_sorteado(dado_verde, dado_amarelo, dado_vermelho, cerebro, passo, tiro):
    sorteado = sortear_dado(dado)
    if sorteado == "verde":
        lado = random.choice(dado_verde)
        print(f"O dado caiu no {lado}")
        if lado == "cerebro":
            cerebro += 1
            print(f"Você está com {cerebro} cérebros")

        elif lado == "passo":
            passo += 1
            print(f"Você deu {passo} passos")

        else:
            tiro += 1
            print(f"Você levou {tiro} tiros")
        print('-'* 15)

    elif sorteado == "amarelo":
        lado = random.choice(dado_amarelo)
        print(f"O dado caiu no {lado}")
        if lado == "cerebro":
          cerebro += 1
          print(f"Você está com {cerebro} cérebros")

        elif lado == "passo":
          passo += 1
          print(f"Você deu {passo} passos")

        else:
          tiro += 1
          print(f"{tiro} tiros")      
          print(f"Você levou {tiro} tiros")
        print('-'* 15)


    else:
      lado = random.choice(dado_vermelho)
      print(f"O dado caiu no {lado}")
      if lado == "cerebro":
        cerebro += 1
        print(f"Você está com {cerebro} cérebros")

      elif lado == "passo":
        passo += 1
        print(f"Você deu {passo} passos")

      else:
        tiro += 1
        print(f"Você levou {tiro} tiros")     
      print('-'* 15)

    return cerebro, passo, tiro

def mostrar_dados(dado):
    print(f"Os dados disponíveis são {dado}")


def cor_sorteado():
    sortear = sortear_dado(dado)
    print(f"O dado sorteado foi {sortear}")


def mostrar_pontuacao(jogadores):
  for jogador in jogadores:
     print(f'O player {jogador["nome"]} está com {jogador["cerebro"]} cérebros, {jogador["passo"]} passos e {jogador["tiro"]} tiros!')


def jogador_venceu(jogador):
  return True if jogador["cerebro"] >= 13 else False


def proximo_jogador():
    global jogador_atual_indice
    if jogador_atual_indice >= len(jogadores) - 1:       
            jogador_atual_indice = 0
    else:
            jogador_atual_indice += 1
    print(f"O próximo jogador é {jogadores[jogador_atual_indice]['nome']}")


def resetar_dado():
  global dado
  dado = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde', 'amarelo', 'amarelo', 'amarelo', 'amarelo', 'vermelho', 'vermelho', 'vermelho']

# Programa Principal

while True:
    print('')
    mostrar_dados(dado)
    mostrar_pontuacao(jogadores)
    mostrar_menu()
    escolha = comecar_rodada()

# Aqui o jogador escolhe se vai jogar

    if escolha == 1:
      if len(dado) >= 3:
        for i in range(3):
            sortear_dado(dado)
            cor_sorteado()
            jogadores[jogador_atual_indice]['cerebro'], jogadores[jogador_atual_indice]['passo'], jogadores[jogador_atual_indice]['tiro'] = dado_sorteado(dado_verde, dado_amarelo, dado_vermelho, jogadores[jogador_atual_indice]["cerebro"], jogadores[jogador_atual_indice]['passo'], jogadores[jogador_atual_indice]['tiro'])
            remover(dado)
    
        if jogadores[jogador_atual_indice]["cerebro"] >= 13:
            print("*** ACABOU ***")
            print(f"Temos um vencedor: {jogadores[jogador_atual_indice]['nome']}")
            print("PARABÉNS :D")
            break

        if jogadores[jogador_atual_indice]["tiro"] >= 3:
            print(f'Acabou seu turno! Voce levou {jogadores[jogador_atual_indice]["tiro"]} tiros.')
            jogadores[jogador_atual_indice]["tiro"] = 0
            proximo_jogador()
            resetar_dado()
            continue

      else:
        print("Acabou os dados. Fim do turno!")
        jogadores[jogador_atual_indice]["tiro"] = 0
        proximo_jogador()
        resetar_dado()  
        continue

# Aqui o jogador escolhe se vai parar

    elif escolha == 2:
        print("Acabou seu turno!")
        resetar_dado()
        jogadores[jogador_atual_indice]["tiro"] = 0
        mostrar_pontuacao(jogadores)
        proximo_jogador()
        continue

# Esta mensagem irá aparecer caso o jogador digite outra coisa que não seja 1 ou 2

    else:
      print("ERRO! Tente novamente.")    