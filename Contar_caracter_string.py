def contar_caracter(string):
    ordem = sorted(string)
    cont = 1
    anterior = ordem[0]
    
    for caracter in ordem[1:]:
        
        if caracter == anterior:
            cont += 1
            
        else:
            print(f'{anterior}: {cont}')
            anterior = caracter
            cont = 1
    print(f'{anterior}: {cont}')

           



contar_caracter('ronaldo')
