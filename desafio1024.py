from math import ceil 

n = int(input())

for i in range(n):
    m = str(input())
    m2 = ''

    #Primeiro passo
    for i in m: #Percorre cada caractere da msg
        if i.isalpha() == True: #Verifica se os caracteres são Texto 
            m2 += chr(ord(i) + 3) #caso for texto, soma +3 letras pra frente
        else:
            m2 += i #caso não texto, não faz nada

    #Segundo passo
    m3 = m2[::-1] #Inverte a mensagem criptografada.

    #Terceiro passo
    metade = ceil(len(m3) / 2)
    m4 = m3[-metade:]
    m5 = ''
    for i in m4:
        m5 += chr(ord(i) - 1)
    cripm = m3.replace(m4, m5)
    print(cripm)



        
