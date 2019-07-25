numero = int( input ("Digite numero 1 "))
numero2 = int ( input ("Digite numero 2 "))
print("")
operacion = int (input ("Digite -->[1] para suma, para resta -->[2], para multiplicion -->[3], para dividir -->[4] "))
print("")

if operacion==1:
    print("La suma es: ", (numero+numero2))
elif operacion==2:
    print("La resta es: ", (numero-numero2))
elif operacion==3:
    print("La multiplicacion es: ", (numero*numero2))
elif operacion==4:
    print ("La division es: ", (numero/numero2))
else:
    print("por favor digite un numero VALIDO!")

