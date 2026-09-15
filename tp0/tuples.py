releve1=("vision supersonic",3.44,"deg")
releve2=("sensor de pression",1.25,"bar")
releve3=("force de hulk",10000.00,"N")

releves=[releve1,releve2,releve3]

def afficher_releves(tuples):
    a,b,c=tuples
    print(f"Capteur {a} : {b} {c}")

assert len(releves) == 3
assert releves[0][0] == "vision supersonic"
assert afficher_releves(releve1) == "Capteur vision supersonic : 3.44 deg"
afficher_releves(releve1) #quand je fait cet affichage j'ai le bon resultat mais le assert ne fonctionne pas


def recalibrer(list,capteur,val):

    for i in range(len(list)):
        if list[i][0]==capteur:
            list[i]=(list[i][0],val,list[i][2])
            return list

nouveaux_releves=recalibrer(releves,"vision supersonic",7.77)
assert nouveaux_releves[0] == ("vision supersonic", 7.77, "deg")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
            


