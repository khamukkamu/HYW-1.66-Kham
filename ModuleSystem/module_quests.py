# -*- coding: cp1252 -*-
from header_quests import *
from compiler import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

quests = [
# Note : This is defined as the first governer quest in module_constants.py: 
 ("deliver_message", "Deliver Message to {s13}", qf_random_quest,
  "{!}{s9} asked you to take a message to {s13}. {s13} was at {s4} when you were given this quest."
  ),
 ("deliver_message_to_enemy_lord", "Deliver Message to {s13}", qf_random_quest,
  "{!}{s9} asked you to take a message to {s13} of {s15}. {s13} was at {s4} when you were given this quest."
  ),
 ("raise_troops", "Raise {reg1} {s14}", qf_random_quest,
  "{!}{s9} asked you to raise {reg1} {s14} and bring them to him."
  ),
 ("escort_lady", "Escort {s13} to {s14}", qf_random_quest,
  "{!}None"
  ),
## ("rescue_lady_under_siege", "Rescue {s3} from {s4}", qf_random_quest,
##  "{s1} asked you to rescue his {s7} {s3} from {s4} and return her back to him."
##  ),
## ("deliver_message_to_lover", "Deliver Message to {s3}", qf_random_quest,
##  "{s1} asked you to take a message to his lover {s3} at {s4}."
##  ),
## ("bring_prisoners_to_enemy", "Bring Prisoners to {s4}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} as prisoners to the guards at {s4}."
##  ),
## ("bring_reinforcements_to_siege", "Bring Reinforcements to the Siege of {s5}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3} to {s4} at the siege of {s5}."
##  ),
## ("deliver_supply_to_center_under_siege", "Deliver Supplies to {s5}", qf_random_quest,
##  "TODO: Take {reg1} cartloads of supplies from constable {s3} and deliver them to constable {s4} at {s5}."
##  ),
 ("deal_with_bandits_at_lords_village", "Save the Village of {s15} from Marauding Bandits", qf_random_quest,
  "{!}{s13} asked you to deal with the bandits who took refuge in his village of {s15} and then report back to him."
  ),
 ("collect_taxes", "Collect Taxes from {s3}", qf_random_quest,
  "{!}{s9} asked you to collect taxes from {s3}. He offered to leave you one-fifth of all the money you collect there."
  ),
 ("hunt_down_fugitive", "Hunt Down {s4}", qf_random_quest,
  "{!}{s9} asked you to hunt down the fugitive named {s4}. He is currently believed to be at {s3}."
  ),
## ("capture_messenger", "Capture {s3}", qf_random_quest,
##  "{s1} asked you to capture a {s3} and bring him back."
##  ),
## ("bring_back_deserters", "Bring {reg1} {s3}", qf_random_quest,
##  "{s1} asked you to bring {reg1} {s3}."
##  ),
 ("kill_local_merchant", "Assassinate Local Merchant at {s3}", qf_random_quest,
  "{!}{s9} asked you to assassinate a local merchant at {s3}."
  ),
 ("bring_back_runaway_serfs", "Bring Back Runaway Serfs", qf_random_quest,
  "{!}{s9} asked you to bring back the three groups of runaway serfs back to {s2}. He said all three groups must be running away in the direction of {s3}."
  ),
 ("follow_spy", "Follow the Spy to Meeting", qf_random_quest,
  "{!}{s11} asked you to follow the spy that will leave {s12}. You must be careful not to be seen by the spy during his travel, or else he may get suspicious and turn back. Once the spy meets with his accomplice, you are to ambush and capture them and bring them both back to {s11}."
  ),
 ("capture_enemy_hero", "Capture a Lord from {s13}", qf_random_quest,
  "{!}TODO: {s11} asked you to capture a lord from {s13}."
  ),
 ("lend_companion", "Lend Your Companion {s3} to {s9}", qf_random_quest,
  "{!}{s9} asked you to lend your companion {s3} to him for a week."
  ),
 ("collect_debt", "Collect the Debt {s3} Owes to {s9}", qf_random_quest,
  "{!}{s9} asked you to collect the debt of {reg4} denars {s3} owes to him."
  ),
## ("capture_conspirators", "Capture Conspirators", qf_random_quest,
##  "TODO: {s1} asked you to capture all troops in {reg1} conspirator parties that plan to rebel against him and join {s3}."
##  ),
## ("defend_nobles_against_peasants", "Defend Nobles Against Peasants", qf_random_quest,
##  "TODO: {s1} asked you to defend {reg1} noble parties against peasants."l
##  ),
 ("incriminate_loyal_commander", "Incriminate the Loyal Commander of {s13}, {s16}", qf_random_quest,
  "{!}None"
  ),
# ("raid_caravan_to_start_war", "Raid {reg13} Caravans of {s13}", qf_random_quest,   #This is now a dynamic quest, integrated into the provocation system
#  "None"
#  ),
 ("meet_spy_in_enemy_town", "Meet Spy in {s13}", qf_random_quest,
  "{!}None"
  ),
 ("capture_prisoners", "Bring {reg1} {s3} Prisoners", qf_random_quest,
  "{!}{s9} wanted you to bring him {reg1} {s3} as prisoners."
  ),

## ("hunt_down_raiders", "Hunt Down Raiders",qf_random_quest,
##  "{s1} asked you to hunt down and punish the raiders that attacked a village near {s3} before they reach the safety of their base at {s4}."
##  ),

##################
# Enemy Kingdom Lord quests
##################
# Note : This is defined as the first enemy lord quest in module_constants.py:
 ("lend_surgeon", "Lend Your Surgeon {s3} to {s1}", qf_random_quest,
  "{!}Lend your experienced surgeon {s3} to {s1}."
  ),

##################
# Kingdom Army quests
##################
# Note : This is defined as lord quests end in module_constants.py:
 ("follow_army", "Follow {s9}'s Army", qf_random_quest,
  "{!}None"
  ),
 ("report_to_army", "Report to {s13}, the Marshall", qf_random_quest,
  "{!}None"
  ),
# Note : This is defined as the first army quest in module_constants.py:
# maybe disable these army quests, except as volunteer quests that add to the capacity of the army
 ("deliver_cattle_to_army", "Deliver {reg3} Heads of Cattle to {s13}", qf_random_quest,
  "{!}None"
  ),
 ("join_siege_with_army", "Join the Siege of {s14}", qf_random_quest,
  "{!}None"
  ),
 ("screen_army", "Screen the Advance of {s13}'s Army", qf_random_quest,
  "{!}None"
  ),
 ("scout_waypoints", "Scout the assigned areas", qf_random_quest,
  "{!}None"
  ),


##################
# Kingdom Lady quests
##################
# Note : This is defined as the first kingdom lady quest in module_constants.py:
#Rescue lord by replace will become a 
 ("rescue_lord_by_replace", "Rescue {s13} from {s14}", qf_random_quest,
  "{!}None"
  ),
 ("deliver_message_to_prisoner_lord", "Deliver Message to {s13} at {s14}", qf_random_quest,
  "{!}None"
  ),

#Courtship quests
  ("duel_for_lady", "Challenge {s13} to a Trial of Arms", qf_random_quest,
  "{!}None"
  ),

  ("duel_courtship_rival", "Challenge {s13} to a Trial of Arms (optional)", qf_random_quest,
  "{!}None"
  ),

#Other duel quests
  ("duel_avenge_insult", "Challenge {s13} to a Trial of Arms", qf_random_quest,
  "{!}None"
  ),
  
  
  
##################
# Mayor quests
##################
# Note : This is defined as the first mayor quest in module_constants.py: 
 ("move_cattle_herd", "Move Cattle Herd to {s13}", qf_random_quest,
  "{!}Guildmaster of {s10} asked you to move a cattle herd to {s13}."
  ),
 ("escort_merchant_caravan", "Escort Merchant Caravan to {s8}", qf_random_quest, #make this a non-random quest?
  "{!}Escort the merchant caravan to the town of {s8}."
  ),
 ("deliver_wine", "Deliver {reg5} Units of {s6} to {s4}", qf_random_quest,
  "{!}{s9} of {s3} asked you to deliver {reg5} units of {s6} to the tavern in {s4} in 7 days."
  ),
 ("troublesome_bandits", "Hunt Down Troublesome Bandits", qf_random_quest,
  "{!}{s9} of {s4} asked you to hunt down the troublesome bandits in the vicinity of the town."
  ),
  
 ("kidnapped_girl", "Ransom Girl from Bandits", qf_random_quest,
  "{!}Guildmaster of {s4} gave you {reg12} denars to pay the ransom of a girl kidnapped by bandits.\
 You are to meet the bandits near {s3} and pay them the ransom fee.\
 After that you are to bring the girl back to {s4}."
  ),
  
 ("persuade_lords_to_make_peace", "Make Sure Two Lords Do Not Object to Peace", qf_random_quest, #possibly deprecate., or change effects
  "{!}Guildmaster of {s4} promised you {reg12} denars if you can make sure that\
 {s12} and {s13} no longer pose a threat to a peace settlement between {s15} and {s14}.\
 In order to do that, you must either convince them or make sure they fall captive and remain so until a peace agreement is made."
  ),
  
 ("deal_with_looters", "Deal with Looters", qf_random_quest,
  "{!}The Guildmaster of {s4} has asked you to deal with several bands of looters around {s4}, and bring back any goods you recover."
  ),
 ("deal_with_night_bandits", "Deal with Night Bandits", qf_random_quest,
  "{!}TODO: The Guildmaster of {s14} has asked you to deal with night bandits at {s14}."
  ),

############
# Village Elder quests
############
# Note : This is defined as the first village elder quest in module_constants.py:
 ("deliver_grain", "Bring wheat to {s3}", qf_random_quest,
  "{!}The elder of the village of {s3} asked you to bring them {reg5} packs of wheat.."
  ), 
 ("deliver_cattle", "Deliver {reg5} Heads of Cattle to {s3}", qf_random_quest,
  "{!}The elder of the village of {s3} asked you to bring {reg5} heads of cattle."
  ), 
 ("train_peasants_against_bandits", "Train the Peasants of {s13} Against Bandits.", qf_random_quest,
  "{!}None"
  ), 
# Deliver horses, Deliver food, Escort_Caravan, Hunt bandits, Ransom Merchant.
## ("capture_nobleman", "Capture Nobleman",qf_random_quest,
##  "{s1} wanted you to capture an enemy nobleman on his way from {s3} to {s4}. He said the nobleman would leave {s3} in {reg1} days."
##  ),

# Bandit quests: Capture rich merchant, capture banker, kill manhunters?..

# Note : This is defined as the last village elder quest in module_constants.py:
 ("eliminate_bandits_infesting_village", "Save the Village of {s7} from Marauding Bandits", qf_random_quest,
  "{!}A villager from {s7} begged you to save their village from the bandits that took refuge there."
  ),


 # Tutorial quest
## ("destroy_dummies", "Destroy Dummies", qf_show_progression,
##  "Trainer ordered you to destroy 10 dummies in the training camp."
##     ),

  #Courtship and marriage quests begin here
  ("visit_lady", "Visit Lady", qf_random_quest,
  "{!}None"
  ),
  ("formal_marriage_proposal", "Formal Marriage Proposal", qf_random_quest,
  "{!}None"
  ),  #Make a formal proposal to a bride's father or brother
  ("obtain_liege_blessing", "Formal Marriage Proposal", qf_random_quest,
  "{!}None"
  ),  #The equivalent of the above -- ask permission of a groom's liege. Is currently not used
  ("wed_betrothed", "Wed Your Betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the father or guardian of the bride, object troop is the bride
  ("wed_betrothed_female", "Wed Your Betrothed", qf_random_quest,
  "{!}None"
  ),  #in this case, the giver troop is the spouse

  
 # Join Kingdom quest
  ("join_faction", "Give Oath of Homage to {s1}", qf_random_quest,
  "{!}Find {s1} and give him your oath of homage."
  ),

 # Rebel against Kingdom quest
 ("rebel_against_kingdom", "Help {s13} Claim the Throne of {s14}", qf_random_quest,
  "{!}None"
  ),

  #Political quests begin here
 ("consult_with_minister", "Consult With Minister", qf_random_quest, "{!}Consult your minister, {s11}, currently at {s12}"),
 
 ("organize_feast",        "Organize Feast", qf_random_quest,        "{!}Bring goods for a feast to your spouse {s11}, currently at {s12}"),
 ("resolve_dispute",       "Resolve Dispute", qf_random_quest,       "{!}Resolve the dispute between {s11} and {s12}"),
 ("offer_gift",            "Procure Gift", qf_random_quest,          "{!}Give {s10} a gift to provide to {reg4?her:his} {s11}, {s12}"),
 ("denounce_lord",         "Denounce Lord", qf_random_quest,         "{!}Denounce {s11} in Public"),
 ("intrigue_against_lord", "Intrigue against Lord", qf_random_quest, "{!}Criticize {s11} in Private"),
 
 
  #Dynamic quests begin here
  #These quests are determined dynamically by external conditions -- bandits who have carried out a raid, an impending war, etc...
 ("track_down_bandits", "Track Down Bandits", qf_random_quest,
  "{!}{s9} of {s4} asked you to track down {s6}, who attacked travellers on the roads near town."
  ), #this is a fairly simple quest for the early game to make the town guildmaster's description of the economy a little more relevant, and also to give the player a reason to talk to other neutral parties on the map
   
 ("track_down_provocateurs", "Track Down Provocateurs", qf_random_quest,
  "{!}{s9} of {s4} asked you to track down a group of thugs, hired to create a border incident between {s5} and {s6}."
  ), 
 ("retaliate_for_border_incident", "Retaliate for a Border Incident", qf_random_quest,
  "{!}{s9} of {s4} asked you to defeat {s5} of the {s7} in battle, defusing tension in the {s8} to go to war."
  ), #perhaps replaces persuade_lords_to_make_peace
  
 ("raid_caravan_to_start_war", "Attack a Neutral Caravan to Provoke War", qf_random_quest,
  "{!}placeholder",
  ), 

  ("cause_provocation", "Give a Kingdom Provocation to Attack Another", qf_random_quest,
  "{!}placeholder",
  ), #replaces raid_caravan_to_start_war
  
 ("rescue_prisoner", "Rescue or Ransom a Prisoner", qf_random_quest,
  "{!}placeholder"
  ), #possibly replaces rescue lord

 ("destroy_bandit_lair", "Destroy Bandit Lair", qf_random_quest,
  "{!}{s9} of {s4} asked you to discover a {s6} and destroy it."
  ), 
  
 ("blank_quest_2", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),
  
 ("blank_quest_3", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_4", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_5", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_6", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_7", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_8", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_9", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_10", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_11", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_12", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_13", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_14", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_15", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_16", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_17", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_18", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_19", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_20", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_21", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_22", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_23", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_24", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_25", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_26", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("blank_quest_27", "{!}blank_quest", qf_random_quest,
  "{!}placeholder"
  ),

 ("collect_men", "Collect Five Men", 0,
  "{!}{s9} asked you to collect at least 5 men before you move against the bandits threatening the townsmen. You can recruit soldiers from villages as well as town taverns. You can find {s9} at the tavern in {s4} when you have think you have enough men."
  ), 
  
  ("learn_where_merchant_brother_is", "Learn Where the Hostages are Held.", 0,
  "{!}placeholder."
  ), 
  
  ("save_relative_of_merchant", "Attack the Bandit Lair", 0,
  "{!}placeholder."
  ),   

  ("save_town_from_bandits", "Save Town from Bandits", 0,
  "{!}placeholder."
  ),

#1429 NEWS QUESTS, YEAH! ;)
 ("rebelc1", "[Rebels] Rencontrer le chef rebel de Montpellier.", 0,
  "{!}None"
  ),

 ("rebelvivre_montpelier", "[Rebels] Trouver des provisions pour les rebels de Montpellier.", 0,
  "{!}None"
  ),

 ("rebel_attack_c1", "[Rebels] Attaquer le convoi d'armes pret du village de Rodez.", 0,
  "{!}None"
  ),

 ("sl_1caserne", "[Compagnie du SansLys] Passer le test d'admission pour travailler avec les SansLys.", 0,
  "{!}None"
  ),

 ("sl_patrouil1", "[Compagnie du SansLys] Patrouiller a Bourges en renfort de la millice.", 0,
  "{!}None"
  ),

 ("sl_ivrogne1", "[Compagnie du SansLys] Débarasser la taverne des trois Lys de Bourges du mercenaire ivre.", 0,
  "{!}None"
  ),

 ("sl_viland_troop1", "[Compagnie du SansLys] Débarasser Bourges de la troupe de brigands rodant aux allentours de la ville.", 0,
  "{!}None"
  ), 

 ("sl_viland_attack1", "[Compagnie du SansLys] Rejoindre la bataille des entrepots de Bourges.", 0,
  "{!}None"
  ),

 ("sl_deffensse_benezet", "[Compagnie du SansLys] Ralier Avignon deffendue par le SansLys pour soutenire le siege.", 0,
  "{!}None"
  ),

 ("rebel_camp_atck1", "[Rebels] Attaquer le camp Anglais qui attend des renforts pret du chateau du Puy.", 0,
  "{!}None"
  ),

 ("rebel_toul", "[Rebels] Rejoindre les rebels au village de Toul autrefois gagné par la peste.", 0,
  "{!}None"
  ),

 ("rebel_chearchcamp", "[Rebels] Fouiller les ruines de Toul pour retrouver les rebels de Bourgogne.", 0,
  "{!}None"
  ),

 ("rebel_entrepmetz", "[Rebels] Attaquer l'entrepot de nouriture de Metz.", 0,
  "{!}None"
  ),

 ("rebel_placeforte", "[Rebels] Prendre la place forte Bourgignone.", 0,
  "{!}None"
  ),

 ("rebel_shearchlico", "[La Licorne] Rencontrer le heros rebel que tout le monde appelle la Licorne.", 0,
  "{!}None"
  ), 

 ("rebel_assas_comtcaen", "[La Licorne] Assassiner des perssonages enemis importants.", 0,
  "{!}None"
  ),

 ("rebel_asassin_chasse", "[La Licorne] Tuer le gouverneur Anglois dans son campement de chasse.", 0,
  "{!}None"
  ),

 ("rebel_manoir", "[La Licorne] Empoisoner le banquier au manoire de Reims.", 0,
  "{!}None"
  ),

 ("rodrig_vol_cle", "[Brigands] Récuperer une clé pour Villandrandro.", 0,
  "{!}None"
  ),
 

 ("cambriolage_chateau", "[Brigands] Cambrioler le chateau a Tours.", 0,
  "{!}None"
  ),


 ("extorsion", "[Brigands] Réclamer le verssement des marchands de Paris.", 0,
  "{!}None"
  ),


 ("kill_mathieu", "[Brigands] Tuer le traitre.", 0,
  "{!}None"
  ),


 ("conffes_chevalier", "[Licorne] Se conffesser aux fins de devenire Chevalier.", 0,
  "{!}None"
  ),

 ("rebel_catahugry", "[Rebels] Trouver des victuailles pour les rebels de Paris cachés dans les catacombes.", 0,
  "{!}None"
  ),


 ("rebel_cataparang", "[Rebels] débarasser les rebels des catacombes de Paris de la patrouille Anglaise.", 0,
  "{!}None"
  ),


 ("crypt_sworr", "Retrouver l'épée de l'écuyer.", 0,
  "{!}None"
  ),

# ("jeanne_siegorl", "[Jeanne la Lorraine] Atteindre le pont des tourelles en compagnie de Jeanne d'Arc.", 0,
#  "{!}None"
#  ),

# ("jeanne_orl_attack", "[Jeanne la Lorraine] Lever le siège d'Orléans en compagnie de Jeanne d'Arc.", 0,
#  "{!}None"
 # ),

 #("bomb_for_win", "[Jeanne la Lorraine] Préparer l'attaque finale des tourelles d'Orléans.", 0,
 # "{!}None"
 # ), 

 ("find_epeepour_jeanne", "[Jeanne la Lorraine] Retrouver une mysterieuse épée.", 0,
  "{!}None"
  ),

 ("foret_filleroeun", "Retrouver la fille du riche marchand de Rouen.", 0,
  "{!}None"
  ),

 ("cata_compagnon", "Retrouver le mari de Madeleine de Montpellier.", 0,
  "{!}None"
  ),
 
###### calais
 ("messager_qst0", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Montpellier.", 0,
  "{!}None"
  ),

 ("messager_qst1", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Marseille.", 0,
  "{!}None"
  ),

 ("messager_qst2", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst3", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Dijon.", 0,
  "{!}None"
  ),

 ("messager_qst4", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Caen.", 0,
  "{!}None"
  ),

 ("messager_qst5", "[Guilde des Messagers de France] Apporter la cargaison au vendeur de livres de Bordeau.", 0,
  "{!}None"
  ),

 ("messager_qst6", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst7", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier d'Avignon.", 0,
  "{!}None"
  ),

 ("messager_qst9", "[Guilde des Messagers de France] Apporter la cargaison au forgeron de Reims.", 0,
  "{!}None"
  ),

###### bourges
 ("messager_qst0b", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Montpellier.", 0,
  "{!}None"
  ),

 ("messager_qst1b", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Marseille.", 0,
  "{!}None"
  ),

 ("messager_qst2b", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst3b", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Dijon.", 0,
  "{!}None"
  ),

 ("messager_qst4b", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Caen.", 0,
  "{!}None"
  ),

 ("messager_qst5b", "[Guilde des Messagers de France] Apporter la cargaison au vendeur de livres de Bordeau.", 0,
  "{!}None"
  ),

 ("messager_qst6b", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst7b", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier d'Avignon.", 0,
  "{!}None"
  ),

 ("messager_qst9b", "[Guilde des Messagers de France] Apporter la cargaison au forgeron de Reims.", 0,
  "{!}None"
  ),

 ###### bordeau
 ("messager_qst0d", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Montpellier.", 0,
  "{!}None"
  ),

 ("messager_qst1d", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Marseille.", 0,
  "{!}None"
  ),

 ("messager_qst2d", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst3d", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Dijon.", 0,
  "{!}None"
  ),

 ("messager_qst4d", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Caen.", 0,
  "{!}None"
  ),

 ("messager_qst5d", "[Guilde des Messagers de France] Apporter la cargaison au vendeur de livres de Bordeau.", 0,
  "{!}None"
  ),

 ("messager_qst6d", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst7d", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier d'Avignon.", 0,
  "{!}None"
  ),

 ("messager_qst9d", "[Guilde des Messagers de France] Apporter la cargaison au forgeron de Reims.", 0,
  "{!}None"
  ),

 ###### marseille
 ("messager_qst0m", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Montpellier.", 0,
  "{!}None"
  ),

 ("messager_qst1m", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Marseille.", 0,
  "{!}None"
  ),

 ("messager_qst2m", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst3m", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Dijon.", 0,
  "{!}None"
  ),

 ("messager_qst4m", "[Guilde des Messagers de France] Apporter la lettre au Maistre de guilde des Marchands de Caen.", 0,
  "{!}None"
  ),

 ("messager_qst5m", "[Guilde des Messagers de France] Apporter la cargaison au vendeur de livres de Bordeau.", 0,
  "{!}None"
  ),

 ("messager_qst6m", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier de Paris.", 0,
  "{!}None"
  ),

 ("messager_qst7m", "[Guilde des Messagers de France] Apporter la cargaison a l'armurier d'Avignon.", 0,
  "{!}None"
  ),

 ("messager_qst9m", "[Guilde des Messagers de France] Apporter la cargaison au forgeron de Reims.", 0,
  "{!}None"
  ), 

 ("banque30", "[Banquiers] Remboursser 3300 écus au Banquiers.", 0,
  "{!}None"
  ),

 ("banque60", "[Banquiers] Remboursser 6600 écus au Banquiers.", 0,
  "{!}None"
  ),

 ("banque90", "[Banquiers] Remboursser 9900 écus au Banquiers.", 0,
  "{!}None"
  ),

 ("banque14", "[Banquiers] Remboursser 15.400 écus au Banquiers.", 0,
  "{!}None"
  ),
 
 # 1429 enhanced quests
 ("braconage", "Les braconniers.", 0,
  "{!}None"
  ),

 ("tresort_t", "Le tresor des Templiers.", 0,
  "{!}None"
  ),

  ("rennes_chateau", "Une piste improbable.", 0,
  "{!}None"
  ),

  ("ouvrire_loge", "La loge secrete.", 0,
  "{!}None"
  ),

  ("loge_s_paris", "Prés du but.", 0,
  "{!}None"
  ), 

 #quetes steel edition
  ("auberge_quete_1", "Le manoir dans la vallée.", 0,
  "{!}None"
  ), 

  ("cheval_perdu", "Le cheval dans la prairie.", 0,
  "{!}None"
  ), 

   ("pour_le_duc", "Pour le Duc !", 0,
  "{!}None"
  ),

    ("fer_pour_la_guerre", "Du fer pour la guerre.", 0,
  "{!}None"
  ), 

    ("volntaires_mine", "Des volontaires.", 0,
  "{!}None"
  ),

    ("expedition_mine", "Vers le centre de la terre.", 0,
  "{!}None"
  ),  

    ("terrier", "Le terrier des hermines de fer.", 0,
  "{!}None"
  ),  

    ("tuer_mercenaire", "Par tous les moyens.", 0,
  "{!}None"
  ),  

    ("bois_descerfs", "Le bois des cerfs.", 0,
  "{!}None"
  ),  

    ("port_lac", "La porte du lac.", 0,
  "{!}None"
  ),  

    ("pnj_perdu_foretaub", "La foret glacée.", 0,
  "{!}None"
  ),
#quetes cranes de fer
    ("vangeance_cravane", "La revanche des Caravaniers.", 0,
  "{!}None"
  ),

     ("surveillance1", "Le poste de garde.", 0,
  "{!}None"
  ),

      ("siege_penthievre", "Le siège de Quintin.", 0,
  "{!}None"
  ),

 #si trouv� le passage secret et rassembl� avec moi des deserteurs = lancer l'assaut indisciplin� de quintin et titre : "Le Renard et la colombe"
 
 ("freelancer_enlisted", "Enlisted in the Party of {s13}", 0,
   "{!}You are currently enlisted in the party of {s13} of {s14}."),
 ("freelancer_vacation", "Enlisted: On Leave", 0,
   "{!}You have been granted leave from the party of {s13} of {s14}."),
 ("freelancer_captured", "Enlisted: Captured", 0,
   "{!}Your commander's party has been defeated and you have been captured. Return to the service of {s13} of {s14}."),
  
 ("quests_end", "Quests End", 0, "{!}."),
]
