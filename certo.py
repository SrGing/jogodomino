import random

def criar_pecas():
    pecas = []
    for i in range(7):
        for j in range(i, 7):
            pecas.append((i, j))
    return pecas

def embaralhar_pecas(pecas):
    random.shuffle(pecas)

def distribuir_pecas(pecas):
    jogadores = [[] for _ in range(4)]
    for _ in range(7):
        for jogador in jogadores:
            jogador.append(pecas.pop())
    return jogadores, pecas

def exibir_mao_jogador(jogador):
    print("Suas peças:")
    for i, peca in enumerate(jogador):
        print(f"{i + 1}: {peca[0]}-{peca[1]}")

def escolher_peca(jogador, jogadas_possiveis):
    while True:
        escolha = input("Escolha uma peça para jogar (digite o número): ")
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(jogadas_possiveis):
                raise ValueError
            return jogadas_possiveis[escolha - 1]
        except ValueError:
            print("Escolha inválida. Digite o número correspondente a uma peça válida da sua mão.")

def verificar_jogada_valida(peca, tabuleiro):
    if not tabuleiro:
        return True
    extremidades = [tabuleiro[0][0], tabuleiro[-1][1]]
    return peca[0] in extremidades or peca[1] in extremidades

def obter_jogadas_possiveis(jogador, tabuleiro):
    jogadas_possiveis = []
    for peca in jogador:
        if verificar_jogada_valida(peca, tabuleiro):
            jogadas_possiveis.append(peca)
    return jogadas_possiveis

def realizar_jogada(peca, jogador, tabuleiro):
    jogador.remove(peca)
    if not tabuleiro:
        tabuleiro.append(peca)
    elif peca[1] == tabuleiro[0][0]:
        tabuleiro.insert(0, peca)
    elif peca[0] == tabuleiro[0][0]:
        tabuleiro.insert(0, (peca[1], peca[0]))
    elif peca[0] == tabuleiro[-1][1]:
        tabuleiro.append(peca)
    elif peca[1] == tabuleiro[-1][1]:
        tabuleiro.append((peca[1], peca[0]))

def exibir_tabuleiro(tabuleiro):
    print("Tabuleiro:")
    for peca in tabuleiro:
        print(f"{peca[0]}-{peca[1]}", end=" ")
    print()

def jogo_domino():
    while True:
        pecas = criar_pecas()
        embaralhar_pecas(pecas)
        jogadores, pecas_restantes = distribuir_pecas(pecas)
        tabuleiro = []
        vez_do_jogador = 0
        vencedor = None

        while any(jogador for jogador in jogadores):
            jogador_atual = jogadores[vez_do_jogador]
            print(f"É a vez do Jogador {vez_do_jogador + 1}.")
            exibir_tabuleiro(tabuleiro)
            exibir_mao_jogador(jogador_atual)
            jogadas_possiveis = obter_jogadas_possiveis(jogador_atual, tabuleiro)
            if not jogadas_possiveis:
                print("Você não tem jogadas possíveis. Passe a vez.")
                vez_do_jogador = (vez_do_jogador + 1) % 4
                continue
            print("Jogadas possíveis:")
            for i, peca in enumerate(jogadas_possiveis):
                print(f"{i + 1}: {peca[0]}-{peca[1]}")
            escolha = escolher_peca(jogador_atual, jogadas_possiveis)
            realizar_jogada(escolha, jogador_atual, tabuleiro)

            if not jogador_atual:
                vencedor = vez_do_jogador
                break

            vez_do_jogador = (vez_do_jogador + 1) % 4

        if vencedor is not None:
            print(f"Parabéns, Jogador {vencedor + 1}! Você venceu!")
        else:
            print("O jogo empatou!")

        reiniciar = input("Deseja jogar novamente? (S/N): ")
        if reiniciar.lower() != "s":
            break

jogo_domino()