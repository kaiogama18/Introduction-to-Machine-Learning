# -*- coding: UTF-8 -*-
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
marcacoes = [1,1,1,-1,-1,-1]

#Aprender
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
#Treinar
modelo.fit(dados,marcacoes)

misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [1,0,1] #0,0,1

testes = [misterioso1,misterioso2,misterioso3]
marcacoes_teste = [-1,1,1] #-1,1,-1

#Predizer
resultado = modelo.predict(testes)
print resultado

# 1  1 => 1-1=0
# -1 -1 => -1 --1 =-1 + 1 = 0
#-1 1 => -1 -1 = -2
#1 -1 => --1 =1 1+1 =2

diferenca = resultado - marcacoes_teste
print diferenca
acertos = [d for d in diferenca if d  == 0] #para cada diferença d dentro das diferenças se o valor for 0 crie o array
print acertos
total_de_acertos = len(acertos) #quantos acertos
print '---> Total de acertos:',total_de_acertos
total_de_elementos = len(testes)
print '---> Total de elementos:',total_de_elementos
#erros = resultado - marcacoes_teste

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print '---> taxa de acerto:',taxa_de_acerto

#erros = resultado - marcacoes_teste
#for erro in erros if erro != 0
#erros = resultado - marcacoes_teste
