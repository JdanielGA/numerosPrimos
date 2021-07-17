def run ():
    bandera = 0

    while bandera < 3:
        menu = input("""
¡Bienvenido!

¿Desea consultar si un número es primo?
        
1 - Si.
2 - No.

Elija una opcion: """)

        if menu == '1':
            numero = int(input('Ingresa el número para evaluarlo: '))
            if evaluacion(numero):
                print('El número ' + str(numero) + ' Es un número primo')
            else:
                print('El número ' + str(numero) + ' No es un número primo')
        
        elif menu == '2':
            print('Gracias, hasta otra ocasión...')
            break

        else:
            print('No se escogió una opción valida. intente de nuevo')
            bandera += 1


if __name__=='__main__':
    run()