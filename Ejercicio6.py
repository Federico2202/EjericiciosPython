edad = int(input("Ingrese su edad: "))
genero = input ("digite su genero [H]--> Hombre , [M]--> Mujer: ")

if edad>=18:
    if genero in 'Hh':
        print ("Señor, Usted es mayor de edad")
    elif genero in 'Mm':
        print ("Señorita, Usted es mayor de edad")
    else:
        print ("*****!ERROR¡*****")
else:
    if genero in 'Mm':
        print ("Señora, Usted es menor de edad")
    elif genero in 'Hh':
        print ("Señor, Usted es menor de edad")
    else:
        print("*****!ERROR¡*****")
        
