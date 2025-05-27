"""
Escribe una función que reciba una frase y retorne:
· La frase en mayúsculas
· La frase en minúsculas
· El número de palabras
· La frase con las palabras en orden inverso
"""
def main():
    text= "Today we are going to make history my fellas"
    print(formater(text, 'rev'))

def formater(text:str, format:str= 'std'):
    result= ''
    words= text.strip().split(' ')
    if format == 'upper':
        result= text.upper()
    elif format == 'lower':
        result= text.lower()
    elif format == 'lword':
        result= len(words)
    elif format == 'rev':
        words.reverse()
        for word in words:
            result+= f'{word} '
    else:
        result= text
    
    return result

if __name__=='__main__':
    main()