#leo zory 19 sept
#exo syracyuse

def syracuse(nombre):
    global tempsDeVol,nombreMax,meilleurtempsdevol
    tempsDeVol+= 1
    if nombre > nombreMax :
        nombreMax = nombre
    #on pllique les regles de la suite de syracuse
    if nombre%2 == 0 :
        nombre = nombre/2
    else :
        nombre = nombre*3 + 1 
    #si on arrive a autre chose que 1, on refait un tour
    if nombre != 1 :
        syracuse(nombre)
    if tempsDeVol>meilleurtempsdevol[0] :
        meilleurtempsdevol=(tempsDeVol,4)
    return tempsDeVol,nombreMax

nombreMax=0
tempsDeVol=0
meilleurtempsdevol=(0,'e')

syracuse(4)
for i in range(2,5):
    tempsDeVol=0
    syracuse(i)
print(meilleurtempsdevol)



