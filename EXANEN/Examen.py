#Brandon de Jesus Garza Jasso  250218
#se realozaran votaciones en un grupo de 15 alumnos (1er lugar y 2do lugar)
#Hugo Paco y Luis son candidatos para : --Jefe de grupo, tesorero--
# y el tercer lugar se le daran las gracias por participar
#--Todos los alumnos deben votar por algun candidato
#--Al final debe mostrar los ganadores, su puesto , cuantos votos y porcentaje

print(f"---Votaciones para candidato \nH.Hugo. \nL.Luis \nP.Paco----")

votos_Hugo=0
votos_Luis= 0
votos_Paco=0
suma_votos=0
hmayor_votos=None
hmenor_votos=None
porcentaj_paco= 0
porcentaj_hugo=0
porcentaj_luis=0

for i in range (1,16):
    while True: 
        voto=input(f"Ingrese su participante a votar alumno {i} :  ").strip().upper()
        
        if voto in [ "H","L", "P"]:
            break
        else:
            print("Ingrese su voto valido porfavor")

    if voto == "H":
            votos_Hugo +=1
            suma_votos += 1
        
    if voto == "L":
            votos_Luis += 1
            suma_votos += 1

    if voto == "P":
            votos_Paco += 1
            suma_votos += 1

porcentaj_paco = (votos_Paco / 15) * 100
porcentaj_hugo = (votos_Hugo / 15) * 100
porcentaj_luis = (votos_Luis / 15) * 100

if votos_Hugo > votos_Luis and votos_Hugo > votos_Paco:
    print(f"\nJefe de Grupo es Hugo con :{votos_Hugo} votos y su porcentaje : {porcentaj_hugo}")
    if votos_Luis > votos_Paco:
         print(f"El Tesorero es Luis con :{votos_Luis} votos y su porcentaje : {porcentaj_luis} \nPaco gracias por participar")
    else:
        votos_Paco > votos_Luis
        print(f"El Tesorero es Paco con : {votos_Paco} votos y su porcentaje : {porcentaj_paco} \nLuis gracias por participar")


if votos_Paco > votos_Hugo and votos_Paco > votos_Luis:
    print(f"\nJefe de Grupo es Paco con :{votos_Paco} votos y su porcentaje : {porcentaj_paco}")
    if votos_Luis > votos_Hugo:
         print(f"El Tesorero es Luis con :{votos_Luis} votos y su porcentaje : {porcentaj_luis} \n Hugo gracias por participar")
    else:
        votos_Hugo > votos_Luis
        print(f"El Tesorero es Hugo con : {votos_Hugo} votos y su porcentaje : {porcentaj_hugo} \n luis gracias por participar")

if votos_Luis > votos_Hugo and votos_Luis > votos_Paco:
    print(f"\nEl jefe de grupo es Luis con : {votos_Luis} y su porcentaje : {porcentaj_luis}")
    if votos_Hugo > votos_Paco:
         print(f"El Tesorero es Luis con :{votos_Luis} votos y su porcentaje : {porcentaj_luis} \npaco gracias por participar")
    else:
        votos_Paco > votos_Hugo
        print(f"El Tesorero es Paco con : {votos_Paco} votos y su porcentaje : {porcentaj_paco}\nHugo gracias por participar")

if votos_Hugo == votos_Luis:
     print(f"Hay un empate por parte de Hugo {votos_Hugo} y porcentaje:{porcentaj_hugo} y  Luis {votos_Luis} y porcentaje{porcentaj_luis}")

if votos_Paco == votos_Luis:
    print(f"Hay un empate por parte de Paco {votos_Paco}: y porcentaje {porcentaj_paco} y  Luis {votos_Luis} y porcentaje{porcentaj_luis}")
if votos_Hugo == votos_Paco:
    print(f"Hay un empate por parte de Hugo {votos_Hugo}: y porcentaje{porcentaj_hugo} y Paco {votos_Paco} y porcentaje{porcentaj_paco}")





print(f"votos Hugo {votos_Hugo} y su porcentaje: {porcentaj_hugo}")
print(f"votos Luis {votos_Luis} y su porcentaje: {porcentaj_luis}")
print(f"votos Paco {votos_Paco} y su porcentaje: {porcentaj_paco}")
print(f"Total votos: {suma_votos}")


    
        


    
