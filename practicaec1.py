aprobado = 0 
aplazado = 0 
reprobado = 0 
for i in range (15) :   
    nota = float (input("Digite su nota final:\n"))
    if nota >= 70 :
        print ("Felicidades, ha aprobado")
        aprobado += 1
    elif nota >= 60 and  nota < 70 :
        print ("Usted está aplazado")
        aplazado += 1 
    else : 
        print ("Usted está reprobado")
        reprobado += 1 
print ("Cantidad de estudiandtes aprobados: ", aprobado)
print ("Cantidad de estudiandtes aprobados: ", aplazado)
print ("Cantidad de estudiandtes aprobados: ", reprobado)

