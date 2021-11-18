## Exercício Programa 1 ######################################################
#  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,             #
#  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.             #
#  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM              #
#  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES               #
#  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA             #
#  OU PLÁGIO.                                                                 #
#  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS                     #
#  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A                       #
#  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E                    #
#  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS                #
#  DIVULGADOS NA PÁGINA DA DISCIPLINA.                                        #
#  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,                     #
#  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.              #
#                                                                             #
#  Nome : Miguel Pereira Ostrowski                                            #
#  NUSP : 10723610                                                            #
#  Turma: BCC                                                                 #
#  Prof.: Ronaldo                                                             #
###############################################################################

'''Referências aqui'''
#Para tratamento de arquivos
#https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html
'''
Exemplo de arquivo de entrada:

A,    !A&C
B,    !A&!B
C,    A&B

Exemplo de execução:

arquivo: exemplo.txt
atrator: ['000', '010'] tamanho da bacia: 5
atrator: ['001', '110'] tamanho da bacia: 3

'''
#seu código aqui

import copy
import math
import numpy as np



############################################### inicio cópia vpl's ##############################################


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


############################################### fim cópia vpl's ############################################## 

''' Trata os textos e os arquivos
    Retorna a lista de Genes e as funções reguladoras de cada uma deles
'''
def trataTexto():
    separadorGenes = ','
    separadorFuncOu = ' | '
    func = []

    arquivo = input("arquivo: ")
    
    print('\n')
    
    # gambiarra pra arrumar erro no teste automático
    #arquivo = arquivo[1:]

    texto = open(arquivo, 'r')

    listaGenes = []


    for linha in texto:
        gene = linha.split(separadorGenes)
        listaGenes.append(gene[0])
        func.append(gene[1].strip().split(separadorFuncOu))

    return listaGenes, func

''' Recebe dois vetores e verifica se eles são iguais
'''
def ehIgual(v1, v2):
    for i in range(len(v1)):
        if (v1[i] != v2[i]):
            return False
    return True

''' Recebe os atratores e um caminho
    Verfica se ao menos um atrator pertence ao gene
'''
def pertenceAoCaminho(atratores, caminho):
    for i in atratores:
        if (caminho[f[i]] == 1):
            return True
    return False


''' Recebe uma string estado (ex 011) e transforma em um inteiro único (possui unicidade)
    Usado para posição da matriz
'''
def f(estado):
    # identificador para a ultima posição do estado
    i = len(estado)-1
    #print(i)
    n = 0
    sum = 0
    while (i >= 0):
        if(estado[i] == '1'):
            sum += pow(2, n)
        i -= 1
        n += 1

    return sum

''' Recebe um caminho, com a ultima posição visitada dele 
    Retorna um ciclo
'''
def cicloRec(listaTransicao, pos, ciclo = []):
    if (len(ciclo) == 0):
        ciclo = np.zeros(len(listaTransicao))

    # verifica se a posição atual já foi visitado
    if (ciclo[f(pos)] == 0):
        # marca que a posição atual já foi visitada
        ciclo[f(pos)] = 1

        proximoPosicao = listaTransicao[f(pos)]

        return cicloRec(listaTransicao, proximoPosicao, ciclo)
    return ciclo

''' Recebe uma lista de Transição e uma posição para começar a procura
    Procura por ciclos no grafo
    Retorna respectivamente um caminho da posição atual até o ciclo e um ciclo
'''
def caminhoRec(listaTransicao, posicao ,  caminho = []):
    # gambiarra pra inicializar o caminho
    if(len(caminho) == 0):
        caminho = np.zeros(len(listaTransicao))

    # marca que a posição atual já foi visitada
    caminho[f(posicao)] = 1

    proximoPosicao = listaTransicao[f(posicao)]

    # verifica se o próximo "passo" já foi visitado
    if (caminho[f(proximoPosicao)] == 0):
        return caminhoRec(listaTransicao, proximoPosicao, caminho)

    ciclo = cicloRec(listaTransicao, proximoPosicao, [])

    return caminho, ciclo

''' Deixa os atratores na ordem pedida no enunciado
'''
def organizaAtratores(bacias, atratores):
    aux = atratores
    aux_bacia = bacias
    novo_atrator_ordenado = []
    nova_bacia = []

    for i in range(len(atratores)):
        menor = np.Infinity
        cont = 0
        for j in range(len(aux)):
            if(f(aux[j][0]) < menor):
                menor = f(aux[j][0])
                cont = j
        novo_atrator_ordenado.append(aux[cont])
        aux.pop(cont)
        nova_bacia.append(aux_bacia[cont])
        aux_bacia.pop(cont)

    return nova_bacia, novo_atrator_ordenado

''' Recebe todos os genes possíveis e a lista de transição gerada por esses genes
    Retorna as bacias de atração e suas respectivas atratores (ciclos)
'''
def BN(genesAtivos, listaTransicao):

    ciclos = []
    bacias = []
    
    for caminhoInicial in genesAtivos:
        rota = []
        atrator = []

        rota, atrator = caminhoRec(listaTransicao, caminhoInicial)

        encontrou = False

        # procura por ciclos que já foram adicionados antes
        for i in range(len(ciclos)):
            if ehIgual(ciclos[i], atrator):
                encontrou = True
                # obs.: ta muito caro
                for j in range(len(genesAtivos)):
                    # atualiza novos estados que não tinham sido visitados antes
                    if (rota[j] == 1 and bacias[i][j] == 0):
                        bacias[i][j] = 1

        # caso não tenha adiciona esse novo ciclo e uma nova bacia de atração
        if not encontrou:
            ciclos.append(atrator)
            bacias.append(rota)

    atratores = []

    # transforma os ciclos em estados
    for i in range(len(bacias)):
        atratores.append([])
        for j in range(len(genesAtivos)):
            if(ciclos[i][j] == 1):
                atratores[i].append(genesAtivos[j])

    return organizaAtratores(bacias, atratores)
            
def remontaAtratores(genesAtivos, listaTransicao, posicao, visitados = [], atrator = []):
    if (len(visitados) == 0):
        visitados = np.zeros(len(listaTransicao))

    if(visitados[f(posicao)] == 0):
        atrator.append(genesAtivos[f(posicao)])
        visitados[f(posicao)] = 1

        return remontaAtratores(genesAtivos, listaTransicao, listaTransicao[f(posicao)], visitados, atrator)
    return atrator


''' Função main
    Faz as coisas rolarem
'''
def main():
    listaGenes, func = trataTexto()
    
    genesAtivos, listaTransicao = transicao(listaGenes, func)

    bacias, atratores = BN(genesAtivos, listaTransicao)

    for i in range(len(bacias)):
        print('atrator: ', remontaAtratores(genesAtivos, listaTransicao, atratores[i][0], [], []), ' tamanho da bacia: ', int(sum(bacias[i])))

main()