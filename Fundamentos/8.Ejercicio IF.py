#Ingrese mes del año en numerico y le proporcionaremos el mes escrito y la estacion del año
mes=int(input("Ingrese un numero de mes de año"))
print("El mes es:")

if mes==1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")    
elif mes == 9:
    print("Setiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("Numero ingresado invalido")

print("Y esta pertenece al: ")

if mes>=1 and mes <= 3:
    print("Invierno")
elif mes>=4 and mes<=6:
    print("Primavera")
elif mes>=7 and mes<=9:
    print("Verano")  
elif mes>=10 and mes<=12:
    print("Otoño")