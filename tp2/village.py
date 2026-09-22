from habitant_privee import Habitant

class Village:
    def __init__(self, nom):
        self.__nom = nom
        self.__habitants = []

    def get_nom(self):
        return self.__nom

    def set_nom(self, new_nom):
        self.__nom = new_nom

    def get_habitants(self):
        return self.__habitants
    
    def set_habitants(self, new_habitants):
        self.__habitants = new_habitants
    
    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        nouvel_habitant = Habitant(nom, age, adresse, animaux)
        self.get_habitants().append(nouvel_habitant)

    def ajouter_habitant_aggregation(self, habitant):
        self.get_habitants().append(habitant)

    def afficher_habitants(self):
        i=0
        for habitant in self.get_habitants():
            print(f"Nom de l'habitant {i + 1}: {habitant.get_nom()}")
            i += 1

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_aggregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_aggregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
#La composition correspond à ajouter_habitant_composition car le village crée directement le nouvel habitant.
#L’agrégation correspond à ajouter_habitant_aggregation car le village reçoit un habitant qui existe déjà et peut donc être associé à plusieurs villages.