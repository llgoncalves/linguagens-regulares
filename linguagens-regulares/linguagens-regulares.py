#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor : Luan Luiz Gonçalves
Data : 30/03/2021
Licença : GPLv3

Sobre : Implementação do Trabalho Prático I da disciplana Teoria de Linguagens
ministrada pela professora Dra. Carolina Ribeiro Xavier. Disciplina do
Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Universidade
Federal de São João del-Rei (UFSJ).
"""

import sys
import os
import argparse
from automato.afd import AFD


def main(palavras):
    """
    Função principal

    Parâmetros
    ----------
    palavras : list
        Lista de palavras a serem processadas
    """
    # Instância do AFD
    afd = AFD()

    # Define os estados
    afd.add_estado('q0', True)  # Estado inicial
    afd.add_estado('q1')
    afd.add_estado('q2')
    afd.add_estado('q3')
    afd.add_estado('q4')
    afd.add_estado('q5')
    afd.add_estado('q6', False, True)  # Estado final

    # Define as transições
    afd.add_transicao('q0', '4', 'q1')
    afd.add_transicao('q1', '2', 'q2')
    afd.add_transicao('q1', '5', 'q3')
    afd.add_transicao('q2', 'l', 'q4')
    afd.add_transicao('q3', 'u', 'q5')
    afd.add_transicao('q4', '2', 'q2')
    afd.add_transicao('q4', '5', 'q3')
    afd.add_transicao('q4', '4', 'q6')
    afd.add_transicao('q5', '5', 'q3')
    afd.add_transicao('q5', '2', 'q2')
    afd.add_transicao('q5', '4', 'q6')

    # Entrar com a palavra, caso não for utilizado os argumentos
    if not palavras:
        palavras.append(input('Entre com a palavra: '))

    # Processa todas as palavras
    for palavra in palavras:
        print(afd.executar(palavra))


if __name__ == '__main__':
    # Argumentos do programas
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--palavra', type=str,
                        help='Entrar com a palavra.')

    parser.add_argument('-a', '--arquivo', type=str,
                        help='Ler arquivo com conjunto de entradas.')

    args = parser.parse_args()

    # Palavras para serem processadas
    palavras = []

    if args.palavra:
        palavras.append(args.palavra)

    if args.arquivo:
        # Abre arquivo para leitura
        arquivo = open(os.path.join(os.path.abspath('../'), args.arquivo), 'r')

        # Lê linha por linha
        for linha in arquivo.readlines():
            linha = linha[:len(linha) - 1]  # Remove \n no final da linha
            palavras += [linha]

        # Fecha arquivo
        arquivo.close()

    # Função principal
    main(palavras)
