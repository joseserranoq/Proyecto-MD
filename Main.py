

from typing import List,Dict,Tuple

class Operaciones():
    def __init__(self,filas: 'list[int,str]',columnas: 'list[int,str]',set: 'dict[tuple]') -> None:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Es el iniciador de la clase, contiene los datos principales que se utilizaran en las funciones contenidas en esta clase.
        #Parametros: filas,columnas,set.
        #Return None
        self.filas = filas
        self.columnas = columnas
        self.set = set 
        return
        
    def make_column(self,c: 'list[int,str]') -> True:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Funcion auxiliar que se utiliza para disenar los valores que se encuentran en la columna.
        #Parametros: c --> contiene la lista con los valores de la columna.
        print(end='   ')    #Acomoda los datos mostrados en pantalla.
        for i in c:
            print('{}'.format(i),end='  ')  #Sirve para darle una posicion a los datos recorridos en el print.
        
        print('\n',end='  ')   
        
        for y in range(len(c)): #Crea unas lineas para distinguir los datos de la columna.
            print('{}'.format('───'),end='')
        print()
        return True
            
    def print_matrix(self,f: 'list[int,str]',c: 'list[int,str]',matriz: 'list[list[int]]') -> None:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Funcion auxiliar de la funcion Imprime_matriz(), ayuda a imprimir la matriz
        #Parametros: f va a conteneder los datos de self.filas
        #            c va a contener los datos de self.columnas
        #            matriz va a contener una lista con listas que contienen 1s y 0s donde se ubican los valores de la grafica de la relacion.
        x = False
        print()
        for i in range(0,len(f)):
            if x == False:
                x = self.make_column(c)
                
            print(f'{f[i]}[',end=' ')
            
            for j in range(0,len(c)):

                print('{}'.format(matriz[i][j]),end='  ')

            print(']')
        print()
        return

    def Imprime_matriz(self) -> None: #Mediante esta funcion se crea la lista matriz donde va otorgar el valor de 1 o 0 dependiendo de los valores que se encuentran en el conjunto
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Ayuda a la obtencion de los datos para la lista con listas; matriz, despues los 3 parametros son enviados a la funcion auxiliar print_matrix
        matriz: list[int,str] = list()
        if self.columnas == []:
            self.columnas = self.filas

        
        for i in range(0,len(self.filas)):
            matriz.append([])        
            for j in range(0,len(self.columnas)):
                if (self.filas[i],self.columnas[j]) in self.set:
                    val: int = 1                   
                else:
                    val: int = 0
                matriz[i].append(val)
        
        self.print_matrix(self.filas,self.columnas,matriz)
        return

    def Reflexiva(self) -> bool:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Se utiliza para saber si el conjunto asignado es reflexivo, se verifican que todos los elementos del dominio esten contenidos en la grafica de la relacion.
        if self.columnas == [] or self.filas == self.columnas:
            for i in self.filas:
                if  (i,i) in self.set:
                    pass
                
                else:
                    return print(False) 
                                       
            return print(True)                    
        else:
            return print(False)
    
    def Simetria(self) -> bool:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Se verifica que si hay aRb tambien haya bRa, mediante un recorrido en el grafico de la relacion y condicionales que determinan si bRa se encuentra en la grafica tambien.
        if self.columnas == [] or self.filas == self.columnas:
            for i in self.set:
                if i[0] == i[1]:
                    pass
                elif i[0] != i[1] and (i[1],i[0]) in self.set:
                    pass
                else:
                    return print(False)
            return print(True)

        else:
            return print(False)

    def Transitiva(self) -> bool: 
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Va a probar si los valores dados son transitivos, mediante un recorrido con los valores grafico de la relacion, los condicionales determinaran si es transitiva mediante un True o falso mediante False.
        if self.columnas == [] or self.filas == self.columnas:
            for i1 in self.set:
                #Valor a buscar i1[0]
                for i2 in self.set:
                    #Buscamos bRc,si esta entonces buscamos aRc se encuentra en diccionario de tuplas.
                    if i1[1] == i2[0] and (i1[0],i2[1]) in self.set:
                        pass
                    #Si el valor es diferente de aRi1[0] y i2[1]Rc.
                    elif i1[1] != i2[0]:
                        pass
                    else:
                        return print(False)
                return print(True)
        
        else:
            return print(False)

    def es_equivalencia(self) -> bool:
        transitiva = self.Transitiva()         
        simetrica = self.Simetria()
        reflexiva = self.Reflexiva()
        if transitiva & simetrica & reflexiva:
            return print(True)
        else:
            return print(False)

    def clase_equivalencia(self, x) -> list:
        claseDeEquivalencia = []
        for i in self.set:
            if i[0] == x and i[1] not in claseDeEquivalencia:
                claseDeEquivalencia.append(i[1])
            
        return print(claseDeEquivalencia)

    def es_antisimetrica(self) -> bool:
        if self.Simetria != True:

            return print(True)
        return print(False)       

                

                
A = Operaciones([1, 2, 3, 4], [2, 4, 6, 8], {(1,2), (1,6), (2,4), (3,4), (3,6), (4,2), (4,8)})
B = Operaciones([1, 2, 3, 4], [], {(1,1), (2,2), (3,3), (4,4)})
C = Operaciones([1,2,3,4],[],{(1,1),(1,4),(2,2),(2,4),(3,3),(4,4)})
D = Operaciones([1,2,3,4],[],{(1,1), (2,3)})
D.Simetria()
A.clase_equivalencia(1)
D.es_antisimetrica()
# A.Imprime_matriz()
# A.Reflexiva()
# A.Simetria()
# A.Transitiva()

# B.Imprime_matriz()
# B.Reflexiva()
# B.Simetria()
# B.Transitiva()

# C.Imprime_matriz()
# C.Reflexiva()
# C.Simetria()
# C.Transitiva()
