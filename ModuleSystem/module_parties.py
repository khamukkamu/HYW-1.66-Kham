# -*- coding: cp1252 -*-
from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *
from compiler import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("freelancer_party_backup","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #Freelancer
  ("freelancer_player_party","{!}",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #Freelancer
  
###############################################################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1","Paris",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.27,43.08),[],170),
  ("town_2","Reims",     icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.50,60.59),[],-45),
  ("town_3","Nantes",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.38,9.89),[],0),
  ("town_4","Bourges",     icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.63,-0.40),[],290),
  ("town_5","Metz",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.75,44.49),[],-10),
  ("town_6","Dijon",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.68,5.29),[],155),
  ("town_7","Montpellier",   icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.41,-87.85),[],30),

  ("town_8","Marseille", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.62,-95.41),[],-45),
  ("town_9","Caen",   icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.97,57.75),[],90),
  ("town_10","Limoges",   icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.08,-35.23),[],310),
  ("town_11","Calais",   icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.23,96.74),[],150),
  ("town_12","Rouen", icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.49,62.10),[],25),
  ("town_13","Toulouse",icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.07,-88.80),[],60),
  ("town_14","Bordeaux",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.03,-69.80),[],135),
  ("town_15","Orleans",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(17.74,21.54),[],135),
  ("town_16","Tours",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.12,2.98),[],40),
  ("town_17","Poitiers",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.73,-14.21),[],135),
  ("town_18","Avignon",  icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.68,-65.94),[],90),
  
  ("town_19","Cherbourg", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.86,77.51),[], 45),##-41.86,79.51
  ("town_20","Lyon", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.56,-36.72),[], 270),
  ("town_21","Auxerre", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.15,18.69),[], 330),
  ("town_22","Rennes", icon_town_steppe|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.20,27.86),[], 0),

#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Cherbourg",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-38.96,79.51),[],-31),
  ("castle_2","Amiens",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(24.26,73.17),[],75),
  ("castle_3","Chartres",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.81,33.08),[],100),
  ("castle_4","Brest",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.79,43.90),[],180),
  ("castle_5","Troyes",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.63,14.03),[],90),
  ("castle_6","La_Rochelle",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-45.20,-13.31),[],55),
  ("castle_7","Angouleme",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.28,-38.68),[],45),
  ("castle_8","Moulins",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.91,-12.18),[],30),
  ("castle_9","Clermont",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.43,-27.20),[],100),
  ("castle_10","Lyon",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.76,-40.32),[],110),
  ("castle_11","Le_Mans",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.82,22.52),[],75),
  ("castle_12","Bayonne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.39,-88.97),[],95),
  ("castle_13","Auch",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.66,-87.59),[],115),
  ("castle_14","Tarbes",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.43,-95.73),[],90),
  ("castle_15","Albe",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.47,38.12),[],235),
  ("castle_16","Carcassonne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.90,-95.95),[],45),
  ("castle_17","Donjon de Grenoble",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.89,-66.13),[],15),
  ("castle_18","St.Malo",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.94,46.13),[],300),
  ("castle_19","Antwerp",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.12,102.98),[],280),
  ("castle_20","Peronne",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.76,78.38),[],260),
  ("castle_21","Verneuilo",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.80,44.76),[],260),
  ("castle_22","Chateauroux",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.84,-12.70),[],260),
  ("castle_23","Laval",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.30,17.51),[],80),
  ("castle_24","Senlis",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(41.56,55.43),[],260),
  ("castle_25","Turenne",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.66,-52.54),[],260),
  ("castle_26","Aurillac",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.82,-50.43),[],260),
  ("castle_27","Nevers",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(43.56,3.08),[],260),
  ("castle_28","Monterean",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.54,26.23),[],260),

  ("castle_29","Dieppe",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.27,77.05),[],280),
  ("castle_30","Rodez",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.19,-73.93),[],260),
  ("castle_31","Le_Puy",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.76,-45.38),[],260),
  ("castle_32","Cahors",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.58,-68.88),[],260),
  ("castle_33","Nantes",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-55.60,10.17),[],80),
  ("castle_34","Neufchateau",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.08,30.26),[],260),
  ("castle_35","Chalons",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.11,47.59),[],260),
  ("castle_36","Albret",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-34.59,-79.21),[],260),
  ("castle_37","Montargis",icon_castle_c|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.78,29.29),[],260),
  ("castle_38","Bruges",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.17,95.94),[],260),
  ("castle_39","Thouars",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.65,-0.48),[],280),
  ("castle_40","Castle_Agincourt",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.02,79.91),[],260),

  ("castle_41","Mont st Michel",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.50,44.13),[],260),
  ("castle_42","Pont de Poitier",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.68,-6.10),[],260),
  ("castle_43","Pont de Tours",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.18,2.78),[],260),
  ("castle_44","Pont de Bordeau",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.31,-70.25),[],260),
  ("castle_45","Pont fortifie",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.84,27.53),[],260),
  ("castle_46","Pont de Bourges",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.46,-5.14),[],260),
  ("castle_47","Pont des tourelles",icon_bridge_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.08,18.49),[],260),
  ("castle_48","chinon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.87,-2.72),[],260),
 

#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1","Bruges_Village",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.47,99.26),[],100),#Done
  ("village_2","Boulogne",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.98,87.99),[],110),#done
  ("village_3","Lille",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.24,89.79),[],120),
  ("village_4","Abbeville",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.01,81.61),[],130),
  ("village_5","Nemours",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.07,34.09),[],170), #swapped with 16
  ("village_6","Mayenne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.70,26.13),[],170),#swapped with 20
  ("village_7","Laon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.69,69.98),[],110),
  ("village_8","Soissons",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(51.92,56.24),[],120),
  ("village_9","Senlis_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.15,53.22),[],130),
  ("village_10","Beaumont",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.46,47.44),[],170),

  ("village_11","Chalons_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.34,51.37),[],100),
  ("village_12","Bar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.61,45.82),[],110),
  ("village_13","Joinville",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.73,35.36),[],120),
  ("village_14","Melun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.47,39.32),[],130),
  ("village_15","Sens",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(39.83,27.78),[],170),
  ("village_16","Dieppe_Village",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.97,76.39),[],170),#swapped with 5
  ("village_17","Harcourt",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-10.10,63.14),[],35),
  ("village_18","Bayeux",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-32.22,63.30),[],170),
  ("village_19","Lisieux",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.88,56.99),[],100), #swapped with 62
  ("village_20","Harfleur",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.32,66.85),[],100), #swapped with 6

  ("village_21","Honflew",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21.76,61.92),[],60),#swapped with 82
  ("village_22","Quimper",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.61,34.42),[],110),
  ("village_23","Laval_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.59,20.29),[],120),
  ("village_24","Graon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.94,13.51),[],130),
  ("village_25","Blois",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.81,8.91),[],170),
  ("village_26","Levet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.63,-6.14),[],170),
  ("village_27","Vierzon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(20.88,2.31),[],170),
  ("village_28","Chateauroux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.54,17.59),[],170),
  ("village_29","Nevers_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.46,0.12),[],170),

  ("village_30","Fontenay",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-56.42,12.89),[],0),
  ("village_31","Niort",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.70,26.54),[],100),
  ("village_32","La_Tremouille",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.70,-13.99),[],110),
  ("village_33","Gueret",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.64,-24.93),[],120),
  ("village_34","Rochefort",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-43.37,-18.45),[],130),
  ("village_35","Saintes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.20,-35.42),[],170),
  ("village_36","Soyaux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.27,-41.26),[],170),
  ("village_37","Turenne_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.23,-55),[],170),
  ("village_38","Perigueux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-11.60,-52.38),[],170),
  ("village_39","Aurillac_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.98,-46.66),[],170),
  ("village_40","Moulins_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(50.51,-9.26),[],170),

  ("village_41","Langres",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.50,21.74),[],100),
  ("village_42","Beaune",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.89,-9.59),[],110),
  ("village_43","Chalon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.31,-17.94),[],120),
  ("village_44","Macon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.81,-24.81),[],130),
  ("village_45","Vienne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(79.46,-44.24),[],170),
  ("village_46","Clermont_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.27,-25.03),[],170),
  ("village_47","Valence",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.28,-68.64),[],170),
  ("village_48","Briancon",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(96.94,-73.27),[],170),
  ("village_49","Fecamp",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-12,73.55),[],100), #swapped with 61
  ("village_50","Verneuilo_Village",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-17.05,47.17),[],100),#swapped with 63

  ("village_51","Castillon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-26.24,-62.41),[],100),
  ("village_52","Cahors_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-5.67,-69.61),[],110),
  ("village_53","Agen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.39,-74.96),[],120),
  ("village_54","Montauban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.87,-77.26),[],130),
  ("village_55","Foix",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.41,-95.58),[],170),
  ("village_56","Narbonne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.51,-95.43),[],170),
  ("village_57","Sete",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.53,-85.39),[],170),
  ("village_58","Nimes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.61,-85.32),[],170),
  ("village_59","Arles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(70.20,-81.39),[],170),
  ("village_60","Toulon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(88.45,-92.41),[],170),

  ("village_61","Dax",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.52,-85.83),[],10),#swapped with 49
  ("village_62","Alencon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-23.50,34.33),[],170),#swapped with 19
  ("village_63","Albret_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.65,-81.42),[],170),#swapped with 50
  ("village_64","Bretigny",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(6.68,27.71),[],100),
  ("village_65","Thouars_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-30.25,-2.14),[],100),
  ("village_66","Peronne_Village",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.36,77.18),[],100),
  ("village_67","Agincourt",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.21,78.15),[],100),
  ("village_68","Ghent",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(40.77,87.69),[],100),
  ("village_69","Vannes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.50,19.66),[],100),
  ("village_70","Guines",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.97,92.48),[],100),

  ("village_71","Lunoges",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.39,-31.45),[],20),
  ("village_72","Elaye",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-31.17,-59.49),[],60),
  ("village_73","Maupertuis",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-13.86,-20.78),[],55),
  ("village_74","Hesdin",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.84,86.08),[],15),
  ("village_75","Autun",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.54,-12),[],10),
  ("village_76","Arras",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.22,85.88),[],35),
  ("village_77","Monterean_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(47.75,27.77),[],160),
  ("village_78","Montargis_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.12,27),[],180),
  ("village_79","Evreux",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.66,53.66),[],0),
  ("village_80","Albi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(2.66,-79.84),[],40),

  ("village_81","La_Teste_de_Buch",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.56,-74.37),[],20),
  ("village_82","Beauvoir",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.50,41.73),[],100),#swapped with 21
  ("village_83","Le_Puy_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(32.82,-43.09),[],55),
  ("village_84","Rodez_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.49,-71.67),[],15),
  ("village_85","Boves",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.46,69.47),[],10),
  ("village_86","Gien",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.89,11.55),[],35),
  ("village_87","Formigny",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.11,67.32),[],160),
  ("village_88","Neufchateau_Village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.47,27.97),[],180),
  ("village_89","Cosne",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38.05,5.18),[],0),
  ("village_90","Vaucouleurs",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.15,39.80),[],40),

   ("village_91","Brest",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-90.79,39.50),[], 20),
   ("village_92","St Brieut",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.44,48.13),[], 60),
   ("village_93","Troyes",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.25,16.24),[], 55),
   ("village_94","Lunery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(16.84,-1.20),[], 15),
  # ("village_95","Tamnuh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(99, -90.5),[], 10),
  # ("village_96","Habba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107, -75),[], 35),
  # ("village_97","Sekhtem",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(82.3, -76.8),[], 160),
  # ("village_98","Mawiti",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.7, -62.2),[], 180),
  # ("village_99","Fishara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(158.35, -98),[], 0),
  # ("village_100","Iqbayl",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150, -106.5),[], 40),

  # ("village_101","Uzgha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154, -69.5),[], 20),
  # ("village_102","Shibal Zumr",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(77.2, -91),[], 60),
  # ("village_103","Mijayet",  icon_village_c|pf_villagae, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(121, -95.6),[], 55),
  # ("village_104","Tazjunat",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(159, -58.5),[], 15),
  # ("village_105","Aab",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135, -88.5),[], 10),
  # ("village_106","Hawaha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.3, -91.0),[], 35),
  # ("village_107","Unriya",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156.6, -84),[], 160),
  # ("village_108","Mit Nun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(28.8, -107.3),[], 180),
  # ("village_109","Tilimsal",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(53, -114.5),[], 0),
  # ("village_110","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(38, -104),[], 40),
# 
  ("salt_mine","Salt_Mine",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",icon_town|pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(3, -7),[]),

  ("training_ground_1","Training_Field",  icon_training_ground|icon_training_ground|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.10,61.10),[],100),
  ("training_ground_2","Training_Field",  icon_training_ground|icon_training_ground|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-63.22,35.99),[],100),
  ("training_ground_3","Training_Field",  icon_training_ground|icon_training_ground|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.23,14.27),[],100),
  ("training_ground_4","Training_Field",  icon_training_ground|icon_training_ground|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(11.32,-83.55),[],100),
  ("training_ground_5","Training_Field",  icon_training_ground|icon_training_ground|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.79,-25.35),[],100),


#  bridge_a
  ("Bridge_1","1",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(75.51,-66.01),[],90),
  ("Bridge_2","2",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(52.84,27.53),[],-70),#
  ("Bridge_3","3",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.41,-64.88),[],-8),
  ("Bridge_4","4",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-21,0.48),[],162),
  ("Bridge_5","5",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-27.31,-70.25),[],108),#
  ("Bridge_6","6",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.93,-83.03),[],62),
  ("Bridge_7","7",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.91,7.51),[],-2),
  ("Bridge_8","8",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-0.14,60.25),[],7),
  ("Bridge_9","9",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.14,41.30),[],0),
  ("Bridge_10","10",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.08,18.49),[],-13),#
  ("Bridge_11","11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-7.18,2.78),[],15),#
  ("Bridge_12","12",icon_village_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.60,-134.10),[],135),
  ("Bridge_13","13",icon_village_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.12,-131.16),[],90),
  ("Bridge_14","14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.46,-5.14),[],123),#
  ("Bridge_15","15",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-9.68,-6.10),[],-68),

#1429 scenes worldmap
  ("camp_anglais","Camp Anglois", icon_camp|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(34.76,-47.58),[],100),
#
  ("toul_village","Village de Toul", icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(80.76,38.58),[],100),

#1429 foret de verzy camp
 # ("camp_ofrebels","Camp des Rebels", icon_camp|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.50,55.60),[],100),
 ("camp_ofrebels","Camp des Rebels", icon_camp|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_black_khergits,0,ai_bhvr_hold,0,(71.50,55.60),[],100),

#1429 place forte
  ("place_forte_b","Place forte Bourgignone", icon_castle_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.69,-20.78),[],100),
 # ("place_forte_b","Place forte Bourgignone", icon_castle_d|pf_always_visible|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(56.69,-20.78),[],100),

#1429 tour des pins
  ("tour_despins","Tour des pins", icon_town_desert|pf_always_visible|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_black_khergits,0,ai_bhvr_hold,0,(38.85,-83.50),[],100),

#1429 assasinat ferme mathieu
  ("fermemat","Ferme de Mathieu", icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.60,29.36),[],100),

#1429 camp de chasse
  ("chasse_camp","Camp de chasse", icon_camp|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(44.12,52.22),[],100),

#1429 toureles orléans script
#  ("tourels","Pont des tourelles", icon_bridge_b|pf_always_visible|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(19.08,18.49),[],260),

#1429 chapelle de fierbois
  ("fierbois","Sainte Catherine de Fierbois", icon_village_a|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-4.87,-3.32),[],260),

#1429 foore de rouen
  ("rouen_foret","Foret de Rouen", icon_bandit_lair|pf_disabled|pf_is_static|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(0.49,67.87),[],260),
#forets braconniers
  ("quest_forest1","Foret de Levet", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.63,-5.14),[],100),
  ("quest_forest2","Foret d'Aurillac", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.98,-44.66),[],100),
  ("quest_forest3","Foret de Narbonne", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(25.51,-95.43),[],100),
  ("quest_forest4","Foret de Rodez", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.49,-68.67),[],100),
  ("quest_forest5","Foret de Arles", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(68.20,-81.39),[],100),
  ("quest_forest6","Foret du Puy", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.82,-45.09),[],100),
  ("quest_forest7","Foret de Vierzon", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(21.88,5.31),[],100),
  ("quest_forest8","Foret de Beaune", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(73.89,-9.59),[],100),
  ("quest_forest9","Foret de Montargis", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(33.12,27),[],100),
  ("quest_forest10","Foret d'Evreux", icon_village_b|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-1.66,53.66),[],100),
  ("quest_forest11","Foret de Guines", icon_village_b|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.97,92.48),[],100),
  ("quest_forest12","Foret de Bayeux", icon_village_b|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.22,63.30),[],100),


#auberges. village_burnt_c > auberge eneigée
  ("auberge_1","Auberge", icon_village_burnt_b|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.39,44.08),[],15),
  ("auberge_2","Auberge", icon_village_burnt_b|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(15.89,4.18),[],-10),
  ("auberge_3","Auberge", icon_village_burnt_c|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.89,72.18),[],-40),
  ("auberge_4","Auberge", icon_village_burnt_b|pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(19.19,-62.18),[],0),

#prairies quete cheval
  ("prairie_bourges","Prairies de Bourges", icon_village_c|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(26.63,-4.40),[],100),

  ("foret_lorges","Foret de Lorges", icon_village_deserted_c|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.20,42.46),[],100),

  ("camp_crane_fer","Camp de la Compagnie des Cranes de Fer", icon_village_deserted_b|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-47.20,20.86),[],100),
 
  ("quintin","Citadelle de Quintin", icon_castle_d|pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.79,44.90),[],100),

  ("looter_spawn_point"   ,"looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-73.52,41.76),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"steppe_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(3.97,-47.61),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(78, 84),[(trp_looter,15,0)]),

  ("forest_bandit_spawn_point"  ,"forest_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(29.50,-76.61),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","mountain_bandit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(37.22,19.48),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-45.33,62.19),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"sea_raider_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-41,-39.76),[(trp_looter,15,0)]),
#  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(110, -100),[(trp_looter,15,0)]),
 #   rebels spawn
  ("black_khergit_spawn_point_1"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_black_khergits,0,ai_bhvr_hold,0,(27.27,-24.93),[(trp_looter,15,0)]),# centre
  ("black_khergit_spawn_point_2"  ,"black_khergit_sp2",pf_disabled|pf_is_static, no_menu, pt_none, fac_black_khergits,0,ai_bhvr_hold,0,(83.75,43.79),[(trp_looter,15,0)]),#METZ
#####sang lys spawn

 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

 ("sang_lys_spawn_point_1"  ,"sang_lys_spawn_point_1",pf_disabled|pf_is_static, no_menu, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(28.83,-0.60),[(trp_looter,15,0)]),# bourges  
#   rebel spawn fin

 ("cranede_fer_spawn_point_1"  ,"cranede_fer_spawn_point_1",pf_disabled|pf_is_static, no_menu, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-51.20,27.86),[(trp_looter,15,0)]),# bourges  

  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),

 

  ]
