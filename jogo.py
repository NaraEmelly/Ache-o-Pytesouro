import random 
from colorama import Fore, Back, Style, init
init(autoreset=True)

print(Fore.YELLOW +"""░█████████             ░██████████                                                                
░██     ░██                ░██                                                                    
░██     ░██ ░██    ░██     ░██     ░███████   ░███████   ░███████  ░██    ░██ ░██░████  ░███████  
░█████████  ░██    ░██     ░██    ░██    ░██ ░██        ░██    ░██ ░██    ░██ ░███     ░██    ░██ 
░██         ░██    ░██     ░██    ░█████████  ░███████  ░██    ░██ ░██    ░██ ░██      ░██    ░██ 
░██         ░██   ░███     ░██    ░██               ░██ ░██    ░██ ░██   ░███ ░██      ░██    ░██ 
░██          ░█████░██     ░██     ░███████   ░███████   ░███████   ░█████░██ ░██       ░███████  
                   ░██                                                                            
             ░███████                                                                             """)

print("")


def criar_tabuleiro(tamanho=5):
  return [["⬜"] * tamanho for _ in range(tamanho)]


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

  print(Back.BLUE +"Bem-vindo ao Caça ao Tesouro!")
  print(Back.BLUE +"Você terá 7 chances para encontrar o tesouro escondido")
  print(Back.BLUE +"Digite o número da linha e da coluna (0 a 4).")
  print()
  mostrar_tabuleiro(tabuleiro)

  for tentativa in range(1, tentativas + 1):
    try:
      linha = int(input(f"Tentativa {tentativas} - Escolha a Linha (0 a 4): "))
      coluna = int(input(f"Tentativa {tentativas} -  Escolha a Coluna (0 a 4): "))

      if linha == tesouro_linha and coluna == tesouro_coluna:
        print(Fore.GREEN + Style.BRIGHT +"""██    ██  ██████   ██████ ███████      ██████   █████  ███    ██ ██   ██  ██████  ██    ██        ██  
██    ██ ██    ██ ██      ██          ██       ██   ██ ████   ██ ██   ██ ██    ██ ██    ██     ██  ██ 
██    ██ ██    ██ ██      █████       ██   ███ ███████ ██ ██  ██ ███████ ██    ██ ██    ██         ██ 
 ██  ██  ██    ██ ██      ██          ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██    ██     ██  ██ 
  ████    ██████   ██████ ███████      ██████  ██   ██ ██   ████ ██   ██  ██████   ██████         ██  """)
        tabuleiro[linha][coluna] = "💰"
        mostrar_tabuleiro(tabuleiro)
        break
      else:
        print(Fore.RED +"Nada aqui. Continue procurando!\n")
        tabuleiro[linha][coluna] = "❌"
        mostrar_tabuleiro(tabuleiro)

    except ValueError:
      print(Fore.RED +"Entrada inválida. Digite números inteiros entre 0 a 4\n")
      continue

  else:
    print(Fore.RED +"""  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███     
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒   
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒   
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░   
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░    
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░        """)
    tabuleiro[tesouro_linha][tesouro_coluna] = "💰"
    print(Back.BLUE + "O tesouro estava aqui: \n")
    mostrar_tabuleiro(tabuleiro)

jogar()






