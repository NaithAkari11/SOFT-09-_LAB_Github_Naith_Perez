
#ejercicio 1
poblacionHormigas=int(input("Ingrese la población inicial de hormigas: "))
cantidadMeses=int(input("Ingrese la cantidad de meses: "))

for mes in range(1, cantidadMeses + 1):
    
    if poblacionHormigas > 28000:
        tasaCrecimiento=0.30
    else:
        tasaCrecimiento=0.40  
    
    poblacionHormigas = poblacionHormigas + (poblacionHormigas * tasaCrecimiento)
    
    if poblacionHormigas < 7000:
        poblacionHormigas = 0
    else:
        poblacionHormigas = poblacionHormigas - 7000
        
    poblacionHormigas = int(poblacionHormigas)

print(f"\nLa población final después de {cantidadMeses} meses es de: {poblacionHormigas} hormigas.")

#Ejercicio 2
print("Vienvenido al cajero automatico:")
claveDigitada=input("Ingresa la clave: ")
clave="6N79"
contador=0
saldo=10000
salir=False 


while len(claveDigitada) != 4 or (claveDigitada != clave and contador < 2):
    if len(claveDigitada) != 4:
        print("Error: La clave debe tener exactamente 4 caracteres.\n")
    else:
        print("Clave incorecta:\n")
    contador+= 1
    
    claveDigitada=input("Ingresa la clave otra vez: ")

if claveDigitada==clave:
    print("Acceso concedido")
    
    while salir != True:
        opcion=int(input(f"\tMenu\n1.Consulta saldo\n2.Retirar\n3.Depositar\n4.Salir\nOpcion: "))
        
        if opcion == 1:
            print(f"Saldo disponible es de {saldo}")
            
        elif opcion == 2:
            retiro=int(input("Ingresa el monto a retirar: "))
            if retiro > 0 and retiro <= saldo:
                saldo=saldo-retiro
                print(f"Retiro completado: monto retirado {retiro}")
            else:
                while retiro <= 0 or retiro > saldo:
                    print("Saldo no disponible o monto inválido")
                    retiro=int(input("Ingresa el monto denuevo: "))
                saldo=saldo-retiro
                
        elif opcion == 3:
            num=int(input("Ingresa el monto a depositar: "))
            saldo=saldo+num
            print(f"Monto depositado\nNuevo saldo: {saldo}")
            
        elif opcion == 4:
            break
        else:
            print("Error: opcion no esta en el menu")
        
        num2=int(input("Ingresa 1 si quieres salir o 2 si no quieres salir: "))
        if num2 == 1:
            salir=True
        retiro=0
        num2=0
        num=0
        
            
else:
    print("Cajero bloqueado")

print("Proceso finalizado")


#Ejercicio 3

nombreEstudiante=input("Ingrese el nombre del estudiante: ")
notaMatematicas=float(input("Ingrese la nota de Matematicas: "))
notaFisica=float(input("Ingrese la nota de Fisica: "))
notaSociales=float(input("Ingrese la nota de Sociales: "))
notaCiencias=float(input("Ingrese la nota de Ciencias: "))
notaEspanol=float(input("Ingrese la nota de Español: "))

promedioCursos=(notaMatematicas + notaFisica + notaSociales + notaCiencias + notaEspanol) / 5

puntosExtras=0
puedeOptar=False

if notaMatematicas > 90 and notaFisica > 90:
    puedeOptar = True
    if promedioCursos > 90:
        puntosExtras=10  
    elif promedioCursos >= 88:
        puntosExtras=7   
    elif promedioCursos >= 85:
        puntosExtras=4 
    else:
        puntosExtras=0

print(f"\nEstudiante: {nombreEstudiante}\nSu promedio es de {promedioCursos}")
if puedeOptar:
    if puntosExtras > 0:
        print(f"El estudiante puede optar por puntos extras\nCantidad de puntos obtenidos: {puntosExtras}")
    else:
        print("El estudiante cumple la condición de materias, pero su clasificación (D) otorga 0 puntos extras")
else:
    print("El estudiante NO puede optar por los puntos extras (No superó los 90 en Matemáticas y Física)") 

#Ejercicio 4
diaActual=int(input("Ingrese el dia de hoy: "))
mesActual=int(input("Ingrese el mes actual (1-12): "))
anioActual=int(input("Ingrese el año actual: "))

diaSiguiente=diaActual + 1
mesSiguiente=mesActual
anioSiguiente=anioActual

diasDelMes=0

if mesActual == 2:
    diasDelMes=28
elif mesActual == 4 or mesActual == 6 or mesActual == 9 or mesActual == 11:
    diasDelMes=30
else:
    diasDelMes=31


if diaSiguiente > diasDelMes:
    diaSiguiente=1
    mesSiguiente = mesActual + 1
    
    if mesSiguiente > 12:
        mesSiguiente=1
        anioSiguiente=anioActual + 1

print(f"\nLa fecha de mañana es: {diaSiguiente}/{mesSiguiente}/{anioSiguiente}")

#Ejecicio 5
diaActual=int(input("Ingrese el día de hoy: "))
mesActual=int(input("Ingrese el mes actual (1-12): "))
anioActual=int(input("Ingrese el año actual: "))


diaCalculado=diaActual
mesCalculado=mesActual
anioCalculado=anioActual


for i in range(8):
    diaCalculado += 1
    
    diasDelMes = 0
    if mesCalculado == 2:
        diasDelMes = 28
    elif mesCalculado == 4 or mesCalculado == 6 or mesCalculado == 9 or mesCalculado == 11:
        diasDelMes = 30
    else:
        diasDelMes = 31
        
    if diaCalculado > diasDelMes:
        diaCalculado = 1
        mesCalculado += 1
        if mesCalculado > 12:
            mesCalculado = 1
            anioCalculado += 1
print(f"\nLa fecha dentro de 8 días será: {diaCalculado}/{mesCalculado}/{anioCalculado}")


































