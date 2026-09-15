robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission(ens1,ens2):
    return ens1 & ens2

def robots_toutes_missions(ens1,ens2):
    return ens1 | ens2

def robots_exploration_seule(ens1,ens2):
    return ens1 - ens2

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seule(robots_exploration, robots_transport)


assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

def ajouter_robot_mission(ens, mission):
    ens_n= set(ens)
    ens_n.add(mission)
    return ens_n


def retirer_robot_mission(ens, mission):
    ens_r= set(ens)#pour créer une copie de l'ensemble, en faisant ens_r= ens on pointe vers le meme ensemble en mémoire
    ens_r.remove(mission)
    return ens_r

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}