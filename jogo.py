import random 

print(r"Bem-vindo ao Pytesouro!")


def criar_tabuleiro(tamanho=5):
  return [["_"] * tamanho for _ in range(tamanho)]


def mostrar_tabuleiro(tabuleiro):
  for linha in tabuleiro:
    print(" ".join(linha))
  print()

def jogar():
  tamanho = 5
  tentativas = 7
  tabuleiro = criar_tabuleiro(tamanho)

  tesouro_linha = random.randint(0, tamanho - 1)
  tesouro_coluna = random.randint(0, tamanho - 1)

  print("Bem-vindo ao Caça ao Tesouro!")
  print("Você terá 7 chances para encontrar o tesouro escondido")
  print("Digite o número da linha e da coluna (0 a 4).")
  print()
  mostrar_tabuleiro(tabuleiro)

  for tentativa in range(1, tentativas + 1):
    try:
      linha = int(input(f"Tentativa {tentativas} - Escolha a Linha (0 a 4): "))
      coluna = int(input(f"Tentativa {tentativas} -  Escolha a Coluna (0 a 4): "))

      if linha == tesouro_linha and coluna == tesouro_coluna:
        print("\nParabéns voce achou")
        tabuleiro[linha][coluna] = "T"
        mostrar_tabuleiro(tabuleiro)
        break
      else:
        print("Nada aqui. Continue procurando!\n")
        tabuleiro[linha][coluna] = "X"
        mostrar_tabuleiro(tabuleiro)

    except ValueError:
      print("Entrada inválida. Digite números inteiros entre 0 a 4\n")
      continue

  else:
    print("GAME OVER! Você não encontrou o tesouro...")
    tabuleiro[tesouro_linha][tesouro_coluna] = "T"
    print("O tesouro estava aqui: \n")
    mostrar_tabuleiro(tabuleiro)

jogar()






