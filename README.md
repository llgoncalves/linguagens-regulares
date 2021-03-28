# Trabalho Prático I - Teoria de Linguagens

Implementação do Trabalho Prático I da disciplana Teoria de Linguagens
ministrada pela professora Dra. Carolina Ribeiro Xavier. Disciplina do
Programa de Pós-Graduação em Ciência da Computação (PPGCC) da Universidade
Federal de São João del-Rei (UFSJ).

Aluno: Luan Luiz Gonçalves\
Data: Março de 2020

## Descrição do Trabalho

Este trabalho prático (TP) deve ser realizado individualmente, e consiste na
implementação de um programa e a redação de um relatório.


### Proposta de TP

O TP proposto consiste em implementar um autômato finito determinístico para
a sua linguagem. Conforme mencionado, os detalhes de implementação devem
ser descritos no relatório que deve acompanhar o programa.

O relatório deve constar ainda de detalhes sobre cada formalismo usado para
as linguagens regulares, a saber: AFD, AFN, AFN-e, ER e gramáticas lineares.

#### Sua linguagem

Você poderá conhecer sua linguagem de acordo a expressão regular que segue,
para chegar ao AFD a ser implementado você seguirá a seguinte sequência:

`ER -> AFN-e -> AFN -> AFD`


Dado que o sua matrícula é `d1d2d3d4d5d6d7d8d9` e as três primeiras letras
de seu nome são `l1l2l3`, sua ER é ![\Large x_{1} (d_{2} l_{1} + d_{9} l_{2})^{+} x_{2}](https://latex.codecogs.com/gif.latex?\inline&space;x_{1}&space;(d_{2}&space;l_{1}&space;&plus;&space;d_{9}&space;l_{2})^{&plus;}&space;x_{2}). Sendo o `x` da forma:

1. `x1` é o número de letras de seu primeiro nome;
2. `x2` é o número de letras de seu segundo nome.

#### Sobre o AFD

O AFD é um formalismo reconhecedor de linguagens regulares, neste TP iremos
implementar uma linguagem diferente para cada aluno.

##### Objetivos da implementação

A implementação deve ser capaz de receber uma entrada de duas formas
alternativas: individualmente (via terminal ou em interface à sua escolha) ou
um conjunto de entradas, via arquivo texto (uma palavra por linha). E responder,
para cada entrada dada, se a palavra foi aceita ou se foi rejeitada, em caso
de rejeição, colocar também o motivo (indefinição ou fim da leitura em estado
não-final).

Para leitura individual é interessante explicitar os passos do
autômato na leitura da cada símbolo.

> Você deve entregar junto ao seu código e relatório um arquivo com 10 palavras aceitas pela sua linguagem, 10 paralavras rejeitadas (5 por indefinição e 5 que após toda palavra lida, assume um estado não final).

### Relatório das características das linguagens do tipo 3, da Implementação e da Utilização

O relatório deve constar de uma breve exposição do assunto visto até agora na
disciplina de teoria de linguagens, fale sobre os formalismos e as ferramentas
vistas até agora de uma forma clara e resumida, explicando claramente como
você chegou no AFD implementado.

O relatório também deve descrever sucintamente a estrutura do programa
e descrição dos algoritmos utilizados. Além disso, também deve ser fornecido
um manual de utilização do código. Tal relatório deve ser entregue em formato
eletrônico juntamente com o programa.

O relatório deve incluir uma descrição das dificuldades encontradas para
implementar o TP.

> Somente arquivos no formato PDF serão considerados.

### Prazos

A entrega do TP pode ser efetuada até o dia 29/03/2021 às 23:59.

### Submissão

Os TPs devem ser enviados pelo Portal didático/UFSJ, alternativamente, em caso
de instabilidade do sistema, utilizar o endereço carolinaxavier@ufsj.edu.br.

Itens necessários:

1. Código fonte com documentação;
2. Arquivo com as palavras;
3. Relatório.

### Critérios de avalilação

Este trabalho vale 30% da nota da disciplina.

* 50% implementação correta do código do autômato e corretude nos
padrões de entrada e saída;
* 10% para os aspectos de boas práticas de programação:
  * Modularização;
  * Legibilidade (nomes de variáveis significativos, código bem formatado, uso de comentários);
  * Consistência (formatação uniforme);
  * Boa documentação descritiva da implementação e do uso do programa;
  * 30% Texto resumindo o tema visto em aula;
  * 10% áudio ou vídeo explicativo da linguagem de até 5 minutos;
  * (+5% das Notas acima somadas) Extras para uma interface amigável.

### Algumas Dicas

Durante o desenvolvimento, é importante não se perder nos detalhes. Portanto,
é recomendado que os alunos comecem o desenvolvimento implementando as funcionalidades básicas. Só depois de garantir que as funcionalidades básicas estão
funcionando conforme o planejado, os alunos devem considerar a implementação
de melhorias e funcionalidades adicionais, como intereface gráfica, por exemplo.
Também recomenda-se que trechos mais complicados do código sejam acompanhados de comentários que esclareçam o seu funcionamento/objetivo/parâmetros
de entrada e resultados.


## Instruções


## Relatório
