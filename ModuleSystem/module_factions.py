from header_factions import *
from compiler import *
####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
#  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
#  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("rebels", 0.05),("sang_lys", -0.00)], [], 0x00308F), #rouge 0xFF4433  bleu 0x00308F changed name so that can tell difference if shows up on map
#  ("faction_fake_end","faction_fake_end",0, 0.9, [], []),
  
  ("kingdom_1",  "Kingdom of France", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("rebels", 0.02),("sang_lys", 0.02),("cane_de_fer",0.00)], [], 0x4169E1),
  ("kingdom_2",  "Kingdom of England",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("rebels", -0.05),("sang_lys", -0.2),("cane_de_fer",0.00)], [], 0xE93014),
  ("kingdom_3",  "Kindom of Bourgogne", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("rebels", -0.05),("sang_lys", -0.2),("cane_de_fer",0.00)], [], 0xDDDD33),
  ("kingdom_4",  "Duche de Bretagne",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05),("rebels", 0.00),("sang_lys", -0.2),("cane_de_fer",0.05)], [], 0x999999),#bleu marine noir 0x000038 #gris 0x7A7A7A #gris clair 0x999999
#  ("kingdom_5",  "Kingdom of Rhodoks",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x33DD33),
#  ("kingdom_6",  "Sarranid Sultanate",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xDDDD33),

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),    ("sang_lys", 0.00)
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  rebels 1429
  #("rebels","Rebels", 0, 0.5,[("player_faction",0.4),("kingdom_1",0.0),("kingdom_2",-0.6),("kingdom_3",-0.6),("deserters", -0.02),("outlaws",-0.02),("sang_lys",-0.00)], [], 0x33DD33),
##sang lys 1429
   


  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),



##  rebels 1429
  ("rebels","Rebels", 0, 0.5,[("player_faction",0.2),("kingdom_1",0.02),("kingdom_2",-0.6),("kingdom_3",-0.6),("deserters", -0.02),("outlaws",-0.02),("sang_lys",-0.00),("cane_de_fer",0.00)], [], 0x228B22),#0x4B5320 camo
##sang lys 1429
  
  ("sang_lys","Compagnie du sang Lys", 0, 0.5,[("player_faction",0.4),("kingdom_1",0.2),("kingdom_2",-0.2),("kingdom_3",-0.2),("deserters", -0.00),("outlaws",-0.02),("rebels", 0.00),("kingdom_4",-0.02),("cane_de_fer",0.00)], [], 0x4169E1),    


##Vilandrandro
  ("vilandrandro","La grande Compagnie de Vilandrandro", 0, 0.5,[("player_faction",0.0),("kingdom_1",-0.2),("kingdom_2",-0.2),("kingdom_3",-0.2),("deserters", 0.05),("outlaws",0.05),("rebels", 0.00),("cane_de_fer",0.00)], [], 0x000000),

  
##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
  ("convoi_weapons","Convoi d'armes Anglais", 0, 0.5,[("player_faction",-1.0)], [], 0xE93014),

#vilandrandro
  #quete de bourges
  ("viland_quest_bourges","La grande Compagnie de Vilandrandro", 0, 0.5,[("player_faction",-1.0)], [], 0x000000),  

#mercenaires bretons
  ("cane_de_fer","Compagnie des Cranes de Fer", 0, 0.5,[("player_faction",0.00),("kingdom_1",0.00),("kingdom_2",0.00),("kingdom_3",0.00),("deserters", -0.00),("outlaws",-0.02),("rebels", 0.00),("kingdom_4",0.05),("sang_lys",0.00)], [], 0x999999),    

  ### HYW Seek: Mercenary factions
 ("flemish_mercenaries","Compagnie de Mercenaires Flamands", 0, 0.5,[("player_faction",0.00),("kingdom_1",0.00),("kingdom_2",0.00),("kingdom_3",0.05),("deserters", -0.00),("outlaws",-0.02),("rebels", 0.00),("kingdom_4",0.00),("sang_lys",0.00)], [], 0x999999),    

  
]
