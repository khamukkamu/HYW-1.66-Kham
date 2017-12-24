from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed.
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#rebels
("black_khergit", "Rebelles", icon_axeman|carries_goods(2), 0, fac_black_khergits, soldier_personality, [(trp_rebel_heros,1,1),(trp_rebel_archer,2,14),(trp_rebel_arbaletier,2,11),(trp_rebel_fantassin,4,12),(trp_rebel_piquier,3,10),(trp_rebel_paysan,1,20)] ),
#rebels fin
("steppe_bandits", "Plundering Bandits", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_steppe_bandit,10,38)] ),
("taiga_bandits", "Tundra Bandits", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_taiga_bandit,4,30),(trp_taiga_bandit_2,4,15),(trp_taiga_bandit_3,4,15)] ),
("desert_bandits","Desert Bandits",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,4,58)]),
("forest_bandits", "Forest Bandits", icon_axeman|carries_goods(2), 0, fac_forest_bandits, bandit_personality, [(trp_forest_bandit,4,42),(trp_forest_bandit_2,4,32)] ),
("mountain_bandits", "Mountain Bandits", icon_axeman|carries_goods(2), 0, fac_mountain_bandits, bandit_personality, [(trp_mountain_bandit,24,70),(trp_mountain_bandit_2,4,20),(trp_mountain_bandit_3,4,20)] ),
("sea_raiders", "Coastal Raiders", icon_axeman|carries_goods(2), 0, fac_outlaws, bandit_personality, [(trp_sea_raider,5,40),(trp_sea_raider_2,2,20)] ),

("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),

("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
("center_reinforcements", "Reinforcements", icon_axeman|carries_goods(16), 0, fac_commoners, soldier_personality, [(trp_townsman,5,30),(trp_watchman,4,20)] ),

("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),

# Reinforcements
# each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
# less-modernised templates are generally includes 7-14 troops in total,
# med-modernised templates are generally includes 5-10 troops in total,
# high-modernised templates are generally includes 3-5 troops in total

("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,1,5),(trp_swadian_crossbowman,1,4),(trp_swadian_militia,1,4)]),
("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_genoese_crossbowman,2,7),(trp_swadian_infantry,2,7),(trp_french_spearmen,1,2)] ),
("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,2,5),(trp_swadian_knight,2,5),(trp_french_chevalier_banneret,1,4)] ),
("kingdom_1_reinforcements_d", "kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_coulveriners_f,2,20),(trp_arquebusier_f,2,10),(trp_swadian_man_at_arms,1,5),(trp_swadian_knight,1,4),(trp_french_chevalier_banneret,2,6)] ),

("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,2,6),(trp_vaegir_recruit,1,4),(trp_vaegir_archer,1,8)] ),
("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_marksman,4,8),(trp_english_pikeman,1,5),(trp_vaegir_infantry,1,2)] ),
("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,1,3),(trp_english_dismounted_knight,1,5),(trp_english_halberdier,1,6),(trp_vaegir_knight,1,2)] ),
("kingdom_2_reinforcements_d", "kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_coulveriners_anglais,5,20),(trp_vaegir_horseman,1,3),(trp_english_dismounted_knight,1,5),(trp_english_halberdier,1,5),(trp_vaegir_knight,1,2)] ),

("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bourg_veteran,2,6),(trp_bourg_recruit,1,6),(trp_bourg_archer,1,6)]),
("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_bourg_marksman,2,7),(trp_bourg_pikeman,2,6)] ),
("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_bourg_horseman,1,3),(trp_bourg_dismounted_knight,1,5),(trp_bourg_halberdier,2,8),(trp_bourg_knight,1,2)] ),

#HYW
#  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_tribesman,3,5),(trp_khergit_skirmisher,4,9)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
#  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_horse_archer,2,4),(trp_khergit_skirmisher,1,2)]),
#  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_khergit_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_breton_veteran,2,6),(trp_breton_recruit,1,6),(trp_breton_archer,1,6)]),
("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_breton_marksman,2,7),(trp_breton_pikeman,2,6)] ),
("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_breton_horseman,1,3),(trp_breton_dismounted_knight,1,5),(trp_breton_halberdier,2,8),(trp_breton_knight,1,2)] ),

#  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_tribesman,5,10),(trp_rhodok_spearman,2,4)]),
#  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_crossbowman,3,6),(trp_rhodok_trained_crossbowman,2,4)]),
#  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,3),(trp_rhodok_veteran_crossbowman,1,2)]),

#  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sarranid_recruit,5,10),(trp_sarranid_footman,2,4)]),
#  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_skirmisher,2,4),(trp_sarranid_veteran_footman,2,3),(trp_sarranid_footman,1,3)]),
#  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,3,5)]),
#HYW


("steppe_bandit_lair" ,"Steppe Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
("taiga_bandit_lair","Tundra Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
("desert_bandit_lair" ,"Desert Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
("forest_bandit_lair" ,"Forest Bandit Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
("mountain_bandit_lair" ,"Mountain Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
("sea_raider_lair","Sea Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),



("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

("english_con", "Convoi d'armes Anglais", icon_gray_knight|carries_goods(2), 0, fac_Convoi_weapons, soldier_personality, [(trp_covoy_english_guard,1,1),(trp_covoy_english_guard2,4,16),(trp_covoy_english_guard3,4,12)] ),

#sangLys
("sang_lys", "Compagnie du SansLys", icon_axeman|carries_goods(2), 0, fac_kingdom_1, bandit_personality, [(trp_serg_sang_lysbasetroop,1,1),(trp_sang_lysbasetroop,10,20)] ),

#vilandrandro quete bourges
("quest_viland_bourges", "La grande Compagnie de Vilandrandro", icon_axeman|carries_goods(2), 0, fac_viland_quest_bourges, bandit_personality, [(trp_vilandrandro_quest_fanta,1,1),(trp_vilandrandro_quest_fanta2,70,90),(trp_vilandrandro_quest_arbaletier,20,40)] ),

#rebels des catas exterieur
("catareb", "Rebelles de Paris", icon_axeman|carries_goods(2), 0, fac_black_khergits, soldier_personality, [(trp_parisassau_rchef,1,1),(trp_parisassau_troop1,4,26),(trp_parisassau_troop2,4,26),(trp_parisassau_troop_wo,4,16)] ),

#crane_de_fer
("cranede_fer", "Compagnie des Cranes de Fer", icon_axeman|carries_goods(2), 0, fac_kingdom_4, bandit_personality, [(trp_crane_de_fer_sergent,1,1),(trp_crane_de_fer_fantassin,5,21),(trp_crane_de_fer_archer,4,17)] ),

 ("bandits_rennes", "Tueurs de caravaniers", icon_axeman|carries_goods(2), 0, fac_viland_quest_bourges, soldier_personality, [(trp_tueur_caravane_chef,1,1),(trp_tueur_caravane_1,4,8),(trp_tueur_caravane_2,4,8)] ),


]
