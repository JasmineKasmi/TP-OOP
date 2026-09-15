pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(dico, modele, piece):
    return dico[modele][piece] #faire return piece in list[modele] retourne vrai ou faux, c'est comme ca qu'on accede a la valeur

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(dico, modele, piece, nombre):
    dico[modele][piece]-=nombre
consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

def ajouter_modele(dico, modele, mot, capt, wheel):

    dico[modele]={"moteurs":mot, "capteurs":capt, "roues":wheel}
    
ajouter_modele(pieces_stock, "ModeleC",mot=4, capt=10, wheel=16)
assert pieces_stock["ModeleC"] == \
{"moteurs": 4, "capteurs": 10, "roues": 16}

def total_pieces(dico):
    moteurs=0
    capteurs=0
    roues=0
    for i in range (len(dico)):
        moteurs+=dico[list(dico.keys())[i]]["moteurs"]
        capteurs+=dico[list(dico.keys())[i]]["capteurs"]
        roues+=dico[list(dico.keys())[i]]["roues"]
    return {"moteurs":moteurs, "capteurs":capteurs, "roues":roues}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}




    