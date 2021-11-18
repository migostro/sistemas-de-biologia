'''
Faça um programa que receba uma lista de genes e uma única função de regulação simples, 
que não contém o operador or (' | ') e imprima uma lista dos estados estados que podem ativar o suposto gene.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função: !A&B
['010', '011']

'''
import copy

''' Recebe uma lista de genes, o index do gene que queremos testar da lista de genes e sua respectiva função
    Retorna o estado com base na sua função '''
'''
def estado(listaGenes, gene):
    if (gene in listaGenes):
        #print("estado 0 ", gene)
        return 1
    else:
        #print("estado 1 ", func[1:len(func)])
        #print("estado 1 ", func[1:len(func)])
        return (estado(listaGenes, gene[1:len(gene)]) + 1)%2
'''
# adiciona val a todos estados de lista estados
def adicionaEstado(listaEstados, val):
    n = len(listaEstados)
    for j in range(n) :
        # adiciona val no final da lista
        listaEstados[j] += val

# retorna o index da func caso exista
# caso não exista retorna -1
def esta(gene, func):
    for i in range(len(func)):
        if gene in func[i]:
            return i
    return -1


def estado(gene):
    if '!' in gene:
        return '0'
    else:
        return '1'


def estados(listaGenes, func):
    listaEstados = ['']

    for i in range(len(listaGenes)):
        
        index = esta(listaGenes[i], func)
        #caso o gene tenha uma função definida
        # adiciona a tabela apenas o estado possivel
        if index != -1:
            adicionaEstado(listaEstados, estado(func[index]))
        # caso o genenão tenha função definida
        # adiciona os dois estados (duplica a tabela)
        else:
            lista0 = copy.deepcopy(listaEstados)
            lista1 = copy.deepcopy(listaEstados)
            
            adicionaEstado(lista0, '0')
            adicionaEstado(lista1, '1')

            # duplica a lista
            listaEstados = lista0 + lista1

    return listaEstados
        



def main():
    separadorGenes = ','
    separadorFunc = '&'

    #listaGenes = input().strip().split(separadorGenes)
    #func = input().strip().split(separadorFunc)

    listaGenes = ['x1', 'x2', 'x3', 'x4']
    func = ['x3']
    
    print("Nomes dos genes (separados por vírgula): ")
    print("Função: ")

    lista = estados(listaGenes, func)

    print(sorted(lista))

main()