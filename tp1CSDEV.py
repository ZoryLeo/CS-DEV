def test_bisextile (anne):
    if anne%4==0 and anne%100!=0 or anne%400==0 :
        return True
    else :
        return False


def nb_jours(mois,anne):
    if not 0<mois<13 :
        return 'probleme de saisie'
    if mois==2 : 
        if test_bisextile(anne) == True : 
            return 29
        else:
            return 28
    for i in range(4):
        if mois==(2*i+1):
            return 31
        if i==3 :
            for j in range (3):
                if mois == 2*(i+1)+j*2 :
                    return 31
    for i in range(3):
        if mois == 4+i*2 and i<2 or mois == 4+i*2+1 and i==2 or mois == 4+i*2+1+i and i==2:
            return 30
        

def date_valide (jour,mois,anne):
    
    if mois == 2:
        if 0<jour<29 or jour == 29 and test_bisextile(anne) == True:
            return 'date valide'
    elif 0<jour<nb_jours(mois,anne):
            return 'date valide'
    
    return 'date non valide'

def mesImpots(revenu):
    if 

