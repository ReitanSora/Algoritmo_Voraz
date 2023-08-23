class Ordenamiento:
    #función para ordenar la lista de elementos que le llegase
    def quicksort(self, arreglo: list, elemento:int):
        if len(arreglo) <= 1:
            return arreglo
        pivote = arreglo[len(arreglo)//2]
        left = [x for x in arreglo if x[elemento] < pivote[elemento]]
        middle = [x for x in arreglo if x[elemento] == pivote[elemento]]
        right = [x for x in arreglo if x[elemento] > pivote[elemento]]
        return self.quicksort(left, elemento) + middle + self.quicksort(right, elemento)
    
    def bubblesort(self, lista: list, elemento: int):
        for i in range(len(lista)-1, -1, -1):
            ordenado = False
            for j in range(i):
                if lista[j][elemento] < lista[j+1][elemento]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    ordenado = True
            if not ordenado:
                break

        return lista
    
    def ordenar_quick(self, lista: list):
        self.quicksort(lista, 1)
    
    def ordenar_burbuja(self, lista: list):
        self.bubblesort(lista, 1)