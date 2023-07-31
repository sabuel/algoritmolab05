class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores) -> int:
        for i in range(len(valores)):
            #menor = valores[i]
            #maior = valores[i]
            #menorIndice = i
            menor = i
            for j in range(i+1, len(valores)):
                #if (valores[i] > valores[j]):
                    #menor = valores[j]
                    #valores[j] = valores[i]
                    #valores[i] = menor
                if (valores[j] < valores[menor]):
                    menor = j

            valores[i], valores[menor] = valores[menor], valores[i]
        return valores



    def ordene_insertion(self, valores):
        for i in range(1, len(valores)):
            atual = valores[i]
            j = i - 1
            while j >= 0 and atual < valores[j]:
                valores[j + 1] = valores[j]
                j -= 1
            valores[j + 1] = atual
        return valores

