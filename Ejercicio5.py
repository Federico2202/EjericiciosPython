peso = float ( input ("Digite su peso en kg "))
altura = float ( input ("Digite su altura en Mts "))
total = (peso/(altura*altura))
print("")


if total<=18.5:
    print("Usted esta bajo de peso con un IMC de: ",total)
elif total>=18.5 and total<=24.9:
    print("Usted esta con un peso Normal con un IMC de: ",total)
elif total>=25 and total<=29.9:
    print ("Usted esta de Sobre Peso con un IMC de: ",total)
elif total>=30 and total<=34.9:
    print ("Usted tiene una obesida tipo I con un IMC de: ",total)
elif total>=35 and total<=39.9:
    print ("Usted tiene una obesida tipo II con un IMC de: ",total)
elif total>=40 and total<=49.9:
    print ("Usted tiene una obesida tipo III con un IMC de: ",total)
elif total>=50:
    print ("Usted tiene una obesida tipo IV con un IMC de: ",total)
