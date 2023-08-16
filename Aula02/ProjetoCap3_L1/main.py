#COLECOES
#1.TUPLAS
#Armazenam seus elementos dentro de ()
#Uma colecao IMUTAVEL
'''
nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

#Slicing de Dados
print(nomes[0])
print(nomes[2:]) #Dois pra frente
print(nomes[1:3]) #Primeiro inclusivo Segundo Exclusivo
print(nomes[-2]) #Conta ao contrario
print(nomes)
#Nao permite INSERT, UPDATE e DELETE
nomes[0] = 'Bulma'

'''

'''
#2.Listas
#GUARDA ELEMENTOS DENTRO DE []
#COLECAO MUTAVEL

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
# INSERT
nomes.append('Kuririm')
# UPDATE
nomes[0] = 'Bulma'
# DELETE
del nomes[2]
nomes.pop(3)
nomes.remove('Bulma')
print(nomes)
'''
'''
#3.CONJUNTOS (SET)
#NAO GUARDA POSICAO DOS ELEMENTOS
#NAO GUARDA ELEMENTOS REPETIDOS

nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Goku'}
print(nomes)
lista = [1,1,1,2,9,3,8,3,4,5]
print(set(lista))
#INSET
nomes.add('Bulma')
#DELETE
nomes.remove('Trunks')
'''

#4. DICIONARIOS
#ESTRUTURA DO TIPO CHAVE-VALOR

dados = {'nome':'Goku', 'idade':42, 'sexo':'M'}
dados2 = {
        'nome':'Bulma',
        'idade':38,
        'sexo':'F'
}
#INSERT
dados['altura'] = 1.79
#UPDATE
dados['idade'] = 50
#DELETE
del dados['sexo']
#print(dados['idade'])
#print(dados)

#COLECOES DENTRO DE COLECOES
personagens = [dados,dados2]

print('Idade da Bulma: ', personagens[1]['idade'])
