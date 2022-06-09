nombre = ""
while len(nombre) < 6:
    nombre = input("Indique su nombre y apellido: ") #Esto pide el nombre y apellido del usuario
    if len(nombre) > 6:
        break
    print("Tu nombre y apellido deberia ser mas largo")
HorasT = 0
while HorasT <= 0:
    HorasT = int(input("Indique las horas trabajadas: ")) #Esto pide las horas trabajadas
    if HorasT <= 0:
        print("Coloque un numero mayor que 0")
SueldoB = HorasT * 9500
SueldoIn = SueldoB #Aca se guarda el sueldo Bruto del trabajador
while True:
    print("1. Isapre")
    print("2. Fonasa")
    IsOrFon = int(input("Seleccione el numero correspondiente: "))
    if IsOrFon == 1 or IsOrFon == 2:
        break
if IsOrFon == 1:
    print("1. Mas vida");print("2. Consalud");print("3. Colmena");print("4. Banmedica");print("5. Cruz Blanca");print("6. Vida Tres")
    NumIs = int(input("Seleccione Su Isapre:")) 
    if NumIs == 1:
        DesIsapre = 32500 * 2
        SueldoB= SueldoB - DesIsapre
        Isapre = "Mas vida"
    elif NumIs == 2:
        DesIsapre = 32500 * 2
        SueldoB= SueldoB - DesIsapre
        Isapre = "Consalud"
    elif NumIs == 3:
        DesIsapre = 32500 * 2.11
        SueldoB= SueldoB - DesIsapre
        Isapre = "Colmena"
    elif NumIs == 4:
        DesIsapre = 32500 * 2.34
        SueldoB= SueldoB - DesIsapre
        Isapre = "Banmedica"
    elif NumIs == 5:
        DesIsapre = 32500 * 2.76
        SueldoB= SueldoB - DesIsapre
        Isapre = "Cruz Blanca"
    elif NumIs == 6:
        DesIsapre = 32500 * 2.78
        SueldoB= SueldoB - DesIsapre
        Isapre = "Vida Tres"
elif IsOrFon == 2:
    fonasa = SueldoIn * (7 / 100)
    SueldoB -= fonasa

else:
    print("Inicie de nuevo el programa")

desAFP = SueldoIn * 0.12
SueldoB -= desAFP
DesAFC = SueldoIn * (3 / 100)
SueldoB -= DesAFC
print("El Sueldo del Sr/a",nombre," Es:")
print("Sueldo Bruto: ",SueldoIn)
print("Sueldo Liquido: ", SueldoB)
print("Descuento AFP: ", desAFP)
print("Descuento AFC: ", DesAFC)
if IsOrFon == 1:
    print("El descuento de isapre es: ",DesIsapre)
else:
    import math
    fonasa = math.trunc(fonasa)
    print("El descuento de fonasa es:",fonasa )
