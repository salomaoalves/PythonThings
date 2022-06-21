def campeonato():
    t = 2
    cont = usu = comp = 0
    print("Voce escolheu um campeonato!")
    while cont < 3:
        cont += 1
        print()
        print("**** Rodada",cont,"****")
        print()
        t = partida()
        if t == 1:
            usu += 1
        else:
            comp += 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",usu,"X",comp,"Computador")

def computador_escolhe_jogada(n,m):
    jogada = 1
    while jogada < m:
        if (n - jogada) % (m+1) == 0:
            return jogada
        jogada += 1
    return m

def usuario_escolhe_jogada(n,m):
    if n <= m:
        return False
    jogada = False
    while jogada == False:
        possivel_jogada = int(input("Quantas peças você vai tirar? "))
        print()
        if possivel_jogada > m or possivel_jogada <= 0:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            jogada = False
        else:
            jogada = True
    return possivel_jogada

def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    a = int(input("2 - para jogar um campeonato "))
    print()
    if a == 1:
        print()
        print("**** Rodada 1 ****")
        print()
        t = partida()
        if t == 1:
            print("Placar: Você 1 X 0 Computador")
        else:
            print("Placar: Você 0 X 1 Computador")
    else:
        campeonato()

def partida():
    jogador = 2
    escolha = False
    while escolha == False:
        n = int(input("Quantas peças? "))
        m = int(input("Limites de peças por jogada? "))
        print()
        if n <= m:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            escolha = False
        else:
            escolha = True
        
    if n%(m+1) == 0:#define quem começa
        print("Voce começa!")
        print()
        jogadaVoce = usuario_escolhe_jogada(n,m)
        n -= jogadaVoce
        print("Você tirou",jogadaVoce,"peças")
        if n != 0:
            print("Agora resta apenas",n,"peças no tabuleiro")
        else:
            print("Fim do jogo! Você ganhou!")
            return 1
        jogador = 0
    else:
        print("Computador começa!")
        print()
        jogadaPc = computador_escolhe_jogada(n,m)
        n -= jogadaPc
        print("Computador tirou",jogadaPc,"peças")
        if n != 0:
            print("Agora resta apenas",n,"peças no tabuleiro")
        else:
            print("Fim do jogo! O computador ganhou!")
            return 0
        print()
        jogador = 1
    
    while n != 0:#as jogadas vão ocorerr
        if jogador == 1:
            jogadaVoce = usuario_escolhe_jogada(n,m)
            n -= jogadaVoce
            print("Você tirou",jogadaVoce,"peças")
            if n != 0:
                print("Agora resta apenas",n,"peças no tabuleiro")
            else:
                print("Fim do jogo! Você ganhou!")
                return 1
            print()
            jogador = 0
        else:
            jogadaPc = computador_escolhe_jogada(n,m)
            n -= jogadaPc
            print()
            print("Computador tirou",jogadaPc,"peças")
            if n != 0:
                print("Agora resta apenas",n,"peças no tabuleiro")
            else:
                print("Fim do jogo! O computador ganhou!")
                return 0
            jogador = 1
