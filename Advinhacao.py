
#funcoes:
def apresentacao():
    print('*********************************************')
    print('Olá!Bem vindo ao jogo de adinhação de número!')
    print('*********************************************')

def escolha_dificuldade():
    # escolha da dificuldade:
    nivel = 0
    while (nivel < 1 or nivel > 3):
        print('Selecione um dos níveis de dificuldade:')
        print("(1) Fácil{0}(2) Médio{0}(3) Difícil{0}".format('\n'))
        nivel = int(input('Digita um nível:'))

    if (nivel == 1):
        toltal_de_tentativas = 20
    elif (nivel == 2):
        toltal_de_tentativas = 10
    elif (nivel == 3):
        toltal_de_tentativas = 5
    return toltal_de_tentativas

def pedir_chute():
    # Entrada dos dados:
    chute = input('digite um número entre 1 e 100:')
    print("você digitou: ", chute)
    numero_chute = int(chute)  # todo o input entra como string,logo,eu tenho que converter para int para comparar
    return numero_chute

def mensagem_final():
    # Fim:
    print('*********************************************')
    print('Fim do jogo!')
    print('*********************************************')

def jogar():
    # bibliotecas
    import random  # a funcao random não esta imbutida

    apresentacao()

    toltal_de_tentativas = escolha_dificuldade()

    pontuacao=1000

    numero_secreto= random.randrange(1,101) #bilioteca.funcao-->funcao randrange-->gera um número int entre 1 e 100(N+1)

    rodada=1
    for rodada in range(1,toltal_de_tentativas+1) : #OBS: for i in range(1,N-1,passo)

        print("tentativa {} de {}".format(rodada,toltal_de_tentativas))

        numero_chute = pedir_chute() #Entrada dos dados

        #Verificar se o número é aceitavel:
        fora_do_intervalo = numero_chute < 1 or numero_chute > 100

        if (fora_do_intervalo):
            print('incorreto! O número deve ser entre 1 e 100!')
            continue  # ele volta sai desse IF e vai para o inicio do for em rodada+1-->continua o laço!

        #Testes:
        acertou = numero_secreto == numero_chute
        maior   = numero_secreto < numero_chute
        menor   = numero_secreto > numero_chute

        #Verificacao:
        if (acertou):
            print('Você acertou! e fez {} pontos!'.format(pontuacao))
            break #sai do laço
        else:
            if (maior):
                print('Você errou!O seu chute foi maior do que o número secreto')
                pontuacao=pontuacao-abs(numero_secreto-numero_chute)
                print('Pontuação = {} pontos'.format(pontuacao))
            elif(menor):
                print('Você errou!O seu chute foi menor do que o número secreto')
                pontuacao = pontuacao - (numero_secreto - numero_chute)
                print('Pontuação = {} pontos'.format(pontuacao))
    mensagem_final()

if(__name__=="__main__"):#se o arquivo for o programa principal,chame essa funcao:
    jogar()
