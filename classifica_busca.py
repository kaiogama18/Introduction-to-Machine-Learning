# -*- coding: UTF-8 -*-
from collections import Counter
import pandas as pd

df = pd.read_csv('busca.csv') #0 e 1
#df = pd.read_csv('buscas2.csv') #0 e 1
X_df = df[['home','busca','logado']] #Recebe um Array de coluna
Y_df = df['comprou']

#Devolver a tabela busca em dummies - perguntas sim não
#Xdummies_df = pd.get_dummies(X_df)
#Ydummies_df = Y_df
Xdummies_df = pd.get_dummies(X_df).astype(int)
Ydummies_df = Y_df


X = Xdummies_df.values
Y = Ydummies_df.values

""" Implementando o algoritmo base
    Verificar a eficacia do algoritmos
        que chuta tudo 0 e 1
"""
#porcentagem_de_treino = 0.9
porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = porcentagem_de_treino * len(Y)
tamanho_de_teste = porcentagem_de_teste * len(Y)
tamanho_de_validacao = len(Y) - tamanho_de_treino - tamanho_de_teste


"""Erro
    TypeError: slice indices must be integers or None or have an __index__ method
    É quando o formado da variavel não e mesmo da variavel de envio
    X[:int(tamanho_de_treino)] --> 'Tamanho treino' é String e não int,
     então tem que converter para integer
"""

# 0 até 799
treino_dados = X[:int(tamanho_de_treino)]
treino_marcacoes = Y[:int(tamanho_de_treino)]

fim_de_treino = tamanho_de_treino + tamanho_de_teste
# 800 até 899
teste_dados = X[int(tamanho_de_treino):int(fim_de_treino)]
teste_marcacoes = Y[int(tamanho_de_treino):int(fim_de_treino)]
# 900 até 999
validacao_dados = X[int(fim_de_treino):]
validacao_marcacoes = Y[int(fim_de_treino):]





def fit_and_predict(nome, modelo, treino_dados, treino_marcacoes, \
                    teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)
    resultado = modelo.predict(teste_dados)
    acertos = resultado == teste_marcacoes

    total_de_acertos = sum(acertos) # ver o total_de_acertos

    total_de_elementos = len(teste_dados)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
    msg = 'Taxa de acerto do {0}: {1}'.format(nome, taxa_de_acerto)
    print msg
    return taxa_de_acerto

from sklearn.naive_bayes import MultinomialNB
modeloMultinomial = MultinomialNB()
resultadoMultinomial =  fit_and_predict('MultinomialNB', modeloMultinomial, treino_dados, treino_marcacoes, teste_dados, \
            teste_marcacoes)
''' AdaBoostClassifier
 Em caso é melhor!
'''
from sklearn.ensemble import AdaBoostClassifier
modeloAdaBoost = AdaBoostClassifier()
resultadoAdaBoost =  fit_and_predict('AdaBoostClassifier', modeloAdaBoost, treino_dados, treino_marcacoes, \
                    teste_dados, teste_marcacoes)

if resultadoMultinomial > resultadoAdaBoost:
	vencedor = modeloMultinomial
else:
	vencedor = modeloAdaBoost

resultado = vencedor.predict(validacao_dados)
acertos = (resultado == validacao_marcacoes)

total_de_acertos = sum(acertos)
total_de_elementos = len(validacao_marcacoes)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

msg = "Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_de_acerto)
print(msg)

"""Criação de um contador generico
    collections e importando o Counter
    A eficacia do algoritmo que chuta tufo um unico valor
"""
#Retorna a soma da variavel que tem a  maior quantidade
#acerto_base = max(Counter(teste_marcacoes).itervalues())
acerto_base = max(Counter(validacao_marcacoes).itervalues())

taxa_de_acerto_base = 100.0 *  acerto_base / len(validacao_marcacoes)

#taxa_de_acerto_base = 100.0 *  max(acerto_de_um, acerto_de_zero) / len(Y)
print 'Taxa de acerto base: %f' % taxa_de_acerto_base
print 'Total de testes: %d '% len(validacao_dados)
