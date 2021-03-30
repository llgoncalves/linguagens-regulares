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


class AFD():
    """
    Está classe representa um Autômato Finito Deterministico (AFD)

    Métodos
    -------

    add_estado(nome, inicial=False, final=False)
        Define um novo estado
    add_transicao(origem, simbolo, destino)
        Define uma nova transição
    executar(palavra)
        Processa a palavra
    """

    def __init__(self):
        """
        Método construtor
        """

        # Abstração de um AFD
        self.__afd = {}
        # Guarda o nome do estado inicial
        self.__estadoInicial = None

    def add_estado(self, nome, inicial=False, final=False):
        """
        Define um novo estado

        Parâmetros
        ----------
        nome : str, opcional
            Nome do estado
        inicial : boolean, opcional
            Define se o estado é inicial ou não
        final : boolean, opcional
            Define se o estado é finão ou não
        """

        # Abstração de estados
        # Define se é final e suas transições
        estado = {'final': final,
                  'transicoes': {}}

        # Define o estado inicial
        if (inicial):
            self.__estadoInicial = nome

        # Adiciona o estado
        self.__afd[nome] = estado

    def add_transicao(self, origem, simbolo, destino):
        """
        Define uma nova transição

        Parâmetros
        ----------
        origem : str
            Estado de origem
        simbolo : str
            Símbolo lido
        destino : str
            Estado de destino
        """

        # Adiciona trasição
        self.__afd[origem]['transicoes'][simbolo] = destino

    def executar(self, palavra):
        """
        Processar a palavra

        Parâmetro
        ---------
        palavra : str
            Palavra a ser processada

        Retorno
        -------
        mensagem : str
        Retorna uma mensagem de aceitação ou rejeição da palavra
        """

        # Atribui ao estado atual o estado inicial
        estadoAtual = self.__estadoInicial

        # Atribui 'True' se o estado o estado atual é final
        # Atribui 'False' se o estado o estado atual é final
        estadoFinal = self.__afd[estadoAtual]['final']

        # Para cada letra da palavra
        for indice, simbolo in enumerate(palavra):
            # Recupera as transição definidas a partir do estado atual
            transicoes = self.__afd[estadoAtual]['transicoes']

            # Recupera o estado destino
            estado = transicoes.get(simbolo)

            # Se a transição foi definida
            if (estado is not None):
                # Atribui novo estado atual
                estadoAtual = estado
                # Atribui True ou False, caso o novo estado sejá final ou não
                estadoFinal = self.__afd[estadoAtual]['final']

            # Transição não definida
            else:
                return f'Palavra \"{palavra}\" ==> REJEITADA por indefinição!'

        # Se para em um estado final
        if estadoFinal:
            return f'Palavra \"{palavra}\" ==> ACEITA!'

        # Se não parou em um estado final
        return f'Palavra \"{palavra}\" ==> REJEITADA (fim da leitura em estado não-final!)'
