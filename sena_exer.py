def main():
    user_str= input('Submit a string: ').replace(' ', '')
    counter(user_str)

def counter(user_answ):
    upper,lower= 0,0
    for char in user_answ:
        if char.isupper():
            upper+=1
        else:
            lower+=1
    return print(f'Upper Case: {upper} \nLower Case: {lower}')

main()