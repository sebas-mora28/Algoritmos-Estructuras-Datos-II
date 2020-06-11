import math 


lista = [[4,6],[25,4],[8,7],[6,-8],[7,4],[15,14],[16,20]]





def closestPair(lista):
    lista.sort()
    return closestPair_aux(lista, len(lista))



def closestPair_aux(lista, leen):

    middle = leen//2;
    middle_value = lista[middle]


    left = closestPair_aux(lista[:middle], middle)
    right = closestPair_aux(lista[middle:], leen - middle)


    d = min(left, right)

    strip = []
    for i in range(len(lista)):
        if(abs(lista[i][0] - middle_value[0] < d)):
           strip.append(lista[i][0])

    return min(d, script_closest(strip, len(string), d))
  

           

def script_closest(strip, size, d):
    min_val = d

    strip.sort()


    for i in range(size):
        j = i +1
        while j < size and (strip[j][1] - strip[i][1] < min_val):
           min_val = dist(strip[i], strip[j])
           j+=1

    return min_val
    



def dist(point1, point2):
    return math.sqtr((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) 
           
                            
closestPair(lista)
    



