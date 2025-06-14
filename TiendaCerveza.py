Seguir=True
ConsumenLicor=0
MujeresMenores=0
HombresNoAguardiente=0
TomanCerveza=0
PromedioEdadCerveza=0
TomaWhisky=0
PorcentajeWhiskyEncuestados=0
TotalEncuestados=0
while Seguir:
    respuesta = int(input("Ingrese 1 para continuar o 0 para salir: "))
    if respuesta == 0:
        Seguir = False
        break
    TotalEncuestados += 1
    ConsumeLicor=int(input("¿Consume licor? (1-Si, 2-No): "))
    if ConsumeLicor == 1:
        ConsumenLicor += 1
        Genero=int(input("¿Género? (1-Mujer, 2-Hombre): "))
        if Genero == 1:
            EdadMujer=int(input("¿Ingrese la edad: "))
            if EdadMujer < 18:
                MujeresMenores += 1
            LicorPreferido=int(input("¿Licor preferido? (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila. 5-Whisky, 6-Otro): "))
            if LicorPreferido == 3:
                TomanCerveza += 1
                PromedioEdadCerveza += EdadMujer
                PromedioEdadCerveza = PromedioEdadCerveza/TomanCerveza
            elif LicorPreferido == 5:
                TomaWhisky += 1
        elif Genero == 2:
            EdadHombre=int(input("¿Ingrese la edad: "))
            LicorPreferido=int(input("¿Licor preferido? (1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila. 5-Whisky, 6-Otro): "))
            if LicorPreferido != 1 and EdadHombre >= 20 and EdadHombre <= 25:
                HombresNoAguardiente += 1
            if LicorPreferido == 3:
                    PromedioEdadCerveza += EdadHombre
                    PromedioEdadCerveza = PromedioEdadCerveza/TomanCerveza 
            elif LicorPreferido == 5:
                TomaWhisky += 1

    elif ConsumeLicor == 2:
        Genero=int(input("¿Género? (1-Mujer, 2-Hombre): "))
        if Genero == 1:
            EdadMujer=int(input("¿Ingrese la edad: "))
            if EdadMujer < 18:
                MujeresMenores += 1
        elif Genero == 2:
            EdadHombre=int(input("¿Ingrese la edad: "))
            if EdadHombre >= 20 and EdadHombre <= 25:
                HombresNoAguardiente += 1

PorcentajeWhiskyEncuestados +=  (TomaWhisky / TotalEncuestados) * 100               

print("Total de personas que consumen licor:", ConsumenLicor)
print("Total de mujeres menores de edad:", MujeresMenores)
print("Total de hombres que no consumen aguardiente:", HombresNoAguardiente)
print("Promedio de edad de las personas que consumen cerveza:", PromedioEdadCerveza)
print("Porcentaje de personas que consumen whisky:", PorcentajeWhiskyEncuestados)       
    

        



