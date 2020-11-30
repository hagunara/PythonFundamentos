num1=int(input("Ingrese Primer Numero: "))
num2=int(input("Ingrese Segundo Numero: "))
num3=int(input("Ingrese Tercero Numero: "))

if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>num3:
    print(num2)
else:
    print(num3)