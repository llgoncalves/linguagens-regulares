#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AFD:
    def __init__(self):
        self.__afd = {}
        self.__estadoInicial = None

    def add_estado(self, nome, inicial=False, final=False):
        estado = {'final': final,
                  'transicoes': {}}

        if (inicial):
            self.__estadoInicial = nome

        self.__afd[nome] = estado

    def add_transicao(self, origem, simbolo, destino):
        self.__afd[origem]['transicoes'][simbolo] = destino

    def executar(self, palavra):
        estadoAtual = self.__estadoInicial
        estadoFinal = self.__afd[estadoAtual]['final']

        for indice, simbolo in enumerate(palavra):
            transicoes = self.__afd[estadoAtual]['transicoes']

            estado = transicoes.get(simbolo)

            if (estado is not None):
                estadoAtual = estado
                estadoFinal = self.__afd[estadoAtual]['final']
            else:
                return f'Palavra \"{palavra}\" rejeitada por indefinição!'

        if estadoFinal:
            return f'Palavra \"{palavra}\" aceita!'

        return f'Palavra \"{palavra}\" rejeitada (fim da leitura em estado não-final!)'
