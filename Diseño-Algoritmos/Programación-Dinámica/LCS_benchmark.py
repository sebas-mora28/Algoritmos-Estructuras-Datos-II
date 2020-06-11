from time import time


"""

SUBSTRING MAS LARGO Divide y Conquista 

"""

def LCS_recursivo(string1, string2):
    return LCS_recursivo_aux(string1, string2, len(string1), len(string2))



def LCS_recursivo_aux(string1, string2, size1, size2):
    if(size1 == 0 or size2 == 0):
        return 0
    if(string1[size1-1] == string2[size2-1]):
        return 1 + LCS_recursivo_aux(string1, string2, size1-1, size2-1)
    else:
        return max(LCS_recursivo_aux(string1, string2, size1, size2-1), LCS_recursivo_aux(string1, string2, size1-1, size2))





"""

SUBSTRING MAS LARGO APLICANDO PROGRAMACION DINAMICA


"""

def LCS(string1, string2):
    return LCS_aux(string1, string2, len(string1), len(string2))



def LCS_aux(string1, string2, size1, size2):
    lista = getEmptyArray(size1 +1, size2+1)
    for i in range(size1+1):
        for j in range(size2 +1):

            if(i == 0 or j == 0):
                lista[i][j]= 0
                
            elif(string1[i-1] == string2[j-1]):
                lista[i][j] = lista[i-1][j-1] + 1
            else:
                lista[i][j] = max(lista[i-1][j], lista[i][j-1])

    return lista[size1][size2]
                

def getEmptyArray(row, columns):
    lista = []
    for i in range(0,row):
        lista.append([0]*columns)

    return lista






"""
          BENCHMARK


"""


def tiempo_ejecucion_LCS_recursivo(string1, string2):
    inicial = time();
    LCS_recursivo(string1, string2)
    final = time();
    return final - inicial



def tiempo_ejecucion_LCS_programacion_dinamica(string1, string2):
    inicial = time();
    LCS(string1, string2)
    final = time();
    return final - inicial







"""
 PRIMERA PRUEBA
"""
print(tiempo_ejecucion_LCS_recursivo("tofoofie", "toody"))
print(tiempo_ejecucion_LCS_programacion_dinamica("tofoofie", "toody"))
print();


"""
SEGUNDA PRUEBA
"""

print(tiempo_ejecucion_LCS_recursivo("abcas", "baba"))
print(tiempo_ejecucion_LCS_programacion_dinamica("abcas", "baca"))
print()



"""
TERCERA PRUEBA

"""
print(tiempo_ejecucion_LCS_recursivo("ssffkkttff", "xxmmyykk"))
print(tiempo_ejecucion_LCS_programacion_dinamica("ssffkkttff", "xxmmyykk"))
print()



"""
CUARTA PRUEBA

"""

print(tiempo_ejecucion_LCS_recursivo("dffdfogergdgddttt", "mdftttdsdszcx"))
print(tiempo_ejecucion_LCS_programacion_dinamica("dffdfogergdgddttt", "mdftttdsdszcx"))
print()



"""
 RESULTADOS DEL BENCHMARK


 SE REALIZARON CUATRO PRUEBAS DISTINTAS EN CON STRING DIFERENTES PARA CALCULAR EL TIEMPO DE EJECUCION ENTRE LOS DOS ENFOQUES PARA
 RESOLVER EL PROBLEMA:

            Dividi y conquista              Programación dinámica 

             1. 0.0007684  s                 1. 0.00009870  s
             2. 0.0000605  s                 2. 0.00006628  s
             3. 0.0263872  s                 3. 0.00005459  s
             4. 5.1695387  s                 4. 0.00025415  s


  Como podemos observar y como se esperaba la programación dinámica es más eficiente en tiempo de ejecución, sin embargo, en resultados
  pequeños como el caso de la segunda prueba observamos que los resultados fueron bastantes similares, no así en las cadenas de string
  mas largos, donde la programación dinámica fue más eficiente. 


  En la cuarta prueba observemos que existen una gran diferencia de tiempo entre los dos enfoques

"""














