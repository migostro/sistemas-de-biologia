'''
Faça um programa que receba uma lista de genes e uma única função de regulação simples, 
que não contém o operador or (' | ') e imprima uma lista dos estados estados que podem ativar o suposto gene.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função: !A&B
['010', '011']

'''
# seu código aqui
''' Recebe uma lista de genes, o index do gene que queremos testar da lista de genes e sua respectiva função
    Retorna o estado com base na sua função '''
def estado(gene, func):
    if (gene == func):
        return 1
    else:
        return (estado(gene, func[1:len(func)]) + 1)%2


def estados(listaGenes, func):
    print(func)
    i = 0
    for g in listaGenes:
        if g in func:
            print(g)
            #print(estado(listaGenes, i, func))
        i += 1


def main():
    separadorFunc = '&'
    separadorGenes = ','

    listaGenes = input().split(separadorGenes)
    func = input().split(separadorFunc)

    #func = func.split(separador)

    #listaGenes = listaGenes.split(',')

    estados(listaGenes, func)

main()