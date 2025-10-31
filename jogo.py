import random 
from colorama import Fore, Back, Style, init
init(autoreset=True)
import os
import time

print(Fore.YELLOW +"""░█████████             ░██████████                                                                
░██     ░██                ░██                                                                    
░██     ░██ ░██    ░██     ░██     ░███████   ░███████   ░███████  ░██    ░██ ░██░████  ░███████  
░█████████  ░██    ░██     ░██    ░██    ░██ ░██        ░██    ░██ ░██    ░██ ░███     ░██    ░██ 
░██         ░██    ░██     ░██    ░█████████  ░███████  ░██    ░██ ░██    ░██ ░██      ░██    ░██ 
░██         ░██   ░███     ░██    ░██               ░██ ░██    ░██ ░██   ░███ ░██      ░██    ░██ 
░██          ░█████░██     ░██     ░███████   ░███████   ░███████   ░█████░██ ░██       ░███████  
                   ░██                                                                            
             ░███████                                                                             """)
print(input("\n                        Prensione Enter para Jogar"))
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)


# def limpar_terminal():
#   os.system('cls' if os.name == 'nt' else 'clear')

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

  print(Back.BLUE +"\nPyTesouro!")
  print(Back.BLUE +"\nVocê terá 7 chances para encontrar o tesouro escondido")
  print(Back.BLUE +"Digite o número da linha e da coluna (0 a 4).")
  mostrar_tabuleiro(tabuleiro)

  for tentativa in range(1, tentativas + 1):
    try:
      linha = int(input(f" Escolha a Linha (0 a 4): "))
      coluna = int(input(f" Escolha a Coluna (0 a 4): "))

      if linha == tesouro_linha and coluna == tesouro_coluna:
        print(Fore.GREEN + Style.BRIGHT +"""\n██    ██  ██████   ██████ ███████      ██████   █████  ███    ██ ██   ██  ██████  ██    ██        ██  
██    ██ ██    ██ ██      ██          ██       ██   ██ ████   ██ ██   ██ ██    ██ ██    ██     ██  ██ 
██    ██ ██    ██ ██      █████       ██   ███ ███████ ██ ██  ██ ███████ ██    ██ ██    ██         ██ 
 ██  ██  ██    ██ ██      ██          ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██    ██     ██  ██ 
  ████    ██████   ██████ ███████      ██████  ██   ██ ██   ████ ██   ██  ██████   ██████         ██  """)
        tabuleiro[linha][coluna] = "💰"
        mostrar_tabuleiro(tabuleiro)
        break

      elif linha >= 5:
        print(Fore.RED +"\nNÚMERO INVÁLIDO DE LINHA TENTE (0 a 4)")
        continue
      

      elif coluna >= 5:
        print(Fore.RED +"\nNÚMERO INVÁLIDO DE COLUNA TENTE (0 a 4)")
        continue


      else:
        print(Fore.RED +"Nada aqui. Continue procurando!\n")
        tabuleiro[linha][coluna] = "❌"
        mostrar_tabuleiro(tabuleiro)

    except ValueError:
      print(Fore.RED +"Entrada inválida. Digite números inteiros entre 0 a 4\n")
      continue

  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED +"""\n  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███     
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒   
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒   
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄     
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒   
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░   
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░   
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░    
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░        """)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    tabuleiro[tesouro_linha][tesouro_coluna] = "💰"
    print(Back.BLUE + "O tesouro estava aqui: \n")
    mostrar_tabuleiro(tabuleiro)
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

    input("Pressione Enter para jogar novamente") 
    os.system('cls' if os.name == 'nt' else 'clear')
    jogar() 
  time.sleep(2)
 
   
jogar()






