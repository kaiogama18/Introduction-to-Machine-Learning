# -*- coding: UTF-8 -*-
from collections import Counter
import pandas as pd


#teste inicial: home, busca, logado => comprou
# home, buscaSN3 home, logado
# busca, logafo
# busca, logda
# busca: 85.71% (7 testes)

df = pd.read_csv('busca.csv') #0 e 1
#df = pd.read_csv('buscaSN.csv') #0 e 1
#df = pd.read_csv('buscas2.csv') #0 e 1
#X_df = df[['home','busca','logado']] #Recebe um Array de coluna
X_df = df[['home','busca','logado']] #Recebe um Array de coluna
Y_df = df['comprou']
#Devolver a tabela busca em dummies - perguntas sim não
Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

""" Implementando o algoritmo base
    Verificar a eficacia do algoritmos
        que chuta tudo 0 e 1
"""
#acerto_de_um = sum(Y) #Total de 1
#acerto_de_zero = len(Y) - acerto_de_um #Total de Zero

#acerto_de_um = len(Y[Y==1]) #Total de 1  | Maneira mas usada | Funcionalidade de Data Frame
#acerto_de_zero = len(Y[Y==0]) #Total de Zero | Maneira mas usada

#Trocando para sim e Não
#acerto_de_um = len(Y[Y=='sim']) #Total de Sim  | Maneira mas usada | Funcionalidade de Data Frame
#acerto_de_zero = len(Y[Y=='nao']) #Total de Não | Maneira mas usada

#porcentagem_de_treino = 0.9
porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1
tamanho_de_treino = porcentagem_de_treino * len(Y)
#tamanho_de_teste = len(Y) - tamanho_de_treino
tamanho_de_teste = porcentagem_de_teste * len(Y)
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste
"""Erro
    TypeError: slice indices must be integers or None or have an __index__ method
    É quando o formado da variavel não e mesmo da variavel de envio
    X[:int(tamanho_de_treino)] --> 'Tamanho treino' é String e não int,
     então tem que converter para integer
"""
# 0 até 799
#treino_dados = X[:int(tamanho_de_treino)] #As primeiras 90 linhas
#treino_marcacoes = Y[:int(tamanho_de_treino)] #As primeiras 90 linhas

# 0 até 799
treino_dados = X[0:int(tamanho_de_treino)] #As primeiras 90 linhas
treino_marcacoes = Y[0:int(tamanho_de_treino)] #As primeiras 90 linhas

#teste_dados = X[int(-tamanho_de_teste):]
#teste_marcacoes = Y[int(-tamanho_de_teste):]
# 800 até 899
fim_de_teste = int(tamanho_de_treino + tamanho_de_teste)

teste_dados = X[int(tamanho_de_treino): fim_de_teste]
teste_marcacoes = Y[int(tamanho_de_teste): fim_de_teste]

# 900 até 999
validacao_dados = X[int(fim_de_teste):]
validacao_marcacoes = Y[int(fim_de_teste):]

def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, \
                    teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)
    resultado = modelo.predict(teste_dados)
    #diferenca = resultado - teste_marcacoes

    acertos = resultado == teste_marcacoes

    #acertos = [d for d in diferenca if d == 0]
    #total_de_acertos = len(diferenca) # ver o total_de_acertos


    total_de_acertos = sum(acertos) # ver o total_de_acertos

    total_de_elementos = len(teste_dados)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    #print taxa_de_acerto
    #print 'Taxa de acerto do algoritmo: %f' % taxa_de_acerto
    msg = 'Taxa de acerto do {0}: {1}'.format(nome, taxa_de_acerto)
    print msg

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
fit_and_predict('MultinomialNB', modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)
''' AdaBoostClassifier
 Em caso é melhor!
'''
from sklearn.ensemble import AdaBoostClassifier
modelo = AdaBoostClassifier()
fit_and_predict('AdaBoostClassifier', modelo, treino_dados, treino_marcacoes, \
                    teste_dados, teste_marcacoes)

#print total_de_elementos

#print X
#Ydummies = pd.get_dummies(Y)[1] ''' Não é o correto '''

#from dados import carregar_buscas
#X,Y = carregar_buscas()
#print X
#print X[0]
#print Y[0]
#Usando a biblioteca usando o pandas
#print(df)


"""Criação de um contador generico
    collections e importando o Counter
    A eficacia do algoritmo que chuta tufo um unico valor
"""
#Retorna a soma da variavel que tem a  maior quantidade
acerto_base = max(Counter(teste_marcacoes).itervalues())

taxa_de_acerto_base = 100.0 *  acerto_base / len(teste_marcacoes)

#taxa_de_acerto_base = 100.0 *  max(acerto_de_um, acerto_de_zero) / len(Y)
print 'Taxa de acerto base: %f' % taxa_de_acerto_base
print 'Total de testes: %d '% len(teste_dados)
