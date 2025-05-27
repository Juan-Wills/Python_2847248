"""
Crea una función que reciba una tupla con coordenadas (x, y) de varios puntos y retorne:
· El punto más cercano al origen (0,0)
· La distancia promedio de todos los puntos al origen
"""
from math import sqrt

def main():
    coor= [(2,3), (2,7), (0,0), (-9,7), (0,1), (-5,-5)]
    print(tup_ops(coor, 'avg_orig'))

def tup_ops(coor:list, operation:str):
    if operation == 'near_orig':
        total=[]
        for x,y in coor:
            total.append(sqrt((x**2 + y**2)))
        i= total.index(min(total)) 
        result= coor[i]

    elif operation == 'avg_orig':
        total= int()
        for x,y in coor:
            total+= sqrt((x**2 + y**2))
        result= f'{total/len(coor):.2f}'

    return result

if __name__== '__main__':
    main()