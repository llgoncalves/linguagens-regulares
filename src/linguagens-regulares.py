#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from modules.afd import AFD
from modules.io import IO


def main(palavras):
    afd = AFD()

    afd.add_estado('q0', True)
    afd.add_estado('q1')
    afd.add_estado('q2')
    afd.add_estado('q3')
    afd.add_estado('q4')
    afd.add_estado('q5')
    afd.add_estado('q6', False, True)

    afd.add_transicao('q0', '4', 'q1')
    afd.add_transicao('q1', '2', 'q3')
    afd.add_transicao('q1', '5', 'q2')
    afd.add_transicao('q2', 'u', 'q4')
    afd.add_transicao('q3', 'l', 'q5')
    afd.add_transicao('q4', '5', 'q2')
    afd.add_transicao('q4', '2', 'q3')
    afd.add_transicao('q4', '4', 'q6')
    afd.add_transicao('q5', '2', 'q3')
    afd.add_transicao('q5', '5', 'q2')
    afd.add_transicao('q5', '4', 'q6')

    if not palavras:
        palavras.append(input('Entre com a palavra: '))

    for palavra in palavras:
        print(afd.executar(palavra))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--palavra', type=str,
                        help='Entrar com a palavra.')

    parser.add_argument('-a', '--arquivo', type=str,
                        help='Ler arquivo com conjunto de entradas.')

    args = parser.parse_args()

    palavras = []

    if args.palavra:
        palavras.append(args.palavra)

    if args.arquivo:
        palavras += None

    main(palavras)
