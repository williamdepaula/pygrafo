#!/usr/bin/python

import os
import platform

class JogoDaVelha:

    def __init__(self, jogador = "x"):
        self.tabuleiro = {}
        self.copiaTabuleiro = {}
        self.combosVencedores = (
            [0,1,2], [3,4,5], [6,7,8], # Vitorias horizontais
            [0,3,6], [1,4,7], [2,5,8], # Vitorias verticais
            [0,4,8], [2,4,6],           # vitorias diagonais
        )
        self.clean = ('clear', 'cls')[platform.system() == 'Windows']

    def criarTabuleiro(self):
        for i in range(9):
            self.tabuleiro[i] = "."
        # print(self.tabuleiro)

    def mostraTabuleiro(self):
        os.system(self.clean)
        print(self.tabuleiro[0], self.tabuleiro[1], self.tabuleiro[2])
        print(self.tabuleiro[3], self.tabuleiro[4], self.tabuleiro[5])
        print(self.tabuleiro[6], self.tabuleiro[7], self.tabuleiro[8])

    def pegaJogadasPossiveis(self):
        self.jogadasPossiveis = []
        for i in range(9):
            if self.tabuleiro[i] == ".":
                self.jogadasPossiveis.append(i)
        return self.jogadasPossiveis

    def joga(self, posicao, jogador):
        self.tabuleiro[posicao] = jogador
        # self.mostraTabuleiro()

    def completo(self):
        if "." not in self.tabuleiro.values():
            return True
        if self.pegaVencedor() != None:
            return True
        return False

    def pegaVencedor(self):
        # for jogador in ["x", "o"]:
        jogador = "x"
        for combos in self.combosVencedores:
            if self.tabuleiro[combos[0]] == jogador and self.tabuleiro[combos[1]] == jogador and self.tabuleiro[combos[2]] == jogador:
                return jogador
            if "." not in self.tabuleiro.values():
                return "empate"


        jogador = "o"
        for combos in self.combosVencedores:
            if self.tabuleiro[combos[0]] == jogador and self.tabuleiro[combos[1]] == jogador and self.tabuleiro[
                combos[2]] == jogador:
                return jogador
            if "." not in self.tabuleiro.values():
                return "empate"



        return None

    def pegaInimigo(self, jogador):
        if jogador == "x":
            return "o"
        return "x"

    def minimax(self, jogador, profundidade = 0):
        if jogador == "o":
            melhor = -10
        else:
            melhor = 10
        if self.completo():
            if self.pegaVencedor() == "x":
                return profundidade - 10, None
            elif self.pegaVencedor() == "empate":
                return 0, None
            elif self.pegaVencedor() == "o":
                return 10 - profundidade, None

        for movimento in self.pegaJogadasPossiveis():
            self.joga(movimento, jogador)

            val, _ = self.minimax(self.pegaInimigo(jogador), profundidade+1)
            # print(val)

            self.joga(movimento, ".")
            if jogador == "o":
                if val > melhor:
                    melhor, melhorJogada = val, movimento
            else:
                if val < melhor:
                    melhor, melhorJogada = val, movimento

        return melhor, melhorJogada



jogo = JogoDaVelha()
jogo.criarTabuleiro()
jogador = "o"
print("Entre com o tipo de jogo!")
print("1 para jogar contra o computador e qualquer outra tecla para jogoa contra outro jogador.")
tipo = int(input())
if tipo == 1:
    oponente = "Computador"
else:
    oponente = "Jogador"



while True:
    jogador = jogo.pegaInimigo(jogador)
    jogo.mostraTabuleiro()
    print("Jogador %s" % jogador)
    movimento = int(input())
    if movimento in jogo.pegaJogadasPossiveis():
        jogo.joga(movimento, jogador)
        vencedor = jogo.pegaVencedor()
        if vencedor == "empate":
            print("Empatou!!!!")
            break
        elif vencedor != None:
            print("O jogador vencedor é %s" % vencedor)
            break

    if oponente == "Jogador":

        jogador = jogo.pegaInimigo(jogador)
        jogo.mostraTabuleiro()
        print("Jogador1 %s" % jogador)
        movimento = int(input())
        if movimento in jogo.pegaJogadasPossiveis():
            jogo.joga(movimento, jogador)
            vencedor = jogo.pegaVencedor()

            if vencedor == "empate":
                print("Empatou!!!!")
                break
            elif vencedor != None:
                print("O jogador vencedor é %s" % vencedor)
                break
    else:
        jogador = jogo.pegaInimigo(jogador)
        val, melhor = jogo.minimax(jogador)
        jogo.joga(melhor, jogador)
        vencedor = jogo.pegaVencedor()
        if vencedor == "empate":
            jogo.mostraTabuleiro()
            print("Empatou!!!!")
            break
        elif vencedor != None:
            jogo.mostraTabuleiro()
            print("O jogador vencedor é %s" % vencedor)
            break
