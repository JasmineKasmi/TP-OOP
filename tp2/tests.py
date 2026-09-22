import unittest
from habitant_privee import Habitant
from village import Village
from heritage import Adulte, Enfant



class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l'encapsulation."""

    def test_age_setter_valide(self):
        """Vérifie qu'on peut modifier l'âge avec une valeur valide."""
        h = Habitant("BOVO", 66, "Rue Elec", {"microcontroleurs": 3})

        h.age = 26

        self.assertEqual(h.age, 26)

    def test_age_setter_invalide(self):
        """Cas limite : âge négatif."""
        h = Habitant("BOVO", 66, "Rue Elec", {"microcontroleurs": 3})

        with self.assertRaises(ValueError):
            h.age = -5

    def test_compte_animal(self):
        """Vérifie le nombre d'animaux possédés."""
        h = Habitant("BOVO", 66, "Rue Elec", {"microcontroleurs": 3})

        self.assertEqual(h.compte_animal("microcontroleurs"), 3)

    def test_compte_animal_non_possede(self):
        """Cas limite : l'animal n'est pas possédé."""
        h = Habitant("BOVO", 66, "Rue Elec", {"microcontroleurs": 3})

        self.assertEqual(h.compte_animal("diode"), 0)





class TestVillage(unittest.TestCase):
    """Tests pour la composition et l'agrégation."""

    def test_ajouter_habitant_composition(self):
        """Vérifie que le village peut créer lui-même un habitant."""
        village = Village("PyPolytech")

        village.ajouter_habitant_composition("Plumet",78,"Rue ROB",{"fanuc": 3})

        self.assertEqual(len(village.get_habitants()), 1)
        self.assertEqual(village.get_habitants()[0].get_nom(),"Plumet")

    def test_ajouter_habitant_aggregation(self):
        """Vérifie qu'un habitant existant peut être ajouté au village."""
        village = Village("PyPolytech")

        habitant = Habitant("Pasqui",28,"Rue Meca",{"torseurs": 10})

        village.ajouter_habitant_aggregation(habitant)

        self.assertIn(habitant, village.get_habitants())

    def test_meme_habitant_dans_deux_villages(self):
        """Cas limite : le même habitant est dans deux villages."""
        village1 = Village("PyPolytech")
        village2 = Village("VillageVoisin")

        habitant = Habitant("Pasqui",28,"Rue Meca",{"torseurs": 10})

        village1.ajouter_habitant_aggregation(habitant)
        village2.ajouter_habitant_aggregation(habitant)

        self.assertIn(habitant, village1.get_habitants())
        self.assertIn(habitant, village2.get_habitants())

        


class TestHeritage(unittest.TestCase):
    """Tests pour l'héritage et le polymorphisme."""

    def test_retraite_adulte(self):
        """Vérifie le calcul des années avant la retraite."""
        adulte = Adulte("Carillet","Lilian",45,"Rue Solidworks")

        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(),17)

    def test_retraite_enfant(self):
        """Vérifie qu'un enfant ne peut pas calculer sa retraite."""
        enfant = Enfant("Kasmi","Jasmine",12,"Rue diplome")

        self.assertIn("enfant",enfant.calcul_nombre_annee_avant_retraite())

    def test_enfant_age_20(self):
        """Cas limite : un enfant de 20 ans doit provoquer une ValueError."""
        with self.assertRaises(ValueError):
            Enfant("Oups","Jasmine",20,"Rue C")




if __name__ == "__main__":
    unittest.main(verbosity=2)