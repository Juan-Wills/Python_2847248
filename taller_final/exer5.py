"""
Dados dos conjuntos de números, implementa funciones para:
· Encontrar elementos comunes (intersección)
· Encontrar elementos únicos de cada conjunto
· Crear un conjunto con todos los elementos (unión)
· Verificar si un conjunto es subconjunto del otro
"""
import random as rn
rn.seed(1)

def main():
   s1= set(rn.randrange(100) for _ in range(10))
   s2= set(rn.randrange(100) for _ in range(10))
   print(set_ops(s1, s2, 'subset'))

def set_ops(s1:set, s2:set, action:str):
    if action == 'inter':
        result= s1.intersection(s2)
    elif action == 'unique':
        result= s1.difference(s2)
    elif action == 'union':
        result= s1.union(s2)
    elif action == 'subset':
        result= s1.issubset(s2)

    return result

if __name__== '__main__':
    main()