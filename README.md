# TP-OOP - Travaux Pratiques en Programmation Orientée Objet

Bienvenue ! Ce repo contient les travaux pratiques pour l'apprentissage des structures de données et concepts fondamentaux en Python.

## 📁 Structure du projet

### `TP0/` - Structures de Données Fondamentales

#### `tuples.py`
Travail avec les **tuples** et les capteurs :
- **`afficher_releves(tuples)`** : Affiche les informations d'un capteur (nom, valeur, unité)
- **`recalibrer(list, capteur, val)`** : Recalibre la valeur d'un capteur spécifique
- Données d'exemple : capteurs de vision, de pression et force

#### `ensembles.py`
Travail avec les **ensembles (sets)** et les robots :
- **`robots_double_mission(ens1, ens2)`** : Robots en mission d'exploration ET de transport (intersection)
- **`robots_toutes_missions(ens1, ens2)`** : Tous les robots de toutes les missions (union)
- **`robots_exploration_seule(ens1, ens2)`** : Robots en exploration uniquement (différence)
- **`ajouter_robot_mission(ens, mission)`** : Ajoute un robot à une mission
- **`retirer_robot_mission(ens, mission)`** : Retire un robot d'une mission
- Données d'exemple : robots d'exploration et de transport

#### `dictionnaire.py`
Travail avec les **dictionnaires** et la gestion de stock :
- **`quantite_piece(dico, modele, piece)`** : Récupère la quantité d'une pièce pour un modèle
- **`consommer_piece(dico, modele, piece, nombre)`** : Consomme/réduit la quantité d'une pièce
- **`ajouter_modele(dico, modele, mot, capt, wheel)`** : Ajoute un nouveau modèle au stock
- **`total_pieces(dico)`** : Calcule les totaux de tous les types de pièces
- Données d'exemple : stock de pièces pour différents modèles (moteurs, capteurs, roues)

---

## 🚀 Comment lancer le code

### Prérequis
- Python 3.6+

### Option 1 : Lancer un fichier individuellement

```bash
# Lancer tuples.py
python TP0/tuples.py

# Lancer ensembles.py
python TP0/ensembles.py

# Lancer dictionnaire.py
python TP0/dictionnaire.py
```

### Option 2 : Lancer tous les fichiers à la fois

```bash
python TP0/tuples.py && python TP0/ensembles.py && python TP0/dictionnaire.py
```

### Option 3 : Lancer depuis un IDE (VS Code, PyCharm, etc.)
- Ouvrir le fichier souhaité
- Cliquer sur le bouton "Run" (▶️) en haut à droite
- Ou appuyer sur les raccourcis :
  - **VS Code** : `Ctrl+F5`
  - **PyCharm** : `Shift+F10`

### Option 4 : Lancer via un script principal

Créer un fichier `main.py` à la racine :
```python
import TP0.tuples
import TP0.ensembles
import TP0.dictionnaire

print("✅ Tous les TP0 ont fonctionné correctement !")
```

Puis exécuter :
```bash
python main.py
```

---

## 🧪 Résultats attendus

Si tout fonctionne correctement, **aucun message d'erreur n'apparaît**. Les assertions intégrées dans chaque fichier valident automatiquement :
- L'extraction et l'affichage des données
- Les opérations sur les structures
- L'intégrité des données après modification

Si une assertion échoue, tu verras une erreur `AssertionError` avec le contexte.

---

## 📚 Concepts clés

### Tuples
- Structure **immuable** (ne peut pas être modifiée après création)
- Représente un enregistrement de données (capteur, valeur, unité)
- Accès par index : `tuple[0]`

### Ensembles (Sets)
- Collection d'éléments **uniques**
- Opérations : intersection (`&`), union (`|`), différence (`-`)
- Pratique pour les problèmes de logique d'appartenance

### Dictionnaires
- Structure **clé-valeur** flexible
- Permet l'accès rapide par clé
- Idéal pour gérer des ressources indexées (stock, configurations)

---

## ✅ Checklist

- [ ] Cloner le repo
- [ ] Installer Python 3.6+
- [ ] Lancer `python TP0/tuples.py`
- [ ] Lancer `python TP0/ensembles.py`
- [ ] Lancer `python TP0/dictionnaire.py`
- [ ] Tous les tests passent ✅

---

**Auteur** : Jasmine Kasmi  
**Contexte** : Apprentissage des structures de données en Python
