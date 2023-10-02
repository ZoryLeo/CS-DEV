import random
dico = open("dicomot.txt","r")
listemot=dico.read().split(",")
mot ='test'


def pendu(mot):
    affichagemot = str(mot[0]+' _'*(len(mot)-1))
    affichagemot = affichagemot.split()
    print(affichagemot)
    erreur = 0
    while True :
        print(" ".join(affichagemot),"tu as déja fait ",erreur,"erreurs")
        lettre = input('choisis une lettre')
        if not lettre in mot :
            erreur += 1 
            if erreur == 8:
                return False
        for i in range(len(mot)) :
            if lettre == mot[i] :
                affichagemot[i] = lettre
        print(affichagemot.count("_"))
        if affichagemot.count('_') ==0 :
            return True
pendu('7')