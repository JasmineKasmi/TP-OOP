class Habitant:
    def __init__(self, nom, age, adresse, animaux=None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age > 130:
            raise ValueError("L'âge ne peut pas être négatif ni supérieur à 130.")
        else :
            self.__age = new_age

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, new_nom):
        self.__nom = new_nom

#question 1 ( accesseurs et mutateurs pour age )
    #def get_age(self):
    #   return self.__age

    #def set_age(self, new_age):
    #   self.__age = new_age

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, new_adresse):
        self.__adresse = new_adresse

    def get_animaux(self):
        return self.__animaux

    def set_animaux(self, new_animaux):
        self.__animaux = new_animaux

    def affichage_adresse(self):
        print(f"{self.get_nom()} habite à {self.get_adresse()}.")

    def compte_animal(self, animal):
        return self.get_animaux().get(animal, 0)

    
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

h1.age = 26
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass   
    