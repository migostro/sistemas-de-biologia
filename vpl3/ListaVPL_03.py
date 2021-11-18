'''
Faça um programa que receba uma lista de genes e uma função de regulação para cada gene 
com operadores not, and e or ('!', '&', ' | ') e imprima a TABELA de TRANSIÇÃO de ESTADOS. 
Utilize o que foi feito nos exercícios anteriores. 
(Se quiser, pode fazer tudo diferente também)

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função para A: !A&C | B&C | !C
Função para B: !A&!B | C
Função para C: A&B
Tabela de Transição de Estados:
000 110
001 110
010 100
011 110
100 100
101 010
110 101
111 111

'''

import copy
import math

''' Trata os textos e os inputs
    Retorna a lista de Genes e as funções reguladoras de cada uma deles
'''
def trataTexto():
    separadorGenes = ','
    separadorFuncOu = ' | '
    func = []

    listaGenes = input("Nomes dos genes (separados por vírgula): ").strip().split(separadorGenes)

    

    for i in range(len(listaGenes)):
        texto = "\nFunção para " + listaGenes[i] + ": "
        func.append(input(texto).strip().split(separadorFuncOu))

    '''listaGenes = "A,B,C".strip().split(separadorGenes)
    func.append("!A&C | B&C | !C".strip().split(separadorFuncOu))
    func.append("!A&!B | C".strip().split(separadorFuncOu))
    func.append("A&B".strip().split(separadorFuncOu))'''

    return listaGenes, func

# adiciona val a todos estados de lista estados
def adicionaEstado(listaEstados, val):
    n = len(listaEstados)
    for j in range(n) :
        # adiciona val no final da lista
        listaEstados[j] += val


''' Recebe um gene a sua função reguladora
    Retorna o index da func caso exista ou -1 caso contrario
'''
def esta(gene, func):
    for i in range(len(func)):
        if gene in func[i]:
            return i
    return -1


''' Recebe um gene
    Retorna o valor que ativa esse gene
'''
def estado(gene):
    if '!' in gene:
        return '0'
    else:
        return '1'


''' Recebe a lista de genes e a função reguladora de cada um deles
    Retorna a lista de ativação de cada gene (na mesma ordem de listaGenes)
'''
def estados(listaGenes, func):
    listaEstados = ['']

    for i in range(len(listaGenes)):
        
        index = esta(listaGenes[i], func)
        #caso o gene tenha uma função definida
        # adiciona a tabela apenas o estado possivel
        if index != -1:
            adicionaEstado(listaEstados, estado(func[index]))
        # caso o gene não tenha função definida
        # adiciona os dois estados (duplica a tabela)
        else:
            lista0 = copy.deepcopy(listaEstados)
            lista1 = copy.deepcopy(listaEstados)
            
            adicionaEstado(lista0, '0')
            adicionaEstado(lista1, '1')

            # duplica a lista
            listaEstados = lista0 + lista1

    return listaEstados

        
''' Recebe uma lista de genes e uma função reguladora deles
    Retorna os genes supostamente ativos e a lista que ativada por cada um gene desses
'''
def listaAtivacao(listaGenes, func):
    separadorFuncE = '&'

    listaAtivacoes = []

    # faz a tabela de cada gene
    for i in range(len(func)):
        # estado parcial
        estadoFunc = []

        # j é cada função que tem apenas &
        for j in func[i]:
            estadosAux = estados(listaGenes, j.split(separadorFuncE))

            # procura por estados que ainda não estão em estadosFunc
            for k in estadosAux:
                if not k in estadoFunc:
                    estadoFunc.append(k)
        listaAtivacoes.append(estadoFunc)

    return listaAtivacoes

''' Recebe um vetor vazio v com fim+1 posições, o inicio dele e o fim e o numero que adicionaremos das posições
'''
def permutacaoRec(v, inicio, fim, val):
    

    i = inicio

    while (i <= fim):
        v[i] += val

        i = i+1
    
    if (inicio < fim):
        meio = math.floor((inicio+fim)/2)

        v = permutacaoRec(v, inicio, meio, '0')
        v = permutacaoRec(v, meio+1, fim, '1')

    return v

''' Recebe um vetor v
    Retorna a permutação de 0 e 1 com tamanho de v
    '''
def permutacao(n):
    m = 2**n

    v = []

    for i in range(m):
        v.append('')

    meio = math.floor((len(v)-1)/2)

    v = permutacaoRec(v, 0, meio, '0')
    v = permutacaoRec(v, meio+1, m-1, '1')

    return v

''' Recebe uma lista de genes a a função que regula eles
    Retorna a tabela de transição de cada gene da lista 
'''
def transicao(listaGenes, func):
    listaTransicao = []
    listaDeAtivacoes = listaAtivacao(listaGenes, func)

    # calcuala a permutação de 0 e 1 para simular cada gene ativo
    genesAtivos = permutacao(len(listaGenes))

    for gene in genesAtivos:
        geneTransicao = ''
        for ativacoes in listaDeAtivacoes:
            if gene in ativacoes:
                geneTransicao += '1'
            else:
                geneTransicao += '0'
        listaTransicao.append(geneTransicao)

    return genesAtivos, listaTransicao


''' Função main
    Faz as coisas rolarem
'''
def main():
    listaGenes, func = trataTexto()
    n = 2**len(listaGenes)

    genesAtivos, listaTransicao = transicao(listaGenes, func)

    print("\nTabela de Transição de Estados:")

    for i in range(n):
        print(genesAtivos[i], ' ', listaTransicao[i])


main()