# -*- coding: cp1252 -*-
from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *
from compiler import *
####################################################################################################################
#  Each item record contains the following fields:  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# def custom_reskin(item):
  # return (ti_on_init_item, [
   ## (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    # (store_trigger_param_2, ":troop_no"),
    # (str_clear, s1),
    # (item_get_slot, ":start", item, slot_item_materials_begin),
    # (item_get_slot, ":end", item, slot_item_materials_end),
    # (store_sub, ":total", ":end", ":start"),
    # (gt, ":total", 0),
    # (try_begin),
      # (gt, ":troop_no", -1),
      # (troop_is_hero, ":troop_no"),
      # (item_get_slot, ":value", item, slot_item_player_color),
      # (neq, ":value", -1),
      # (val_mod, ":value", ":total"),
      # (val_add, ":value", ":start"),
    # (else_try),
      # (store_random_in_range, ":value", ":start", ":end"),
    # (try_end),
    # (try_begin),
      # (str_store_string, s1, ":value"),
      # (cur_item_set_material, s1, 0),
    # (try_end),
    # ])
	 
# def custom_remodel(item):
  # return (ti_on_init_item, [
    ## (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    # (store_trigger_param_2, ":troop_no"),
    # (str_clear, s1),
    # (item_get_slot, ":start", item, slot_item_materials_begin),
    # (item_get_slot, ":end", item, slot_item_materials_end),
    # (store_sub, ":total", ":end", ":start"),
    # (gt, ":total", 0),
    # (try_begin),
      # (gt, ":troop_no", -1),
      # (troop_is_hero, ":troop_no"),
      # (item_get_slot, ":value", item, slot_item_player_color),
      # (neq, ":value", -1),
      # (val_mod, ":value", ":total"),
      # (val_add, ":value", ":start"),
    # (else_try),
      # (store_random_in_range, ":value", ":start", ":end"),
    # (try_end),
    # (try_begin),
      # (str_store_string, s1, ":value"),
      # (cur_item_add_mesh, s1, 0),
    # (try_end),
    # ])	  	 
	 
def custom_reskin(item):
  return (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    (item_get_slot, ":start", item, slot_item_materials_begin),
    (item_get_slot, ":end", item, slot_item_materials_end),
    
    (item_get_slot, ":france_start", item, slot_item_france_materials_begin),
    (item_get_slot, ":france_end", item, slot_item_france_materials_end),
    
    (item_get_slot, ":english_start", item, slot_item_english_materials_begin),
    (item_get_slot, ":english_end", item, slot_item_english_materials_end),
    
    (item_get_slot, ":burgundy_start", item, slot_item_burgundy_materials_begin),
    (item_get_slot, ":burgundy_end", item, slot_item_burgundy_materials_end),
    
    (item_get_slot, ":breton_start", item, slot_item_breton_materials_begin),
    (item_get_slot, ":breton_end", item, slot_item_breton_materials_end),
	 
    (item_get_slot, ":flemish_start", item, slot_item_flemish_materials_begin),
    (item_get_slot, ":flemish_end", item, slot_item_flemish_materials_end),	 

    (item_get_slot, ":rebel_start", item, slot_item_rebel_materials_begin),
    (item_get_slot, ":rebel_end", item, slot_item_rebel_materials_end),	 	 
	 
    (store_troop_faction, ":faction", ":troop_no"),
	 
    (store_sub, ":total", ":end", ":start"),
    (gt, ":total", 0),
	 
    (try_begin),
      (gt, ":troop_no", -1),
      (troop_is_hero, ":troop_no"),
      (item_get_slot, ":value", item, slot_item_player_color),
      (neq, ":value", -1),
      (val_mod, ":value", ":total"),
      (val_add, ":value", ":start"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_1"),
    	(store_random_in_range, ":value", ":france_start", ":france_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_2"),
    	(store_random_in_range, ":value", ":english_start", ":english_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_3"),
    	(store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_4"),
    	(store_random_in_range, ":value", ":breton_start", ":breton_end"),
    (else_try),
    	(eq, ":faction", "fac_flemish_mercenaries"),
    	(store_random_in_range, ":value", ":flemish_start", ":flemish_end"),	
    (else_try),
    	(eq, ":faction", "fac_rebels"),
    	(store_random_in_range, ":value", ":rebel_start", ":rebel_end"),			
    (else_try),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (str_store_string, s1, ":value"),
      (cur_item_set_material, s1, 0),
    (try_end),
    ])	 
	 
def custom_remodel(item):
  return (ti_on_init_item, [
    # (store_trigger_param_1, ":agent_no"), #disabled to suppress compiler warnings
    (store_trigger_param_2, ":troop_no"),
    (str_clear, s1),
    (item_get_slot, ":start", item, slot_item_materials_begin),
    (item_get_slot, ":end", item, slot_item_materials_end),
    
    (item_get_slot, ":france_start", item, slot_item_france_materials_begin),
    (item_get_slot, ":france_end", item, slot_item_france_materials_end),
    
    (item_get_slot, ":english_start", item, slot_item_english_materials_begin),
    (item_get_slot, ":english_end", item, slot_item_english_materials_end),
    
    (item_get_slot, ":burgundy_start", item, slot_item_burgundy_materials_begin),
    (item_get_slot, ":burgundy_end", item, slot_item_burgundy_materials_end),
    
    (item_get_slot, ":breton_start", item, slot_item_breton_materials_begin),
    (item_get_slot, ":breton_end", item, slot_item_breton_materials_end),
	 
    (item_get_slot, ":flemish_start", item, slot_item_flemish_materials_begin),
    (item_get_slot, ":flemish_end", item, slot_item_flemish_materials_end),		 
	 
    (item_get_slot, ":rebel_start", item, slot_item_rebel_materials_begin),
    (item_get_slot, ":rebel_end", item, slot_item_rebel_materials_end),	 	 

    (store_troop_faction, ":faction", ":troop_no"),
	 
    (store_sub, ":total", ":end", ":start"),
    (gt, ":total", 0),
	 
    (try_begin),
      (gt, ":troop_no", -1),
      (troop_is_hero, ":troop_no"),
      (item_get_slot, ":value", item, slot_item_player_color),
      (neq, ":value", -1),
      (val_mod, ":value", ":total"),
      (val_add, ":value", ":start"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_1"),
    	(store_random_in_range, ":value", ":france_start", ":france_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_2"),
    	(store_random_in_range, ":value", ":english_start", ":english_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_3"),
    	(store_random_in_range, ":value", ":burgundy_start", ":burgundy_end"),
    (else_try),
    	(eq, ":faction", "fac_kingdom_4"),
    	(store_random_in_range, ":value", ":breton_start", ":breton_end"),
    (else_try),
    	(eq, ":faction", "fac_flemish_mercenaries"),
    	(store_random_in_range, ":value", ":flemish_start", ":flemish_end"),	
    (else_try),
    	(eq, ":faction", "fac_rebels"),
    	(store_random_in_range, ":value", ":rebel_start", ":rebel_end"),			
    (else_try),
      (store_random_in_range, ":value", ":start", ":end"), #Anyone else gets a random mix of everything
    (try_end),
    (try_begin),
      (str_store_string, s1, ":value"),
      (cur_item_add_mesh, s1, 0),
    (try_end),
    ])	

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
["tutorial_short_bow", "Short Bow", [("w_short_bow_ash",0),("w_short_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1)|difficulty(0)|spd_rtng(98)|shoot_speed(53)|thrust_damage(12,pierce), imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|difficulty(0)|spd_rtng(70)|shoot_speed(90)|thrust_damage(32,pierce)|max_ammo(1), imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["tutorial_dagger","Dagger", [("w_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


["horse_meat", "Horse Meat", [("raw_meat",0)], itp_type_goods|itp_food|itp_consumable, 0, 18, weight(40)|food_quality(30)|max_ammo(40), imodbits_none ],
# Items before this point are hardwired and their order should not be changed!
["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
["practice_dagger","Practice Dagger", [("w_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
["arena_axe", "Axe", [("w_onehanded_war_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
["arena_sword", "Sword", [("w_onehanded_sword_hospitaller",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
["arena_sword_two_handed",  "Two Handed Sword", [("w_twohanded_sword_steward",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
["arena_lance",         "Lance", [("w_lance_6",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_great_lance_upstab, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
["practice_shield","Practice Shield", [("s_small_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
["practice_bow", "Practice Bow", [("w_hunting_bow_ash",0),("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90)|shoot_speed(55)|thrust_damage(21,blunt), imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(70)|shoot_speed(90)|thrust_damage(32,blunt)|max_ammo(1), imodbits_crossbow ],
["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new",ixmesh_carry)], itp_type_thrown|itp_primary|itp_next_item_as_melee, itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5)|spd_rtng(91)|shoot_speed(28)|thrust_damage(32,pierce)|max_ammo(50)|weapon_length(75), imodbits_thrown ],
["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown|itp_primary, itcf_throw_knife, 193, weight(3.5)|spd_rtng(110)|shoot_speed(25)|thrust_damage(25,blunt)|max_ammo(13)|weapon_length(0), imodbits_thrown ],
["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
["practice_arrows", "Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|weapon_length(95)|max_ammo(80), imodbits_missile ],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
["practice_arrows_10_amount", "Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|weapon_length(95)|max_ammo(10), imodbits_missile ],
["practice_arrows_100_amount", "Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|weapon_length(95)|max_ammo(100), imodbits_missile ],
["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
["practice_boots", "Practice Boots", [("b_leather_boots",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
["red_tourney_armor", "Red Tourney Armor", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["blue_tourney_armor", "Blue Tourney Armor", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["green_tourney_armor", "Green Tourney Armor", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["gold_tourney_armor", "Gold Tourney Armor", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["red_tourney_helmet", "Red Tourney Helmet", [("tilting_helm_crow",0)], itp_type_head_armor, 0, 1240, weight(2.75)|head_armor(55), imodbits_none ],
["gold_tourney_helmet", "Gold Tourney Helmet", [("tilting_helm_horns",0)], itp_type_head_armor, 0, 1240, weight(2.75)|head_armor(55), imodbits_none ],

["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("tilting_helm_crow",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("tilting_helm_unicorn",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("tilting_helm_swan_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("great_helm_joust_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("tilting_helmet",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_red", "Steppe Helmet Red", [("tilting_helm_crow",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_blue", "Steppe Helmet Blue", [("tilting_helm_unicorn",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_green", "Steppe Helmet Green", [("tilting_helm_swan_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("great_helm_joust_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_white", "Tourney Helm White", [("tilting_helmet",0)], itp_type_head_armor|itp_covers_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tilting_helm_crow",0)], itp_type_head_armor|itp_covers_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tilting_helm_unicorn",0)], itp_type_head_armor|itp_covers_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tilting_helm_swan_f",0)], itp_type_head_armor|itp_covers_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("great_helm_joust_f",0)], itp_type_head_armor|itp_covers_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tilting_helm_crow",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tilting_helm_unicorn",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tilting_helm_swan_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("great_helm_joust_f",0)], itp_type_head_armor|itp_fit_to_head, 0, 1240, weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
["book_leadership","The Life of Alexander the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

#other trade goods (first one is spice)
["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],


#["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

["iron", "Iron", [("iron",0)], itp_type_goods|itp_merchandise, 0, 110, weight(60)|abundance(60), imodbits_none ],
["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],
["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|food_quality(50)|max_ammo(50),imodbits_none],
["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|food_quality(50)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
["cheese", "Cheese", [("cheese_b",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, weight(6)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
["sausages", "Sausages", [("sausages",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, weight(10)|abundance(110)|food_quality(40)|max_ammo(40), imodbits_none ],
["cabbages", "Cabbages", [("cabbage",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 40, weight(15)|abundance(110)|food_quality(40)|max_ammo(50), imodbits_none ],
["dried_meat", "Dried Meat", [("raw_meat",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, weight(15)|abundance(100)|food_quality(70)|max_ammo(50), imodbits_none ],
["apples", "Fruit", [("apple_basket",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 54, weight(20)|abundance(110)|food_quality(40)|max_ammo(50), imodbits_none ],
["raw_grapes", "Grapes", [("grapes_inventory",0)], itp_type_goods|itp_merchandise|itp_consumable, 0, 85, weight(40)|abundance(90)|food_quality(10)|max_ammo(10), imodbits_none ],
["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
["grain", "Grain", [("wheat_sack",0)], itp_type_goods|itp_merchandise|itp_consumable, 0, 40, weight(30)|abundance(110)|food_quality(40)|max_ammo(50), imodbits_none ],

["cattle_meat", "Beef", [("smoked_meat",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, weight(20)|abundance(100)|food_quality(80)|max_ammo(50), imodbits_none ],
["bread", "Bread", [("bread_a",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 70, weight(30)|abundance(110)|food_quality(40)|max_ammo(50), imodbits_none ],
["bier", "Cervoise", [("bierr",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, weight(30)|abundance(70)|food_quality(50)|max_ammo(50), imodbits_none ],
["vinn", "Vin", [("vinn",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 220, weight(30)|abundance(60)|food_quality(50)|max_ammo(50), imodbits_none ],
["rhumm", "Hydromel", [("rhumm",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 310, weight(30)|abundance(70)|food_quality(50)|max_ammo(50), imodbits_none ],
["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
["pork", "Pork", [("pork",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, weight(15)|abundance(100)|food_quality(70)|max_ammo(50), imodbits_none ],
["butter", "Butter", [("oil",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 150, weight(6)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["oeufss", "Oeufs", [("fry_pan_a",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 70, weight(4)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["soup", "Soupe", [("plate_b",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 76, weight(6)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["pate1", "terrine de lapin", [("pate3",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, weight(2)|abundance(110)|food_quality(50)|max_ammo(30), imodbits_none ],
["pate2", "paté de chevreuil", [("pate2",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, weight(2)|abundance(110)|food_quality(40)|max_ammo(40), imodbits_none ],
["pate3", "paté de sanglier", [("pate1",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 85, weight(2)|abundance(70)|food_quality(50)|max_ammo(40), imodbits_none ],
["sausc", "sauscissons", [("sausc",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 95, weight(2)|abundance(110)|food_quality(50)|max_ammo(30), imodbits_none ],



["pasteques", "Pasteque", [("marrow_b",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 75, weight(6)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["melons", "Melon", [("marrow_a",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 78, weight(4)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["champi", "Champignons", [("champi_2",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 15, weight(5)|abundance(110)|food_quality(20)|max_ammo(30), imodbits_none ],
["fesan", "Faisans", [("item_from_quest_9",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 230, weight(8)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["legum", "Panier de légumes", [("item_from_quest_21",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 25, weight(5)|abundance(110)|food_quality(20)|max_ammo(30), imodbits_none ],
["potee", "Potée de choux", [("item_from_quest_23",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 260, weight(8)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],
["poiss_soup", "Soupe de poissons", [("item_from_quest_24",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 270, weight(8)|abundance(110)|food_quality(40)|max_ammo(30), imodbits_none ],


#Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
# Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Tutorial Items

["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["tutorial_arrows", "Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(20), imodbits_missile ],
["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
["tutorial_short_bow", "Short Bow", [("w_short_bow_ash",0),("w_short_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1)|difficulty(0)|spd_rtng(98)|shoot_speed(53)|thrust_damage(16,pierce), imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|difficulty(0)|spd_rtng(70)|shoot_speed(90)|thrust_damage(32,pierce)|max_ammo(1), imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],




###################################################################################################### HYW HORSES
# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
["ho_sumpter_1", "Sumpter Horse", [("ho_sumpter_1",0)], itp_type_horse|itp_merchandise, 0, 299, abundance(100)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(36)|horse_maneuver(42)|horse_charge(10)|horse_scale(100), imodbits_horse_basic ],
["ho_sumpter_2", "Sumpter Horse", [("ho_sumpter_2",0)], itp_type_horse|itp_merchandise, 0, 299, abundance(100)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(36)|horse_maneuver(42)|horse_charge(10)|horse_scale(100), imodbits_horse_basic ],

["ho_rouncey_1", "Rouncey Horse", [("ho_rouncey_1",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_2", "Rouncey Horse", [("ho_rouncey_2",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_3", "Rouncey Horse", [("ho_rouncey_3",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_4", "Rouncey Horse", [("ho_rouncey_4",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_5", "Rouncey Horse", [("ho_rouncey_5",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],
["ho_rouncey_6", "Rouncey Horse", [("ho_rouncey_6",0)], itp_type_horse|itp_merchandise, 0, 341, abundance(90)|hit_points(110)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(42)|horse_charge(12)|horse_scale(100), imodbits_horse_basic ],

["ho_courser_1", "Courser", [("ho_courser_1",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_2", "Courser", [("ho_courser_2",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_3", "Courser", [("ho_courser_3",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_4", "Courser", [("ho_courser_4",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_5", "Courser", [("ho_courser_5",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_6", "Courser", [("ho_courser_6",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_7", "Courser", [("ho_courser_7",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_8", "Courser", [("ho_courser_8",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_9", "Courser", [("ho_courser_9",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["ho_courser_10", "Courser", [("ho_courser_10",0)], itp_type_horse|itp_merchandise, 0, 493, abundance(80)|body_armor(14)|hit_points(90)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(16)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],

["ho_hunting_horse_france", "French Hunter", [("ho_hunting_horse_france",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(70)|hit_points(120)|body_armor(14)|difficulty(2)|horse_speed(44)|horse_maneuver(42)|horse_charge(20)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_hunting_horse_england", "English Hunter", [("ho_hunting_horse_england",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(70)|hit_points(120)|body_armor(14)|difficulty(2)|horse_speed(44)|horse_maneuver(42)|horse_charge(20)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_horse_barded_black", "Barded Horse", [("ho_horse_barded_black",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_blue", "Barded Horse", [("ho_horse_barded_blue",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_brown", "Barded Horse", [("ho_horse_barded_brown",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_green", "Barded Horse", [("ho_horse_barded_green",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_red", "Barded Horse", [("ho_horse_barded_red",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_white", "Barded Horse", [("ho_horse_barded_white",0)], itp_type_horse|itp_merchandise, 0, 624, abundance(60)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_horse_barded_black_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_black_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_blue_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_blue_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_brown_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_brown_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_green_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_green_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_red_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_red_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_horse_barded_white_chamfrom", "Barded Horse with Chamfrom", [("ho_horse_barded_white_chamfrom",0)], itp_type_horse|itp_merchandise, 0, 983, abundance(40)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(38)|horse_charge(26)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_war_horse_breton", "Breton War Horse", [("ho_war_horse_breton",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_england_1", "English War Horse", [("ho_war_horse_england_1",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_england_2", "English War Horse", [("ho_war_horse_england_2",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_england_3", "English War Horse", [("ho_war_horse_england_3",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_france_1", "French War Horse", [("ho_war_horse_france_1",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_france_2", "French War Horse", [("ho_war_horse_france_2",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_war_horse_france_3", "French War Horse", [("ho_war_horse_france_3",0)], itp_type_horse|itp_merchandise, 0, 1445, abundance(40)|hit_points(120)|body_armor(22)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["ho_charger_black_prince", "Charger", [("ho_charger_black_prince",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_breton", "Charger", [("ho_charger_breton",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_chandos", "Charger", [("ho_charger_chandos",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_charles", "Charger", [("ho_charger_charles",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_edward", "Charger", [("ho_charger_edward",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["ho_charger_guesclin", "Charger", [("ho_charger_guesclin",0)], itp_type_horse|itp_merchandise, 0, 1540, abundance(40)|hit_points(120)|body_armor(25)|difficulty(3)|horse_speed(42)|horse_maneuver(40)|horse_charge(28)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],

["sumpter_horse", "Sumpter Horse", [("sumpter_horse",0)], itp_type_horse|itp_merchandise, 0, 254, abundance(90)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100), imodbits_horse_basic ],
["sumpter_horse_paris", "Cheval malade", [("sumpter_horse",0)], itp_type_horse|itp_merchandise, 0, 134, abundance(90)|hit_points(90)|body_armor(7)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100), imodbits_horse_basic ],
["saddle_horse", "Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 360, abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],
["saddle_horseparis", "Cheval faible", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 50, abundance(90)|hit_points(88)|body_armor(6)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],
["saddle_horseparis2", "Cheval faible", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 50, abundance(90)|hit_points(87)|body_armor(6)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HELMETS ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["h_bascinet_great", "Great Bascinet", [("h_bascinet_great",0)], itp_merchandise|itp_type_head_armor |itp_covers_head| itp_attach_armature  ,0, 540 , weight(3)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_bascinet_great_fi", "Great Bascinet", [("h_bascinet_great_fi",0)], itp_merchandise|itp_type_head_armor |itp_covers_head| itp_attach_armature  ,0, 540 , weight(3)|abundance(100)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_zitta_bascinet", "Houndskull Bascinet", [("h_zitta_bascinet",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 520 , weight(3)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_hounskull_narf", "Houndskull Bascinet", [("h_houndskull_narf",0)], itp_merchandise|itp_type_head_armor|itp_covers_head| itp_attach_armature   ,0, 500 , weight(3)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_klappvisier_pigface", "Pigface Bascinet", [("h_klappvisier_pigface",0)], itp_merchandise|itp_type_head_armor|itp_covers_head| itp_attach_armature   ,0, 500 , weight(3)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_klappvisier_pigface_open", "Pigface Bascinet", [("h_klappvisier_pigface_open",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 500 , weight(3)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_houndskull_thick", "Houndskull Bascinet", [("h_houndskull_thick",0)], itp_merchandise|itp_type_head_armor|itp_covers_head| itp_attach_armature   ,0, 480 , weight(3)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_houndskull_fi", "Houndskull Bascinet", [("h_houndskull_fi",0)], itp_merchandise|itp_type_head_armor|itp_covers_head| itp_attach_armature   ,0, 480 , weight(3)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_bascinet_fi_noseguard", "Bascinet with Noseguard", [("h_bascinet_fi_noseguard",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 470 , weight(2.25)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_zitta_bascinet_novisor", "Bascinet with Aventail", [("h_zitta_bascinet_novisor",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 450 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["h_bascinet_oniontop", "Onion-top Bascinet", [("h_bascinet_oniontop",0)], itp_merchandise|itp_type_head_armor| itp_attach_armature   ,0, 450 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],


["h_barbute_1", "Barbute", [("h_barbute_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 360 , weight(2.5)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["h_barbute_1_padded", "Barbute", [("h_barbute_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 420 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_barbute_1_mail", "Barbute", [("h_barbute_1",0)],  itp_type_head_armor| itp_attach_armature   ,0, 450 , weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_barbute_2", "Barbute", [("h_barbute_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 360 , weight(2.5)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["h_barbute_2_padded", "Barbute", [("h_barbute_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 420 , weight(2.5)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_barbute_2_mail", "Barbute", [("h_barbute_2",0)],  itp_type_head_armor| itp_attach_armature   ,0, 450 , weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

# Bascinet Base: 29; Hood: 8; Padding: 12; Mail Narf: 16
["h_bascinet_fi_padded", "Bascinet with Padded Cloth", [("h_bascinet_fi",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 410 , weight(1.75)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_bascinet_fi_mail", "Bascinet with Mail Coif", [("h_bascinet_fi",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 450 , weight(1.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

# Eyeslot Kettlehat Base: 28; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_kettlehat_eyeslot_padded", "Kettle Helmet with Padded Cloth", [("h_kettlehat_eyeslot",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_eyeslot_mail", "Kettle Helmet with Mail Coif", [("h_kettlehat_eyeslot",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 440 , weight(1.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_eyeslot_gorget", "Kettle Helmet with Gorget", [("h_kettlehat_eyeslot",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 460 , weight(2)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

# Sallet Base: 26; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_sallet_padded", "Sallet Helmet with Padded Cloth", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_sallet_mail", "Sallet Helmet with Mail Coif", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 420 , weight(1.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_sallet_gorget", "Sallet Helmet with Gorget", [("h_sallet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 440 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

# Cerveliere Base: 25; Hood: 8; Padding: 12; Mail Narf: 16
["h_cerveliere_padded", "Cerveliere with Padded Cloth", [("h_cerveliere",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 370 , weight(1.5)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_cerveliere_mail", "Cerveliere with Mail Coif", [("h_cerveliere",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 410 , weight(1.5)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

# Byzantion Base: 24; Hood: 8; Padding: 12; Mail Narf: 16
["h_byzantion_padded", "Byzantion Helmet with Padded Cloth", [("h_byzantion",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 360 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_byzantion_mail", "Byzantion Helmet with Mail Coif", [("h_byzantion",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(1.75)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

["h_byzantion_painted_padded", "Byzantion Helmet with Padded Cloth", [("h_byzantion_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_byzantion_painted_mail", "Byzantion Helmet with Mail Coif", [("h_byzantion_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

# Chapel de Fer Base: 22; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_chapel_de_fer_1_padded", "Chapel de Fer with Padded Cloth", [("h_chapel_de_fer_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_chapel_de_fer_1_mail", "Chapel de Fer with Mail Coif", [("h_chapel_de_fer_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_chapel_de_fer_1_gorget", "Chapel de Fer with Gorget", [("h_chapel_de_fer_1",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_chapel_de_fer_2_padded", "Chapel de Fer with Padded Cloth", [("h_chapel_de_fer_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_chapel_de_fer_2_mail", "Chapel de Fer with Mail Coif", [("h_chapel_de_fer_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_chapel_de_fer_2_gorget", "Chapel de Fer with Gorget", [("h_chapel_de_fer_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_chapel_de_fer_3_padded", "Chapel de Fer with Padded Cloth", [("h_chapel_de_fer_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_chapel_de_fer_3_mail", "Chapel de Fer with Mail Coif", [("h_chapel_de_fer_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_chapel_de_fer_3_gorget", "Chapel de Fer with Gorget", [("h_chapel_de_fer_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_chapel_de_fer_4_padded", "Chapel de Fer with Padded Cloth", [("h_chapel_de_fer_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_chapel_de_fer_4_mail", "Chapel de Fer with Mail Coif", [("h_chapel_de_fer_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_chapel_de_fer_4_gorget", "Chapel de Fer with Gorget", [("h_chapel_de_fer_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

# Kettle Hat Base: 22; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_kettlehat_padded", "Kettle Hat with Padded Cloth", [("h_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_mail", "Kettle Hat with Mail Coif", [("h_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_gorget", "Kettle Hat with Gorget", [("h_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_kettlehat_2_padded", "Kettle Hat with Padded Cloth", [("h_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_2_mail", "Kettle Hat with Mail Coif", [("h_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_2_gorget", "Kettle Hat with Gorget", [("h_kettlehat_2",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_kettlehat_3_padded", "Kettle Hat with Padded Cloth", [("h_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_3_mail", "Kettle Hat with Mail Coif", [("h_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_3_gorget", "Kettle Hat with Gorget", [("h_kettlehat_3",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_kettlehat_4_padded", "Kettle Hat with Padded Cloth", [("h_kettlehat_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_4_mail", "Kettle Hat with Mail Coif", [("h_kettlehat_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_4_gorget", "Kettle Hat with Gorget", [("h_kettlehat_4",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_kettlehat_painted_padded", "Kettle Hat with Padded Cloth", [("h_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_kettlehat_painted_mail", "Kettle Hat with Mail Coif", [("h_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_kettlehat_painted_gorget", "Kettle Hat with Gorget", [("h_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

# Round Kettle Hat Base: 20; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_round_kettlehat_padded", "Kettle Hat with Padded Cloth", [("h_round_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 320 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_round_kettlehat_mail", "Kettle Hat with Mail Coif", [("h_round_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 360 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_round_kettlehat_gorget", "Kettle Hat with Gorget", [("h_round_kettlehat",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

["h_round_kettlehat_painted_padded", "Kettle Hat with Padded Cloth", [("h_round_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 320 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_round_kettlehat_painted_mail", "Kettle Hat with Mail Coif", [("h_round_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 360 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],
["h_round_kettlehat_painted_gorget", "Kettle Hat with Gorget", [("h_round_kettlehat_painted",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 400 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_gorget", 0, 0),(cur_item_add_mesh, "@o_gorget_strap", 0, 0),])]],

# Pot Helmet Base: 14; Hood: 8; Padding: 12; Mail Narf: 16
["h_pot_helmet_padded", "Pot Helmet with Padded Cloth", [("h_pot_helmet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 260 , weight(1.75)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_padded_coif_narf", 0, 0),])]],
["h_pot_helmet_mail", "Pot Helmet with Mail Coif", [("h_pot_helmet",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[(ti_on_init_item,[(cur_item_add_mesh, "@o_mail_coif_narf", 0, 0),])]],

["h_mail_coif_full", "Mail Coif", [("h_mail_coif_full",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature   ,0, 240 , weight(1.25)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["h_mail_coif_balaclava", "Mail Coif", [("h_mail_coif_balaclava",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature   ,0, 220 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["h_mail_coif", "Mail Coif", [("h_mail_coif",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature   ,0, 200 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HOODS | HATS ##########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################
# Light headgear
["h_arming_cap", "Arming Cap", [("h_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_simple_coif", "Arming Cap", [("h_simple_coif",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 4, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_leather_cap", "Leather Cap", [("h_leather_cap",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_mitre", "Mitre", [("h_mitre",0)],  itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_straw_hat", "Straw Hat", [("h_straw_hat",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Women headgear
["habit", "Coiffe", [("habit",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["habit_flying", "Coiffe", [("habit_flying",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_court_barbette", "Barbette", [("h_court_barbette",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_court_lady_hood", "Lady's Hood", [("h_court_lady_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_court_wimple_1", "Wimple", [("h_court_wimple_1",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_court_wimple_2", "Wimple", [("h_court_wimple_2",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Woolen Cap
["h_woolen_cap_black", "Woolen Cap", [("h_woolen_cap_black",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_blue", "Woolen Cap", [("h_woolen_cap_blue",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_brown", "Woolen Cap", [("h_woolen_cap_brown",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_green", "Woolen Cap", [("h_woolen_cap_green",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_red", "Woolen Cap", [("h_woolen_cap_red",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_white", "Woolen Cap", [("h_woolen_cap_white",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_woolen_cap_yellow", "Woolen Cap", [("h_woolen_cap_yellow",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Felt Hats
["h_felt_hat_b_black", "Felt Hat", [("h_felt_hat_b_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_blue", "Felt Hat", [("h_felt_hat_b_blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_brown", "Felt Hat", [("h_felt_hat_b_brown",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_green", "Felt Hat", [("h_felt_hat_b_green",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_red", "Felt Hat", [("h_felt_hat_b_red",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_white", "Felt Hat", [("h_felt_hat_b_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_b_yellow", "Felt Hat", [("h_felt_hat_b_yellow",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["h_felt_hat_black", "Felt Hat", [("h_felt_hat_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_blue", "Felt Hat", [("h_felt_hat_blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_brown", "Felt Hat", [("h_felt_hat_brown",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_green", "Felt Hat", [("h_felt_hat_green",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_red", "Felt Hat", [("h_felt_hat_red",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_white", "Felt Hat", [("h_felt_hat_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_felt_hat_yellow", "Felt Hat", [("h_felt_hat_yellow",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# Berets
["h_highlander_beret_black", "Beret", [("h_highlander_beret_black",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_blue", "Beret", [("h_highlander_beret_blue",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_brown", "Beret", [("h_highlander_beret_brown",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_green", "Beret", [("h_highlander_beret_green",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_red", "Beret", [("h_highlander_beret_red",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_white", "Beret", [("h_highlander_beret_white",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_yellow", "Beret", [("h_highlander_beret_yellow",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 45, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],

["h_highlander_beret_black_2", "Beret with plume", [("h_highlander_beret_black_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_blue_2", "Beret with plume", [("h_highlander_beret_blue_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_brown_2", "Beret with plume", [("h_highlander_beret_brown_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_green_2", "Beret with plume", [("h_highlander_beret_green_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_red_2", "Beret with plume", [("h_highlander_beret_red_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_white_2", "Beret with plume", [("h_highlander_beret_white_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["h_highlander_beret_yellow_2", "Beret with plume", [("h_highlander_beret_yellow_2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 50, weight(0.6)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],

# Hoods
["h_hood_black", "Hood", [("h_hood_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_blue", "Hood", [("h_hood_blue",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_blue_white", "Hood", [("h_hood_blue_white",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_blue_yellow", "Hood", [("h_hood_blue_yellow",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_brown", "Hood", [("h_hood_brown",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_brown_green", "Hood", [("h_hood_brown_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_green", "Hood", [("h_hood_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_red", "Hood", [("h_hood_red",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_red_blue", "Hood", [("h_hood_red_blue",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_red_green", "Hood", [("h_hood_red_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_red_white", "Hood", [("h_hood_red_white",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_red_yellow", "Hood", [("h_hood_red_yellow",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_white", "Hood", [("h_hood_white",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_white_black", "Hood", [("h_hood_white_black",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_white_brown", "Hood", [("h_hood_white_brown",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_white_green", "Hood", [("h_hood_white_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_white_yellow", "Hood", [("h_hood_white_yellow",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_yellow", "Hood", [("h_hood_yellow",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_yellow_brown", "Hood", [("h_hood_yellow_brown",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["h_hood_yellow_green", "Hood", [("h_hood_yellow_green",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# Padded Coifs
["h_padded_coif_black", "Padded Coif", [("h_padded_coif_black",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_blue", "Padded Coif", [("h_padded_coif_blue",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_brown", "Padded Coif", [("h_padded_coif_brown",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_green", "Padded Coif", [("h_padded_coif_green",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_red", "Padded Coif", [("h_padded_coif_red",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_white", "Padded Coif", [("h_padded_coif_white",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["h_padded_coif_yellow", "Padded Coif", [("h_padded_coif_yellow",0)], itp_merchandise| itp_type_head_armor   ,0, 22 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


############################################################################################################################################################################################################################################
###################################################################################################### HYW CLOTHES | DRESSES  ##############################################################################################################
############################################################################################################################################################################################################################################

# Peasants
["a_peasant_shirt_white", "Shirt", [("a_peasant_shirt_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["a_peasant_shirt_green", "Shirt", [("a_peasant_shirt_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["a_tavern_keeper_shirt", "Shirt", [("a_tavern_keeper_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["a_commoner_apron", "Leather Apron", [("a_commoner_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["a_merchant_outfit", "Merchant Outfit", [("a_merchant_outfit",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["a_peasant_tunic", "Peasant Tunic", [("a_peasant_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_farmer_tunic", "Tunic with vest", [("a_farmer_tunic",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["a_hunter_coat", "Pelt Coat", [("a_hunter_coat",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_peasant_coat", "Coat", [("a_peasant_coat",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

# Church
["a_priest_robe", "Priest Robe", [("a_priest_robe",0)],  itp_type_body_armor  |itp_covers_legs ,0, 69 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_black", "Monk Robe", [("a_monk_robe_black",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_brown", "Monk Robe", [("a_monk_robe_brown",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_monk_robe_white", "Monk Robe", [("a_monk_robe_white",0)],  itp_type_body_armor  |itp_covers_legs ,0, 66 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["a_surgeon_dress", "Surgeon Robe", [("a_surgeon_dress",0)],  itp_type_body_armor  |itp_covers_legs ,0, 69 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

# Nobles
["a_noble_shirt_black", "Shirt", [("a_noble_shirt_black",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_blue", "Shirt", [("a_noble_shirt_blue",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_brown", "Shirt", [("a_noble_shirt_brown",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_green", "Shirt", [("a_noble_shirt_green",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_red", "Shirt", [("a_noble_shirt_red",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["a_noble_shirt_white", "Shirt", [("a_noble_shirt_white",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

["a_nobleman_court_outfit_charles", "Noble Outfit", [("a_nobleman_court_outfit_charles",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["a_nobleman_court_outfit_english", "Noble Outfit", [("a_nobleman_court_outfit_english",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["a_nobleman_court_outfit_1", "Noble Outfit", [("a_nobleman_court_outfit_1",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["a_nobleman_court_outfit_2", "Noble Outfit", [("a_nobleman_court_outfit_2",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["a_nobleman_court_outfit_3", "Noble Outfit", [("a_nobleman_court_outfit_3",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["a_tabard", "Tabard", [("a_tabard",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["a_leather_jerkin", "Leather Jerkin", [("a_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

# Robes
["a_woman_common_dress_1", "Dress", [("a_woman_common_dress_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_woman_common_dress_2", "Dress", [("a_woman_common_dress_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_woman_common_dress_3", "Dress", [("a_woman_common_dress_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_woman_common_dress_4", "Dress", [("a_woman_common_dress_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_woman_common_dress_5", "Dress", [("a_woman_common_dress_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["a_woman_common_dress_6", "Dress", [("a_woman_common_dress_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

["a_woman_court_dress_1", "Noblewoman Dress", [("a_woman_court_dress_1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_2", "Noblewoman Dress", [("a_woman_court_dress_2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_3", "Noblewoman Dress", [("a_woman_court_dress_3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_4", "Noblewoman Dress", [("a_woman_court_dress_4",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_5", "Noblewoman Dress", [("a_woman_court_dress_5",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["a_woman_court_dress_6", "Noblewoman Dress", [("a_woman_court_dress_6",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW ARMORS ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Gambesons
["a_gambeson_black", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_black", 0, 0),])]],
["a_gambeson_blue", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_blue", 0, 0),])]],
["a_gambeson_brown", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_brown", 0, 0),])]],
["a_gambeson_green", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_green", 0, 0),])]],
["a_gambeson_red", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ,[(ti_on_init_item,[(cur_item_set_material, "@a_gambeson_red", 0, 0),])]],
["a_gambeson_white", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

["a_penthievre_armor", "Penthièvre Mail Hauberk", [("a_penthievre_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1420 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(7) ,imodbits_armor],

["a_hauberk_narf", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],
["a_hauberk_narf_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1420 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate", 0, 0),])]],
["a_hauberk_narf_full_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1480 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(24)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate_full", 0, 0),])]],

["a_hauberk_narf_jackchain", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1380 , weight(19)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],
["a_hauberk_narf_jackchain_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1480 , weight(19)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate", 0, 0),])]],
["a_hauberk_narf_jackchain_full_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1540 , weight(19)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(24)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_jackchain_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate_full", 0, 0),])]],

["a_hauberk_plate_narf", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1600 , weight(19)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],
["a_hauberk_plate_narf_jackchain_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1700 , weight(19)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate", 0, 0),])]],
["a_hauberk_plate_narf_jackchain_full_plate_hose", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1780 , weight(19)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(24)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk_plate_full", 0, 0),])]],

["a_brigandine_sl", "Brigandine", [("a_brigandine_bogmir",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor],

["a_churburg_narf_mail", "Churburg Plate", [("a_churburg_narf_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(20)|difficulty(10), imodbits_armor ,[(ti_on_init_item,[(cur_item_set_material, "@a_churburg_mail", 0, 0),])]],

["a_milanese_armour_narf", "Milanese Armour", [("a_milanese_armour_narf",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 5660, weight(28)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(22)|difficulty(10), imodbits_plate ],
["a_gothic_armour_narf", "Gothic Armour", [("a_gothic_armour_narf",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6230, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(0), imodbits_plate ],

["a_plate_english", "English Plate Armour", [("a_english_plate",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6540, weight(29)|abundance(100)|head_armor(8)|body_armor(64)|leg_armor(24)|difficulty(9), imodbits_armor ],
["a_plate_joan", "Joan's Plate Armour", [("a_plate_joan",0)], itp_type_body_armor|itp_covers_legs, 0, 9000, weight(29)|abundance(100)|head_armor(0)|body_armor(70)|leg_armor(28)|difficulty(12), imodbits_armor ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW HERALDIC ARMOR ########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["mail_long_surcoat_new_heraldic", "Heraldic Mail with Tabard", [("mail_long_surcoat_new_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3412 , weight(21)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_mail_long_surcoat_new", ":agent_no", ":troop_no")])]],

["brigandine_b_heraldic", "Heraldic Brigandine", [("brigandine_b_heraldic",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2230 , weight(20)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(16)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_brigandine_b_heraldic_new", ":agent_no", ":troop_no")])]],

["heraldic_tunic_new", "Heraldic Tunic", [("heraldic_tunic_new",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1940 , weight(20)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(10) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_short_tunic_new", ":agent_no", ":troop_no")])]],

["heraldic_mail_tabard", "Heraldic Tabard with Mail", [("tabard_b_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_mail_tabard", ":agent_no", ":troop_no")])]],

["heraldic_churburg_13_tabard", "Heraldic Churburg Armor", [("heraldic_churburg_13_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4250, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(20)|difficulty(8), imodbits_plate, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_tabard",":agent_no",":troop_no"),])] ],
["heraldic_churburg_13_brass_tabard", "Heraldic Brass Churburg Armor", [("heraldic_churburg_13_brass_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4430, weight(27)|abundance(100)|head_armor(0)|body_armor(58)|leg_armor(20)|difficulty(8), imodbits_plate, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_brass_tabard",":agent_no",":troop_no"),])] ],

["heraldic_early_transitional", "Heavy Mail and Plate", [("early_transitional_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2460 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8) ,imodbits_armor , [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_early_transitional_heraldic",":agent_no",":troop_no"),])] ],

["heraldic_plate", "Heraldic Plate Harness", [("heraldic_plate",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6550, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_plate  , [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_plate",":agent_no",":troop_no"),])] ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW BOOTS | SHOES | LEG ARMOR #############################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["b_wrapping_boots", "Wrapping Boots", [("b_wrapping_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["b_ankle_boots", "Ankle Boots", [("b_ankle_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["b_leather_boots", "Leather Boots", [("b_leather_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0, 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["b_mail_chausses", "Mail Chausses", [("b_mail_chausses",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["b_mail_boots", "Mail Boots", [("b_mail_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 880 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
["b_steel_greaves", "Steel Greaves", [("b_steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
["b_splinted_greaves_nospurs", "Splinted Greaves", [("b_splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
["b_splinted_greaves_spurs", "Splinted Greaves with Spurs", [("b_splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
["b_shynbaulds", "Shynbaulds", [("b_shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],
["b_steel_greaves_full", "Steel Greaves", [("b_steel_greaves_full",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW GLOVES | GAUNTLETS | POWER GAUNTLETS ##################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["g_leather_gauntlet","Leather Gloves", [("g_leather_gauntlet_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["g_mail_gauntlets","Mail Mittens", [("g_mail_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["g_demi_gauntlets","Demi Gauntlets", [("g_demi_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["g_finger_gauntlets","Finger Gauntlets", [("g_finger_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["g_wisby_gauntlets_black","Splinted Leather Gauntlets", [("g_wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["g_wisby_gauntlets_red","Splinted Leather Gauntlets", [("g_wisby_gauntlets_red_L",0)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["g_hourglass_gauntlets","Hourglass Gauntlets", [("g_hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 1240, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],
["g_hourglass_gauntlets_ornate","Ornate Hourglass Gauntlets", [("g_hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 1390, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],
["g_plate_mittens","Plate Mittens", [("g_plate_mittens_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1640, weight(1.5)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
 
 
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW SWORDS | DAGGERS | GREATSWORDS ########################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Daggers
["w_dagger_bollock", "Bollock Dagger", [("w_dagger_bollock",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
73 , weight(0.5)|difficulty(0)|spd_rtng(105) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(31 ,  pierce),imodbits_sword ],
["w_dagger_pikeman", "Pikeman Dagger", [("w_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
122 , weight(0.7)|difficulty(0)|spd_rtng(108) | weapon_length(41)|swing_damage(28 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["w_dagger_italian", "Italian Dagger", [("w_dagger_italian",0),("w_dagger_italian_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
136 , weight(0.6)|difficulty(0)|spd_rtng(105) | weapon_length(47)|swing_damage(25 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],

# Onehanded Swords with Scabbards
["w_onehanded_flachion_italian", "Italian Falchion", [("w_onehanded_flachion_italian",0),("w_onehanded_flachion_italian_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
325 , weight(1.2)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["w_onehanded_sword_a", "Sword", [("w_onehanded_sword_a",0),("w_onehanded_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
488 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_a_long", "Longsword", [("w_onehanded_sword_a_long",0),("w_onehanded_sword_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
572 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_c", "Sword", [("w_onehanded_sword_c",0),("w_onehanded_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
400 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_c_long", "Longsword", [("w_onehanded_sword_c_long",0),("w_onehanded_sword_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
572 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_c_small", "Shortsword", [("w_onehanded_sword_c_small",0),("w_onehanded_sword_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
533 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_d", "Sword", [("w_onehanded_sword_d",0),("w_onehanded_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
488 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_d_long", "Longsword", [("w_onehanded_sword_d_long",0),("w_onehanded_sword_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
572 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_flemish", "Flemish Sword", [("w_onehanded_sword_flemish",0),("w_onehanded_sword_flemish_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
582 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(28 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_italian", "Italian Sword", [("w_onehanded_sword_italian",0),("w_onehanded_sword_italian_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
506 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(98)|swing_damage(32 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_irish", "Irish Longsword", [("w_onehanded_sword_irish",0),("w_onehanded_sword_irish_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
670 , weight(1.6)|difficulty(0)|spd_rtng(97) | weapon_length(107)|swing_damage(28 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_longbowman", "Longbowman Sword", [("w_onehanded_sword_longbowman",0),("w_onehanded_sword_longbowman_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(83)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["w_onehanded_messer", "Messer", [("w_onehanded_messer",0),("w_onehanded_messer_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
415 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(36 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_milanese", "Milanese Shortsword", [("w_onehanded_sword_milanese",0),("w_onehanded_sword_milanese_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
402 , weight(1.3)|difficulty(0)|spd_rtng(103) | weapon_length(74)|swing_damage(28 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_scottish", "Scottish Shortsword", [("w_onehanded_sword_scottish",0),("w_onehanded_sword_scottish_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(81)|swing_damage(26 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],

["w_onehanded_sword_baron", "Baron Sword", [("w_onehanded_sword_baron",0),("w_onehanded_sword_baron_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
487 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_caithness", "Caithness Longsword", [("w_onehanded_sword_caithness",0),("w_onehanded_sword_caithness_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
582 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_castellan", "Castelan Sword", [("w_onehanded_sword_castellan",0),("w_onehanded_sword_castellan_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
508 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(27 , cut) | thrust_damage(34 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_constable", "Constable Sword", [("w_onehanded_sword_constable",0),("w_onehanded_sword_constable_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
514 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(28 , cut) | thrust_damage(34 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_hospitaller", "Hospitaller Sword", [("w_onehanded_sword_hospitaller",0),("w_onehanded_sword_hospitaller_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_knight", "Knight Sword", [("w_onehanded_sword_knight",0),("w_onehanded_sword_knight_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(29 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_laird", "Laird Sword", [("w_onehanded_sword_laird",0),("w_onehanded_sword_laird_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_poitiers", "Poitiers Sword", [("w_onehanded_sword_poitiers",0),("w_onehanded_sword_poitiers_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
497 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(92)|swing_damage(27 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_prince", "Prince Sword", [("w_onehanded_sword_prince",0),("w_onehanded_sword_prince_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
505 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(96)|swing_damage(31 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_ritter", "Ritter Longsword", [("w_onehanded_sword_ritter",0),("w_onehanded_sword_ritter_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
570 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(102)|swing_damage(31 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_sovereign", "Sovereign Shortsword", [("w_onehanded_sword_sovereign",0),("w_onehanded_sword_sovereign_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(83)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_squire", "Squire Sword", [("w_onehanded_sword_squire",0),("w_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
["w_onehanded_sword_templar", "Templar Longsword", [("w_onehanded_sword_templar",0),("w_onehanded_sword_templar_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(102)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
## Alternative texture versions
["w_onehanded_sword_baron_2", "Baron Sword", [("w_onehanded_sword_baron",0),("w_onehanded_sword_baron_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
487 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_caithness_2", "Caithness Longsword", [("w_onehanded_sword_caithness",0),("w_onehanded_sword_caithness_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
582 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(103)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_castellan_2", "Castelan Sword", [("w_onehanded_sword_castellan",0),("w_onehanded_sword_castellan_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
508 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(27 , cut) | thrust_damage(34 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_constable_2", "Constable Sword", [("w_onehanded_sword_constable",0),("w_onehanded_sword_constable_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
514 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(28 , cut) | thrust_damage(34 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_hospitaller_2", "Hospitaller Sword", [("w_onehanded_sword_hospitaller",0),("w_onehanded_sword_hospitaller_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(99)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_knight_2", "Knight Sword", [("w_onehanded_sword_knight",0),("w_onehanded_sword_knight_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(29 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_laird_2", "Laird Sword", [("w_onehanded_sword_laird",0),("w_onehanded_sword_laird_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
491 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(93)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_poitiers_2", "Poitiers Sword", [("w_onehanded_sword_poitiers",0),("w_onehanded_sword_poitiers_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
497 , weight(1.4)|difficulty(0)|spd_rtng(101) | weapon_length(92)|swing_damage(27 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_prince_2", "Prince Sword", [("w_onehanded_sword_prince",0),("w_onehanded_sword_prince_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
505 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(96)|swing_damage(31 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_ritter_2", "Ritter Longsword", [("w_onehanded_sword_ritter",0),("w_onehanded_sword_ritter_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
570 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(102)|swing_damage(31 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_sovereign_2", "Sovereign Shortsword", [("w_onehanded_sword_sovereign",0),("w_onehanded_sword_sovereign_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
406 , weight(1.3)|difficulty(0)|spd_rtng(102) | weapon_length(83)|swing_damage(32 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_squire_2", "Squire Sword", [("w_onehanded_sword_squire",0),("w_onehanded_sword_squire_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
499 , weight(1.4)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_onehanded_sword_templar_2", "Templar Longsword", [("w_onehanded_sword_templar",0),("w_onehanded_sword_templar_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
577 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(102)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],

# Bastard Swords with Scabbards
["w_bastard_sword_a", "Bastard Sword", [("w_bastard_sword_a",0),("w_bastard_sword_a_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
294, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(99)|swing_damage(35,cut)|thrust_damage(26,pierce), imodbits_sword_high ],
["w_bastard_sword_b", "Bastard Sword", [("w_bastard_sword_b",0),("w_bastard_sword_b_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
526, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(104)|swing_damage(37,cut)|thrust_damage(27,pierce), imodbits_sword_high ],
["w_bastard_sword_c", "Bastard Sword", [("w_bastard_sword_c",0),("w_bastard_sword_c_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
548, weight(2.5)|difficulty(9)|spd_rtng(97)|weapon_length(104)|swing_damage(38,cut)|thrust_damage(27,pierce), imodbits_sword_high ],
["w_bastard_sword_d", "Bastard Sword", [("w_bastard_sword_d",0),("w_bastard_sword_d_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
698, weight(2.25)|difficulty(9)|spd_rtng(98)|weapon_length(99)|swing_damage(38,cut)|thrust_damage(31,pierce), imodbits_sword_high ],

["w_bastard_sword_english", "English Bastard Sword", [("w_bastard_sword_english",0),("w_bastard_sword_english_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
676, weight(2)|difficulty(9)|spd_rtng(99)|weapon_length(101)|swing_damage(37,cut)|thrust_damage(33,pierce), imodbits_sword_high ],
["w_bastard_sword_german", "German Bastard Sword", [("w_bastard_sword_german",0),("w_bastard_sword_german_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
724, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(106)|swing_damage(38,cut)|thrust_damage(33,pierce), imodbits_sword_high ],
["w_bastard_sword_italian", "Italian Bastard Sword", [("w_bastard_sword_italian",0),("w_bastard_sword_italian_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
638, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(107)|swing_damage(36,cut)|thrust_damage(35,pierce), imodbits_sword_high ],

["w_bastard_sword_agincourt", "Agincourt Bastard Sword", [("w_bastard_sword_agincourt",0),("w_bastard_sword_agincourt_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
892, weight(2.75)|difficulty(9)|spd_rtng(96)|weapon_length(111)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_sword_high ],
["w_bastard_sword_baron", "Baron Bastard Sword", [("w_bastard_sword_baron",0),("w_bastard_sword_baron_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
831, weight(2.5)|difficulty(9)|spd_rtng(96)|weapon_length(110)|swing_damage(41,cut)|thrust_damage(30,pierce), imodbits_sword_high ],
["w_bastard_sword_count", "Count Bastard Sword", [("w_bastard_sword_count",0),("w_bastard_sword_count_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
784, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(40,cut)|thrust_damage(29,pierce), imodbits_sword_high ],
["w_bastard_sword_crecy", "Crecy Bastard Sword", [("w_bastard_sword_crecy",0),("w_bastard_sword_crecy_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
938, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(107)|swing_damage(40,cut)|thrust_damage(34,pierce), imodbits_sword_high ],
["w_bastard_sword_duke", "Duke Bastard Sword", [("w_bastard_sword_duke",0),("w_bastard_sword_duke_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
822, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(106)|swing_damage(42,cut)|thrust_damage(26,pierce), imodbits_sword_high ],
["w_bastard_sword_landgraf", "Landgraf Bastard Sword", [("w_bastard_sword_landgraf",0),("w_bastard_sword_landgraf_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
798, weight(2.2)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(37,cut)|thrust_damage(34,pierce), imodbits_sword_high ],
["w_bastard_sword_mercenary", "Mercenary Bastard Sword", [("w_bastard_sword_mercenary",0),("w_bastard_sword_mercenary_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
760, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(101)|swing_damage(36,cut)|thrust_damage(33,pierce), imodbits_sword_high ],
["w_bastard_sword_regent", "Regent Bastard Sword", [("w_bastard_sword_regent",0),("w_bastard_sword_regent_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
885, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(39,cut)|thrust_damage(34,pierce), imodbits_sword_high ],
["w_bastard_sword_sempach", "Sempach Bastard Sword", [("w_bastard_sword_sempach",0),("w_bastard_sword_sempach_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
873, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(38,cut)|thrust_damage(35,pierce), imodbits_sword_high ],
## Alternative texture versions
["w_bastard_sword_agincourt_2", "Agincourt Bastard Sword", [("w_bastard_sword_agincourt",0),("w_bastard_sword_agincourt_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
892, weight(2.75)|difficulty(9)|spd_rtng(96)|weapon_length(111)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_baron_2", "Baron Bastard Sword", [("w_bastard_sword_baron",0),("w_bastard_sword_baron_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
831, weight(2.5)|difficulty(9)|spd_rtng(96)|weapon_length(110)|swing_damage(41,cut)|thrust_damage(30,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_count_2", "Count Bastard Sword", [("w_bastard_sword_count",0),("w_bastard_sword_count_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
784, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(40,cut)|thrust_damage(29,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_crecy_2", "Crecy Bastard Sword", [("w_bastard_sword_crecy",0),("w_bastard_sword_crecy_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
938, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(107)|swing_damage(40,cut)|thrust_damage(34,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_duke_2", "Duke Bastard Sword", [("w_bastard_sword_duke",0),("w_bastard_sword_duke_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
822, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(106)|swing_damage(42,cut)|thrust_damage(26,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_landgraf_2", "Landgraf Bastard Sword", [("w_bastard_sword_landgraf",0),("w_bastard_sword_landgraf_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
798, weight(2.2)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(37,cut)|thrust_damage(34,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_mercenary_2", "Mercenary Bastard Sword", [("w_bastard_sword_mercenary",0),("w_bastard_sword_mercenary_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
760, weight(2)|difficulty(9)|spd_rtng(98)|weapon_length(101)|swing_damage(36,cut)|thrust_damage(33,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_regent_2", "Regent Bastard Sword", [("w_bastard_sword_regent",0),("w_bastard_sword_regent_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
885, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(39,cut)|thrust_damage(34,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_bastard_sword_sempach_2", "Sempach Bastard Sword", [("w_bastard_sword_sempach",0),("w_bastard_sword_sempach_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
873, weight(2.25)|difficulty(9)|spd_rtng(96)|weapon_length(109)|swing_damage(38,cut)|thrust_damage(35,pierce), imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],

# Twohanded Swords
["w_twohanded_messer", "Grosse Messer", [("w_twohanded_messer",0),("w_twohanded_messer_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 
920 , weight(2.2)|difficulty(10)|spd_rtng(99) | weapon_length(93)|swing_damage(44 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["w_twohanded_sword_claymore", "Claymore", [("w_twohanded_sword_claymore",0),("w_twohanded_sword_claymore_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 
1290 , weight(3.5)|difficulty(12)|spd_rtng(94) | weapon_length(115)|swing_damage(43 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["w_twohanded_sword_danish", "Danish Greatsword", [("w_twohanded_sword_danish",0),("w_twohanded_sword_danish_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 
1344 , weight(3.2)|difficulty(12)|spd_rtng(94) | weapon_length(114)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high ],
["w_twohanded_sword_steward", "Steward Greatsword", [("w_twohanded_sword_steward",0),("w_twohanded_sword_steward_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1036 , weight(2.25)|difficulty(11)|spd_rtng(96) | weapon_length(99)|swing_damage(41 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
["w_twohanded_talhoffer", "Talhoffer Greatsword", [("w_twohanded_talhoffer",0),("w_twohanded_talhoffer_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
998 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(115)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ],
## Alternative texture versions
["w_twohanded_sword_steward_2", "Steward Greatsword", [("w_twohanded_sword_steward",0),("w_twohanded_sword_steward_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
1036 , weight(2.25)|difficulty(11)|spd_rtng(96) | weapon_length(99)|swing_damage(41 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
["w_twohanded_talhoffer_2", "Talhoffer Greatsword", [("w_twohanded_talhoffer",0),("w_twohanded_talhoffer_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,  
998 , weight(2.5)|difficulty(11)|spd_rtng(95) | weapon_length(115)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_sword_high ,[(ti_on_init_item,[(cur_item_set_material, "@w_swords_2", 0, 0),])]],
##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW AXES | BARDICHES ######################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_archer_hatchet", "Archer Hatchet", [("w_archer_hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
71 , weight(1.25)|difficulty(7)|spd_rtng(98) | weapon_length(46)|swing_damage(21 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_onehanded_war_axe", "Onehanded War Axe", [("w_onehanded_war_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
221 , weight(1.5)|difficulty(9)|spd_rtng(97) | weapon_length(70)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_2", "Onehanded War Axe", [("w_onehanded_war_axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
87 , weight(1.5)|difficulty(9)|spd_rtng(96) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_3", "Onehanded War Axe", [("w_onehanded_war_axe_3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
142 , weight(2)|difficulty(9)|spd_rtng(95) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_onehanded_war_axe_4", "Onehanded War Axe", [("w_onehanded_war_axe_4",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
190 , weight(1.75)|difficulty(9)|spd_rtng(96) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_horseman_axe_1", "Horseman Axe", [("w_horseman_axe_1",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
202 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(77)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_horseman_axe_2", "Horseman Axe", [("w_horseman_axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
176 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_horseman_axe_3", "Horseman Axe", [("w_horseman_axe_3",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
234 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(79)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_german_knight_axe", "German Knight Axe", [("w_german_knight_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
354 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(94)|swing_damage(35 , cut) | thrust_damage(19 ,  pierce),imodbits_axe ],
["w_german_knight_axe_2", "German Knight Axe", [("w_german_knight_axe_2",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
246 , weight(2)|difficulty(9)|spd_rtng(96) | weapon_length(79)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_knight_battle_axe", "Knight Battle Axe", [("w_knight_battle_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_longsword|itcf_carry_axe_left_hip, 
371 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(97)|swing_damage(36 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],

["w_twohanded_war_axe", "Twohanded War Axe", [("w_twohanded_war_axe",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
236, weight(3.5)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(41,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_2", "Twohanded War Axe", [("w_twohanded_war_axe_2",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 
287, weight(4)|difficulty(10)|spd_rtng(94)|weapon_length(98)|swing_damage(43,cut)|thrust_damage(0,blunt), imodbits_axe ],
["w_twohanded_war_axe_3", "Twohanded War Axe", [("w_twohanded_war_axe_3",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back,
321, weight(4)|difficulty(10)|spd_rtng(95)|weapon_length(99)|swing_damage(44,cut)|thrust_damage(0,blunt), imodbits_axe ],

["w_gallowglass_axe",      "Gallowglass Axe", [("w_gallowglass_axe",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
304 , weight(4)|difficulty(10)|spd_rtng(90) | weapon_length(156)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["w_bardiche_1",  "Bardiche", [("w_bardiche_1",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
539 , weight(5.75)|difficulty(10)|spd_rtng(86) | weapon_length(140)|swing_damage(51 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_2",  "Bardiche", [("w_bardiche_2",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
628 , weight(6)|difficulty(10)|spd_rtng(85) | weapon_length(155)|swing_damage(52 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_3",  "Bardiche", [("w_bardiche_3",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
334 , weight(5)|difficulty(10)|spd_rtng(89) | weapon_length(107)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_4",  "Bardiche", [("w_bardiche_4",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
306 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(103)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_5",  "Bardiche", [("w_bardiche_5",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
368 , weight(5.25)|difficulty(10)|spd_rtng(90) | weapon_length(106)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_6",  "Bardiche", [("w_bardiche_6",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
399 , weight(5.25)|difficulty(10)|spd_rtng(89) | weapon_length(110)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_7",  "Bardiche", [("w_bardiche_7",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
291 , weight(5)|difficulty(10)|spd_rtng(91) | weapon_length(106)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_8",  "Bardiche", [("w_bardiche_8",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
498 , weight(5.5)|difficulty(10)|spd_rtng(88) | weapon_length(105)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["w_bardiche_9",  "Bardiche", [("w_bardiche_9",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 
464 , weight(5.5)|difficulty(10)|spd_rtng(89) | weapon_length(101)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW MACES | CLUBS | HAMMERS ###############################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_wooden_stick",         "Wooden Stick", [("w_wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["w_archers_maul",         "Archer Maul", [("w_archers_maul",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
77 , weight(2)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],

["w_warhammer_1",         "Warhammer", [("w_warhammer_1",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
293 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_warhammer_2",         "Warhammer", [("w_warhammer_2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_knight_warhammer_1",         "Spiked Knight Warhammer", [("w_knight_warhammer_1",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_longsword,
372 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(76)|swing_damage(33 , blunt) | thrust_damage(19,  pierce),imodbits_mace ],
["w_knight_warhammer_2",         "Knight Warhammer", [("w_knight_warhammer_2",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
334 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_great_hammer", "Greathammer", [("w_great_hammer",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
422 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

["w_knight_winged_mace", "Knight Winged Mace", [("w_knight_winged_mace",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
336, weight(4)|difficulty(0)|spd_rtng(96)|weapon_length(69)|swing_damage(28,blunt)|thrust_damage(0,pierce), imodbits_mace ],
["w_mace_english", "English Mace", [("w_mace_english",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 
262, weight(3.25)|difficulty(0)|spd_rtng(97)|weapon_length(72)|swing_damage(26,blunt)|thrust_damage(0,pierce), imodbits_mace ],

["w_spiked_club",         "Spiked Club", [("w_spiked_club",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3.25)|difficulty(0)|spd_rtng(96) | weapon_length(75)|swing_damage(23 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_knobbed",         "Knobbed_Mace", [("w_mace_knobbed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_spiked",         "Spiked Mace", [("w_mace_spiked",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(71)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["w_mace_winged",         "Winged_Mace", [("w_mace_winged",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
212 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(71)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],

##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW POLEARMS ##############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["w_awlpike_1", "Short Pike", [("w_awlpike_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
278 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(185)|swing_damage(27 , blunt) | thrust_damage(34 ,  pierce),imodbits_polearm ],
["w_awlpike_2", "Short Pike", [("w_awlpike_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
283 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(188)|swing_damage(29 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["w_awlpike_3", "Short Pike", [("w_awlpike_3",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
280 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(188)|swing_damage(28 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["w_awlpike_4", "Short Pike", [("w_awlpike_4",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
275 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(187)|swing_damage(22 , blunt) | thrust_damage(36 ,  pierce),imodbits_polearm ],
["w_awlpike_5", "Short Pike", [("w_awlpike_5",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
273 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(181)|swing_damage(24 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["w_awlpike_6", "Short Pike", [("w_awlpike_6",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
275 , weight(2.0)|difficulty(0)|spd_rtng(85) | weapon_length(193)|swing_damage(19 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

["w_pike_1", "Pike", [("w_pike_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
497 , weight(3.5)|difficulty(0)|spd_rtng(78) | weapon_length(450)|swing_damage(18 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["w_pike_swiss_1", "Swiss Pike", [("w_pike_swiss_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
344 , weight(3.0)|difficulty(0)|spd_rtng(82) | weapon_length(255)|swing_damage(27 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["w_pike_swiss_2", "Swiss Pike", [("w_pike_swiss_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_has_upper_stab, itc_pike_upstab, 
336 , weight(3.0)|difficulty(0)|spd_rtng(82) | weapon_length(246)|swing_damage(24 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["w_bill_1", "Bill", [("w_bill_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
424, weight(4)|difficulty(9)|spd_rtng(85)|weapon_length(191)|swing_damage(38,cut)|thrust_damage(29,pierce), imodbits_polearm ],
["w_bill_2", "Bill", [("w_bill_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
455, weight(4.1)|difficulty(9)|spd_rtng(85)|weapon_length(207)|swing_damage(44,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_bill_3", "Bill", [("w_bill_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
480, weight(4.3)|difficulty(9)|spd_rtng(85)|weapon_length(233)|swing_damage(46,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_bill_4", "Bill", [("w_bill_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
505, weight(4.5)|difficulty(9)|spd_rtng(85)|weapon_length(246)|swing_damage(45,cut)|thrust_damage(37,pierce), imodbits_polearm ],

["w_bec_de_corbin", "Bec de Corbin", [("w_bec_de_corbin",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
375, weight(3.9)|difficulty(9)|spd_rtng(84)|weapon_length(154)|swing_damage(33,blunt)|thrust_damage(29,pierce), imodbits_polearm ],

["w_fauchard_1", "Fauchard", [("w_fauchard_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(151)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_2", "Fauchard", [("w_fauchard_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(130)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_3", "Fauchard", [("w_fauchard_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(196)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_4", "Fauchard", [("w_fauchard_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(183)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_5", "Fauchard", [("w_fauchard_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(169)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],

["w_fauchard_fork_1", "Forked Fauchard", [("w_fauchard_fork_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(167)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_fork_2", "Forked Fauchard", [("w_fauchard_fork_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(173)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_fork_3", "Forked Fauchard", [("w_fauchard_fork_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(177)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_fauchard_fork_4", "Forked Fauchard", [("w_fauchard_fork_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(147)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],

["w_fork_1", "Pitch Fork", [("w_fork_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 
19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(135)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["w_fork_2", "Pitch Fork", [("w_fork_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 
19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(126)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["w_fork_3", "Reinforced Fork", [("w_fork_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 
19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(168)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],

["w_glaive_1", "Glaive", [("w_glaive_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(174)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_2", "Glaive", [("w_glaive_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(175)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_3", "Glaive", [("w_glaive_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(255)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_4", "Glaive", [("w_glaive_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(179)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_5", "Glaive", [("w_glaive_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(185)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_6", "Glaive", [("w_glaive_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(160)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_7", "Glaive", [("w_glaive_7",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(164)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_8", "Glaive", [("w_glaive_8",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(208)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_glaive_burgundy", "Burgundian Glaive", [("w_glaive_burgundy",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(160)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],

["w_goedendag",  "Goedendag", [("w_goedendag",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 200 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],
["w_goedendag_burgundy",  "Burgundian Goedendag", [("w_goedendag_burgundy",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 200 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(125)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["w_guisarme_burgundy", "Burgundian Guisarme", [("w_guisarme_burgundy",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(184)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["w_halberd_1", "Halberd", [("w_halberd_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
406, weight(3.5)|difficulty(9)|spd_rtng(86)|weapon_length(170)|swing_damage(39,cut)|thrust_damage(31,pierce), imodbits_polearm ],
["w_halberd_2", "Halberd", [("w_halberd_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
428, weight(3.5)|difficulty(9)|spd_rtng(82)|weapon_length(193)|swing_damage(37,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["w_halberd_3", "Halberd", [("w_halberd_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
423, weight(3.6)|difficulty(9)|spd_rtng(84)|weapon_length(180)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_halberd_4", "Halberd", [("w_halberd_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
412, weight(3.5)|difficulty(9)|spd_rtng(84)|weapon_length(180)|swing_damage(33,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_halberd_5", "Halberd", [("w_halberd_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
396, weight(3.6)|difficulty(9)|spd_rtng(82)|weapon_length(190)|swing_damage(39,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_halberd_6", "Halberd", [("w_halberd_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
415, weight(3.8)|difficulty(9)|spd_rtng(85)|weapon_length(173)|swing_damage(41,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_halberd_7", "Halberd", [("w_halberd_7",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
428, weight(3.7)|difficulty(9)|spd_rtng(82)|weapon_length(188)|swing_damage(40,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_halberd_8", "Halberd", [("w_halberd_8",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
417, weight(3.7)|difficulty(9)|spd_rtng(85)|weapon_length(174)|swing_damage(42,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["w_halberd_9", "Halberd", [("w_halberd_9",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
435, weight(3.6)|difficulty(9)|spd_rtng(82)|weapon_length(190)|swing_damage(43,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_10", "Halberd", [("w_halberd_10",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
436, weight(3.6)|difficulty(9)|spd_rtng(82)|weapon_length(193)|swing_damage(41,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_11", "Halberd", [("w_halberd_11",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
458, weight(3.7)|difficulty(9)|spd_rtng(81)|weapon_length(209)|swing_damage(44,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_halberd_12", "Halberd", [("w_halberd_12",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
406, weight(3.6)|difficulty(9)|spd_rtng(84)|weapon_length(172)|swing_damage(43,cut)|thrust_damage(27,pierce), imodbits_polearm ],
["w_halberd_13", "Halberd", [("w_halberd_13",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
441, weight(3.9)|difficulty(9)|spd_rtng(82)|weapon_length(192)|swing_damage(45,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["w_halberd_flemish", "Flemish Halberd", [("w_halberd_flemish",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 
419, weight(4)|difficulty(9)|spd_rtng(82)|weapon_length(175)|swing_damage(46,cut)|thrust_damage(33,pierce), imodbits_polearm ],

["w_lochaber_axe_1", "Lochaber Axe", [("w_lochaber_axe_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
376, weight(4)|difficulty(9)|spd_rtng(83)|weapon_length(148)|swing_damage(45,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_lochaber_axe_2", "Lochaber Axe", [("w_lochaber_axe_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
383, weight(4.5)|difficulty(9)|spd_rtng(83)|weapon_length(150)|swing_damage(48,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_lochaber_axe_3", "Lochaber Axe", [("w_lochaber_axe_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
376, weight(4.3)|difficulty(9)|spd_rtng(84)|weapon_length(146)|swing_damage(46,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_lochaber_axe_4", "Lochaber Axe", [("w_lochaber_axe_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
359, weight(4.4)|difficulty(9)|spd_rtng(87)|weapon_length(129)|swing_damage(47,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_lochaber_axe_5", "Lochaber Axe", [("w_lochaber_axe_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 
355, weight(4.2)|difficulty(9)|spd_rtng(88)|weapon_length(124)|swing_damage(48,cut)|thrust_damage(0,pierce), imodbits_polearm ],

["w_native_spear_a", "Short Pike", [("w_native_spear_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(246)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["w_native_spear_c", "Glaive", [("w_native_spear_c",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(155)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_native_spear_d", "Spear", [("w_native_spear_d",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(179)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_native_spear_e", "Glaive", [("w_native_spear_e",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(228)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],
["w_native_spear_g", "Spear", [("w_native_spear_g",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(120)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_native_spear_h", "Spear", [("w_native_spear_h",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(134)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_native_spear_i", "Spear", [("w_native_spear_i",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],

["w_partisan_1", "Partisan", [("w_partisan_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(130)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["w_partisan_2", "Partisan", [("w_partisan_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(137)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["w_partisan_3", "Partisan", [("w_partisan_3",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(146)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["w_partisan_4", "Partisan", [("w_partisan_4",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(126)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["w_poleaxe_1", "Poleaxe", [("w_poleaxe_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(179)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_poleaxe_2", "Poleaxe", [("w_poleaxe_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(158)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_poleaxe_3", "Poleaxe", [("w_poleaxe_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(188)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["w_poleaxe_english", "English Poleaxe", [("w_poleaxe_english",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(144)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["w_polehammer_1", "Polehammer", [("w_polehammer_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(154)|swing_damage(39,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_polehammer_2", "Polehammer", [("w_polehammer_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(177)|swing_damage(39,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_polehammer_lucern", "Lucern Polehammer", [("w_polehammer_lucern",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(150)|swing_damage(39,blunt)|thrust_damage(35,pierce), imodbits_polearm ],
["w_polehammer_milan", "Milanese Polehammer", [("w_polehammer_milan",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(163)|swing_damage(39,blunt)|thrust_damage(35,pierce), imodbits_polearm ],

["w_ranseur_1", "Ranseur", [("w_ranseur_1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(124)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["w_ranseur_2", "Ranseur", [("w_ranseur_2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_pike_upstab, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(167)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["w_scythe_1", "Scythe", [("w_scythe_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_voulge|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(133)|swing_damage(39,cut)|thrust_damage(0,pierce), imodbits_polearm ],

["w_spear_1", "Spear", [("w_spear_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(107)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_2", "Spear", [("w_spear_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(128)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_3", "Spear", [("w_spear_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(132)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_4", "Spear", [("w_spear_4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(142)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_5", "Spear", [("w_spear_5",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(144)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_6", "Spear", [("w_spear_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(149)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_7", "Spear", [("w_spear_7",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(204)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["w_spear_8", "Spear", [("w_spear_8",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_spear_upstab|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(95)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],

["w_spetum_1", "Spetum", [("w_spetum_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(154)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["w_spetum_2", "Spetum", [("w_spetum_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(159)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["w_spetum_3", "Spetum", [("w_spetum_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(156)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["w_spetum_4", "Spetum", [("w_spetum_4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(127)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],

["w_voulge_1", "Voulge", [("w_voulge_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(152)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_2", "Voulge", [("w_voulge_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(140)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_3", "Voulge", [("w_voulge_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(162)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_4", "Voulge", [("w_voulge_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(170)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_5", "Voulge", [("w_voulge_5",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(149)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_6", "Voulge", [("w_voulge_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(100)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_7", "Voulge", [("w_voulge_7",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(177)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_8", "Voulge", [("w_voulge_8",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(210)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_french", "French Voulge", [("w_voulge_french",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(174)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_short", "Shortened Voulge", [("w_voulge_short",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(99)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_swiss_1", "Swiss Voulge", [("w_voulge_swiss_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(213)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_swiss_2", "Swiss Voulge", [("w_voulge_swiss_2",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(240)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_swiss_3", "Swiss Voulge", [("w_voulge_swiss_3",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(203)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],
["w_voulge_swiss_4", "Swiss Voulge", [("w_voulge_swiss_4",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_poleaxe|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(195)|swing_damage(39,cut)|thrust_damage(18,pierce), imodbits_polearm ],

["w_warbrand",         "Warbrand", [("w_warbrand",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(115)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW LANCES ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################


["w_light_lance",         "Light Lance", [("w_light_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_pike_upstab, 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(355)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["w_native_spear_b",         "Light Lance", [("w_native_spear_b",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_pike_upstab, 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["w_native_spear_f",         "Light Lance", [("w_native_spear_f",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_pike_upstab, 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],

["w_lance_1", "Lance", [("w_lance_1",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(267)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_2", "Lance", [("w_lance_2",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(226)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_3", "Lance", [("w_lance_3",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(253)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_4", "Lance", [("w_lance_4",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(253)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_5", "Lance", [("w_lance_5",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_6", "Lance", [("w_lance_6",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(241)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],

["w_lance_colored_english_1", "English Lance", [("w_lance_colored_english_1",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_colored_english_2", "English Lance", [("w_lance_colored_english_2",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_colored_english_3", "English Lance", [("w_lance_colored_english_3",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(267)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],

["w_lance_colored_french_1", "French Lance", [("w_lance_colored_french_1",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_colored_french_2", "French Lance", [("w_lance_colored_french_2",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],
["w_lance_colored_french_3", "French Lance", [("w_lance_colored_french_3",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(252)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW RANGED ################################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["arrows", "Arrows", [("arrow",0),("arrow_flying",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
72, weight(3)|abundance(100)|weapon_length(95)|thrust_damage(20,cut)|max_ammo(30), imodbits_missile ],
["arrows_b", "English Arrows", [("arrow_b",0),("arrow_b_flying",ixmesh_flying_ammo),("quiver_b",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
144, weight(3)|abundance(80)|weapon_length(95)|thrust_damage(18,pierce)|max_ammo(24), imodbits_missile ],
["barbed_arrows", "Barbed Arrows", [("barbed_arrow",0),("barbed_arrow_flying",ixmesh_flying_ammo),("quiver_d",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
98, weight(3)|abundance(90)|weapon_length(95)|thrust_damage(24,cut)|max_ammo(24), imodbits_missile ],
["piercing_arrows", "Bodkin Arrows", [("piercing_arrow",0),("piercing_arrow_flying",ixmesh_flying_ammo),("quiver_c",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 
104, weight(3)|abundance(90)|weapon_length(95)|thrust_damage(16,pierce)|max_ammo(24), imodbits_missile ],

["bolts", "Bolts", [("bolt",0),("bolt_flying",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(5,pierce)|max_ammo(29), imodbits_missile ],
["steel_bolts", "Steel Bolts", [("bolt",0),("bolt_flying",ixmesh_flying_ammo),("bolt_bag_c",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210, weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(6,pierce)|max_ammo(29), imodbits_missile ],
["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],

["w_short_bow_ash", "Ash Short Bow", [("w_short_bow_ash",0),("w_short_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 42, weight(0.5)|difficulty(0)|spd_rtng(95)|shoot_speed(40)|thrust_damage(9,pierce), imodbits_bow ],
["w_short_bow_elm", "Elm Short Bow", [("w_short_bow_elm",0),("w_short_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 50, weight(0.6)|difficulty(0)|spd_rtng(94)|shoot_speed(42)|thrust_damage(10,pierce), imodbits_bow ],
["w_short_bow_oak", "Oak Short Bow", [("w_short_bow_oak",0),("w_short_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 58, weight(0.7)|difficulty(1)|spd_rtng(93)|shoot_speed(44)|thrust_damage(11,pierce), imodbits_bow ],
["w_short_bow_yew", "Yew Short Bow", [("w_short_bow_yew",0),("w_short_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 66, weight(0.7)|difficulty(1)|spd_rtng(92)|shoot_speed(45)|thrust_damage(12,pierce), imodbits_bow ],

 ["w_hunting_bow_ash", "Ash Hunting Bow", [("w_hunting_bow_ash",0),("w_hunting_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 90, weight(0.8)|difficulty(1)|spd_rtng(90)|shoot_speed(45)|thrust_damage(15,pierce), imodbits_bow ],
["w_hunting_bow_elm", "Elm Hunting Bow", [("w_hunting_bow_elm",0),("w_hunting_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 102, weight(0.9)|difficulty(1)|spd_rtng(89)|shoot_speed(48)|thrust_damage(16,pierce), imodbits_bow ],
["w_hunting_bow_oak", "Oak Hunting Bow", [("w_hunting_bow_oak",0),("w_hunting_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 124, weight(0.9)|difficulty(2)|spd_rtng(88)|shoot_speed(51)|thrust_damage(17,pierce), imodbits_bow ],
["w_hunting_bow_yew", "Yew Hunting Bow", [("w_hunting_bow_yew",0),("w_hunting_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 136, weight(1)|difficulty(2)|spd_rtng(87)|shoot_speed(54)|thrust_damage(18,pierce), imodbits_bow ],

["w_war_bow_ash", "Ash War Bow", [("w_war_bow_ash",0),("w_war_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 140, weight(1.2)|difficulty(3)|spd_rtng(85)|shoot_speed(71)|thrust_damage(20,pierce), imodbits_bow ],
["w_war_bow_elm", "Elm War Bow", [("w_war_bow_elm",0),("w_war_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 154, weight(1.3)|difficulty(3)|spd_rtng(84)|shoot_speed(76)|thrust_damage(21,pierce), imodbits_bow ],
["w_war_bow_oak", "Oak War Bow", [("w_war_bow_oak",0),("w_war_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 168, weight(1.3)|difficulty(3)|spd_rtng(83)|shoot_speed(82)|thrust_damage(22,pierce), imodbits_bow ],
["w_war_bow_yew", "Yew War Bow", [("w_war_bow_yew",0),("w_war_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 184, weight(1.4)|difficulty(3)|spd_rtng(82)|shoot_speed(89)|thrust_damage(23,pierce), imodbits_bow ],

 ["w_long_bow_ash", "Ash Long Bow", [("w_long_bow_ash",0),("w_long_bow_ash_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 220, weight(1.4)|difficulty(4)|spd_rtng(80)|shoot_speed(107)|thrust_damage(25,pierce), imodbits_bow ],
["w_long_bow_elm", "Elm Long Bow", [("w_long_bow_elm",0),("w_long_bow_elm_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 235, weight(1.5)|difficulty(4)|spd_rtng(79)|shoot_speed(115)|thrust_damage(26,pierce), imodbits_bow ],
["w_long_bow_oak", "Oak Long Bow", [("w_long_bow_oak",0),("w_long_bow_oak_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 250, weight(1.5)|difficulty(5)|spd_rtng(78)|shoot_speed(128)|thrust_damage(27,pierce), imodbits_bow ],
["w_long_bow_yew", "Yew Long Bow", [("w_long_bow_yew",0),("w_long_bow_yew_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back,
 265, weight(1.6)|difficulty(5)|spd_rtng(77)|shoot_speed(134)|thrust_damage(28,pierce), imodbits_bow ],

["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(3.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],

["hunting_crossbow", "Hunting Crossbow", [("crossbow",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
88, weight(2.25)|difficulty(0)|spd_rtng(80)|shoot_speed(81)|thrust_damage(48,pierce)|max_ammo(1), imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
132, weight(2.5)|difficulty(8)|spd_rtng(76)|shoot_speed(92)|thrust_damage(52,pierce)|max_ammo(1), imodbits_crossbow ],
["crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
218, weight(3)|difficulty(9)|spd_rtng(72)|shoot_speed(124)|thrust_damage(56,pierce)|max_ammo(1), imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("heavy_crossbow",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349, weight(3.5)|difficulty(10)|spd_rtng(68)|shoot_speed(139)|thrust_damage(60,pierce)|max_ammo(1), imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683, weight(3.75)|difficulty(11)|spd_rtng(62)|shoot_speed(142)|thrust_damage(66,pierce)|max_ammo(1), imodbits_crossbow ],

["w_handgonne_1", "Handgonne", [("w_handgonne_1",0)], itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
1850, weight(4.5)|abundance(90)|difficulty(0)|spd_rtng(58)|shoot_speed(160)|thrust_damage(100,pierce)|max_ammo(1)|accuracy(95), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot_2"),(position_move_x,pos1,0),(position_move_y,pos1,112),(particle_system_burst,"psys_pistol_smoke",pos1,15)])] ],
["w_handgonne_2", "Handgonne", [("w_handgonne_2",0)], itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
2230, weight(3.8)|abundance(90)|difficulty(0)|spd_rtng(60)|shoot_speed(180)|thrust_damage(120,pierce)|max_ammo(1)|accuracy(98), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,107),(particle_system_burst,"psys_pistol_smoke",pos1,15)])] ],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW SHIELDS ###############################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

### Regular shields
["s_battle_shield_charles", "Battle Shield",   [("s_battle_shield_charles" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_edward", "Battle Shield",   [("s_battle_shield_edward" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_prince_1", "Battle Shield",   [("s_battle_shield_prince_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_prince_2", "Battle Shield",   [("s_battle_shield_prince_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_a1", "Battle Shield",   [("s_battle_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_a2", "Battle Shield",   [("s_battle_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_b1", "Battle Shield",   [("s_battle_shield_b1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_b2", "Battle Shield",   [("s_battle_shield_b2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_e1", "Battle Shield",   [("s_battle_shield_e1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_e2", "Battle Shield",   [("s_battle_shield_e2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_f1", "Battle Shield",   [("s_battle_shield_f1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_battle_shield_f2", "Battle Shield",   [("s_battle_shield_f2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],

["s_large_shield_a1", "Large Shield",   [("s_large_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,140 , weight(3)|hit_points(280)|body_armor(10)|spd_rtng(90)|shield_width(48)|shield_height(120),imodbits_shield],
["s_large_shield_a2", "Large Shield",   [("s_large_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,140 , weight(3)|hit_points(280)|body_armor(10)|spd_rtng(90)|shield_width(48)|shield_height(120),imodbits_shield],
["s_large_shield_b1", "Large Shield",   [("s_large_shield_b1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,140 , weight(3)|hit_points(280)|body_armor(10)|spd_rtng(90)|shield_width(48)|shield_height(120),imodbits_shield],
["s_large_shield_b2", "Large Shield",   [("s_large_shield_b2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,140 , weight(3)|hit_points(280)|body_armor(10)|spd_rtng(90)|shield_width(48)|shield_height(120),imodbits_shield],

["s_kite_shield_1", "Kite Shield",   [("s_kite_shield_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,120 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_2", "Kite Shield",   [("s_kite_shield_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,120 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_a1", "Kite Shield",   [("s_kite_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,120 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_a2", "Kite Shield",   [("s_kite_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,120 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_b1", "Kite Shield",   [("s_kite_shield_b1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,130 , weight(3)|hit_points(270)|body_armor(9)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_b2", "Kite Shield",   [("s_kite_shield_b2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,130 , weight(3)|hit_points(270)|body_armor(9)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_c1", "Kite Shield",   [("s_kite_shield_c1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_c2", "Kite Shield",   [("s_kite_shield_c2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(270)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_d1", "Kite Shield",   [("s_kite_shield_d1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,130 , weight(3)|hit_points(270)|body_armor(9)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],
["s_kite_shield_d2", "Kite Shield",   [("s_kite_shield_d2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,130 , weight(3)|hit_points(270)|body_armor(9)|spd_rtng(90)|shield_width(48)|shield_height(110),imodbits_shield],

["s_war_shield_a1", "War Shield",   [("s_war_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_a2", "War Shield",   [("s_war_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_c1", "War Shield",   [("s_war_shield_c1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_c2", "War Shield",   [("s_war_shield_c2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_d1", "War Shield",   [("s_war_shield_d1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_d2", "War Shield",   [("s_war_shield_d2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_e1", "War Shield",   [("s_war_shield_e1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_e2", "War Shield",   [("s_war_shield_e2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_f1", "War Shield",   [("s_war_shield_f1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],
["s_war_shield_f2", "War Shield",   [("s_war_shield_f2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,115 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(48)|shield_height(100),imodbits_shield],

["s_heraldic_shield_a1", "Heraldic Shield",   [("s_heraldic_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_a2", "Heraldic Shield",   [("s_heraldic_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_b1", "Heraldic Shield",   [("s_heraldic_shield_b1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_b2", "Heraldic Shield",   [("s_heraldic_shield_b2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_c1", "Heraldic Shield",   [("s_heraldic_shield_c1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_c2", "Heraldic Shield",   [("s_heraldic_shield_c2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_d1", "Heraldic Shield",   [("s_heraldic_shield_d1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heraldic_shield_d2", "Heraldic Shield",   [("s_heraldic_shield_d2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,105 , weight(2)|hit_points(210)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],

["s_heater_shield_a1", "Heater Shield",   [("s_heater_shield_a1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_a2", "Heater Shield",   [("s_heater_shield_a2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_b1", "Heater Shield",   [("s_heater_shield_b1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_b2", "Heater Shield",   [("s_heater_shield_b2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_c1", "Heater Shield",   [("s_heater_shield_c1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_c2", "Heater Shield",   [("s_heater_shield_c2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_d1", "Heater Shield",   [("s_heater_shield_d1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],
["s_heater_shield_d2", "Heater Shield",   [("s_heater_shield_d2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,100 , weight(2)|hit_points(200)|body_armor(6)|spd_rtng(95)|shield_width(50)|shield_height(85),imodbits_shield],

["s_steel_buckler", "Steel Buckler", [("s_steel_buckler",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  80 , weight(2)|hit_points(100)|body_armor(20)|spd_rtng(100)|shield_width(33),imodbits_shield ],
["s_steel_buckler_2", "Steel Buckler", [("s_steel_buckler_2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  95 , weight(2)|hit_points(120)|body_armor(20)|spd_rtng(100)|shield_width(30)|shield_height(45),imodbits_shield ],

### Heraldics
["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,105 , weight(3.5)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_e", "Board Shield",[("tableau_shield_pavise_3" ,0)], itp_type_shield|itp_cant_use_on_horseback, itcf_carry_board_shield,370 , weight(5)|hit_points(550)|body_armor(10)|spd_rtng(78)|shield_width(45)|shield_height(100),imodbits_shield,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_3", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW QUEST ITEMS ###########################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,43,32,-5),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 20, 40),])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

#quest item 1429
["plan_1", "Plan de fabrication d'epees", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_2", "Plan de fabrication de fleches", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_3", "Plan de fabrication de careaux", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_4", "Plan de fabrication d'un bouclier", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_5", "Plan de fabrication d'arcs", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_6", "Plan de fabrication d'arbaletes", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_7", "Plan de fabrication de lances", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
["plan_8", "Plan de fabrication d'une armure de plates simple", [("item_from_quest_1",0)], itp_type_goods, 0, 55, weight(1)|abundance(0), imodbits_none ],
["plan_9", "Recette d'une soupe de légumes", [("item_from_quest_1",0)], itp_type_goods, 0, 25, weight(1)|abundance(0), imodbits_none ],
["plan_10", "Recette de la potée de choux", [("item_from_quest_1",0)], itp_type_goods, 0, 25, weight(1)|abundance(0), imodbits_none ],
["plan_11", "Recette d'une soupe de poissons", [("item_from_quest_1",0)], itp_type_goods, 0, 25, weight(1)|abundance(0), imodbits_none ],
["plan_12", "Plan de fabrication de torches", [("item_from_quest_1",0)], itp_type_goods, 0, 15, weight(1)|abundance(0), imodbits_none ],
#
["plis", "Lettre", [("lettres",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["plis_caen", "Fausse invitation au banquet de Caen.", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["plis_toul", "Note des rebels,cela ressemble a un code.", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["plis_recomandation", "Lettre de recomandation pour me proposer a devenire vassal.", [("lettre_ouverte",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["chevaliere", "Chevaliere", [("item_from_quest_2",0)], itp_type_goods, 0, 3000, weight(2)|abundance(0), imodbits_none ],
["medaille", "Medaille de Mathieu", [("item_from_quest_3",0)], itp_type_goods, 0, 2000, weight(2)|abundance(0), imodbits_none ],
["plume", "Plumes", [("item_from_quest_4",0)], itp_merchandise|itp_type_goods, 0, 5, weight(1)|abundance(0), imodbits_none ],
["poison", "Poison", [("item_from_quest_5",0)], itp_type_goods, 0, 500, weight(1)|abundance(0), imodbits_none ],
["pier", "Pierre a aiguiser", [("item_from_quest_6",0)], itp_merchandise|itp_type_goods, 0, 12, weight(2)|abundance(0), imodbits_none ],
["bois", "Bois", [("item_from_quest_7",0)], itp_merchandise|itp_type_goods, 0, 10, weight(15)|abundance(0), imodbits_none ],
["alchimi", "Alcool d'Alchimiste", [("item_from_quest_10",0)], itp_type_goods, 0, 140, weight(5)|abundance(0), imodbits_none ],
["corde", "Corde", [("item_from_quest_11",0)], itp_merchandise|itp_type_goods, 0, 8, weight(3)|abundance(0), imodbits_none ],
["cuir", "Cuir", [("item_from_quest_12",0)], itp_merchandise|itp_type_goods, 0, 14, weight(2)|abundance(0), imodbits_none ],
["champiv", "Champignons veneneux", [("champi_1",0)], itp_merchandise|itp_type_goods, 0, 3, weight(1)|abundance(0), imodbits_none ],
["enclume", "Enclume", [("smithy_anvil_noscript",0)], itp_merchandise|itp_type_goods, 0, 550, weight(70)|abundance(0), imodbits_none ],
["cle_1", "clé", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["cle_2", "clé du coffre du Chambellan", [("item_from_quest_17",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],

["epee_jeanne_charles", "épée mysterieuse", [("long_sword",0),("scab_longsw_a",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0, weight(1.5)|difficulty(0)|spd_rtng(100)|weapon_length(102)|swing_damage(40,cut)|thrust_damage(36,pierce), imodbits_sword ],
#
["daggerspecial_medievale", "Dague empoisonée", [("w_dagger_pikeman",0)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left, 364, weight(0.75)|difficulty(0)|spd_rtng(109)|weapon_length(57)|swing_damage(40,cut)|thrust_damage(51,pierce), imodbits_sword_high ],
["bolts5", "Carreaux", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(49,pierce)|max_ammo(5), imodbits_missile ],
["throwing_daggers_poison", "Dagues empoisonées", [("throwing_dagger",0)], itp_type_thrown|itp_primary, itcf_throw_knife, 193, weight(3.5)|difficulty(0)|spd_rtng(110)|shoot_speed(24)|thrust_damage(100,cut)|max_ammo(2)|weapon_length(0), imodbits_thrown ],
["boltsspecial", "Carreaux  empoisonés", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 564, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(50,pierce)|max_ammo(10), imodbits_missile ],
["arrows_speciale", "fl?hes empoison?s", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back, 372, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(30,pierce)|max_ammo(20), imodbits_missile ],
["espee_ecuyer", "épée rouillée avec des Armoiries", [("w_onehanded_sword_hospitaller",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 230 , weight(1.75)|difficulty(0)|spd_rtng(99) | weapon_length(104)|swing_damage(20 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

#lettres et colis quetes messager begin
["lettre0", "Lettre pour le maitre de guilde des marchands de Montpelier", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["lettre1", "Lettre pour le maitre de guilde des marchands de Marseille", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["lettre2", "Lettre pour le maitre de guilde des marchands de Paris", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["lettre3", "Lettre pour le maitre de guilde des marchands de Dijon", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["lettre4", "Lettre pour le maitre de guilde des marchands de Caen", [("item_from_quest_15",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["lettre5", "Cargaison du vendeur de livres de Bordeau", [("chest_simple",0)], itp_type_goods, 0, 0, weight(3)|abundance(0), imodbits_none ],
["lettre6", "Cargaison de l'armurier de Paris", [("chest_simple",0)], itp_type_goods, 0, 0, weight(3)|abundance(0), imodbits_none ],
["lettre7", "Cargaison de l'armurier d'Avignon", [("chest_simple",0)], itp_type_goods, 0, 0, weight(3)|abundance(0), imodbits_none ],
["lettre9", "Cargaison du forgeron de Reims", [("chest_simple",0)], itp_type_goods, 0, 0, weight(3)|abundance(0), imodbits_none ],

["chaudron", "Chaudron", [("cauldron_a",0)], itp_type_goods, 0, 230, weight(6)|abundance(0), imodbits_none ],
["ustensil", "Ustensiles de cuisine", [("item_from_quest_20",0)], itp_type_goods, 0, 30, weight(1)|abundance(0), imodbits_none ],


["rpg_anterroche_armor", "Cotte de mailles aux armoiries Anterroche", [("a_surcoat_over_mail_base",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["rpg_armor_arloing", "Cotte de mailles aux Arloing", [("a_surcoat_over_mail_base",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],


["templar_q_sword", "épée Maconique", [("templar_sword",0),], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip, 494, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(121)|swing_damage(35,cut)|thrust_damage(32,pierce), imodbits_sword_high ],
["maconique_armor", "Cotte de mailles Maconique", [("a_surcoat_over_mail_base",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
#["bouclier_maconique","Bouclier Maconique", [("bouclier_mac",0)], itp_type_shield , itcf_carry_kite_shield, 165 , weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],

#["dagger_medievale", "Dague", [("dagger_medievale",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 64 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(57)|swing_damage(25 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["grimoire_rennes_chat", "Initiation au savoir franc maconique (a lire au menu documents).", [("m_book2",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["grimoire_orleans", "Les loges secrettes (a lire au menu documents).", [("m_book",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],


["tresort_1", "Rubis", [("rubis",0)], itp_type_goods, 0, 3200, weight(1)|abundance(0), imodbits_none ],
["tresort_2", "améthyste", [("pierre_bleue",0)], itp_type_goods, 0, 1800, weight(1)|abundance(0), imodbits_none ],
["tresort_3", "améthyste", [("pierre_bleue",0)], itp_type_goods, 0, 1800, weight(1)|abundance(0), imodbits_none ],
["tresort_4", "Emeraude", [("emeraude",0)], itp_type_goods, 0, 2300, weight(1)|abundance(0), imodbits_none ],
["tresort_5", "Anneau d'or", [("anneau_or",0)], itp_type_goods, 0, 1800, weight(1)|abundance(0), imodbits_none ],
["tresort_6", "Anneau d'or et améthyste", [("anneau_pierre",0)], itp_type_goods, 0, 3000, weight(1)|abundance(0), imodbits_none ],

["cidre", "Cidre", [("bierr",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, weight(30)|abundance(70)|food_quality(50)|max_ammo(50), imodbits_none ],
["practice_sword_figurants","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(5,blunt)|thrust_damage(4,blunt),imodbits_none],

["cle_auberge_maison", "clé de la maison abandonnée", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],

["dedal_kufel","Kufel",[("dedal_kufelL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lutnia","Lutnia",[("dedal_lutniaL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lira","Lira",[("dedal_liraL",0)],		itp_type_hand_armor,0,0,weight(1),0],


["cavalier_invisible_casque", "Armet", [("cavalier_invisible_casque",0)], itp_type_head_armor|itp_covers_head, 0, 1210, weight(2.85)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["cavalier_invisible_armor", "Light Mail and Plate", [("cavalier_invisible_armor",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["cavalier_invisible_bottes", "English Mail Chausses", [("cavalier_invisible_bottes",0)], itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["cavalier_invisible_gants","Plate Mittens", [("plate_mittens_trans_L",imodbit_reinforced)], itp_type_hand_armor,0, 1940, weight(1.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor],

["cheval_praire", "Cheval exceptionnel", [("ho_hunting_horse_france",0)], itp_type_horse, 0, 730, abundance(70)|body_armor(12)|hit_points(130)|difficulty(4)|horse_speed(52)|horse_maneuver(54)|horse_charge(13)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["cheval_praire_barder", "Cheval exceptionnel bardé", [("ho_horse_barded_blue",0)], itp_type_horse, 0, 1324, abundance(50)|hit_points(130)|body_armor(15)|difficulty(4)|horse_speed(50)|horse_maneuver(52)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],

# ["duke_joutes", "Duc", [("landgraf",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1000, weight(3)|difficulty(1)|spd_rtng(95) | weapon_length(135)|swing_damage(20 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],

["laisse_passer_lorges", "Laissé passé du Duc de Bretagne pour la foret de Lorges", [("lettres",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["cle_mine", "clé de la mine de la foret de Lorges", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["choppe_bier", "Chope de bierre", [("choppe",0)], itp_merchandise|itp_type_goods|itp_food|itp_consumable, 0, 5, weight(1)|abundance(110)|food_quality(20)|max_ammo(5), imodbits_none ],
["cle_de_grotte", "clé de l'ancienne mine de la foret de Lorges", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],

["quest_sniper_crossbow", "Arbalète du chasseur", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 683, weight(3.75)|difficulty(10)|spd_rtng(82)|shoot_speed(90)|thrust_damage(60,pierce)|max_ammo(1), imodbits_crossbow ],

["preuve_mort_pantievre", "Chevaliere de Pantièvre [preuve de sa mort]", [("item_from_quest_2",0)], itp_type_goods, 0, 2000, weight(2)|abundance(0), imodbits_none ],

["a_hauberk_narf_english", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_set_material, "@a_hauberk_narf_english", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],
["a_hauberk_narf_french", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_set_material, "@a_hauberk_narf_french", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],
["a_hauberk_narf_french_red", "Mail Hauberk", [("a_hauberk_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[(ti_on_init_item,[(cur_item_set_material, "@a_hauberk_narf_french_red", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_aketon_base", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_hauberk_narf_arms_aketon_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_hauberk", 0, 0),])]],


##################################################################################################################################################################################################################################################################################################################
###################################################################################################### HYW CUSTOMIZABLE ITEMS ####################################################################################################################################################################################
##################################################################################################################################################################################################################################################################################################################

# Seek & Destroy Item variants with Kham's Armor customization
# Material Switch

### Custom Hoods for helmets
### The custom helmets are inside a loop for the color assignment, don't change their position without changing the loop boundaries	
# Bascinet Base: 29; Hood: 8; Padding: 12; Mail Narf: 16
["h_bascinet_fi_hood_custom", "Bascinet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 370 , weight(1.75)|abundance(100)|head_armor(37)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_bascinet_fi_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_bascinet_fi", 0, 0),])]],
# Eyeslot Kettlehat Base: 28; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_kettlehat_eyeslot_hood_custom", "Kettle Helmet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 360 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_eyeslot_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat_eyeslot", 0, 0),])]],
# Sallet Base: 26; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_sallet_hood_custom", "Sallet Helmet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 340 , weight(1.75)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_sallet_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_sallet", 0, 0),])]],
# Cerveliere Base: 25; Hood: 8; Padding: 12; Mail Narf: 16
["h_cerveliere_hood_custom", "Cerveliere with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 330 , weight(1.5)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_cerveliere_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_cerveliere", 0, 0),])]],
# Byzantion Base: 24; Hood: 8; Padding: 12; Mail Narf: 16
["h_byzantion_hood_custom", "Byzantion Helmet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 320 , weight(1.75)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_byzantion_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_byzantion", 0, 0),])]],
["h_byzantion_painted_hood_custom", "Byzantion Helmet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_byzantion_painted_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_byzantion_painted", 0, 0),])]],
# Chapel de Fer Base: 22; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_chapel_de_fer_1_hood_custom", "Chapel de Fer with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_1_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_chapel_de_fer_1", 0, 0),])]],
["h_chapel_de_fer_2_hood_custom", "Chapel de Fer with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_2_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_chapel_de_fer_2", 0, 0),])]],
["h_chapel_de_fer_3_hood_custom", "Chapel de Fer with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_3_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_chapel_de_fer_3", 0, 0),])]],
["h_chapel_de_fer_4_hood_custom", "Chapel de Fer with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_chapel_de_fer_4_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_chapel_de_fer_4", 0, 0),])]],
# Kettle Hat Base: 22; Hood: 8; Padding: 12; Mail Narf: 16; Gorget: 18
["h_kettlehat_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat", 0, 0),])]],
["h_kettlehat_2_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_2_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat_2", 0, 0),])]],
["h_kettlehat_3_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_3_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat_3", 0, 0),])]],
["h_kettlehat_4_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_4_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat_4", 0, 0),])]],
["h_kettlehat_painted_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 300 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_kettlehat_painted_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_kettlehat_painted", 0, 0),])]],
# Round Kettle Hat Base: 20; Hood: 8; Padding: 12; Mail Narf: 16
["h_round_kettlehat_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 280 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_round_kettlehat_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_round_kettlehat", 0, 0),])]],
["h_round_kettlehat_painted_hood_custom", "Kettle Hat with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 280 , weight(1.75)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_round_kettlehat_painted_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_round_kettlehat_painted", 0, 0),])]],
# Pot Helmet Base: 14; Hood: 8; Padding: 12; Mail Narf: 16
["h_pot_helmet_hood_custom", "Pot Helmet with Hood", [("o_hood_narf_base",0)], itp_merchandise| itp_type_head_armor| itp_attach_armature,0, 220 , weight(1.75)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[custom_reskin("itm_h_pot_helmet_hood_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@h_pot_helmet", 0, 0),])]],
### Seek: Don't put items between h_bascinet_fi_hood_custom and a_peasant_man_custom without editing the script

### Armors
["a_peasant_man_custom", "Peasant Tunic", [("a_peasant_tunic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_peasant_man_custom")]], 
["a_gambeson_custom", "Gambeson", [("a_gambeson_white",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_gambeson_custom")]], 
["a_gambeson_narf_custom", "Padded Jack", [("a_gambeson_narf",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 415 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(6)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_gambeson_narf_custom")]], 
["a_padded_cloth_custom", "Padded Cloth", [("a_padded_cloth_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth, [custom_reskin("itm_a_padded_cloth_custom")]], 
["a_padded_over_mail_custom", "Mail Hauberk", [("a_padded_over_mail",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor , [custom_reskin("itm_a_padded_over_mail_custom")]], 

### Seek: The custom Aketons are inside a loop for the color assignment, don't change their position without changing the loop boundaries																																																																								
["a_aketon_narf_custom", "Aketon", [("a_aketon_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 455 , weight(7)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_aketon_narf_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@o_hosen_aketon", 0, 0),(cur_item_add_mesh, "@a_aketon_narf_arms", 0, 0),])],],
["a_aketon_jackchain_narf_custom", "Aketon", [("a_aketon_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 480 , weight(7)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_aketon_jackchain_narf_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@o_hosen_aketon", 0, 0),(cur_item_add_mesh, "@a_aketon_narf_arms_jackchain", 0, 0),])],],
["a_aketon_plate_hose_narf_custom", "Aketon", [("a_aketon_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 555 , weight(7)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(18)|difficulty(0) ,imodbits_cloth ,[custom_reskin("itm_a_aketon_plate_hose_narf_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@o_hosen_aketon_plate", 0, 0),(cur_item_add_mesh, "@a_aketon_narf_arms", 0, 0),])],],
["a_aketon_jackchain_plate_hose_narf_custom", "Aketon", [("a_aketon_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 580 , weight(7)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_aketon_jackchain_plate_hose_narf_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@o_hosen_aketon_plate", 0, 0),(cur_item_add_mesh, "@a_aketon_narf_arms_jackchain", 0, 0),])],],

["a_brigandine_bogmir_custom", "Brigandine", [("a_brigandine_bogmir",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor, [custom_reskin("itm_a_brigandine_bogmir_custom")]], 
["a_surcoat_over_mail_custom", "Surcoat over Mail", [("a_surcoat_over_mail_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ,[custom_reskin("itm_a_surcoat_over_mail_custom")]], 
["a_coat_of_plates_custom", "Coat of Plates", [("a_coat_of_plates_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ,[custom_reskin("itm_a_coat_of_plates_custom")]], 

### Seek: The Brigandines are in a loop for the color assignment, be weary of this if planning to change their order/location
["a_brigandine_narf_padded_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 800 , weight(7)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_padded_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 940 , weight(7)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_padded_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1020 , weight(7)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

["a_brigandine_narf_padded_jackchain_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 880 , weight(7)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_jackchain_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_padded_jackchain_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1020 , weight(7)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_jackchain_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_padded_jackchain_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1100 , weight(7)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_jackchain_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon_jackchain", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

["a_brigandine_narf_padded_plate_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_padded_plate_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1930 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_padded_plate_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2170 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

["a_brigandine_narf_padded_plate_disc_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_disc_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate_disc", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_padded_plate_disc_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1930 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_disc_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate_disc", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_padded_plate_disc_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2170 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_padded_plate_disc_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_plate_disc", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

["a_brigandine_narf_mail_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1780 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_mail_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],], 
["a_brigandine_narf_mail_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1930 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_mail_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_mail_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2170 , weight(7)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_mail_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_aketon", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_arms_mail", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],], 

["a_brigandine_narf_plate_mail_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1980 , weight(7)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_mail_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_plate_mail_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2130 , weight(7)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_mail_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],], 
["a_brigandine_narf_plate_mail_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2270 , weight(7)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_mail_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],

["a_brigandine_narf_plate_disc_mail_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2080 , weight(7)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_disc_mail_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine", 0, 0),])],],
["a_brigandine_narf_plate_disc_mail_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2230 , weight(7)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_disc_mail_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate", 0, 0),])],],
["a_brigandine_narf_plate_disc_mail_full_plate_hose_custom", "Brigandine", [("a_brigandine_narf_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 2330 , weight(7)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(24)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_a_brigandine_narf_plate_disc_mail_full_plate_hose_custom"),(ti_on_init_item,[(cur_item_add_mesh, "@a_brigandine_narf_arms_mail_plate", 0, 0),(cur_item_add_mesh, "@a_brigandine_narf_skirt_mail", 0, 0),(cur_item_add_mesh, "@o_hosen_brigandine_plate_full", 0, 0),])],],


["a_churburg_narf_custom", "Churburg Plate", [("a_churburg_narf_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1460, weight(27)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(18)|difficulty(8), imodbits_armor , [custom_reskin("itm_a_churburg_narf_custom")]], 
["a_churburg_brass_narf_custom", "Churburg Brass Plate", [("a_churburg_narf_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 1680, weight(27)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(18)|difficulty(8), imodbits_armor , [custom_reskin("itm_a_churburg_brass_narf_custom")]], 
["a_early_transitional_narf_custom", "Heavy Mail and Plate", [("a_early_transitional_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1920 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(18)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_early_transitional_narf_custom")]],  
["a_corrazina_narf_custom", "Corrazina", [("a_corrazina_narf_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 2140 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(14)|difficulty(8) ,imodbits_armor , [custom_reskin("itm_a_corrazina_narf_custom")]], 
["a_plate_harness_custom", "Plate Harness", [("a_plate_harness_base",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 6230, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor  , [custom_reskin("itm_a_plate_harness_custom")]],  

["b_hosen_shoes_custom", "Woolen Hose", [("b_hosen_shoes",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_b_hosen_shoes_custom")]],  
["b_hosen_poulaines_custom", "Woolen Hose Poulaines", [("b_hosen_poulaines",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [custom_reskin("itm_b_hosen_poulaines_custom")]],  

# Model Switch
["a_leather_vest_custom", "Leather Vest", [("a_leather_vest_base",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 325 , weight(3)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth,[custom_remodel("itm_a_leather_vest_custom")]], 
["a_leather_armor_custom", "Padded Leather", [("a_leather_armor_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ,[custom_remodel("itm_a_leather_armor_custom")]], 
["a_mail_shirt_custom", "Mail Shirt", [("a_mail_shirt_base",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ,[custom_remodel("itm_a_mail_shirt_custom")]], 


["items_end", "Items End", [("s_small_shield",0)], 0, 0, 1, 0, 0],
]

#MOTO generate no-swing versions of weapons
#Warning: this makes additions to item table non-save compatible, as the system only reads in the "new" ones, effectively overwriting the real new ones
#It may be best to comment out until the table is set
#append_noswing_items(items)
