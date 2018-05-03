from dados import carregar_acessos
X,Y = carregar_acessos()

#Separa treino e testes

treinos_dados = X[:90] #As primeiras 90 linhas
treinos_marcacoes = Y[:90] #As primeiras 90 linhas

teste_dados = X[-9:] #As ultimas 9 linhas
teste_marcacoes = Y[-9:] #As ultimas 9 linhas
#Aprender
from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
#Treinar

modelo.fit(treinos_dados,treinos_marcacoes)
resultado = modelo.predict(teste_dados)
diferencas = resultado - teste_marcacoes

#modelo.fit(X,Y)
#resultado = modelo.predict(X)
#diferencas = resultado - Y
#
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
#total_de_elementos = len(X)
total_de_elementos = len(teste_dados)
taxa_de_acerto =100.0 * total_de_acertos / total_de_elementos

print taxa_de_acerto
print 'Total de elementos:',total_de_elementos

#print(resultado)
#print(Y)
#print(modelo.predict([[1,0,1],[0,1,0],[1,0,0],[1,1,0],[1,1,1]]))

#X,Y = carregar_acessos()
#print '---> X', X
#print '---> Y', Y
