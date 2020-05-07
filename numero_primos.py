input_numero = int(input("Ingrese un numero entero positivo-->"))
numeros_primos = []


def obtenerNumerosPrimos(numero_primo):
    i = 2

    while(len(numeros_primos) < numero_primo):

        if(i == 2 or i == 3):
            numeros_primos.append(i)
        else:
            contador = 0
            for j in range(2, i):
                if(i % j == 0):
                    contador = contador + 1
            if(contador == 0):
                numeros_primos.append(i)

        i = i + 1

    print(numeros_primos)


def esPrimo(numero):
    seguir = True
    newNumber = numero

    while (seguir):
        if (newNumber > 0):
            seguir = False
        else:
            newNumber = int(input("Ingrese un numero entero positivo-->"))

    if(newNumber == 2 or newNumber == 3):
        obtenerNumerosPrimos(newNumber)
    else:
        contador = 0
        if(newNumber % 2 == 0):
            return False
        else:
            for i in range(2, newNumber):
                if(newNumber % i == 0):
                    contador = contador + 1
            if(contador == 0):
                obtenerNumerosPrimos(newNumber)
            else:
                return False


esPrimo(input_numero)
