from random import randint
from os import system
from time import sleep
global contador

def primo(numero):
    contador = 0
    for num in range(1, numero + 1):
        if numero % num == 0:
            contador += 1
    print('Esse número é divisivel por {} outros numeros!'.format(contador))


def organizador(o):
    for j in range(len(o)):
        print(o)
        if o[j] < o[(j - 1)]:
            t = o[j]
            o[j] = o[(j - 1)]
            o[j - 1] = t
            print(o)

def jogo():
    n = randint(0, 1000)
    cont = 0
    denovo = "s"
    certo = False
    chutes = [1]
    errados = [0]
    nome = str(input('Bom dia, vamos jogar! Qual seu nome? '))
    while nome == "":  # impedidno que o usuário coloque um nome em branco
        nome = input("Por favor, Digite um nome válido: ")
    system("cls")
    print('''Olá {}, vamos jogar um jogo de adivinhação matemática?
Como funciona o jogo, eu escolhi um nùmero entre 0 e 1000 e você tem que adivinhar esse número.
Mas calma temos algumas dicas para te ajudar...'''.format(nome))
    print('-=-' * 30)
    print('''Você podera chutar um número qualquer e eu te direi se é o numero escolhido ou não.
Se não for, direi se meu numero é ou não divisivel pelo numero escolhido.
Vamos começar?'''.format(nome))
    print('Vamos as primeiras dicas')
    while certo == False and denovo == "s":
        print('O número escolhido é divisivel por {}!'.format(chutes))
        print('E também não é divisivel por {}, interessante!'.format(errados))
        primo(n) # identificar quantos divisores tem
        c = input('Digite o {}º chute:'.format(cont + 1)).strip()  # impedindo caracteres em branco no chute
        while c.isnumeric() is False:
            c = input('Por favor, digite um numero válido: ').lower().strip()
        c = int(c)
        if n == c:
            system("cls")
            print('Caraca, você acertou, parabéns!')
            print('Você utilizou {} tentativas para acertar!'.format(cont + 1))
            certo = True
        else:
            system("cls")
            print('Que pena, não era esse número!')
            if (n % c) == 0:
                chutes.append(c)
                cont = cont + 1
                print('Porém o meu número escolhido é sim divisivel por {}'.format(c))
            else:
                print('O número também não é divisivel por {}'.format(c))
                errados.append(c)
                cont = cont + 1
            if (cont % 5) == 0:
                tentar = str(input('''Está dificil né?
                Quer continuar tentando? (S/N)''').strip().lower())
                while tentar != 's' and tentar != 'n':
                    tentar = str(input("Digite uma opção válida? (S/N)").strip().lower())
                if tentar == 'n':
                    novamente()
        print(len(chutes))
        organizador(chutes)

    print('Meu número era {}'.format(n))
    novamente()


def novamente():
    d = str(input('Deseja jogar novamente?')).strip().lower()
    if d == 's':
        system("cls")
        jogo()
    else:
        system("cls")
        print('Ok, foi muito bom jogar com você!')
        sleep(3)


jogo()