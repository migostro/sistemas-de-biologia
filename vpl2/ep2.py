'''
Faça um programa que receba uma lista de genes e uma função de regulação para cada gene 
com operadores not, and e or ('!', '&', ' | ') e imprima uma lista dos estados em que 
cada gene estará ativado. A ordem dos genes deverá ser a ordem dada na lista. 
Repare que o operador or está entre espaços que equivale a separar com parênteses. 
Por exemplo, '!A&C | B&C | !C' que equivale a (!A&C) | (B&C) | (!C). 
Não haverá parênteses nas expressões.
Para simplificar, consideraremos que as funções serão sempre nesse formato, 
sem encadeamentos sobrepostos difíceis de identificar. 

Em outras palavras: dá para fazer um split primeiro com ' | ' para separar os pedaços 
e depois use o que foi feito no exercício anterior para '&'. 
Repita para todos os genes. 
Se quiser usar outra implementação muito mais simples, utilize-a.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função para A: !A&C | B&C | !C
Função para B: !A&!B | C
Função para C: A&B
Estados que ativarão A: ['000', '001', '010', '011', '100', '110', '111']
Estados que ativarão B: ['000', '001', '011', '101', '111']
Estados que ativarão C: ['110', '111']

'''
import copy

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
    separadorFuncOu = ' | '
    separadorFuncE = '&'

    listaGenes = input("Nomes dos genes (separados por vírgula): ").strip().split(separadorGenes)

    func = []

    for i in range(len(listaGenes)):
        texto = "Função para " + listaGenes[i] + ": "
        func.append(input(texto).strip().split(separadorFuncOu))

    # faz a tabela de cada gene
    for i in range(len(func)):
        # estado parcial
        estadosFunc = []

        # j é cada função que tem apenas &
        for j in func[i]:
            estadosAux = estados(listaGenes, j.split(separadorFuncE))

            # procura por estados que ainda não estão em estadosFunc
            for k in estadosAux:

                if not k in estadosFunc:
                    estadosFunc.append(k)
        print("Estados que ativarão ", listaGenes[i], ": ", sorted(estadosFunc))


main()