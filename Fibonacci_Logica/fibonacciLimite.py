def FibonacciLimite():
    #Receber o limite
    limite = 100
    try:
        limite = int(input("Digite um limite para a geração da Sequência de Fibonacci: "))
    except:
        limite = 100
    if limite < 0:
        limite = 100

    #Realizar o calculo
    numeros = [0,1]
    for indice,numero in enumerate(numeros):
        if numero <= limite:
            print(numero)
        else:
            break
        numeros.append(numeros[indice] + numeros[indice+1])
FibonacciLimite()    
#Verificar se o usuário deseja repetir
while True:
    continuar = input("Deseja verificar outro número? (Sim ou Não): ").lower()[0]
    if(continuar == 's'):
       FibonacciLimite()
    else:
        break
