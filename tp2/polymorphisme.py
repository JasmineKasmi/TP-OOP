from abc import ABC, abstractmethod

class Habitant(ABC):
    def __init__(self, nom, prenom, age, adresse):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        self.__adresse = adresse

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

    def get_prenom(self):
        return self.__prenom

    def set_prenom(self, new_prenom):
        self.__prenom = new_prenom

    def get_adresse(self):
        return self.__adresse
    
    def set_adresse(self, new_adresse):
        self.__adresse = new_adresse
    
    
    def affichage_adresse(self):
        print(f"{self.get_nom()} habite à {self.get_adresse()}.")
    
    def compte_animal(self, animal):
        return self.get_animaux().get(animal, 0)

    def __str__(self):
        return f"{self.get_nom()} {self.get_prenom()}, {self.age} ans, habite à {self.get_adresse()}."

    @abstractmethod

    def calcul_nombre_annee_avant_retraite(self):
        if self.age < 62:
            return 62 - self.age
        else:
            print("deja a la retraite")

class Adulte(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        super().__init__(nom, prenom, age, adresse)
        if self.age < 18:
            ValueError("L'adulte doit avoir au moins 18 ans.")
        

    def calcul_nombre_annee_avant_retraite(self):
        if self.age < 62:
            return 62 - self.age
        else:
            print("deja a la retraite")

class Enfant(Habitant):
    def __init__(self, nom, prenom, age, adresse):
        super().__init__(nom, prenom, age, adresse)
        if self.age >= 18:
            raise ValueError("L'enfant doit avoir moins de 18 ans.")
        

    def calcul_nombre_annee_avant_retraite(self):
            return "Erreur: un enfant ne peut pas calculer sa retraite"


def affichage(h: Habitant):
    message=str(h)
    print(message)

adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")
affichage(adulte)
affichage(enfant)

#Rendre alcul_nombre_annee_avant_retraite abstraite oblige chaque classe fille, comme Adulte ou Enfant, à définir sa propre version de la méthode, ce qui garantit que l'appel polymorphique dans affichage utilise toujours une méthode adaptée au type réel de l'objet.
 