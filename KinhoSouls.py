import pygame
import emoji
import math
from time import sleep
from random import choice , randint

# Sorteando o que encontrar no caminho 
caminhos = ["Penhasco", "Caminho vazio", "Buraco"]
inimigo = ["Inimigo Forte" , "Inimigo Fraco"]
          
inimigo_ou_livre = choice(caminhos + inimigo)

# Seleção de personagens
print()
print("-_-"*20)
print('Bem - Vindo a KINHO SOULS')
print('Escolha sua Classe')
print("-_-"*20)
print()
print('[1] - Guerreiro')
print('[2] - Mago')
print('[3] - Samurai')
print('[4] - Barbaro')
print()
menu_de_personagem = str(input("Escolha seu personagem: "))
print()

# exibir nome das classes
if menu_de_personagem == "1":
    menu_de_personagem = "Guerreiro"

elif menu_de_personagem == "2":
    menu_de_personagem = "Mago"

elif menu_de_personagem == "3":
    menu_de_personagem = "Samurai"

elif menu_de_personagem == "4" :
    menu_de_personagem = "Barbaro"

# O Beneficos de cada Classe
if menu_de_personagem == "Guerreiro" : 
    
    print("você escolheu guerreiro\n")
    sleep(0.5)
    print('''A classe Guerreiro possui

40% de resistencia a dano fisico.
10% de resistencia a dano magico.
20% a mais de poder de ataque.\n''')
    
elif menu_de_personagem == "Mago":
        print("Você escolheu mago\n")
        sleep(0.5)
        print('''A classe Mago possui

60% de resistencia a dano magico
10% resistência a dano fisico
20% a mais de poder de ataque mágico.\n
''')

elif menu_de_personagem == "Samurai":
     print("Você escolheu a classe Samurai\n")
     sleep(0.5)
     print('''A classe samurai possui

21% de resistencia a dano magico
14% de resistencia a dano fisico
20% a mais de poder de ataque\n''')
     
elif menu_de_personagem == "Barbaro" :
     print("Você escolheu a classe Barbaro\n")
     sleep(0.5)
     print('''A classe Barbaro possui

5% de resistencia a dano magico
40% de resistencia a dano fisico
30% a mais de poder de ataque\n''')

else:
    print("Escolha uma opção válida !!\n")

    for menu in range(3):
         print()
         print("-_-"*20)
         print('Bem - Vindo a KINHO SOULS')
         print('Escolha sua Classe')
         print("-_-"*20)
         print()
         print('[1] - Guerreiro')
         print('[2] - Mago')
         print('[3] - Samurai')
         print('[4] - Barbaro')
         menu_de_personagem = str(input("Escolha seu personagem: "))

         if menu_de_personagem == "1" : 
            print("você escolheu guerreiro\n")
            sleep(0.5)
            print('''A classe Guerreiro possui

40% de resistencia a dano fisico.
10% de resistencia a dano magico.
20% a mais de poder de ataque.\n''')
            break
    
         elif menu_de_personagem == "2":
            print("Você escolheu Mago\n")
            sleep(0.5)
            print('''A classe Guerreiro possui

60% de resistencia a dano magico
10% resistência a dano fisico
20% a mais de poder de ataque mágico.\n
''')
            break

         elif menu_de_personagem == "3":
            print("Você escolheu a classe Samurai\n")
            sleep(0.5)
            print('''A classe samurai possui

21% de resistencia a dano magico
14% de resistencia a dano fisico
20% a mais de poder de ataque\n''')
            break
     
         elif menu_de_personagem == "4" :
            print("Você escolheu a classe Barbaro\n")
            sleep(0.5)
            print('''A classe Barbaro possui

5% de resistencia a dano magico
40% de resistencia a dano fisico
30% a mais de poder de ataque\n''')
            break

# Exibir nome das classes
if menu_de_personagem == "1":
    menu_de_personagem = "Guerreiro"

elif menu_de_personagem == "2":
    menu_de_personagem = "Mago"

elif menu_de_personagem == "3":
    menu_de_personagem = "Samurai"

elif menu_de_personagem == "4" :
    menu_de_personagem = "Barbaro"

sleep(0.7)

# Escolha de caminhos a seguir
print()
print("-_-"*20)
print('Na sua frente há dois caminhos, Qual deseja seguir ?')
print("-_-"*20)
print()
print('[1] - Esquerda')
print('[2] - Direita')
print()

direcao = str(input('Qual caminho seguir? ')).lower()
sleep(0.7)
print()
# Dando valor a direcao
if direcao == "1":
    direcao = "Esquerda"

elif direcao == "2":
    direcao = "Direita"

while True:

    # Sorteando o que encontrar no caminho
    caminhos = ["Penhasco", "Caminho vazio", "Buraco"]
    inimigo = ["Inimigo Forte" , "Inimigo Fraco"]
    inimigo_ou_livre = choice(caminhos + inimigo)
    sleep(0.7)

    # Variaveis de Caminhos
    if direcao == "Esquerda":

        if inimigo_ou_livre not in caminhos:
            print(f'Você entrou a {direcao} e encontrou um {inimigo_ou_livre}\n')

        # Sorteando novamente se o valor sorteado estiver em caminhos
        if inimigo_ou_livre in caminhos :
            print(f'''Você entrou a {direcao} e encontrou um {inimigo_ou_livre} e decidiu voltar pois impedia sua passagem
Ao voltar, você encontrou outros caminhos. Qual você vai escolher?
[1] - Esquerda
[2] - Direita\n''')
            direcao = str(input("Qual deseja seguir? "))
            sleep(0.7)
            print()

            #Dando valor a direcao
            if direcao == "1":
                direcao = "Esquerda"
            elif direcao == "2":
                direcao = "Direita"

            else:
                print("Você tentou seguir um caminho que não existe")
                sleep(0.4)
                direcao = str(input('''
                [1] - Esquerda
                [2] - Direita
                Qual deseja seguir? '''))
        else:
            break

    elif direcao == "Direita":
        if inimigo_ou_livre not in caminhos:
            print(f'Você entrou a {direcao} e encontrou um {inimigo_ou_livre}\n')
        sleep(0.7)
        print()

        # Sorteando novamente se o valor sorteado estiver em caminhos
        if inimigo_ou_livre in caminhos :
                print(f'''Você entrou a {direcao} e encontrou um {inimigo_ou_livre} e decidiu voltar pois impedia sua passagem
Ao voltar, você encontrou outros caminhos. Qual você vai escolher?
[1] - Esquerda
[2] - Direita''')
                direcao = str(input("Qual deseja seguir? "))
                sleep(0.7)
                print()

                 # Dando valor a direcao
                if direcao == "1":
                    direcao = "Esquerda"

                elif direcao == "2":
                    direcao = "Direita"
                else:
                    print("Você tentou seguir um caminho que não existe")
                    sleep(0.4)
                    direcao = str(input('''
                    [1] - Esquerda
                    [2] - Direita
                    Qual deseja seguir? '''))
        else :
            break
    # Se a opção digitada não corresponder
    else :
        print("opção inválida. Escolha um caminho válido\n")

        direcao = str(input("Qual caminho deseja seguir ?"))
        sleep(0.7)
        print()

        # Dando valor a direcao
        if direcao == "1":
            direcao = "Esquerda"

        elif direcao == "2":
            direcao = "Direita"

# Escolhas de combate
print()
print("-_-"*20)
print(f'''Um {inimigo_ou_livre} te desafiou para a batalha
Você vai aceitar ou não ?\n''')
print('I AI qual vai ser ?\n')
print("-_-"*20)
print()
print('[1] - Aceitar Combate')
print('[2] - Recusar combate\n')
escolha_combate = str(input("Faça sua decisão: "))
sleep(0.7)
print()



# Loop de repetição
while True :
    inimigo = ["Inimigo Forte" , "Inimigo Fraco"]
    inimigo_em_caminho = choice(inimigo)

    #Dando valor a escolha_combate
    if escolha_combate == "1":
        escolha_combate = "Aceitar Combate"
        
    elif escolha_combate == "2":
        escolha_combate = "Recusar Combate"

# variaveis de escolha
    if escolha_combate == "Aceitar Combate":
        print(f'''Você decidiu {escolha_combate} contra {inimigo_ou_livre}''')
        print()
        break

    elif escolha_combate == "Recusar Combate":
        print(f'''Você decidiu {escolha_combate} e decidiu desviar do inimigo\n
Ao seguir o caminho você encontra uma passagem estranha, você fica pensativo e pensa se vai entrar ou não.''')
        print('''
    [1] - Você decide entrar
    [2] - Você decide fugir\n''')
    entrar_ou_nao = input("O que você vai escolher ? ")
    print()

    if entrar_ou_nao == "1":
        entrar_ou_nao = "Você decide entrar"
    elif entrar_ou_nao == "2":
        entrar_ou_nao = "Você decide fugir"
        
    if entrar_ou_nao == "Você decide fugir":
        print(f'Você decide fugir, ao fugir você encontra um caminho.\nAo entrar você se depara com um {inimigo_em_caminho}\n')
        sleep (0.5)

        if escolha_combate == "1":
            escolha_combate = "Você decide entrar"
        
        if escolha_combate == "2":
            escolha_combate = "Você decide fugir"


    else:
        print('''O inimigo nao aceitou isso como resposta\n
de uma resposta certa ao inimigo.
\n''')
    
    break


print('O inimigo já está pronto para o combate')

inicio = 1
fim = 6

for tempo in range(inicio , fim-2, -1):
    print(f'''A batalha começará em \n
    ''')
    if tempo > 1 :
        print(f'{tempo} Segundos')
    else:
        print(f'{tempo} Segundo')
    
    for tempo in range(1):
        sleep(1)


#  Vida do player e do inimigo
vida_player = 50
vida_inimigo = 50

while vida_player < 0 or vida_inimigo < 0:
    
    #Mostar as opçoes de ação
    print('-_-' * 20)
    print()
    print('''Escolha seu movimento a seguir
    [1] - Atacar
    [2] - Defender''')
    print('-_-' * 20)
    print()
    sleep(1)

    #Obter a acao do jogador
    acao_de_combate = str(input('O que vai ser ? '))

    #Verificar a acao do jogador
    if acao_de_combate == '1':
        acao_de_combate = "Atacar"

    elif acao_de_combate == '2':
        acao_de_combate = "Defender"

    #Sortear acao do inimigo
    dano_player = randint(10,30)
    dano_inimigo = randint(10,30)

    #Calcular a resistencia fisica do jogador
    resistencia_fisico_player = 0
    if menu_de_personagem == "Guerreiro":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 40 / 100)

    elif menu_de_personagem == "Mago":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 10 /100)

    elif menu_de_personagem == "Samurai":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 14 / 100)

    elif menu_de_personagem == "Barbaro":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 40 / 100)

    dano_sofrido_player = dano_inimigo - resistencia_fisico_player

    # Calcular a resistencia fisica do Inimigo
    resistencia_fisico_inimigo = 0
    if inimigo_ou_livre == "Inimigo Fraco" or inimigo_em_caminho == "Inimigo Fraco":
        resistencia_fisico_inimigo = dano_player - (dano_player * 20 / 100)
    
    elif inimigo_ou_livre == "Inimigo Forte" or inimigo_em_caminho == "Inimigo Forte":
        resistencia_fisico_inimigo = dano_player - (dano_player * 35 / 100)

    dano_sofrido_inimigo = dano_player - resistencia_fisico_inimigo

    # Sorteando combate ou defesa do inimigo
    acao_do_inimigo = choice(["Atacar","Defender"])

    if acao_de_combate == "Defender" and acao_do_inimigo == "Defender":
        print(f'Não houve dano pois ambos resolveram {acao_de_combate}.')

        sleep(2)
        print()

    elif acao_de_combate == "Atacar" and acao_do_inimigo == "Defender":
        print(f'''Você decidiu {acao_de_combate} e o inimigo decidiu {acao_do_inimigo}.
        \nSendo assim o dano causado foi de {dano_sofrido_inimigo:.2f}''')

        vida_inimigo -= dano_sofrido_inimigo
        print(f'A vida atual do inimigo é de {vida_inimigo:.2f}')

        if dano_sofrido_inimigo <0:
            print('O dano foi 0 ')

        sleep(2)
        print()

    elif acao_de_combate == "Defender" and acao_do_inimigo == "Atacar":
        print(f'''Você decidiu {acao_de_combate} e o inimigo decidiu {acao_do_inimigo}.
        \nSendo assim o dano foi de {dano_sofrido_player:.2f}
        Sua vida atual é de {vida_player:.2f}''')
        vida_player -= dano_sofrido_player

        sleep(2)
        print()

    elif acao_de_combate == "Atacar" and acao_do_inimigo == "Atacar" :
        print(f'''Os dois decidiram {acao_de_combate}.
        Então ambos sofreram dano, o dano sofrido foi de {dano_sofrido_player:.2f} 
        E o dano causado foi de {dano_sofrido_inimigo:.2f}''')

        vida_player -= dano_sofrido_player
        vida_inimigo -= dano_sofrido_inimigo
        print(f'''Sua vida atual é de {vida_player:.2f}.
        A vida atual do inimigo é de {vida_inimigo:.2f}.''')

        if dano_sofrido_inimigo <0 or dano_sofrido_player <0 :
            print('O dano foi 0 ')

        sleep(2)
        print()

    if vida_player <=0:
        print(f'Você morreu')
        break

    elif vida_inimigo <=0:
        print(f'O {inimigo_ou_livre or inimigo_em_caminho} CAIU !')
        break


# Loop de repetição
while True :
    inimigo = ["Inimigo Forte" , "Inimigo Fraco"]
    inimigo_em_caminho = choice(inimigo)

    #Dando valor a escolha_combate
    if escolha_combate == "1":
        escolha_combate = "Aceitar Combate"
        
    elif escolha_combate == "2":
        escolha_combate = "Recusar Combate"

# variaveis de escolha
    if escolha_combate == "Aceitar Combate":
        print(f'''Você decidiu {escolha_combate} contra {inimigo_ou_livre}''')
        print()
        break

    elif escolha_combate == "Recusar Combate":
        print(f'''Você decidiu {escolha_combate} e decidiu desviar do inimigo\n
Ao seguir o caminho você encontra uma passagem estranha, você fica pensativo e pensa se vai entrar ou não.''')
        print('''
    [1] - Você decide entrar
    [2] - Você decide fugir\n''')
    entrar_ou_nao = input("O que você vai escolher ? ")
    print()

    if entrar_ou_nao == "1":
        entrar_ou_nao = "Você decide entrar"
    elif entrar_ou_nao == "2":
        entrar_ou_nao = "Você decide fugir"
        
    if entrar_ou_nao == "Você decide fugir":
        print(f'Você decide fugir, ao fugir você encontra um caminho.\nAo entrar você se depara com um {inimigo_em_caminho}\n')
        sleep (0.5)

        if escolha_combate == "1":
            escolha_combate = "Você decide entrar"
        
        if escolha_combate == "2":
            escolha_combate = "Você decide fugir"


    else:
        print('''O inimigo nao aceitou isso como resposta\n
de uma resposta certa ao inimigo.
\n''')
    
    break



print('O inimigo já está pronto para o combate')

inicio = 1
fim = 6
for tempo in range(inicio , fim-2, -1):
    print(f'''A batalha começará em \n
    ''')
    if tempo > 1 :
        print(f'{tempo} Segundos')
    else:
        print(f'{tempo} Segundo')
    
    for tempo in range(1):
        sleep(1)


#  Vida do player e do inimigo
vida_player = 10
vida_inimigo = 10

while vida_player > 1 and vida_inimigo > 1:
    
    #Mostar as opçoes de ação
    print('-_-' * 20)
    print()
    print('''Escolha seu movimento a seguir
    [1] - Atacar
    [2] - Defender''')
    print('-_-' * 20)
    print()
    sleep(1)

    #Obter a acao do jogador
    acao_de_combate = str(input('O que vai ser ? '))

    #Verificar a acao do jogador
    if acao_de_combate == '1':
        acao_de_combate = "Atacar"

    elif acao_de_combate == '2':
        acao_de_combate = "Defender"

    #Sortear acao do inimigo
    dano_player = randint(10,30)
    dano_inimigo = randint(10,30)

    #Calcular a resistencia fisica do jogador
    resistencia_fisico_player = 0
    if menu_de_personagem == "Guerreiro":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 40 / 100)

    elif menu_de_personagem == "Mago":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 10 /100)

    elif menu_de_personagem == "Samurai":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 14 / 100)

    elif menu_de_personagem == "Barbaro":
        resistencia_fisico_player = dano_inimigo - (dano_inimigo * 40 / 100)

    dano_sofrido_player = dano_inimigo - resistencia_fisico_player

    # Calcular a resistencia fisica do Inimigo
    resistencia_fisico_inimigo = 0
    if inimigo_ou_livre == "Inimigo Fraco" or inimigo_em_caminho == "Inimigo Fraco":
        resistencia_fisico_inimigo = dano_player - (dano_player * 20 / 100)
    
    elif inimigo_ou_livre == "Inimigo Forte" or inimigo_em_caminho == "Inimigo Forte":
        resistencia_fisico_inimigo = dano_player - (dano_player * 35 / 100)

    dano_sofrido_inimigo = dano_player - resistencia_fisico_inimigo

    # Sorteando combate ou defesa do inimigo
    acao_do_inimigo = choice(["Atacar","Defender"])

    if acao_de_combate == "Defender" and acao_do_inimigo == "Defender":
        print(f'Não houve dano pois ambos resolveram {acao_de_combate}.')

        sleep(2)
        print()

    elif acao_de_combate == "Atacar" and acao_do_inimigo == "Defender":
        print(f'''Você decidiu {acao_de_combate} e o inimigo decidiu {acao_do_inimigo}.
        \nSendo assim o dano causado foi de {dano_sofrido_inimigo:.2f}''')

        vida_inimigo -= dano_sofrido_inimigo
        print(f'A vida atual do inimigo é de {vida_inimigo:.2f}')

        if dano_sofrido_inimigo <0:
            print('O dano foi 0 ')

        sleep(2)
        print()

    elif acao_de_combate == "Defender" and acao_do_inimigo == "Atacar":
        print(f'''Você decidiu {acao_de_combate} e o inimigo decidiu {acao_do_inimigo}.
        \nSendo assim o dano foi de {dano_sofrido_player:.2f}
        Sua vida atual é de {vida_player:.2f}''')
        vida_player -= dano_sofrido_player
        print(f'O dano sofrido foi de {dano_sofrido_player:.2f}')

        sleep(2)
        print()

    elif acao_de_combate == "Atacar" and acao_do_inimigo == "Atacar" :
        print(f'''Os dois decidiram {acao_de_combate}.
        Então ambos sofreram dano, o dano sofrido foi de {dano_sofrido_player:.2f} 
        E o dano causado foi de {dano_sofrido_inimigo:.2f}''')

        vida_player -= dano_sofrido_player
        vida_inimigo -= dano_sofrido_inimigo
        print(f'''Sua vida atual é de {vida_player:.2f}.
        A vida atual do inimigo é de {vida_inimigo:.2f}.''')

        if dano_sofrido_inimigo <0 or dano_sofrido_player <0 :
            print('O dano foi 0 ')

        sleep(2)
        print()

    if vida_player <1:
        print(f'Você morreu')
        break

    elif vida_inimigo <1 :
        print(f'O {inimigo_em_caminho or inimigo_ou_livre} CAIU !')
        break