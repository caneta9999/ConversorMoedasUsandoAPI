def VerificarHappyNumber():
    #Serve para evitar um loop infinito caso o número não seja um "Happy Number"
    numerosPassados = []

    #Receber o número passado pelo usuário
    numero = 1
    try:
        numero = int(input("Digite um número inteiro e positivo: "))
    except:
        numero = 1
    if numero < 1:
        numero = 1
    numeroOriginal = numero
    numerosPassados.append(numeroOriginal)
    
    #Verificando se é um "Happy Number"
    print(f'Verificando se {numeroOriginal} é um Happy Number')
    while numero != 1:
        numeroNovo = 0
        while True:
            if numero > 9:
                numeroNovo += (numero%10)**2
                numero = numero // 10
            else:
                numeroNovo += numero**2
                break
        numero = numeroNovo
        if numero in numerosPassados:
            print(f'{numeroOriginal} não é um Happy Number!')
            break
        numerosPassados.append(numero)
    if numero == 1:
        print(f'{numeroOriginal} é um Happy Number!')
VerificarHappyNumber()

#Verificar se o usuário deseja verificar outro número
while True:
    continuar = input("Deseja verificar outro número? (Sim ou Não): ").upper()[0]
    if(continuar == 'S'):
       VerificarHappyNumber()
    else:
        break
