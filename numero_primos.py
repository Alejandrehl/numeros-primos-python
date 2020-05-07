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
    if(numero == 2 or numero == 3):
        obtenerNumerosPrimos(numero)
    else:
        contador = 0
        if(numero % 2 == 0):
            return False
        else:
            for i in range(2, numero):
                if(numero % i == 0):
                    contador = contador + 1
            if(contador == 0):
                obtenerNumerosPrimos(numero)
            else:
                return False


esPrimo(input_numero)
