

from typing import List,Dict,Tuple

class Metodos():
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
        #Retorna un booleano.
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
        #Return None
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
        #Return None
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
        #Return None
        if self.columnas == [] or self.filas == self.columnas:
            for i in self.filas:
                if  (i,i) not in self.set:
                    print(False)
                    return False
            #print(True)                           
            return True                     
        else:
            #print(False)
            return False 
    
    def Simetria(self) -> bool:
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Se verifica que si hay aRb tambien haya bRa, mediante un recorrido en el grafico de la relacion y 
        # condicionales que determinan si bRa se encuentra en la grafica tambien.
        #Return None
        
        if self.columnas == [] or self.filas == self.columnas:
            for i in self.set:
                if (i[1],i[0]) not in self.set:
                    #print(False)
                    return False
            #print(True)
            return True            
        else:
            #print(False)
            return False

    def Transitiva(self) -> bool: 
        #Autor: Jose Serrano Quesada
        # Realizado: 28/5/21
        #Va a probar si los valores dados son transitivos, mediante un recorrido con los valores grafico de la relacion, 
        # los condicionales determinaran si es transitiva mediante un True o falso mediante False.
        #Return Booleano.
        if self.columnas == [] or self.filas == self.columnas:
            for i1 in self.set:
                #Valor a buscar i1[0]
                for i2 in self.set:
                    #Buscamos bRc,si esta entonces buscamos aRc se encuentra en diccionario de tuplas.
                    if i1[1] == i2[0] and (i1[0],i2[1]) not in self.set:
                        #print(False)
                        return False

            #print(True)
            return True 
        
        else:
            #print(False)
            return False

    def es_equivalencia(self) -> bool:
        #Autor: Luis Andrés Alfaro Rojas.
        #Realizado: 15/6/2021.
        #Todo Funciona en su totalidad.
        #Return Un bool.
        transitiva = self.Transitiva()         
        simetrica = self.Simetria()
        reflexiva = self.Reflexiva()
        if transitiva & simetrica & reflexiva:
            #print(True)
            return True 
        else:
            #print(False)
            return False 

    def clase_equivalencia(self, x: int) -> list:

        claseDeEquivalencia = []
        for i in self.set:
            if i[0] == x and i[1] not in claseDeEquivalencia:
                claseDeEquivalencia.append(i[1])
        #print(claseDeEquivalencia)    
        return claseDeEquivalencia 

    def es_antisimetrica(self) -> bool:
        #Autor:Diego Carrillo, Jose Serrano(observación)
        #Realizado: 09/6/21 
        #Observación: antisimetría se puede cumplir incluso si la función también es simétrica.
        #Se hace un recorrido for del grafico de la relación donde mediante la contrapositiva se determina si es antisimétrica.
        for i in self.set:
            if (i[1],i[0]) in self.set and i[0] != i[1]: #Se produce la contrapositiva
                return False
        #print(True)    
        return True
    
    def es_orden(self)-> bool:
        if self.filas == self.columnas or self.columnas == []:
            if self.Transitiva() & self.Reflexiva() & self.es_antisimetrica():
                #print(True)
                return True
            else: 
                #print(False)
                return False

    def es_total(self)-> bool:
        # Autor: Katherine Amador González y Jose Serrano
        # Realizado: 09/06/21
        #Determina si la funcion es de orden, entonces puede ser total, mediante la contrapositiva de la relacion de orden, para determinar si es verdadera o falsa.
        #Return Booleano
        if self.filas == self.columnas or self.columnas == []:
            if self.es_orden() == True:
                for x in range(0, len(self.filas)):
                    for i in range(0, len(self.filas)):
                        if (self.filas[x], self.filas[i]) in self.set:
                            pass
                        elif (self.filas[i], self.filas[x]) in self.set:
                            pass
                        else:
                            #print(False)
                            return False
                #print(True)
                return True
        else:
            #print(False)
            return False
    
    def clases_equivalencia(self)->None:
        #Autora:Britany Alexandra Romero Hernández
        #Realizado: 15/6/21
        #Tiene como funcion devolver todas las clases de equivalencia de los elementos.
        # Return None 
        lista = list()
        for i in self.filas:
            x  = self.clase_equivalencia(i)
            x.sort()   
            lista.append(x)
        for i2 in range(len(lista)):
            print(f'{self.filas[i2]} = {lista[i2]}') 
        return 

    def __neg__(self)->list:
        #Autor:Diego Carrillo, Jose Serrano
        #Realizado: 15/6/21
        #Operador que tiene como funcion dar como resultado el complemento de la relacion
        #Se genera el universo para restarle la relacion que se le asigne.
        #Return Lista
        universo = list()
        if self.columnas == []:
            self.columnas = self.filas
        for i in self.filas:
            for i2 in self.columnas:
                if (i,i2) not in universo:
                    universo.append((i,i2))
        #Ya realizado el universo sigue realizar el complemento U-A
        
        for i3 in self.set:
            if i3 in universo:
                f = universo.index(i3)
                universo.pop(f)       
        #print(universo)
        return universo 
              
    def __invert__(self)->list:
        #Autor:Diego Carrillo, Jose Serrano
        #Realizado: 15/6/21
        #Funcion encargada de encontrar el inverso de la relacion asignada. Mediante "-" como operador.
        #Return Lista
        lista = list()
        for i in self.set:
            lista.append((i[1],i[0]))
        #print(lista)
        return lista            

    def __or__(self,otro: 'dict[tuple]')->list: #union
        #Autor: Jose Serrano Quesada
        #Realizado: 15/6/21
        #Funcion encargada de encontrar la union de 2 relaciones asignadas mediante "|"" como operador.    
        # Return Lista  
        lista = list()
        for i in self.set:
            lista.append(i)
        for i2 in otro.set:
            if i2 not in lista:
                lista.append(i2)
        return lista
        
    def __and__(self,otro: 'dict[tuple]')->list:
        #Autor: Jose Serrano Quesada
        #Realizado: 15/6/21
        #Funcion encargada de realizar la intersección de 2 relaciones. Mediante "&" como operador.
        #Parametro otro 
        #Return Lista
        lista = list()
        for i in self.set:
            if i in otro.set:
                lista.append(i)
        return lista
    
    def __sub__(self,otro: 'dict[tuple]')->list:
        #Autor: Jose Serrano Quesada
        #Realizado: 15/6/21        
        #Funcion encargada de realizar la subtraccion de una relacion. Mediante el operador "-" de tipo binario.
        #PARÁMETRO OTRO 
        lista = list()
        for i in self.set:
            if i not in otro.set:
                lista.append(i)
        return lista

    def __mul__(self,otro)->list:
        #Autor: Jose Serrano Quesada
        #Realizado: 15/6/21
        #Funcion encargada de realizar el complemento de B o A por ejemplo. Mediante el operador "*".
        #Parametro otro
        #Return Lista 
        lista = list()
        for i in otro.set:
            for i2 in self.set:
                if i[1] == i2[0]: #si el codominio de i es igual a el dominio de i2.
                    lista.append((i[0],i2[1]))    #Se genera la composicion de algun valor.
        return lista

    def __le__(self,otro)->bool:
        #Autor: Jose Serrano Quesada
        #Realizado: 15/6/21
        #Funcion encargada de determinar si la primera relacion es menor igual a la segunda. 
        # Se determina mediante el operador de comparacion "<=".
        #parametro otro
        #Return booleano
        x=len(self.set) 
        y=len(otro.set)

        if x<=y:
            return True
        else: 
            return False
        
    
#Ejemplos                       
A = Metodos([1, 2, 3, 4], [2, 4, 6, 8], {(1,2), (1,6), (2,4), (3,4), (3,6), (4,2), (4,8)})
B = Metodos([1, 2, 3, 4], [], {(1,1), (2,2), (3,3), (4,4)})
C = Metodos([1,2,3,4],[],{(1,1),(1,4),(2,2),(2,4),(3,3),(4,4)})
D = Metodos([1,2,3,4],[],{(1,1), (2,3),(2,4)})
E = Metodos([1,2,3],[],{(1,1),(2,2),(3,3),(1,2),(1,3),(2,3)})

#Ejemplos
#print(-A)
#print(~A)
#print(C-D)
#print(A<=B)
#print(A*D)

''' Ejemplos utilizados
A.Imprime_matriz()
print(f'\nReflexiva:\n{A.Reflexiva()}\nSimetría:\n{A.Simetria()}\nTransitiva:\n{A.Transitiva()}\nEquivalencia:\n{A.es_equivalencia()}\nClase de equivalencia de un número:\n{A.clase_equivalencia(2)}\nAntisimétrica:\n{A.es_antisimetrica()}\nOrden:\n{A.es_orden()}\nTotal:\n{A.es_total()}\nClases de equivalencia')
A.clases_equivalencia()

B.Imprime_matriz()
print(f'\nReflexiva:\n{B.Reflexiva()}\nSimetría:\n{B.Simetria()}\nTransitiva:\n{B.Transitiva()}\nEquivalencia:\n{B.es_equivalencia()}\nClase de equivalencia de un número:\n{B.clase_equivalencia(2)}\nAntisimétrica:\n{B.es_antisimetrica()}\nOrden:\n{B.es_orden()}\nTotal:\n{B.es_total()}\nClases de equivalencia')
B.clases_equivalencia()

C.Imprime_matriz()
print(f'\nReflexiva:\n{C.Reflexiva()}\nSimetría:\n{C.Simetria()}\nTransitiva:\n{C.Transitiva()}\nEquivalencia:\n{C.es_equivalencia()}\nClase de equivalencia de un número:\n{C.clase_equivalencia(2)}\nAntisimétrica:\n{C.es_antisimetrica()}\nOrden:\n{C.es_orden()}\nTotal:\n{C.es_total()}\nClases de equivalencia')
C.clases_equivalencia()

D.Imprime_matriz()
print(f'\nReflexiva:\n{D.Reflexiva()}\nSimetría:\n{D.Simetria()}\nTransitiva:\n{D.Transitiva()}\nEquivalencia:\n{D.es_equivalencia()}\nClase de equivalencia de un número:\n{D.clase_equivalencia(2)}\nAntisimétrica:\n{D.es_antisimetrica()}\nOrden:\n{D.es_orden()}\nTotal:\n{D.es_total()}\nClases de equivalencia')
D.clases_equivalencia()

E.Imprime_matriz()
print(f'\nReflexiva:\n{E.Reflexiva()}\nSimetría:\n{E.Simetria()}\nTransitiva:\n{E.Transitiva()}\nEquivalencia:\n{E.es_equivalencia()}\nClase de equivalencia de un número:\n{E.clase_equivalencia(2)}\nAntisimétrica:\n{E.es_antisimetrica()}\nOrden:\n{E.es_orden()}\nTotal:\n{E.es_total()}\nClases de equivalencia')
E.clases_equivalencia()
'''