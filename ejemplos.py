


'''
Utilicé como punto de referencia esta función 

def dibujaMatriz():
    filas = int(input('Introduce número de filas: '))
    columnas = int(input('Introduce número de columnas: '))
    
    #Se utiliza para realizar la matriz 
    matriz = list()
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor =  0   #'fila: {}: Columna:{}: '.format(i+1, j+1)
            matriz[i].append(valor)
    #Se utiliza para mostrar la matriz
    print()
    for fila in matriz:
        print('[', end=' ')
        for elemento in fila:
            print('{}'.format(elemento), end=' ')
        print(']')
    print()

#dibujaMatriz()
'''

A = [1,2,3,4]
B = ['a','b','c']
set = {(1,'a'),(3,'b'),(3,'c')}


#Esta función muestra los valores que posee cada columna según su posición.
def make_column(columna):
    print('   ',end='')
    for i in columna:
        print('{}'.format(i),end='  ') #Sirve para darle un orden a los valores
    
    print('\n',end='   ')
    
    for y in range(len(columna)):
        print('{}'.format('__'),end='  ')
    print()
    return True
  
#Se encarga de imprimir la matriz cuando esta ya sea completada con todos los valores
def print_matrix(filas,columnas,matriz):

    x = False
    print()
    for i in range(0,len(filas)):
        if x == False:
            x = make_column(columnas)
            
        print(f'{filas[i]}[',end=' ')
        
        for j in range(0,len(columnas)):

            print('{}'.format(matriz[i][j]),end='  ')

        print(']')
    print()
    return

#Se encarga de ingresar los valores en una lista con listas será la matriz, que al ser completada se muestra en pantalla
def Imprime_matriz(c1,c2,set):
    
    if c2 == []:    
        c2 = c1

    matriz = list()
    for i in range(0,len(c1)): 
        matriz.append([])        
        for j in range(0,len(c2)):
            if (c1[i],c2[j]) in set:
                val = 1                   
            else:
                val = 0
            matriz[i].append(val)
    
    print_matrix(c1,c2,matriz)
    return matriz

matriz= Imprime_matriz(A,B,set)
Imprime_matriz([1, 2, 3, 4], [2, 4, 6, 8], {(1,2), (1,6), (2,4), (3,4), (3,6), (4,2), (4,0)})
Imprime_matriz([1, 2, 3, 4], [], {(1,1), (2,2), (3,3), (4,4)})

