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
["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1)|difficulty(0)|spd_rtng(98)|shoot_speed(53)|thrust_damage(12,pierce), imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|difficulty(0)|spd_rtng(70)|shoot_speed(90)|thrust_damage(32,pierce)|max_ammo(1), imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("wooden_buckler1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


["horse_meat", "Horse Meat", [("raw_meat",0)], itp_type_goods|itp_food|itp_consumable, 0, 18, weight(40)|food_quality(30)|max_ammo(40), imodbits_none ],
# Items before this point are hardwired and their order should not be changed!
["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_great_lance_upstab, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
["practice_shield","Practice Shield", [("small_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
["practice_bow", "Practice Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90)|shoot_speed(55)|thrust_damage(21,blunt), imodbits_bow ],
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
["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
["red_tourney_armor", "Red Tourney Armor", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["blue_tourney_armor", "Blue Tourney Armor", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["green_tourney_armor", "Green Tourney Armor", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["gold_tourney_armor", "Gold Tourney Armor", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30.0)|body_armor(62)|leg_armor(22), imodbits_none ],
["red_tourney_helmet", "Red Tourney Helmet", [("tilting_helm_crow",0)], itp_type_head_armor, 0, 1240, weight(2.75)|head_armor(55), imodbits_none ],
["gold_tourney_helmet", "Gold Tourney Helmet", [("tilting_helm_horns",0)], itp_type_head_armor, 0, 1240, weight(2.75)|head_armor(55), imodbits_none ],

["arena_shield_blue", "Shield", [("battle_shield_f1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],
["arena_shield_green", "Shield", [("kite_shield_a2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],
["arena_shield_yellow", "Shield", [("kite_shield_a2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield, 165, weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|weapon_length(92), imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("milanese_armour",0)], itp_type_body_armor|itp_covers_legs, 0, 2496, weight(30)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(22), imodbits_cloth ],
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
["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1)|difficulty(0)|spd_rtng(98)|shoot_speed(53)|thrust_damage(16,pierce), imodbits_bow ],
["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|difficulty(0)|spd_rtng(70)|shoot_speed(90)|thrust_damage(32,pierce)|max_ammo(1), imodbits_crossbow ],
["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["tutorial_shield", "Kite Shield", [("wooden_buckler1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
["sumpter_horse", "Sumpter Horse", [("sumpter_horse",0)], itp_type_horse|itp_merchandise, 0, 254, abundance(90)|hit_points(100)|body_armor(10)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100), imodbits_horse_basic ],
["sumpter_horse_paris", "Cheval malade", [("sumpter_horse",0)], itp_type_horse|itp_merchandise, 0, 134, abundance(90)|hit_points(90)|body_armor(7)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100), imodbits_horse_basic ],
["saddle_horse", "Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 360, abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],
["saddle_horseparis", "Cheval faible", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 50, abundance(90)|hit_points(88)|body_armor(6)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],
["saddle_horseparis2", "Cheval faible", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 50, abundance(90)|hit_points(87)|body_armor(6)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104), imodbits_horse_basic ],
["steppe_horse", "Steppe Horse", [("steppe_horse",0)], itp_type_horse|itp_merchandise, 0, 292, abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98), imodbits_horse_basic, [], [fac_kingdom_2,fac_kingdom_2] ],
["arabian_horse_a", "Desert Horse", [("arabian_horse_a",0)], itp_type_horse|itp_merchandise, 0, 650, abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2,fac_kingdom_1] ],
["courser", "Courser", [("courser",0)], itp_type_horse|itp_merchandise, 0, 730, abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["arabian_horse_b", "Arabian Horse", [("arabian_horse_b",0)], itp_type_horse|itp_merchandise, 0, 800, abundance(80)|hit_points(110)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["hunter", "Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_type_horse|itp_merchandise, 0, 910, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["warhorse", "War Horse", [("warhorse_chain",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["charger", "Charger", [("charger_new",0)], itp_type_horse|itp_merchandise, 0, 1911, abundance(40)|hit_points(135)|body_armor(25)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1,fac_kingdom_2] ],

["hunter_f", "French Hunter", [("hunting_horse_f",0)], itp_type_horse|itp_merchandise, 0, 910, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["hunter_e", "French Hunter", [("hunting_horse_e",0)], itp_type_horse|itp_merchandise, 0, 910, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108), imodbits_horse_basic|imodbit_champion ],
["warhorse_en1", "English War Horse", [("warhorse_en1",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(12)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["warhorse_en2", "English War Horse", [("warhorse_en2",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(12)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["warhorse_en3", "English War Horse", [("warhorse_en3",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(12)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["warhorse_f1", "French War Horse", [("warhorse_f1",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(13)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["warhorse_f2", "French War Horse", [("warhorse_f2",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(13)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["warhorse_f3", "French War Horse", [("warhorse_f3",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(115)|body_armor(13)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["war_horse_teu", "Teutonic War Horse", [("war_horse_teu",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(125)|body_armor(12)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["breton_war_horse", "Cheval de guerre Breton", [("warhorse_breton",0)], itp_type_horse|itp_merchandise, 0, 1324, abundance(50)|hit_points(125)|body_armor(12)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],

# old mod horses begin
["horse1", "Hunter", [("horse1",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse6", "Hunter", [("horse6",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse7", "Hunter", [("horse7",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse8", "Hunter", [("horse8",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse1e01", "English Destrier", [("horse1e01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 700, abundance(60)|hit_points(115)|body_armor(11)|difficulty(4)|horse_speed(41)|horse_maneuver(39)|horse_charge(30), imodbits_horse_basic|imodbit_champion ],
["horse6e01", "English Hunter", [("horse6e01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse7e01", "English Hunter", [("horse7e01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse8e01", "English Hunter", [("horse8e01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["hunting_horsee01", "English Hunter", [("hunting_horsee01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 564, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],

["horse1f01", "French Hunter", [("hunting_horse_f",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 834, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(37)|horse_charge(29), imodbits_horse_basic|imodbit_champion ],
["horse7f01", "French Hunter", [("hunting_horse_f",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 834, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(37)|horse_charge(29), imodbits_horse_basic|imodbit_champion ],
["courserf01", "French Hunter", [("courserf01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 834, abundance(60)|hit_points(110)|body_armor(20)|difficulty(3)|horse_speed(40)|horse_maneuver(37)|horse_charge(29), imodbits_horse_basic|imodbit_champion ],
["hunting_horsef01", "French Hunter", [("hunting_horse_f",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 834, abundance(60)|hit_points(110)|body_armor(11)|difficulty(3)|horse_speed(40)|horse_maneuver(37)|horse_charge(29), imodbits_horse_basic|imodbit_champion ],

["horse_bardede01", "English Barded Hunter", [("horse_bardede01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 1034, abundance(80)|hit_points(110)|body_armor(13)|difficulty(3)|horse_speed(39)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse_bardede02", "English Barded Hunter", [("horse_bardede02",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 1034, abundance(80)|hit_points(110)|body_armor(13)|difficulty(3)|horse_speed(39)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse_bardede03", "English Barded Hunter", [("horse_bardede03",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 1034, abundance(80)|hit_points(110)|body_armor(13)|difficulty(3)|horse_speed(39)|horse_maneuver(36)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse_bardedf01", "French Barded Hunter", [("horse_bardedf01",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 1034, abundance(80)|hit_points(110)|body_armor(13)|difficulty(3)|horse_speed(39)|horse_maneuver(37)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],
["horse_bardedf02", "French Barded Hunter", [("horse_bardedf02",0),("hunting_horse",imodbits_horse_good)], itp_type_horse, 0, 1034, abundance(80)|hit_points(110)|body_armor(13)|difficulty(3)|horse_speed(39)|horse_maneuver(37)|horse_charge(28), imodbits_horse_basic|imodbit_champion ],



["warhorse2lys", "French_Warhorse", [("warhorse_f1",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(37)|horse_maneuver(40)|horse_charge(40), imodbits_horse_basic ],
["warhorsebluewhite", "French_Warhorse", [("warhorse_f2",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(37)|horse_maneuver(40)|horse_charge(40), imodbits_horse_basic ],
["warhorseblueyellow", "French_Warhorse", [("warhorse_f3",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(37)|horse_maneuver(40)|horse_charge(40), imodbits_horse_basic ],
["warhorsebluecross", "French_Warhorse", [("warhorse_f1",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(37)|horse_maneuver(40)|horse_charge(40), imodbits_horse_basic ],
["warhorse3lions", "English_Warhorse", [("warhorse_en1",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(110)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(37), imodbits_horse_basic ],
["warhorseredwhite", "English_Warhorse", [("warhorse_en2",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(110)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(37), imodbits_horse_basic ],
["warhorseredyellow", "English_Warhorse", [("warhorse_en3",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(110)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(37), imodbits_horse_basic ],
["warhorseredblack", "English_Warhorse", [("warhorse_en1",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(110)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(37), imodbits_horse_basic ],
["warhorseboar", "Warhorse", [("war_horse_teu",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(130)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(38), imodbits_horse_basic ],
["warhorsehre", "Warhorse", [("war_horse_teu",0)], itp_type_horse, 0, 1224, abundance(50)|hit_points(120)|body_armor(15)|difficulty(4)|horse_speed(36)|horse_maneuver(39)|horse_charge(38), imodbits_horse_basic ],

#Out dated horses, cannot buy V
#["barded_horse","English Hunter", [("barded_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 434,abundance(100)|hit_points(110)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28),imodbits_horse_basic|imodbit_champion],
#["barded_horse","English Hunter", [("barded_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 434,abundance(100)|hit_points(110)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(36)|horse_charge(28),imodbits_horse_basic|imodbit_champion],
#["warhorse_long_barding","Warhorse", [("wwarhorse_long_barding",0)], itp_merchandise|itp_type_horse, 0, 924,abundance(100)|hit_points(135)|body_armor(52)|difficulty(4)|horse_speed(37)|horse_maneuver(35)|horse_charge(19),imodbits_horse_basic],
["warhorsecharlesv", "Charles_V's_Warhorse", [("warhorse_charles",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],
["warhorseduguesclin", "Du_Guesclin's_Warhorse", [("warhorse_du_gusclin",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],
["warhorseedwardiii", "Edward_lll's_Warhorse", [("warhorse_edwardiii",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],
["warhorseblackprince", "Black_Prince's_Warhorse", [("warhorse_black_prince",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],
["warhorsechandos", "John Chandos's_Warhorse", [("warhorse_chandos",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],
["breton_warhorse_2", "Cheval de Batailles Breton", [("war_horde_breton_2",0)], itp_type_horse, 0, 1224, abundance(50)|body_armor(15)|hit_points(115)|difficulty(1)|horse_speed(36)|horse_maneuver(34)|horse_charge(45), imodbits_horse_basic ],


["chargerplainblue", "French_Charger", [("chargerplainblue",0)], itp_type_horse, 0, 2511, abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|horse_speed(37)|horse_maneuver(32)|horse_charge(40), imodbits_horse_basic ],
["chargershinyblue", "French_Charger", [("chargershinyblue",0)], itp_type_horse, 0, 2511, abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|horse_speed(37)|horse_maneuver(32)|horse_charge(40), imodbits_horse_basic ],
["chargerred", "English_Charger", [("chargerred",0)], itp_type_horse, 0, 2511, abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|horse_speed(37)|horse_maneuver(32)|horse_charge(40), imodbits_horse_basic ],
["chargerplainred", "English_Charger", [("chargerplainred",0)], itp_type_horse, 0, 1911, abundance(40)|hit_points(120)|body_armor(25)|difficulty(4)|horse_speed(35)|horse_maneuver(31)|horse_charge(45), imodbits_horse_basic ],
#old mod horses end



#whalebone crossbow, yew bow, war bow, arming sword
["arrows", "Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo|itp_merchandise, itcf_carry_quiver_back, 72, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30), imodbits_missile ],
["khergit_arrows", "English Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 410, weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(8,pierce)|max_ammo(60), imodbits_missile ],
["barbed_arrows", "Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124, weight(3)|abundance(70)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30), imodbits_missile ],
["bodkin_arrows", "Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c",ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350, weight(3)|abundance(50)|weapon_length(91)|thrust_damage(4,pierce)|max_ammo(28), imodbits_missile ],
["bolts", "Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(5,pierce)|max_ammo(29), imodbits_missile ],
["steel_bolts", "Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210, weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(6,pierce)|max_ammo(29), imodbits_missile ],
["cartridges", "Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_default_ammo|itp_can_penetrate_shield, 0, 410, weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(15), imodbits_missile ],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

#HYW MOD STUFF
["wisby_gauntlets_black","Splinted Leather Gauntlets", [("wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["wisby_gauntlets_red","Splinted Leather Gauntlets", [("wisby_gauntlets_red_L",0)], itp_merchandise|itp_type_hand_armor,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
["mail_gauntlets","Mail Gauntlets", [("mail_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 490, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["hourglass_gauntlets_ornate","Ornate Hourglass Gauntlets", [("hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor,0, 1190, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],
["hourglass_gauntlets","Hourglass Gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0, 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0, 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0, 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 310 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 853 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["khergit_leather_boots", "Khergit Leather Boots", [("woolen_hose_a",0)],  itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],

#HYW begin Boots

["splinted_greaves_e1", "English Splinted Leather Greaves", [("splinted_greaves_e1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 310 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["splinted_greaves_f1", "French Splinted Leather Greaves", [("splinted_greaves_f1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 310 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
["mail_chausses_e1", "English Mail Chausses", [("mail_chausses_e1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["mail_chausses_f1", "French Mail Chausses", [("mail_chausses_f1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],

["splinted_greaves_nospurs", "Splinted Greaves", [("splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
["splinted_greaves_spurs", "Splinted Greaves with Spurs", [("splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],

["shynbaulds", "Shynbaulds", [("shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],
["steel_greaves", "Cased Greaves", [("steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],

#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("red_dress2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Khergit Lady Dress", [("black_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("red_dress2",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outfit_b_new",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["nobleman_outfit_charles", "Tenue de Noble", [("nobleman_outfit_charles",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit_anglais", "Tenue de Noble", [("nobleman_outfit_anglais",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["nobleman_out", "Tenue de Noble", [("new_noble_tunic_a",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nobleman_out_fr", "Tenue de Noble", [("new_noble_tunic_b",0)],  itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],



["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)],  itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],
#1429 robes ribaudes
["ribaude_dresss", "Robe de fille de joie", [("ribaude_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["ribaude_dress6bluues", "Robe de fille de joie bleue", [("ribaude_dress6bluue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

#for future:
["coat", "Coat", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_mail_coat", "Sleeveless Coat of Mail", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_coat", "Sleeveless Coat", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_coat", "Hide Coat", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["homespun_dress", "Homespun Dress", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_outfit", "Nordic Outfit", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_armor", "Nordic Armor", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("leather_vest_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

["dress", "Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress_tw", "Robe bleue", [("blue_dress2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress_tw2", "Robe de paysane", [("blue_dress3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["woolen_dress", "Woolen Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0, 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["red_tunic", "Red Tunic", [("surcoat_over_mail_e1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_vest_z",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1544 , weight(22)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_type_body_armor  |itp_covers_legs ,0, 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_type_body_armor  |itp_covers_legs ,0, 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4553, weight(27)|abundance(100)|head_armor(0)|body_armor(56)|leg_armor(17)|difficulty(9), imodbits_plate ],

["tavern_shirt", "Tunique d'artisant", [("tavern_keep_shirt",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["g_tw_shirt", "Tunique", [("shirt_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],




##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
##armors_e
["sarranid_elite_armor", "Sarranid Elite Armor", [("surcoat_over_mail_e1",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 260 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

#Quest-specific - perhaps can be used for prisoners,

["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3610 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],

#mod armor begin

#["arena_armore01", "English Shirt and Mail ", [("arena_armore01",0)],itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15), imodbits_armor ],
#["arena_armore02", "English Shirt and Mail", [("arena_armore02",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15), imodbits_armor ],
#["arena_armorf01", "French Shirt and Mail", [("arena_armorf01",0)],itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15), imodbits_armor ],
#["arena_armorf02", "French Shirt and Mail", [("arena_armorf02",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15), imodbits_armor ],


["swiss_armor", "Swiss Armor", [("early_transitional_teu",0)], itp_type_body_armor |itp_covers_legs ,0, 250 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(6)|difficulty(0), imodbits_cloth ],

["rawhide_coatwhite", "White_Fur_Coat", [("thick_coat_a",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 12, weight(5)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(0)|difficulty(0), imodbits_cloth ],


["robeblack", "Black_Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 26 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["robecross", "Monk_Robe", [("robecross",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 26 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["robewhite", "Priest_Robe", [("robepurple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 26 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["robered", "Chaplain_Robe", [("robepurple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 26 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["robepurple", "Bishop_Robe", [("robepurple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 26 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],


["courtly_outfitblue", "French_Royal_Outfit", [("nobleman_outfitblue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["rich_outfitblue", "French_Rich_Outfit", [("merchant_outfitblue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["court_dressblue", "French_Court_Dress", [("court_dressred",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["courtly_outfitred", "English_Royal_Outfit", [("nobleman_outfitred",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["rich_outfitred", "English_Rich_Outfit", [("merchant_outfitred",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["court_dressred", "English_Court_Dress", [("court_dressred",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_vestblue", "French_Leather_Vest", [("coat_of_plates_f1",0)],  itp_type_body_armor|itp_civilian  |itp_covers_legs ,0, 96 , weight(6)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_vestred", "English_Leather_Vest", [("padded_leatherblack",0)], itp_type_body_armor|itp_civilian  |itp_covers_legs ,0, 96 , weight(6)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_vestgreen", "Leather_Vest", [("padded_leatherblack",0)],  itp_type_body_armor|itp_civilian  |itp_covers_legs ,0, 96 , weight(6)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

#["padded_clothblue", "French_Padded_Cloth", [("padded_clothblue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 106 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["padded_clothred", "English_Padded_Cloth", [("padded_clothred",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 106 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["english_paddedcloth", "English Padded Cloth", [("aketon_english",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 257 , weight(11)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["french_paddedcloth", "French Padded Cloth", [("aketon_french02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 257 , weight(11)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["french_paddedcloth1", "French Padded Cloth", [("aketon_french01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 257 , weight(11)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

#["padded_leatherblue", "French_Padded_Leather", [("padded_leather_f01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["padded_leatherblueyellow", "French_Padded_Leather", [("padded_leather_f02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["padded_leather_f03", "French_Padded_Leather", [("padded_leather_f03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],


#["padded_leatherred", "English_Padded_Leather", [("padded_leatherred",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["padded_leatherredyellow", "English_Padded_Leather", [("padded_leatherredyellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["padded_leatherblack", "Black_Padded_Leather", [("padded_leatherblack",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["padded_leatheryellow", "Yellow_Padded_Leather", [("padded_leatheryellow",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 165 , weight(12)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

#["blue_gambeson", "French_Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["red_gambeson", "English_Gambeson", [("red_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#["reinf_jerkin_striped", "English Banded Armor", [("reinf_jerkin_striped",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,  2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
#["reinf_jerkin_english", "English Banded Armor", [("reinf_jerkin_english",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,  2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],

#["english_paddedcloth_striped", "English Padded Cloth", [("aketon_english_striped",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["english_paddedcloth_red", "English Padded Cloth", [("aketon_english_whitered",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["padded_leather_english", "English Padded Leather", [("padded_leather_english",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

#["leather_jerkin_eng", "English_Leather_Jerkin", [("leather_jerkin_eng",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["leather_jerkin_striped", "English_Leather_Jerkin", [("leather_jerkin_striped",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#["haubergeon_english", "Haubergeon", [("haubergeon_english",0),("haubergeon_b",imodbits_good)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 543 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(6)|difficulty(6) ,imodbits_armor ],

# ["leather_jerkinblue", "French_Leather_Jerkin", [("leather_jerkin_f01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
# ["leather_jerkinf01", "French_Leather_Jerkin", [("leather_jerkin_f02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
# ["leather_jerkinf02", "French_Leather_Jerkin", [("leather_jerkin_f03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
# ["leather_jerkinf03", "French_Leather_Jerkin", [("leather_jerkin_f04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

# ["leather_jerkinred", "English_Leather_Jerkin", [("leather_jerkinred",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_jerkingreen", "Leather_Jerkin", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_jerkinfur", "Leather_Jerkin_with_Mail", [("padded_leatherblack",0)], itp_type_body_armor  |itp_covers_legs ,0, 211 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

#["mail_shirtblue", "French_Mail_Shirt", [("mail_shirt",0)],                         itp_type_body_armor  |itp_covers_legs ,0, 920 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],
#["mail_shirtbluewhite", "French_Mail_Shirt", [("mail_shirtbluewhite",0)],           itp_type_body_armor  |itp_covers_legs ,0, 920 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],
#["mail_shirtred", "English_Mail_Shirt", [("mail_shirtred",0)],                      itp_type_body_armor  |itp_covers_legs ,0, 920 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],
#["mail_shirtredwhite", "English_Mail_Shirt", [("mail_shirtredwhite",0)],            itp_type_body_armor  |itp_covers_legs ,0, 266 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],
#["mail_shirtduguesclin", "Du_Guesclin's_Mail_Shirt", [("mail_shirtduguesclin",0)],  itp_type_body_armor  |itp_covers_legs ,0, 920 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],
#["mail_hauberkblue", "French_Mail_Hauberk", [("mail_hauberkred",0)],                itp_type_body_armor  |itp_covers_legs ,0, 411 , weight(16)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
#["mail_hauberkred", "English_Mail_Hauberk", [("mail_hauberkred",0)],                itp_type_body_armor  |itp_covers_legs ,0, 411 , weight(16)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

#["mail_shirt_redx", "English_Mail_Shirt", [("mail_shirt_redx",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 920 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_armor ],


["black_studded_leather_coat", "Black Studded Leather Coat", [("banded_armor_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
# ["french_studded_leather02", "French Studded Leather Coat", [("frenchstudded02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
# ["french_studded_leather01", "French Studded Leather Coat", [("frenchstudded01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
# ["french_studded_leather03", "French Studded Leather Coat", [("frenchstudded03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],


# ["striped_studded_leather", "English Studded Leather Coat", [("english_std_lthr1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
# ["english_studded_leather", "English Studded Leather Coat", [("englishstudded",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],
# ["english_studded_coat", "English Studded Leather Coat", [("striped_studded_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  690 , weight(14)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(7) ,imodbits_armor ],


# ["surcoat_mail_french01", "French Surcoat over Mail", [("surcoat_mail_french01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_french02", "French Surcoat over Mail", [("surcoat_mail_french02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_french03", "French Surcoat over Mail", [("surcoat_mail_french03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_french04", "French Surcoat over Mail", [("surcoat_mail_french04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_french05", "French Surcoat over Mail", [("surcoat_mail_french05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],

#["heraldic_surcoat_f01", "French Mail and Surcoat", [("mail_surcoat_f04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],

# ["surcoat_over_mail_english", "English Surcoat over Mail", [("surcoat_over_mail_english",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mailwhitered", "English Surcoat over Mail", [("surcoat_mailwhitered",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mailstriped", "English Surcoat over Mail", [("surcoat_mailstriped",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_half", "English Surcoat over Mail", [("surcoat_mail_half",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
# ["surcoat_mail_lion", "English Surcoat over Mail", [("surcoat_mail_lion",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],

# ["dark_surcoat_over_mail", "Black Surcoat over Mail", [("surcoat_over_mailb",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["black_brigandine", "Black Brigandine", [("banded_armor_a",0)], itp_type_body_armor|itp_covers_legs,0, 1162 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
# ["brigandine_english", "English Brigandine", [("brigandine_english",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1162 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
# ["french_brigandine", "French Brigandine", [("french_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1162 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
# ["genoese_brigandine", "Genoese Brigandine", [("genoese_brigandine",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1162 , weight(21)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor ],


["black_cuir_bouilli", "Black Cuir Bouilli", [("cuir_bouilli_a",0)],  itp_type_body_armor  |itp_covers_legs ,0, 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor ],

["byrnie_swiss1", "Swiss Byrnie", [("early_transitional_teu",0)], itp_type_body_armor  |itp_covers_legs ,0, 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor ],




#["heraldic_surcoat_f01", "French Mail and Surcoat", [("mail_surcoat_f04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["french_mail_surcoatc", "French Mail and Surcoat", [("french_mail_surcoatc",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["french_mail_surcoatd", "French Mail and Surcoat", [("french_mail_surcoatd",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["english_mail_surcoatf", "English Mail and Surcoat", [("english_mail_surcoatf",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["english_mail_surcoate", "English Mail and Surcoat", [("english_mail_surcoate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["french_mail_surcoath", "French Mail and Surcoat", [("french_mail_surcoath",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
#["english_mail_surcoatg", "English Mail and Surcoat", [("english_mail_surcoatg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 854 , weight(22)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],

["heraldric_armor3lys", "French_Heraldric_Armor", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorbluewhite", "French_Heraldric_Armor", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorblueyellow", "French_Heraldric_Armor", [("early_transitional_f3",0)], itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorlion", "English_Heraldric_Armor", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorstripes", "English_Heraldric_Armor", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorredwhite", "English_Heraldric_Armor", [("padded_leatherblack",0)],  itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],
["heraldric_armorredyellow", "English_Heraldric_Armor", [("padded_leatherblack",0)], itp_type_body_armor  |itp_covers_legs ,0, 1360 , weight(18)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(16)|difficulty(7) ,imodbits_armor ],

# ["coat_of_plateslys", "French_Coat_of_Plates", [("coat_of_platesf01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["coat_of_plates3lys", "French_Coat_of_Plates", [("coat_of_platesf02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["coat_of_platesf03", "French_Coat_of_Plates", [("coat_of_platesf02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

# ["coat_of_plates3lions", "English_Coat_of_Plates", [("coat_of_plates01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["coat_of_plateslion", "English_Coat_of_Plates", [("coat_of_plates02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
# ["coat_of_platese01", "English_Coat_of_Plates", [("coat_of_plates03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

#["coat_of_platesgreen", "Coat_of_Plates", [("coat_of_platesgreen",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(17)|difficulty(8) ,imodbits_armor ],
#["plate_armorblue", "French_Plate_Armor", [("plate_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
#["plate_armorred", "English_Plate_Armor", [("plate_armorred",0)],  itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
#["plate_armorblack", "English_Plate_Armor", [("plate_armorblack",0)],  itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
#["black_armorgrey", "Plate_Armor", [("black_armorgrey",0)],  itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],

#["plate_armorgolden", "French_Golden_Plate_Armor", [("plate_armorgolden",0)],  itp_type_body_armor  |itp_covers_legs ,0, 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
#["black_armorgolden", "Golden_Black_Armor", [("black_armorgolden",0)],  itp_type_body_armor  |itp_covers_legs ,0, 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
#["black_armorgreygolden", "Golden_Plate_Armor", [("black_armorgreygolden",0)],  itp_type_body_armor  |itp_covers_legs ,0, 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],
#["linen_tunicf01", "Linen Tunic", [("linen_tunicf01",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
# 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#["linen_tunicf02", "Linen Tunic", [("linen_tunicf02",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
# 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#["linen_tunice01", "Linen Tunic", [("linen_tunice01",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
# 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],


["linen_tunic_swiss", "Swiss Leather Tunic", [("early_transitional_teu",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 250 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

#["reinf_jerkin_french", "French Banded Armor", [("reinf_jerkin_french",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,  2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],

#["french_halfchiton", "French_Transtional_Plate", [("french_halfchiton",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(17)|difficulty(9) ,imodbits_plate ],

#["halfchiton", "English_Transtional_Plate", [("halfchiton",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,  6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
#["test_rigged_transitional", "Light Mail and Plate", [("test_rigged_transitional",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(0) ,imodbits_armor ],

["dark_light_mail_and_plate", "Light Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(0) ,imodbits_armor ],


# ["mail_plate_e01", "English Mail and Plate", [("mail_plate_e01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
# ["mail_plate_e02", "English Mail and Plate", [("mail_plate_e02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
# ["mail_plate_e07", "English Mail and Plate", [("mail_plate_e07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
# ["mail_plate_e08", "English Mail and Plate", [("mail_plate_e08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],


#["plate_armor_f01", "French Mail and Plate", [("plate_armor_f01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
#["plate_armor_f02", "French Mail and Plate", [("plate_armor_f02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
#["plate_armor_f03", "French Mail and Plate", [("plate_armor_f03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
#["plate_armor_f04", "French Mail and Plate", [("plate_armor_f04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
#["mail_plate_f05", "French Mail and Plate", [("mail_plate_f05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor ],

#["transitional_plate", "Transitional_Plate", [("transitional_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
#["transitional_plate_french", "French Transitional_Plate", [("transitional_plate_french",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
#2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],

#["full_plate", "Parital Plate", [("full_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],


#["transitional_boots", "Iron Greaves", [("transitional_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
# 2374 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],

["klepp_helmet", "Klappvisor_Bascinet", [("klepp_helmet",0)], itp_merchandise| itp_type_head_armor |itp_covers_head  ,0, 750 , weight(2.75)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["pigface", "Pigface_Bascinet", [("pigface",0)], itp_merchandise| itp_type_head_armor |itp_covers_head  ,0, 750 , weight(2.75)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["flemish_armet", "Armet", [("flemish_armet",0)],  itp_merchandise|itp_type_head_armor |itp_covers_head  ,0, 1750 , weight(2.75)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["greatbascinet1", "Great Bascinet", [("greatbascinet1",0)], itp_merchandise| itp_type_head_armor |itp_covers_head  ,0, 950 , weight(2.75)|abundance(100)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["greathelm1_orig", "Great Helm", [("greathelm1",0)], itp_merchandise| itp_type_head_armor |itp_covers_head  ,0, 1020 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["greathelmwhat_orig", "Great Helm", [("greathelmwhat",0)], itp_merchandise| itp_type_head_armor |itp_covers_head  ,0, 1020 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],



#HYW Begin Armor
["peasant_man_e1", "English Yoeman's Tunic", [("peasant_man_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_man_e2", "English Yoeman's Tunic", [("peasant_man_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_man_f2", "French Yoeman's Tunic", [("peasant_man_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_man_f1", "French Yoeman's Tunic", [("peasant_man_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["breton_peasant_man", "Tenue de paysan Breton", [("peasant_man_breton",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

["tattered_leather_armor_e2", "English Leather Armor", [("leather_armor_e1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["tattered_leather_armor_f1", "French Leather Armor", [("tattered_leather_armor_f1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["tattered_leather_armor_f2", "French Leather Armor", [("tattered_leather_armor_f2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],



["leather_vest_e2", "English Leather Vest", [("leather_vest_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["leather_vest_f1", "French Leather Vest", [("leather_vest_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["leather_vest_f2", "French Leather Vest", [("leather_vest_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

["white_gambeson_e1", "English Gambeson", [("white_gambeson_e1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["white_gambeson_f1", "French Gambeson", [("white_gambeson_f1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

["padded_cloth_e1", "English Aketon", [("padded_cloth_b_e2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["padded_cloth_f1", "French Aketon", [("padded_cloth_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["padded_cloth_b_e1", "English Padded Cloth", [("padded_cloth_b_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["padded_cloth_b_e2", "Gambison anglais", [("padded_cloth_b_e2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["padded_cloth_b_f1", "French Padded Cloth", [("padded_cloth_b_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],



["padded_jack", "Padded Jack", [("gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 415 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["padded_jack_e", "English Padded Jack", [("gambeson_e",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 415 , weight(6)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],



["leather_armor_e1", "English Padded Leather", [("leather_armor_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_armor_e2", "English Padded Leather", [("leather_armor_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_armor_f1", "French Padded Leather", [("leather_armor_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_armor_f2", "French Padded Leather", [("leather_armor_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0, 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],


["haubergeon_e1", "English Haubergeon", [("haubergeon_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],
["haubergeon_e2", "English Haubergeon", [("haubergeon_e2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],
["haubergeon_f1", "French Haubergeon", [("haubergeon_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],
["haubergeon_f2", "French Haubergeon", [("haubergeon_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],



["mail_shirtdeer", "Mail Shirt", [("mail_shirt_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
["mail_shirtgreen", "Mail Shirt", [("mail_shirt_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],
["mail_shirthre", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["surcoat_over_mail_f1", "French Surcoat over Mail", [("surcoat_over_mail_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_f2", "French Surcoat over Mail", [("surcoat_over_mail_f4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_f3", "French Surcoat over Mail", [("surcoat_over_mail_f4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_f4", "French Surcoat over Mail", [("surcoat_over_mail_f4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_brg1", "Armure de mailles et plates Bourguignonne", [("corrazina_brg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(6) ,imodbits_armor ],

["surcoat_over_mail_e1", "English Surcoat over Mail", [("surcoat_over_mail_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_e2", "English Surcoat over Mail", [("surcoat_over_mail_e4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_e3", "English Surcoat over Mail", [("surcoat_over_mail_e4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail_e4", "English Surcoat over Mail", [("surcoat_over_mail_e4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["breton_surcoat_over_mail", "Cotte de mailles Bretonne", [("surcoat_over_mail_breton",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],

["brigandine_e1", "English Brigandine", [("brigandine_e1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_e1_c", "Brigandine Anglaise", [("brigandine_e1_c",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_e2", "English Brigandine", [("brigandine_e2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_f1", "French Brigandine", [("brigandine_f1",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_f2", "French Brigandine", [("brigandine_f2",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_g", "Genoese Brigandine", [("brigandine_g",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0, 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["brigandine_sl", "Armure des SansLys", [("brigandine_sl",0)], itp_type_body_armor|itp_covers_legs, 0, 1830, weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0), imodbits_armor ],

["coat_of_plates_e1", "English Coat of Plates", [("coat_of_plates_e1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_e2", "English Coat of Plates", [("coat_of_plates_e2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_e3", "English Coat of Plates", [("coat_of_plates_e3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_f1", "French Coat of Plates", [("coat_of_plates_f1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_f2", "French Coat of Plates", [("coat_of_plates_f2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["coat_of_plates_f3", "French Coat of Plates", [("coat_of_plates_f3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


["early_transitional_teu", "Teutonic Heavy Surcoat and Plate", [("early_transitional_teu",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_hre", "Holy Roman Empire Surcoat and Plate", [("early_transitional_hre",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_green", "Green Surcoat and Plate", [("early_transitional_teu",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_horse", "French Heavy Mail and Plate", [("early_transitional_teu",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3428, weight(25)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(16)|difficulty(8), imodbits_armor ],
["early_transitional_boar", "French Heavy Mail and Plate", [("early_transitional_teu",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


["early_transitional_white", "Heavy Mail and Plate", [("early_transitional_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["early_transitional_f1", "French Heavy Mail and Plate", [("early_transitional_f1",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_f2", "French Heavy Mail and Plate", [("early_transitional_f2",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_f3", "French Heavy Mail and Plate", [("early_transitional_f3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_f4", "French Heavy Mail and Plate", [("early_transitional_f3",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["early_transitional_f5", "French Heavy Mail and Plate", [("early_transitional_f5",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e1", "English Heavy Mail and Plate", [("early_transitional_e1",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e2", "English Heavy Mail and Plate", [("early_transitional_e1",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e3", "English Heavy Mail and Plate", [("early_transitional_e1",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e4", "English Heavy Mail and Plate", [("early_transitional_e4",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e5", "English Heavy Mail and Plate", [("early_transitional_e4",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e6", "English Heavy Mail and Plate", [("early_transitional_e4",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_e7", "English Heavy Mail and Plate", [("early_transitional_e4",0)],  itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


["corrazina_red", "Corrazina", [("corrazina_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["corrazina_green", "Corrazina", [("corrazina_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["corrazina_grey", "Corrazina", [("corrazina_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
#["steel_greaves", "Corrazina", [("corrazina_grey",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
# 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["churburg_13_e", "Full Plate", [("churburg_13_e",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2828, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_armor ],
["churburg_13_brass_f", "Ornate Full Plate", [("churburg_13_brass_f",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_armor ],

["churburg_13", "Full Plate", [("churburg_13",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 2828, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_armor ],
["churburg_13_brass", "Ornate Full Plate", [("churburg_13_brass",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_armor ],
["churburg_13_mail", "Ornate Full Plate", [("churburg_13_mail",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_armor ],

["early_transitional_heraldic", "Heavy Mail and Plate", [("early_transitional_heraldic",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ,[(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_early_transitional_heraldic", ":agent_no", ":troop_no")])]],
["early_transitional_blue", "Heavy Mail and Plate", [("early_transitional_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["early_transitional_orange", "Heavy Mail and Plate", [("early_transitional_orange",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 3428 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["milanese_armour", "Milanese Armour", [("milanese_armour",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3996, weight(30)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(22)|difficulty(10), imodbits_plate ],
["gothic_armour", "Gothic Armour", [("gothic_armour",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 3796, weight(24)|abundance(100)|head_armor(8)|body_armor(50)|leg_armor(20)|difficulty(0), imodbits_plate ],



#Helmets
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0,36 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
#missing...
["nasal_helmet", "Nasal Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet", "Segmented Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettle_hat_orig", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0,240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["khergit_lady_hat", "Khergit Lady Hat", [("wimple_a",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("wimple_a",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

#helmets
#mod helmets begin

#["padded_coifpurple", "French_Padded_Coif", [("padded_coif",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["padded_coifbrown", "English_Padded_Coif", [("padded_coifbrown",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#["felt_hatred", "English_Felt_Hat", [("felt_hatred",0)], itp_merchandise| itp_type_head_armor   ,0, 4 , weight(1)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["common_hoodblue", "French_Hood", [("common_hoodblue",0)],itp_merchandise|itp_type_head_armor,0,9, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
#["common_hoodred", "English_Hood", [("common_hoodred",0)],itp_merchandise|itp_type_head_armor,0,9, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hoodblack", "Black_Hood", [("hood_a",0)],itp_merchandise|itp_type_head_armor,0,9, weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],


#["pigface_rusty", "Old_Pigface_Bascinet", [("pigface_rusty",0)], itp_merchandise| itp_type_head_armor   ,0, 158 , weight(1.25)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#["kettle_helm1", "Kettle Helm", [("kettle_helm1",0)], itp_merchandise| itp_type_head_armor   ,0, 193 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["kettle_helm2", "Mailed Kettle Helm", [("kettle_helm2",0)], itp_merchandise| itp_type_head_armor   ,0, 193 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["kettle_helm3", "Kettle Helm", [("kettle_helm3",0)], itp_merchandise| itp_type_head_armor   ,0, 193 , weight(1.5)|abundance(100)|head_armor(29)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["kettle_helm4", "Mailed Kettle Helm", [("kettle_helm4",0)], itp_merchandise| itp_type_head_armor   ,0, 193 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
#["common_helm1", "Angular Kettle Helm", [("common_helm1",0)], itp_merchandise| itp_type_head_armor   ,0, 193 , weight(1.5)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#["burgonet", "Burgonet", [("reinforcedburgonet",0)], itp_merchandise| itp_type_head_armor   ,0, 411 , weight(2)|abundance(25)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["flat_topped_helmetblue", "French_Flat_Topped_Helmet", [("flat_topped_helmetblue",0)], itp_merchandise| itp_type_head_armor   ,0, 411 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["flat_topped_helmetred", "English_Flat_Topped_Helmet", [("flat_topped_helmetred",0)], itp_merchandise| itp_type_head_armor   ,0, 411 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["sallet_full", "Simple_Sallet", [("sallet_full",0)], itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(39)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
#["all_inquisitorhelm", "Jousting_Helmet", [("all_inquisitorhelm",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["french_joustinghelmblackhorns", "French_Horned_Jousting_Helmet", [("tilting_helm_horns_f",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["french_joustinghelmcrow", "French_Eagle_Jousting_Helmet", [("tilting_helm_crow_f",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["french_joustinghelmcrowwithwings", "French_Crow_Jousting_Helmet", [("tilting_helm_swan_f",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["english_inquisitorcrowfighterhelm", "English_Wagle_Jousting_Helmet", [("tilting_helm_crow",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["english_joustinghelmblackhorns", "English_Horned_Jousting_Helmet", [("tilting_helm_horns",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["english_joustinghelmcrow", "English_Eagle_Jousting_Helmet", [("tilting_helm_crow",0)],     itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["english_joustinghelmcrowwithwings", "English_Crow_Jousting_Helmet", [("tilting_helm_swan",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmetgrey", "Barbute", [("barbuta2",0)],   itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmetgolden", "Barbute", [("barbuta1",0)],  itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

#["all_salletb", "Opened_Sallet", [("all_salletb",0)], itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["all_opensallet", "Opened_Sallet", [("all_opensallet",0)], itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["all_sallet", "Sallet", [("all_sallet",0)], itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["sallet_bevor", "Sallet_with_Bevor", [("sallet_bevor",0)], itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["french_opengriffinsallet", "French_Opened_Griffin_Sallet", [("french_opengriffinsallet",0)],   itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["french_griffinsallet", "French_Griffin_Sallet", [("french_griffinsallet",0)],   itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["french_salletd", "French_Eagle_Sallet", [("french_salletd",0)],   itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
#["english_salletd", "English_Eagle_Sallet", [("english_salletd",0)],   itp_type_head_armor   ,0, 638 , weight(2.75)|abundance(100)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

#["pigface_bascinet", "Pigface_Bascinet", [("pigface_bascinet_royal",0)], itp_merchandise| itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["klappvisor", "Klappvisor_Bascinet", [("klappvisor",0)], itp_merchandise| itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

#["all_pigface", "Hounskull_Bascinet", [("all_pigface",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["all_barbutecloseddark", "Closed_Barbute", [("all_barbutecloseddark",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["french_barbutclosedcrow", "French_Crow_Barbute", [("french_barbutclosedcrow",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["french_barbuteclosedeagle", "French_Eagle_Barbute", [("french_barbuteclosedeagle",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["english_barbutclosedcrow", "English_Crow_Barbute", [("english_barbutclosedcrow",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["english_barbuteclosedeagle", "English_Eagle_Barbute", [("english_barbuteclosedeagle",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["all_pigfacedragon", "Dragon_Hounskull_Bascinet", [("all_pigfacedragon",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["french_barbuteclosehorse", "French_Dark_Barbute", [("french_barbuteclosehorse",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["french_helmdarkhorse", "French_Pegasus_Barbute", [("french_helmdarkhorse",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["english_barbuteclosehorse", "English_Dark_Barbute", [("english_barbuteclosehorse",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
#["english_helmdarkhorse", "English_Pegasus_Barbute", [("english_helmdarkhorse",0)],   itp_type_head_armor   ,0, 750 , weight(2.75)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

#mod helmet end



#HYW Helms
["hood_f1", "Hood", [("hood_f1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["woolen_cap_f1", "Woolen Cap", [("woolen_cap_f1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["coif_new_f1", "Padded Coif", [("coif_new_f1",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_f1", "Felt Hat", [("felt_hat_f1",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["hood_e1", "Hood", [("hood_e1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["woolen_cap_e1", "Woolen Cap", [("woolen_cap_e1",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["coif_new_e1", "Padded Coif", [("coif_new_e1",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_e1", "Felt Hat", [("felt_hat_e1",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["mail_coif_full", "Full Mail Coif", [("mail_coif_full",0)], itp_merchandise| itp_type_head_armor   ,0, 271 , weight(1.25)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],

["chapel_de_fer", "chapel de fer", [("prato_chapel_de_fer",0)], itp_merchandise| itp_type_head_armor,0, 240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["kettle_hat", "Kettle Hat", [("prato_chapel_de_fer",0)], itp_merchandise| itp_type_head_armor,0, 240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettlehat1", "Kettle Hat", [("kettlehat1",0)], itp_merchandise| itp_type_head_armor,0,280 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettlehat1_painted", "Kettle Hat", [("kettlehat1_painted",0)], itp_merchandise| itp_type_head_armor,0,280 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettlehat2", "Square Kettle Hat", [("kettlehat2",0)], itp_merchandise| itp_type_head_armor,0, 280 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettlehat2_painted", "Square Kettle Hat", [("kettlehat2_painted",0)], itp_merchandise| itp_type_head_armor,0, 280 , weight(1.75)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["byzantion", "Byzantine Kettle Hat", [("byzantion",0)], itp_merchandise| itp_type_head_armor,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["byzantion_painted", "Byzantine Kettle Hat", [("byzantion_painted",0)], itp_merchandise| itp_type_head_armor,0, 380 , weight(1.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],


["oniontop_bascinet", "Onion-top Bascinet", [("onion-top_bascinet",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],


["great_helm_joust", "Great_Helm", [("great_helm_joust",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helm_grif", "Great_Helm", [("great_helm_grif",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["tilting_helm_horns", "Tilting_Helmet", [("tilting_helm_horns",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helmet", "Tilting_Helmet", [("tilting_helmet",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_crow", "Tilting_Helmet", [("tilting_helm_crow",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_unicorn", "Tilting_Helmet", [("tilting_helm_unicorn",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_swan", "Tilting_Helmet", [("tilting_helm_swan",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helm_wings_teut", "Winged Great Helmet", [("great_helm_wings_teut",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["tilting_helm_horns_f", "Tilting_Helmet", [("tilting_helm_horns_f",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helm_joust_f", "Great_Helm", [("great_helm_joust_f",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helm_grif_f", "Great_Helm", [("great_helm_grif_f",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["tilting_helm_crow_f", "Tilting_Helmet", [("tilting_helm_crow_f",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_unicorn_f", "Tilting_Helmet", [("tilting_helm_unicorn_f",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_swan_f", "Tilting_Helmet", [("tilting_helm_swan_f",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["tilting_helm_unicorn_tall_f", "Tilting_Helmet", [("tilting_helm_unicorn_tall_f",0)], itp_merchandise|itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],

["greathelm1", "Great Helmet", [("greathelm1",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["greathelmwhat", "Great Helmet", [("greathelmwhat",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["sugarloaf", "Sugarloaf Greathelm", [("sugarloaf",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(3.25)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["klappvisier", "Klappvisier", [("klappvisier",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["pigface_klappvisor", "Pigface Bascinet", [("pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["hounskull", "Hounskull Bascinet", [("hounskull",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["pigface_klappvisor_open", "Pigface Bascinet", [("pigface_klappvisor_open",0)], itp_merchandise|itp_type_head_armor   ,0, 1180 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["visored_sallet", "Visored Sallet", [("visored_salet",0)], itp_merchandise| itp_type_head_armor   ,0, 638 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["visored_sallet_coif", "Visored Sallet with Coif", [("visored_salet_coif",0)], itp_merchandise| itp_type_head_armor   ,0, 738 , weight(2.25)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["open_sallet", "Open Sallet", [("open_salet",0)], itp_merchandise| itp_type_head_armor   ,0, 538 , weight(1.75)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["open_sallet_coif", "Open Sallet with Coif", [("open_salet_coif",0)], itp_type_head_armor   ,0, 638 , weight(2)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#WEAPONS

#WEAPONS

#mod weapons begin

["1mace",         "Winged Mace", [("1mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 122 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(59)|swing_damage(39 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["2mace",         "Studded Mace", [("2mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 122 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(59)|swing_damage(19 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["4mace",         "Spiked War Mace", [("3mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 122 , weight(3.5)|difficulty(0)|spd_rtng(99) | weapon_length(62)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 180 , weight(3.5)|difficulty(0)|spd_rtng(95) | weapon_length(90)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["1club",      "Studded Club", [("1club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 180 , weight(3.5)|difficulty(0)|spd_rtng(95) | weapon_length(90)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("iron_hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["1hammer", "Military Hammer", [("1hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["2hammer", "Spiked Military Hammer", [("2hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_longsword|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(33 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],
["3hammer", "Military Hammer", [("3hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["4hammer", "War Hammer", [("4hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["5hammer", "Military Hammer", [("5hammer",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 317 , weight(4)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["2polehammer", "Iron Warhammer", [("2polehammer",0)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_two_handed, itc_nodachi|itcf_carry_sword_back, 270 , weight(7)|difficulty(14)|spd_rtng(85) | weapon_length(120)|swing_damage(25 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["3mace",         "Spiked War Mace", [("3mace",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 130 , weight(5.5)|difficulty(13)|spd_rtng(75) | weapon_length(98)|swing_damage(25 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

["hersir", "Hersir", [("hersir",0),("sword_viking_c_scabbard ", ixmesh_carry)],              itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 165 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(25 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
["huskarl", "Huskarl", [("huskarl",0),("sword_viking_c_long_scabbard ", ixmesh_carry)],      itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 170 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["clontarf", "Clontarf", [("clontarf",0),("sword_viking_c_long_scabbard ", ixmesh_carry)],   itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 180 , weight(2)  |difficulty(0)|spd_rtng(97) | weapon_length(98)|swing_damage(26 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
["jarl", "Jarl", [("jarl",0),("sword_viking_a_scabbard", ixmesh_carry)],                     itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 210 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(101)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["gotland", "Gotland", [("gotland",0),("sword_viking_a_long_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 450 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(101) | weapon_length(102)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["berserkr",         "Berserkr", [("berserkr",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary,  itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 185 , weight(2.5)|difficulty(8)|spd_rtng(97) | weapon_length(80)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],

["regent", "Regent", [("regent",0),("bastard_sword_a_scabbard", ixmesh_carry)],          itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 240 , weight(2.25)|difficulty(9)|spd_rtng(100) | weapon_length(116)|swing_damage(34 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["mercenary", "Mercenary", [("mercenary",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(100) | weapon_length(120)|swing_damage(30 , cut) | thrust_damage(24 ,  pierce),imodbits_sword ],
["castellan", "Castellan", [("castellan",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 355 , weight(2.75)|difficulty(9)|spd_rtng(99) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["sempach", "Sempach", [("sempach",0),("bastard_sword_a_scabbard", ixmesh_carry)],       itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 350 , weight(2)|difficulty(9)|spd_rtng(99) | weapon_length(120)|swing_damage(32 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
["talhoffer", "Talhoffer", [("talhoffer",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 400 , weight(2.25)|abundance(70)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(35 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
["agincourt", "Agincourt", [("agincourt",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 500 , weight(2.25)|difficulty(9)|spd_rtng(100) | weapon_length(122)|swing_damage(38 , cut) | thrust_damage(36 ,  pierce),imodbits_sword ],
["constable", "Connstable", [("constable",0),("bastard_sword_a_scabbard", ixmesh_carry)],itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 600 , weight(2.25)|difficulty(9)|spd_rtng(100) | weapon_length(125)|swing_damage(36 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["steward", "Steward", [("steward",0),("bastard_sword_b_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 470, weight(3)|difficulty(11)|spd_rtng(93)|weapon_length(110)|swing_damage(34,cut)|thrust_damage(27,pierce), imodbits_sword ],
["baron", "Baron", [("baron",0)],                                                   itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 524 , weight(3)|difficulty(11)|spd_rtng(93) | weapon_length(130)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword ],
["crecy", "Crecy", [("crecy",0)],                                                   itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|difficulty(11)|spd_rtng(97) | weapon_length(130)|swing_damage(36 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],
["landgraf", "Landgraf", [("duke",0)],                                              itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 700 , weight(3.5)|difficulty(11)|spd_rtng(91) | weapon_length(130)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["duke", "Duke", [("landgraf",0)],                                                  itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1000, weight(3)|difficulty(12)|spd_rtng(95) | weapon_length(135)|swing_damage(40 , cut) | thrust_damage(30 ,  pierce),imodbits_sword ],
["count", "Count", [("count",0)],                                                   itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 430 , weight(3)|difficulty(11)|spd_rtng(92) | weapon_length(126)|swing_damage(33 , cut) | thrust_damage(26 ,  pierce),imodbits_sword ],

["gaddhjalt",      "Gaddhjalt", [("gaddhjalt",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 160 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["ritter",         "Ritter", [("ritter",0),("sword_medieval_c_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 160 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["reeve",         "Reeve", [("reeve",0),("sword_medieval_a_scabbard", ixmesh_carry)],          itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 175 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(101)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["squire",         "Squire", [("squire",0),("sword_medieval_c_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 195 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["laird",         "Laird", [("laird",0),("sword_medieval_a_scabbard", ixmesh_carry)],          itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 225 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(25 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["caithness",   "Caithness", [("caithness",0),("sword_medieval_c_scabbard", ixmesh_carry)],    itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 253 , weight(2)  |difficulty(0)|spd_rtng(98) | weapon_length(102)|swing_damage(27 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["templar",         "Templar",[("templar",0),("sword_medieval_c_scabbard",ixmesh_carry)],      itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 250 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["bayeux",         "Bayeux", [("bayeux",0),("sword_medieval_a_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 220 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(28 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["hospitaller", "Hospitaller", [("hospitaller",0),("sword_medieval_c_scabbard",  ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 230 , weight(1.75)|difficulty(0)|spd_rtng(99) | weapon_length(104)|swing_damage(25 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["senlac",         "Senlac", [("senlac",0),("sword_medieval_c_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 214 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(25 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["knight",         "Knight", [("knight",0),("sword_medieval_c_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 250 , weight(1.5)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(29 , cut) | thrust_damage(26 ,  pierce),imodbits_sword ],
["norman",         "Norman", [("norman",0),("sword_medieval_a_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 230 , weight(1.5)|abundance(25)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(28 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
["poitiers",         "Poitiers", [("poitiers",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 470 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(102)|swing_damage(27 , cut) | thrust_damage(24 ,  pierce),imodbits_sword ],
["prince",         "Prince", [("prince",0),("sword_medieval_c_scabbard", ixmesh_carry)],       itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 550 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(107)|swing_damage(30 , cut) | thrust_damage(25 ,  pierce),imodbits_sword ],
["sovereign",         "Sovereign", [("sovereign",0)],                                          itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 450 , weight(1.25)|abundance(50)|difficulty(9)|spd_rtng(106) | weapon_length(62)|swing_damage(23 , cut) | thrust_damage(30 ,  pierce),imodbits_sword ],


["great_lance_2", "Grande lance", [("heavy_lance",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(55)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(28,pierce), imodbits_polearm ],

["jousting_lanceblueyellow", "French_Jousting_Lance", [("jousting_lanceblueyellow",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["jousting_lancebluewhite", "French_Jousting_Lance", [("jousting_lancebluewhite",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["jousting_lanceredyellow", "English_Jousting_Lance", [("jousting_lanceredyellow",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["jousting_lanceredwhite", "English_Jousting_Lance", [("jousting_lanceredwhite",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["jousting_lance_orig", "Jousting_Lance", [("joust_of_peace",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(61)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["great_lanceblueyellow", "French_Great_Lance", [("greatlance01f",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["great_lancebluewhite", "French_Great_Lance", [("greatlance02f",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["great_lanceredyellow", "English_Great_Lance", [("greatlance01e",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["great_lanceredwhite", "English_Great_Lance", [("greatlance02e",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["banner_kite_plain_diamonds", "French_Banner", [("banner_kite_plain_diamonds",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_kite_plain_lys", "French_Banner", [("banner_kite_plain_lys",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_kite_plain_ermine", "French_Banner", [("banner_kite_plain_ermine",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_blue", "French_Banner", [("banner_war_blue",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_horses", "French_Banner", [("banner_war_horses",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_cross", "French_Banner", [("banner_war_cross",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_eagle", "French_Banner", [("banner_war_eagle",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_heraldric_lys", "French_Banner", [("banner_heraldric_lys",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_heraldric_ermine", "French_Banner", [("banner_heraldric_ermine",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_kite_metal_rose", "English_Banner", [("banner_kite_metal_rose",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_kite_metal_squares", "English_Banner", [("banner_kite_metal_squares",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_kite_plain_cross", "English_Banner", [("banner_kite_plain_cross",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_red", "English_Banner", [("banner_war_red",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_trees", "English_Banner", [("banner_war_trees",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_flowers", "English_Banner", [("banner_war_flowers",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_war_wales", "English_Banner", [("banner_war_wales",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_heraldric_lions", "English_Banner", [("banner_heraldric_lions",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["banner_heraldric_stripes", "English_Banner", [("banner_heraldric_stripes",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["breton_lance", "Lance de Chevalier", [("greatlance_hyw",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 120, weight(5)|difficulty(0)|spd_rtng(65)|weapon_length(215)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],

# ["p_jousting_lanceblueyellow", "French_Jousting_Lance", [("jousting_lanceblueyellow",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 83 , weight(5)|difficulty(0)|spd_rtng(68) | weapon_length(218)|swing_damage(0 , cut) | thrust_damage(14 ,  blunt),imodbits_polearm ],
# ["p_jousting_lancebluewhite",  "French_Jousting_Lance",  [("jousting_lancebluewhite",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 83 , weight(5)|difficulty(0)|spd_rtng(68) | weapon_length(218)|swing_damage(0 , cut) | thrust_damage(14 ,  blunt),imodbits_polearm ],
# ["p_jousting_lanceredyellow",  "English_Jousting_Lance", [("jousting_lanceredyellow",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 83 , weight(5)|difficulty(0)|spd_rtng(68) | weapon_length(218)|swing_damage(0 , cut) | thrust_damage(14 ,  blunt),imodbits_polearm ],
# ["p_jousting_lanceredwhite",  "English_Jousting_Lance",   [("jousting_lanceredwhite",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 83 , weight(5)|difficulty(0)|spd_rtng(68) | weapon_length(218)|swing_damage(0 , cut) | thrust_damage(14 ,  blunt),imodbits_polearm ],
# ["p_great_lanceblueyellow",         "French_Great_Lance", [("greatlance01f",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_great_lancebluewhite",          "French_Great_Lance",  [("greatlance02f",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_great_lanceredyellow",          "English_Great_Lance", [("greatlance01e",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_great_lanceredwhite",           "English_Great_Lance",  [("greatlance02e",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_plain_diamonds",         "French_Banner", [("banner_kite_plain_diamonds",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_plain_lys",              "French_Banner",      [("banner_kite_plain_lys",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_plain_ermine",           "French_Banner",   [("banner_kite_plain_ermine",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_blue",                    "French_Banner",            [("banner_war_blue",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_horses",                  "French_Banner",          [("banner_war_horses",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_cross",                   "French_Banner",           [("banner_war_cross",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_eagle",                   "French_Banner",           [("banner_war_eagle",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_heraldric_lys",               "French_Banner",       [("banner_heraldric_lys",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_heraldric_ermine",            "French_Banner",    [("banner_heraldric_ermine",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_metal_rose",         "English_Banner",    [("banner_kite_metal_rose",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_metal_squares",      "English_Banner", [("banner_kite_metal_squares",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_kite_plain_cross",        "English_Banner",   [("banner_kite_plain_cross",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_red",                 "English_Banner",            [("banner_war_red",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_trees",               "English_Banner",          [("banner_war_trees",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_flowers",             "English_Banner",        [("banner_war_flowers",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_war_wales",               "English_Banner",          [("banner_war_wales",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_heraldric_lions",         "English_Banner",    [("banner_heraldric_lions",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
# ["p_banner_heraldric_stripes",       "English_Banner",  [("banner_heraldric_stripes",0)], itp_type_polearm|itp_merchandise| itp_offset_lance|itp_primary|itp_penalty_with_shield, itc_greatlance, 120 , weight(5)|difficulty(0)|spd_rtng(65) | weapon_length(215)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],

["glaive_dupe_a", "Glaive", [("glaive",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 352, weight(4.5)|difficulty(0)|spd_rtng(81)|weapon_length(157)|swing_damage(35,cut)|thrust_damage(29,pierce), imodbits_polearm ],
["glaive_dupe_b", "Glaive", [("glaive",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 220, weight(4.5)|difficulty(0)|spd_rtng(81)|weapon_length(157)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["1glaive", "Glaive", [("1glaive",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 272, weight(4.5)|difficulty(0)|spd_rtng(81)|weapon_length(195)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["2glaive", "Glaive", [("2glaive",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 280, weight(4.5)|difficulty(0)|spd_rtng(81)|weapon_length(200)|swing_damage(39,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["3glaive", "Glaive", [("3glaive",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 280, weight(4.5)|difficulty(0)|spd_rtng(81)|weapon_length(200)|swing_damage(38,cut)|thrust_damage(32,pierce), imodbits_polearm ],

["polearm", "Polearm", [("polearm",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(180)|swing_damage(39,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["poleaxe_orig", "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(180)|swing_damage(39,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["1halberd", "Halberd", [("1halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(83)|weapon_length(190)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["2halberd", "Halberd", [("2halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(83)|weapon_length(194)|swing_damage(39,cut)|thrust_damage(36,pierce), imodbits_polearm ],
["3halberd", "Halberd", [("3halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(82)|weapon_length(208)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["4halberd", "Halberd", [("4halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(80)|weapon_length(243)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["7halberd", "Halberd", [("7halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(86)|weapon_length(170)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["6halberd", "Halberd", [("6halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(180)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["5halberd", "Halberd", [("5halberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 344, weight(6.5)|difficulty(0)|spd_rtng(81)|weapon_length(211)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["bill", "Guisarme", [("bill",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 358, weight(6.5)|difficulty(0)|spd_rtng(83)|weapon_length(209)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["polehammer_orig", "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 206, weight(7)|difficulty(14)|spd_rtng(89)|weapon_length(130)|swing_damage(30,blunt)|thrust_damage(28,blunt), imodbits_polearm ],
["1polehammer", "Polehammer", [("1polehammer",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 206, weight(7)|difficulty(14)|spd_rtng(86)|weapon_length(150)|swing_damage(38,blunt)|thrust_damage(29,pierce), imodbits_polearm ],
["3polehammer", "Polehammer", [("3polehammer",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 220, weight(7)|difficulty(14)|spd_rtng(82)|weapon_length(150)|swing_damage(30,blunt)|thrust_damage(29,pierce), imodbits_polearm ],
["mallet",         "Mallet", [("mallet",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(14)|spd_rtng(82) | weapon_length(130)|swing_damage(25 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],

["pop_bill", "Guisarme", [("bill_1",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(85)|weapon_length(160)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["pop_halberd", "Halberd", [("halberd_6",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(86)|weapon_length(160)|swing_damage(39,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["lui_vaegirhallberd", "Halberd", [("lui_vaegirhallberd",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(84)|weapon_length(160)|swing_damage(34,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["jam_poleaxe", "Poleaxe", [("jam_poleaxe",0)], itp_type_polearm|itp_merchandise|itp_two_handed|itp_primary|itp_cant_use_on_horseback|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(165)|swing_damage(44,cut)|thrust_damage(33,pierce), imodbits_polearm ],
["banner_jhoan", "Banniere de Jeanne d'arc", [("banner_jhoan",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 336, weight(6.5)|difficulty(0)|spd_rtng(89)|weapon_length(165)|swing_damage(54,cut)|thrust_damage(59,pierce), imodbits_polearm ],




["knighthammerbastard",   "Warhammer", [("lui_knighthammerbastard",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(14)|spd_rtng(87) | weapon_length(130)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["manhuntermaul",   "Warhammer", [("lui_manhuntermaul",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(14)|spd_rtng(87) | weapon_length(120)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["empirewarhammer",   "Longhafted Warhammer", [("lui_empirewarhammer",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(13)|spd_rtng(87) | weapon_length(70)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["empirehammer",   "Warhammer", [("lui_empirehammer",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(13)|spd_rtng(87) | weapon_length(110)|swing_damage(41 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["inquisitionhammer",   "Longhafted Warhammer", [("lui_inquisitionhammer",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(13)|spd_rtng(87) | weapon_length(115)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["knighthammer",   "Warhammer", [("lui_knighthammer",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(13)|spd_rtng(87) | weapon_length(70)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["knighthammerempire",   "Polehammer", [("lui_knighthammerempire",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(14)|spd_rtng(87) | weapon_length(120)|swing_damage(40 , blunt) | thrust_damage(19 ,  pierce),imodbits_polearm ],
["manhuntermace",   "Warhammer", [("lui_manhuntermace",0)], itp_type_two_handed_wpn|itp_merchandise| itp_offset_lance|itp_primary|itp_two_handed, itc_staff|itcf_carry_spear, 206 , weight(7)|difficulty(13)|spd_rtng(83) | weapon_length(110)|swing_damage(40 , blunt) | thrust_damage(15 ,  pierce),imodbits_polearm ],


["lui_battleaxetwoh",   "Battle Axe", [("lui_battleaxetwoh",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(110)|swing_damage(35 , cut) | thrust_damage(10 ,  pierce),imodbits_axe ],
["lui_battleaxeb",   "Battle Axe", [("lui_battleaxeb",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(105)|swing_damage(36 , cut) | thrust_damage(27 ,  pierce),imodbits_axe ],
["lui_battleaxenew",   "Battle Axe", [("lui_battleaxenew",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(110)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_axe ],
["lui_battleaxenewb",   "Battle Axe", [("lui_battleaxenewb",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(115)|swing_damage(38 , cut) | thrust_damage(27 ,  pierce),imodbits_axe ],
["lui_battleaxea",   "Battle Axe", [("lui_battleaxea",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(110)|swing_damage(39 , cut) | thrust_damage(27 ,  pierce),imodbits_axe ],
["lui_knightbattleaxenew",   "Battle Axe", [("lui_knightbattleaxenew",0)], itp_type_two_handed_wpn|itp_merchandise|itp_always_loot| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_axe_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(92) | weapon_length(110)|swing_damage(39 , cut) | thrust_damage(27 ,  pierce),imodbits_axe ],


["lui_knightaxeonehb", "Knight's Battle Axe", [("lui_knightaxeonehb",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 187, weight(1.7)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(36,cut)|thrust_damage(0,pierce), imodbits_axe ],
["lui_knightaxeonehc", "Knight's Battle Axe", [("lui_knightaxeonehc",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 187, weight(1.7)|difficulty(9)|spd_rtng(98)|weapon_length(100)|swing_damage(35,cut)|thrust_damage(0,pierce), imodbits_axe ],
["lui_knightaxeoneh", "Knight's Battle Axe", [("lui_baronaxeoneh",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,187 , weight(1.6)|difficulty(9)|spd_rtng(100) | weapon_length(95)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["lui_knightaxeonehd", "Knight's Battle Axe", [("lui_knightaxeonehd",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,187 , weight(1.8)|difficulty(9)|spd_rtng(93) | weapon_length(95)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["lui_knightaxeonehe", "Knight's Battle Axe", [("lui_baronaxeoneh",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,187 , weight(2.0)|difficulty(9)|spd_rtng(94) | weapon_length(100)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["lui_knightaxetwoha_a", "Knight's Battle Axe", [("lui_baronaxeoneh",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,187 , weight(2.1)|difficulty(9)|spd_rtng(90) | weapon_length(100)|swing_damage(39 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["lui_knightaxetwoha",         "Battle_Axe", [("lui_knightaxetwoha",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,446 , weight(4.5)|difficulty(10)|spd_rtng(93) | weapon_length(105)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["lui_knightaxetwohb",         "Battle_Axe", [("lui_knightaxetwohb",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,446 , weight(4.5)|difficulty(10)|spd_rtng(90) | weapon_length(110)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["lui_smallhallberdb", "Shortened Halberd", [("lui_smallhallberdb",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 145, weight(2.5)|difficulty(11)|spd_rtng(94)|weapon_length(150)|swing_damage(44,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["lui_smallhallberda", "Shortened Halberd", [("lui_smallhallberda",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 145, weight(2.5)|difficulty(11)|spd_rtng(94)|weapon_length(150)|swing_damage(44,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["jam_scorpion", "Shortened Halberd", [("jam_scorpion",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 145, weight(2.5)|difficulty(11)|spd_rtng(93)|weapon_length(155)|swing_damage(43,cut)|thrust_damage(45,pierce), imodbits_polearm ],


#OLD WEAPONS END
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace", "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_scimitar|itcf_carry_mace_left_hip, 122, weight(3.5)|difficulty(0)|spd_rtng(103)|weapon_length(70)|swing_damage(29,blunt)|thrust_damage(0,pierce), imodbits_mace ],
["spiked_mace_new",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer_orig", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe", "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 27, weight(3)|difficulty(0)|spd_rtng(99)|weapon_length(70)|swing_damage(32,pierce)|thrust_damage(0,pierce), imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,83 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itc_scimitar|itcf_carry_axe_left_hip, 108, weight(1.0)|difficulty(0)|spd_rtng(98)|weapon_length(70)|swing_damage(36,pierce)|thrust_damage(0,pierce), imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,280 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_axe_left_hip,305 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,105 , weight(2.5)|difficulty(8)|spd_rtng(96) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Eastern Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Eastern Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,218 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Eastern Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Eastern Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,420 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["great_sword", "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 423, weight(2.75)|difficulty(10)|spd_rtng(95)|weapon_length(125)|swing_damage(39,cut)|thrust_damage(31,pierce), imodbits_sword_high ],
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 524 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,13 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge_0", "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 129, weight(4.5)|difficulty(8)|spd_rtng(87)|weapon_length(119)|swing_damage(46,cut)|thrust_damage(0,pierce), imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 670 , weight(2.75)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
["darkknightsword", "Flamberge a pointes", [("darkknightsword",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1832, weight(3.55)|difficulty(14)|spd_rtng(89)|weapon_length(150)|swing_damage(44,cut)|thrust_damage(26,pierce), imodbits_sword_high ],
["estoc", "Claymore de Chevalier", [("estoc",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1932, weight(3.10)|difficulty(12)|spd_rtng(95)|weapon_length(140)|swing_damage(43,cut)|thrust_damage(30,pierce), imodbits_sword_high ],
["realclaymore", "Claymore lourde", [("realclaymore",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 2020, weight(3.85)|difficulty(15)|spd_rtng(85)|weapon_length(142)|swing_damage(44,cut)|thrust_damage(24,pierce), imodbits_sword_high ],
["realespadon", "Espadon lourd", [("realespadon",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1934, weight(2.95)|difficulty(15)|spd_rtng(90)|weapon_length(121)|swing_damage(46,cut)|thrust_damage(40,pierce), imodbits_sword_high ],
["realespadona", "Espadon de Chevalier", [("realespadona",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 2140, weight(2.95)|difficulty(10)|spd_rtng(94)|weapon_length(121)|swing_damage(43,cut)|thrust_damage(39,pierce), imodbits_sword_high ],
["realflambergeb", "Flamberge lourde", [("realflambergeb",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 2530, weight(2.95)|difficulty(10)|spd_rtng(90)|weapon_length(122)|swing_damage(47,cut)|thrust_damage(27,pierce), imodbits_sword_high ],


["khergit_sword_two_handed_a", "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 523, weight(2.75)|difficulty(10)|spd_rtng(96)|weapon_length(120)|swing_damage(40,cut)|thrust_damage(0,pierce), imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 920 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 640 , weight(2.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 193 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 263 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 220 , weight(1.0)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],


["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 294, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(101)|swing_damage(35,cut)|thrust_damage(31,pierce), imodbits_sword_high ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 526, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(105)|swing_damage(37,cut)|thrust_damage(32,pierce), imodbits_sword_high ],
["bastard_sword_c", "épée batarde de guerre", [("bastard_sword_c",0),("bastard_sword_c_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 526, weight(2.25)|difficulty(9)|spd_rtng(97)|weapon_length(105)|swing_damage(37,cut)|thrust_damage(35,pierce), imodbits_sword_high ],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


["two_handed_axe", "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 90, weight(4.5)|difficulty(10)|spd_rtng(96)|weapon_length(90)|swing_damage(44,cut)|thrust_damage(0,pierce), imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 152 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge", "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 228, weight(4.5)|difficulty(10)|spd_rtng(92)|weapon_length(100)|swing_damage(46,cut)|thrust_damage(0,pierce), imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 316 , weight(4.5)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe", "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 390, weight(4.5)|difficulty(10)|spd_rtng(93)|weapon_length(120)|swing_damage(46,cut)|thrust_damage(28,blunt), imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 390 , weight(4.5)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe_b", "Long War Axe", [("long_axe_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 510, weight(4.5)|difficulty(10)|spd_rtng(92)|weapon_length(125)|swing_damage(50,cut)|thrust_damage(28,blunt), imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 510 , weight(4.5)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe_c", "Great Long Axe", [("long_axe_c",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee, itc_staff|itcf_carry_axe_back, 660, weight(4.5)|difficulty(10)|spd_rtng(91)|weapon_length(127)|swing_damage(47,cut)|thrust_damage(29,blunt), imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 660 , weight(4.5)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 291 , weight(4.5)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 617 , weight(4.5)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["voulge", "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_staff, 120, weight(3.0)|difficulty(10)|spd_rtng(88)|weapon_length(175)|swing_damage(42,cut)|thrust_damage(18,pierce), imodbits_axe ],
["long_bardiche", "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_staff, 390, weight(4.5)|difficulty(11)|spd_rtng(89)|weapon_length(140)|swing_damage(48,cut)|thrust_damage(27,pierce), imodbits_axe ],
["great_long_bardiche", "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_staff, 660, weight(5.0)|difficulty(12)|spd_rtng(88)|weapon_length(155)|swing_damage(50,cut)|thrust_damage(27,pierce), imodbits_axe ],

["hafted_blade_b", "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_guandao|itcf_carry_spear, 185, weight(2.75)|difficulty(0)|spd_rtng(95)|weapon_length(135)|swing_damage(37,cut)|thrust_damage(30,pierce), imodbits_polearm ],
["hafted_blade_a", "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itc_guandao|itcf_carry_spear, 350, weight(3.25)|difficulty(0)|spd_rtng(93)|weapon_length(153)|swing_damage(39,cut)|thrust_damage(29,pierce), imodbits_polearm ],

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back, 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 152 , weight(1.5)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 243 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 480 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 550 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],
#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 147 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 276 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 105 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 191 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 294 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 384 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],



["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 45 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(32 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 152 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 212 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(35 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# Goedendag
["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back, 200 , weight(2.5)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back, 264 , weight(2.5)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace", "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_can_knock_down, itc_staff|itcf_carry_axe_back, 324, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(133)|swing_damage(28,blunt)|thrust_damage(23,blunt), imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back, 310 , weight(2.5)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],


["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 250 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_two_handed_axe_a",         "Eastern Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 350 , weight(3.0)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Eastern War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 280 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe", "Scythe", [("scythe",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_staff|itcf_carry_spear, 43, weight(2)|difficulty(0)|spd_rtng(97)|weapon_length(182)|swing_damage(30,cut)|thrust_damage(24,pierce), imodbits_polearm ],
["pitch_fork", "Pitch Fork", [("trident",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance, itc_spear_upstab, 19, weight(1.5)|difficulty(0)|spd_rtng(87)|weapon_length(154)|swing_damage(16,blunt)|thrust_damage(22,pierce), imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear_upstab, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear_upstab, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab|itcf_carry_spear,76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 158, weight(5)|difficulty(0)|spd_rtng(61)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(25,pierce), imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive", "Glaive", [("glaive_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 352, weight(4.5)|difficulty(0)|spd_rtng(90)|weapon_length(157)|swing_damage(39,cut)|thrust_damage(25,pierce), imodbits_polearm ],
["poleaxe", "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff, 384, weight(4.5)|difficulty(13)|spd_rtng(77)|weapon_length(180)|swing_damage(50,cut)|thrust_damage(19,blunt), imodbits_polearm ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff, 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back, 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back, 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back, 202 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 53 , weight(2.0)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(19 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear, 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 80 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm ],




["war_spear", "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 140, weight(2.5)|difficulty(0)|spd_rtng(95)|weapon_length(150)|swing_damage(20,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 155 , weight(2.5)|difficulty(10)|spd_rtng(89) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear, 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance", "Heavy Lance", [("spear_f_2-9m",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_offset_lance|itp_couchable, itc_cutting_spear, 360, weight(2.75)|difficulty(10)|spd_rtng(75)|weapon_length(190)|swing_damage(16,blunt)|thrust_damage(32,pierce), imodbits_polearm ],
["great_lance", "Great Lance", [("heavy_lance",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(5)|difficulty(11)|spd_rtng(55)|weapon_length(240)|swing_damage(0,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear, 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear, 205 , weight(3.5)|difficulty(11)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(39,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 345 , weight(2.25)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 385 , weight(2.25)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

["bec_de_corbin_a", "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_cutting_spear|itcf_carry_spear, 125, weight(3.0)|difficulty(0)|spd_rtng(81)|weapon_length(120)|swing_damage(43,blunt)|thrust_damage(38,pierce), imodbits_polearm ],

#########HYW Begin Weapons

["bardiche_1",     "Bardiche", [("bardiche_1",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 591 , weight(4.5)|difficulty(10)|spd_rtng(89) | weapon_length(103)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bardiche_2",     "Bardiche", [("bardiche_2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 551 , weight(3.5)|difficulty(10)|spd_rtng(92) | weapon_length(106)|swing_damage(48 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bardiche_3",     "Bardiche", [("bardiche_3",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 651 , weight(4.8)|difficulty(11)|spd_rtng(87) | weapon_length(110)|swing_damage(52 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bardiche_4",     "Bardiche", [("bardiche_4",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 521 , weight(4.4)|difficulty(10)|spd_rtng(89) | weapon_length(106)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["bardiche_5",     "Bardiche", [("bardiche_5",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back, 531 , weight(4.3)|difficulty(10)|spd_rtng(91) | weapon_length(106)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["halberd_1", "Halberd", [("halberd_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 552, weight(4.5)|difficulty(10)|spd_rtng(91)|weapon_length(170)|swing_damage(40,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["halberd_2", "Halberd", [("halberd_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 562, weight(4.6)|difficulty(11)|spd_rtng(86)|weapon_length(191)|swing_damage(32,cut)|thrust_damage(28,pierce), imodbits_polearm ],
["halberd_3", "Halberd", [("halberd_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 592, weight(4.3)|difficulty(10)|spd_rtng(89)|weapon_length(180)|swing_damage(41,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["halberd_4", "Halberd", [("halberd_4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 572, weight(4.4)|difficulty(11)|spd_rtng(88)|weapon_length(180)|swing_damage(35,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["halberd_5", "Halberd", [("halberd_5",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 559, weight(4.3)|difficulty(10)|spd_rtng(90)|weapon_length(187)|swing_damage(33,cut)|thrust_damage(34,pierce), imodbits_polearm ],
["halberd_6", "Halberd", [("halberd_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 599, weight(4.3)|difficulty(11)|spd_rtng(89)|weapon_length(171)|swing_damage(40,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["halberd_7", "Halberd", [("halberd_7",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 559, weight(4.3)|difficulty(10)|spd_rtng(87)|weapon_length(187)|swing_damage(42,cut)|thrust_damage(37,pierce), imodbits_polearm ],
["halberd_8", "Halberd", [("halberd_8",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 599, weight(4.3)|difficulty(11)|spd_rtng(89)|weapon_length(173)|swing_damage(40,cut)|thrust_damage(38,pierce), imodbits_polearm ],

["poleaxe_1", "Poleaxe", [("poleaxe_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 602, weight(4.6)|difficulty(0)|spd_rtng(87)|weapon_length(178)|swing_damage(43,cut)|thrust_damage(33,pierce), imodbits_polearm ],
["poleaxe_2", "Poleaxe", [("poleaxe_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 610, weight(4.4)|difficulty(0)|spd_rtng(91)|weapon_length(156)|swing_damage(42,cut)|thrust_damage(33,pierce), imodbits_polearm ],

["awlpike_1", "Awlpike", [("awlpike_1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 225, weight(3.0)|difficulty(0)|spd_rtng(81)|weapon_length(186)|swing_damage(17,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["awlpike_2", "Awlpike", [("awlpike_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 265, weight(3.0)|difficulty(0)|spd_rtng(80)|weapon_length(187)|swing_damage(17,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["awlpike_3", "Awlpike", [("awlpike_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 235, weight(3.0)|difficulty(0)|spd_rtng(80)|weapon_length(188)|swing_damage(18,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["awlpike_4", "Awlpike", [("awlpike_4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 255, weight(2.9)|difficulty(0)|spd_rtng(80)|weapon_length(187)|swing_damage(17,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["awlpike_5", "Awlpike", [("awlpike_5",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 255, weight(2.9)|difficulty(0)|spd_rtng(80)|weapon_length(181)|swing_damage(15,blunt)|thrust_damage(33,pierce), imodbits_polearm ],
["awlpike_6", "Awlpike", [("awlpike_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield|itp_cant_use_on_horseback, itc_pike_upstab, 265, weight(2.9)|difficulty(0)|spd_rtng(82)|weapon_length(187)|swing_damage(16,blunt)|thrust_damage(30,pierce), imodbits_polearm ],
#["awlpike_7",    "Awlpike", [("awlpike_7",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
# 275 , weight(2.8)|difficulty(0)|spd_rtng(79) | weapon_length(254)|swing_damage(16 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],


["partisan_1", "Partisan", [("partisan_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 185 , weight(2.35)|difficulty(0)|spd_rtng(94) | weapon_length(129)|swing_damage(24 , blunt) | thrust_damage(36 ,  cut),imodbits_polearm ],
["partisan_2", "Partisan", [("partisan_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 195 , weight(2.45)|difficulty(0)|spd_rtng(93) | weapon_length(137)|swing_damage(24 , blunt) | thrust_damage(37 ,  cut),imodbits_polearm ],
["partisan_3", "Partisan", [("partisan_3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 200 , weight(2.45)|difficulty(0)|spd_rtng(92) | weapon_length(146)|swing_damage(25 , blunt) | thrust_damage(39 ,  cut),imodbits_polearm ],
["partisan_4", "Partisan", [("partisan_4",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 175 , weight(2.35)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(24 , blunt) | thrust_damage(35 ,  cut),imodbits_polearm ],

["ranseur_1", "Ranseur", [("ranseur_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 240 , weight(2.4)|difficulty(0)|spd_rtng(96) | weapon_length(124)|swing_damage(14 , blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["ranseur_2", "Ranseur", [("ranseur_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 290 , weight(2.6)|difficulty(0)|spd_rtng(93) | weapon_length(165)|swing_damage(17 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],

["spetum_1", "Spetum", [("spetum_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 140 , weight(2.4)|difficulty(0)|spd_rtng(95) | weapon_length(154)|swing_damage(28 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm ],
["spetum_2", "Spetum", [("spetum_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 160 , weight(2.4)|difficulty(0)|spd_rtng(94) | weapon_length(156)|swing_damage(28 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],
["spetum_3", "Spetum", [("spetum_3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 150 , weight(2.4)|difficulty(0)|spd_rtng(95) | weapon_length(154)|swing_damage(29 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["spetum_4", "Spetum", [("spetum_4",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab |itcf_carry_spear, 145 , weight(2.3)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(27 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["fauchard_1", "Fauchard", [("fauchard_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 185 , weight(2)|difficulty(9)|spd_rtng(90) | weapon_length(129)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_polearm ],
["fauchard_2", "Fauchard", [("fauchard_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 175 , weight(2)|difficulty(9)|spd_rtng(92) | weapon_length(116)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_polearm ],

["lochaber_axe_1", "Lochaber Axe", [("lochaber_axe_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear, 375 , weight(3.8)|difficulty(11)|spd_rtng(94) | weapon_length(159)|swing_damage(40 , cut) | thrust_damage(23 ,  cut),imodbits_polearm ],
["lochaber_axe_2", "Lochaber Axe", [("lochaber_axe_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_poleaxe|itcf_carry_spear, 425 , weight(3.8)|difficulty(11)|spd_rtng(93) | weapon_length(161)|swing_damage(43 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
["lochaber_axe_3", "Lochaber Axe", [("lochaber_axe_3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 405 , weight(3.8)|difficulty(11)|spd_rtng(95) | weapon_length(153)|swing_damage(42 , cut) | thrust_damage(10 ,  cut),imodbits_polearm ],
["lochaber_axe_4", "Lochaber Axe", [("lochaber_axe_4",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 485 , weight(3.8)|difficulty(11)|spd_rtng(96) | weapon_length(137)|swing_damage(41 , cut) | thrust_damage(9 ,  cut),imodbits_polearm ],

["shortened_lochaber_axe","Shortened Lochaber Axe", [("shortened_lochaber_axe",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_voulge|itcf_carry_axe_back, 491 , weight(3.5)|difficulty(12)|spd_rtng(97) | weapon_length(123)|swing_damage(42 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["voulge_1", "Voulge", [("voulge_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 385 , weight(3.8)|difficulty(10)|spd_rtng(89) | weapon_length(153)|swing_damage(36 , cut) | thrust_damage(0 ,  cut),imodbits_polearm],
["voulge_2", "Voulge", [("voulge_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 285 , weight(3.8)|difficulty(10)|spd_rtng(92) | weapon_length(141)|swing_damage(35 , cut) | thrust_damage(0 ,  cut),imodbits_polearm],
["voulge_3", "Voulge", [("voulge_3",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 285 , weight(3.4)|difficulty(11)|spd_rtng(90) | weapon_length(161)|swing_damage(37 , cut) | thrust_damage(26 ,  cut),imodbits_polearm ],
["voulge_4", "Voulge", [("voulge_4",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 290 , weight(2.8)|difficulty(10)|spd_rtng(92) | weapon_length(172)|swing_damage(33 , cut) | thrust_damage(0 ,  cut),imodbits_polearm],
["voulge_5", "Voulge", [("voulge_5",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_voulge, 295, weight(4.1)|difficulty(11)|spd_rtng(88)|weapon_length(161)|swing_damage(39,cut)|thrust_damage(0,cut), imodbits_polearm ],
["voulge_6", "Voulge", [("voulge_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itcf_carry_spear|itc_voulge, 275, weight(3.8)|difficulty(10)|spd_rtng(93)|weapon_length(154)|swing_damage(38,cut)|thrust_damage(0,cut), imodbits_polearm ],
#
["voulge_long", "Longue Voulge", [("pike",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 185, weight(5)|difficulty(0)|spd_rtng(90)|weapon_length(180)|swing_damage(0,cut)|thrust_damage(39,pierce), imodbits_polearm ],
 ["voulge_long_blunt", "Longue Voulge de Hobelar", [("pike",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 185, weight(5)|difficulty(0)|spd_rtng(90)|weapon_length(180)|swing_damage(0,cut)|thrust_damage(39,blunt), imodbits_polearm ],

#["voulge_long", "Longue Voulge", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear, 205 , weight(3.5)|difficulty(0)|spd_rtng(90) | weapon_length(180)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],


["bec_de_corbin", "Bec_de_Corbin", [("bec_de_corbin",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_offset_lance, itc_staff|itcf_carry_spear, 652, weight(2.5)|difficulty(11)|spd_rtng(94)|weapon_length(155)|swing_damage(42,pierce)|thrust_damage(23,pierce), imodbits_polearm ],

["fauchard_3", "Fauchard", [("fauchard_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 275 , weight(2)|difficulty(9)|spd_rtng(93) | weapon_length(182)|swing_damage(24 , cut) | thrust_damage(37 ,  pierce),imodbits_polearm ],
["fauchard_4", "Fauchard", [("fauchard_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 295 , weight(2)|difficulty(9)|spd_rtng(94) | weapon_length(178)|swing_damage(25 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm ],
["glaive_fork", "Glaive-Fork", [("glaive_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 255 , weight(2)|difficulty(10)|spd_rtng(87) | weapon_length(177)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_polearm ],
["glaive_guisarme_1","Glaive-Guisarme", [("glaive_guisarme_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 335 , weight(2)|difficulty(10)|spd_rtng(89) | weapon_length(178)|swing_damage(28 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm ],
["glaive_guisarme_2","Glaive-Guisarme", [("glaive_guisarme_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 285 , weight(2)|difficulty(10)|spd_rtng(90) | weapon_length(185)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["fauchard_fork_1","Glaive-Guisarme", [("fauchard_fork_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 335 , weight(2)|difficulty(10)|spd_rtng(89) | weapon_length(165)|swing_damage(28 , cut) | thrust_damage(36 ,  pierce),imodbits_polearm ],
["fauchard_fork_2","Glaive-Guisarme", [("fauchard_fork_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 285 , weight(2)|difficulty(10)|spd_rtng(90) | weapon_length(174)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],

["lucern_hammer", "Lucern_Hammer", [("lucern_hammer",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 692 , weight(2.4)|difficulty(11)|spd_rtng(96) | weapon_length(151)|swing_damage(35 , blunt) | thrust_damage(29 ,  pierce),imodbits_polearm ],

["bill_1", "Guisarme", [("bill_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 225 , weight(2.3)|difficulty(12)|spd_rtng(91) | weapon_length(176)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_polearm ],
["bill_2", "Guisarme", [("bill_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 225 , weight(2.1)|difficulty(11)|spd_rtng(92) | weapon_length(181)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_polearm ],

["fork_1", "Fork", [("fork_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab, 253 , weight(3.5)|difficulty(0)|spd_rtng(88) | weapon_length(135)|swing_damage(0 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
["fork_2", "Fork", [("fork_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear_upstab, 253 , weight(3.3)|difficulty(0)|spd_rtng(90) | weapon_length(126)|swing_damage(0 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["glaive_1", "Glaive", [("glaive_1",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 325 , weight(2.3)|difficulty(12)|spd_rtng(89) | weapon_length(190)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_polearm ],
["glaive_2", "Glaive", [("glaive_2",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear, 345 , weight(2.2)|difficulty(11)|spd_rtng(90) | weapon_length(190)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["guisarme", "Guisarme", [("guisarme",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_voulge|itcf_carry_spear, 315 , weight(2.3)|difficulty(10)|spd_rtng(88) | weapon_length(174)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_polearm ],

["lance_1", "Wooden Great Lance", [("lance_1",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_great_lance_upstab, 410 , weight(6)|difficulty(12)|spd_rtng(60) | weapon_length(266)|swing_damage(0 , cut) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["lance_2", "Great Lance", [("lance_2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 400, weight(6.3)|difficulty(12)|spd_rtng(59)|weapon_length(226)|swing_damage(0,cut)|thrust_damage(26,pierce), imodbits_polearm ],
["lance_3", "Great Lance", [("lance_3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 460, weight(6.3)|difficulty(12)|spd_rtng(59)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(26,pierce), imodbits_polearm ],
["lance_4", "Wooden Great Lance", [("lance_4",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_great_lance_upstab, 440 , weight(6.3)|difficulty(12)|spd_rtng(59) | weapon_length(251)|swing_damage(0 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["lance_5", "Wooden Great Lance", [("lance_5",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_great_lance_upstab, 412 , weight(5.8)|difficulty(12)|spd_rtng(64) | weapon_length(251)|swing_damage(0 , cut) | thrust_damage(24 ,  pierce),imodbits_polearm ],
["lance_6", "Great Lance", [("lance_6",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(242)|swing_damage(0,cut)|thrust_damage(27,pierce), imodbits_polearm ],
["lance_f2", "Great Lance", [("lance_f1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(27,pierce), imodbits_polearm ],
["lance_f1", "Great Lance", [("lance_f2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(27,pierce), imodbits_polearm ],
["lance_f3", "Great Lance", [("lance_f3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(27,pierce), imodbits_polearm ],
["lance_e1", "Great Lance", [("lance_e1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 460, weight(6.3)|difficulty(12)|spd_rtng(59)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(25,pierce), imodbits_polearm ],
["lance_e2", "Great Lance", [("lance_e2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 460, weight(6.3)|difficulty(12)|spd_rtng(59)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(25,pierce), imodbits_polearm ],
["lance_e3", "Great Lance", [("lance_e3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 460, weight(6.3)|difficulty(12)|spd_rtng(59)|weapon_length(264)|swing_damage(0,cut)|thrust_damage(25,pierce), imodbits_polearm ],

["lance_banner_e1", "Wooden Great Lance", [("lance_banner_e1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_e2", "Wooden Great Lance", [("lance_banner_e2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_e3", "Wooden Great Lance", [("lance_banner_e3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_e4", "Wooden Great Lance", [("lance_banner_e4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_f1", "Wooden Great Lance", [("lance_banner_f1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_f2", "Wooden Great Lance", [("lance_banner_f2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_f3", "Wooden Great Lance", [("lance_banner_f3",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_f4", "Wooden Great Lance", [("lance_banner_f4",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_banner_tut", "Wooden Great Lance", [("lance_banner_tut",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(38,pierce), imodbits_polearm ],
["lance_white", "Wooden Great Lance", [("lance_white",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(32,pierce), imodbits_polearm ],
["lance_banner_jeanne", "Baniere de jeanne d'arc", [("lance_banner_jeanne",0)], itp_type_polearm|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 410, weight(6)|difficulty(12)|spd_rtng(60)|weapon_length(266)|swing_damage(0,cut)|thrust_damage(42,pierce), imodbits_polearm ],
#["regent2", "Epee de Famille", [("regent",0),("bastard_sword_a_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 540, weight(2.25)|difficulty(9)|spd_rtng(100)|weapon_length(116)|swing_damage(39,cut)|thrust_damage(27,pierce), imodbits_sword ],
#["regent2", "Epee de Famille", [("estoc",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 2932, weight(3.10)|difficulty(10)|spd_rtng(95)|weapon_length(140)|swing_damage(44,cut)|thrust_damage(31,pierce), imodbits_sword_high ],
#["dagger_medievale", "Dagger", [("dagger_medievale",0),("scab_dagger_medievale",ixmesh_carry),("dagger_medievale",imodbits_good),("scab_dagger_medievale",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 47,
# weight(0.75)|difficulty(0)|spd_rtng(109)|weapon_length(57)|swing_damage(25,cut)|thrust_damage(21,pierce), imodbits_sword_high ],
["dagger_medievale", "Dague", [("dagger_medievale",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 64 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(57)|swing_damage(25 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["daggerspecial_medievale", "Dague empoisonée", [("dagger_medievale",0)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left, 364, weight(0.75)|difficulty(0)|spd_rtng(109)|weapon_length(57)|swing_damage(40,cut)|thrust_damage(51,pierce), imodbits_sword_high ],

# SPECIAL SHIELDS
["battle_shieldedwardiii", "Edward's_Battle_Shield", [("battle_shield_edward",0)], itp_type_shield , itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(300)|body_armor(1)|spd_rtng(76)|shield_width(91),imodbits_shield ],
["battle_shieldcharlesv", "Charles V's_Battle_Shield", [("battle_shield_charles",0)], itp_type_shield , itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(300)|body_armor(1)|spd_rtng(76)|shield_width(91),imodbits_shield ],

#SHIELDS


["woodenbuckler", "Wooden Archer's Buckler", [("small_shield",0)], itp_merchandise|itp_type_shield ,itcf_carry_round_shield,   12 , weight(1)|hit_points(40)|body_armor(2)|spd_rtng(120)|shield_width(15),imodbits_shield ],
["wooden_buckler1", "Wooden Archer's Buckler", [("wooden_buckler1",0)], itp_merchandise|itp_type_shield ,itcf_carry_round_shield,   12 , weight(1)|hit_points(40)|body_armor(2)|spd_rtng(120)|shield_width(15),imodbits_shield ],
["metal_buckler", "Metal Archer's Buckler", [("metal_buckler",0)], itp_merchandise|itp_type_shield ,itcf_carry_round_shield,   12 , weight(1)|hit_points(40)|body_armor(2)|spd_rtng(120)|shield_width(15),imodbits_shield ],




["kite_shielddiamonds",         "French_Kite_Shield", [("kite_shield_a1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield, 165 , weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["kite_shieldcross",         "English_Kite_Shield", [("wooden_buckler1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
["kite_shieldreddragon",         "English_Kite_Shield", [("kite_shield_a2",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(260)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],


["war_shield3lys",         "French_War_Shield", [("war_shield_e1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  196 , weight(3)|hit_points(280)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["war_shieldeagle",         "French_War_Shield", [("war_shield_c1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  196 , weight(3)|hit_points(280)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["war_shieldtrees",         "English_War_Shield", [("war_shield_c2",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  196 , weight(3)|hit_points(280)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["war_shieldwales",         "Welsh_War_Shield", [("war_shield_c2",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  196 , weight(3)|hit_points(280)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],

["battle_shieldbluecross", "French_Battle_Shield", [("battle_shield_f2",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(300)|body_armor(1)|spd_rtng(76)|shield_width(91),imodbits_shield ],
["battle_shieldbluelysstripes", "French_Battle_Shield", [("battle_shield_f1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(300)|body_armor(1)|spd_rtng(76)|shield_width(91),imodbits_shield ],

["heraldric_shieldblue3lys", "Heraldric_Shield", [("heraldic_shield_d1",0)], itp_merchandise|itp_type_shield ,  itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
["heraldric_shieldblueerminestripes", "French_Heraldric_Shield", [("heraldic_shield_a1",0)], itp_merchandise|itp_type_shield ,  itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],

["heraldric_shieldred3lions", "English_Heraldric_Shield", [("heraldic_shield_a2",0)], itp_merchandise|itp_type_shield , itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
["heraldric_shieldredstripes", "English_Heraldric_Shield", [("heraldic_shield_b1",0)], itp_merchandise|itp_type_shield , itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
["heraldric_shieldredblack", "English Heraldric_Shield", [("heraldic_shield_b2",0)], itp_merchandise|itp_type_shield , itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
["heraldric_shieldredlys", "English_Heraldric_Shield", [("heraldic_shield_d2",0)], itp_merchandise|itp_type_shield , itcf_carry_round_shield,  301 , weight(3.5)|hit_points(320)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],


["heater_shieldblue", "French_Heater_Shield", [("heater_shield_d1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(355)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
["heater_shieldred", "English_Heater_Shield", [("heater_shield_d2",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(355)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
#mod shields end
#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|weapon_length(60),imodbits_shield ],
["steel_buckler1", "Steel Buckler", [("steel_buckler1",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(35)|shield_height(35),imodbits_shield ],
["steel_buckler2", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(28)|shield_height(45),imodbits_shield ],

#SHIELDS END
["wooden_shield", "Wooden Shield", [("small_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("small_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,




#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("wooden_buckler1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",         "Kite Shield", [("wooden_buckler1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
#["steel_shield", "Steel Shield", [("tableau_shield_round_5",0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 697, weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40), imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

["leather_covered_round_shield", "Leather Covered Round Shield", [("small_shield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],

#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],

#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

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

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


#RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,155 , weight(5)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],

["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,300, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,525 , weight(4)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee", "Throwing Spear", [("jarid_new_b",0),("javelins_quiver",ixmesh_carry)], itp_type_polearm|itp_wooden_parry|itp_primary, itc_staff, 525, weight(1)|difficulty(1)|spd_rtng(91)|swing_damage(18,cut)|thrust_damage(33,pierce)|weapon_length(75), imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,560 , weight(4)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,560 , weight(1)|difficulty(2)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(3.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,620, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,620, weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow", "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 72, weight(1)|difficulty(0)|spd_rtng(100)|shoot_speed(55)|thrust_damage(15,pierce), imodbits_bow ],
["short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 58, weight(1)|difficulty(1)|spd_rtng(97)|shoot_speed(53)|thrust_damage(18,pierce), imodbits_bow ],
["nomad_bow", "Nomad Bow", [("nomad_bow",0),("nomad_bow_case",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 164, weight(1.25)|difficulty(2)|spd_rtng(94)|shoot_speed(56)|thrust_damage(20,pierce), imodbits_bow ],
["long_bow", "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 245, weight(1.75)|difficulty(4)|spd_rtng(100)|shoot_speed(65)|thrust_damage(27,pierce), imodbits_bow ],
["khergit_bow", "Turkish Bow", [("khergit_bow",0),("khergit_bow_case",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 269, weight(1.25)|difficulty(3)|spd_rtng(90)|shoot_speed(63)|thrust_damage(21,pierce), imodbits_bow ],
["strong_bow", "Strong Bow", [("strong_bow",0),("strong_bow_case",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 237, weight(1.25)|difficulty(3)|spd_rtng(88)|shoot_speed(64)|thrust_damage(23,pierce), imodbit_cracked|imodbit_bent|imodbit_masterwork ],
["war_bow", "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 128, weight(1.5)|difficulty(3)|spd_rtng(84)|shoot_speed(63)|thrust_damage(22,pierce), imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 22, weight(2.25)|difficulty(0)|spd_rtng(67)|shoot_speed(90)|thrust_damage(45,pierce)|max_ammo(1), imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 67, weight(2.5)|difficulty(8)|spd_rtng(54)|shoot_speed(90)|thrust_damage(38,pierce)|max_ammo(1), imodbits_crossbow ],
["crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 182, weight(3)|difficulty(8)|spd_rtng(58)|shoot_speed(90)|thrust_damage(44,pierce)|max_ammo(1), imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 349, weight(3.5)|difficulty(9)|spd_rtng(72)|shoot_speed(90)|thrust_damage(56,pierce)|max_ammo(1), imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 683, weight(3.75)|difficulty(10)|spd_rtng(82)|shoot_speed(90)|thrust_damage(59,pierce)|max_ammo(1), imodbits_crossbow ],

["matchlock_2", "Arquebuse", [("matchlock_2",0)], itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 3430, weight(5.5)|abundance(90)|difficulty(0)|spd_rtng(60)|shoot_speed(160)|thrust_damage(140,pierce)|max_ammo(1)|accuracy(99), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot_2"),(position_move_x,pos1,0),(position_move_y,pos1,112),(particle_system_burst,"psys_pistol_smoke",pos1,15)])] ],
["matchlock_1", "Couleuvrine a main", [("matchlock_1",0)], itp_type_musket|itp_two_handed|itp_primary|itp_next_item_as_melee, itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 2230, weight(3.5)|abundance(90)|difficulty(0)|spd_rtng(55)|shoot_speed(160)|thrust_damage(110,pierce)|max_ammo(1)|accuracy(99), imodbits_none, [(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,107),(particle_system_burst,"psys_pistol_smoke",pos1,15)])] ],

#["torch",         "Torch", [("new_torch",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none, [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],
#test + lumineux
#["torch",         "Torch", [("new_torch",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none, [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 20, 40),])]],
#["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  11 , weight(0.5)|hit_points(9999999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none ],
#["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],
#["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,50,0,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],
#["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,43,32,5),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),])]],
["torch", "Torche", [("new_torch",0)], itp_type_shield|itp_wooden_parry, 0,  11 , weight(0.5)|hit_points(9999)|body_armor(1)|spd_rtng(1)|weapon_length(1),imodbits_none, [(ti_on_init_item, [(set_position_delta,43,32,-5),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 20, 40),])]],


["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["breton_mail_and_plate", "cotte de mailles Bretonne", [("mail_and_plate_breton",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2", "Practice Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)], itp_type_bow|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90)|shoot_speed(55)|thrust_damage(21,blunt), imodbits_bow ],
["practice_arrows_2", "Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0, weight(3)|weapon_length(95)|max_ammo(80), imodbits_missile ],


["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0, 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0, 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["warhorse_sarranid", "Eastern War Horse", [("warhorse_sarranid",0)], itp_type_horse|itp_merchandise, 0, 1911, abundance(40)|hit_points(115)|body_armor(15)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["warhorse_steppe", "Eastern Charger", [("warhorse_steppe",0)], itp_type_horse|itp_merchandise, 0, 1600, abundance(45)|hit_points(120)|body_armor(25)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112), imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_2,fac_kingdom_2] ],

["flamberge",         "Flamberge Zweihander", [("flamberge",0)], itp_type_polearm|itp_always_loot|itp_two_handed|itp_primary, itc_staff|itcf_carry_sword_back, 1123 , weight(3.75)|difficulty(11)|spd_rtng(77) | weapon_length(125)|swing_damage(52, cut) | thrust_damage(38 ,  pierce),imodbits_sword_high ],
["chapel_de_fer2", "chapel de fer", [("chapel_de_fer",0)],  itp_type_head_armor,0, 293 , weight(1.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["plate_mittens","Plate Mittens", [("plate_mittens_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1940, weight(1.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor],

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
["daggerspecial_medievale", "Dague empoisonée", [("dagger_medievale",0)], itp_type_one_handed_wpn|itp_no_parry|itp_primary|itp_secondary, itc_dagger|itcf_carry_dagger_front_left, 364, weight(0.75)|difficulty(0)|spd_rtng(109)|weapon_length(57)|swing_damage(40,cut)|thrust_damage(51,pierce), imodbits_sword_high ],
["bolts5", "Carreaux", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(49,pierce)|max_ammo(5), imodbits_missile ],
["throwing_daggers_poison", "Dagues empoisonées", [("throwing_dagger",0)], itp_type_thrown|itp_primary, itcf_throw_knife, 193, weight(3.5)|difficulty(0)|spd_rtng(110)|shoot_speed(24)|thrust_damage(100,cut)|max_ammo(2)|weapon_length(0), imodbits_thrown ],
["boltsspecial", "Carreaux  empoisonés", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag",ixmesh_carry),("bolt_bag_b",ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 564, weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(50,pierce)|max_ammo(10), imodbits_missile ],
["arrows_speciale", "fl?hes empoison?s", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver",ixmesh_carry)], itp_type_arrows|itp_default_ammo, itcf_carry_quiver_back, 372, weight(3)|abundance(160)|weapon_length(95)|thrust_damage(30,pierce)|max_ammo(20), imodbits_missile ],
["espee_ecuyer", "épée rouillée avec des Armoiries", [("hospitaller",0),("sword_medieval_c_scabbard",  ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 230 , weight(1.75)|difficulty(0)|spd_rtng(99) | weapon_length(104)|swing_damage(20 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["heraldic_churburg_13_tabard", "Armure de plates Heraldic", [("heraldic_churburg_13_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4900, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(20)|difficulty(8), imodbits_plate, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_tabard",":agent_no",":troop_no"),])] ],
["heraldic_churburg_13_brass_tabard", "Armure de plates Heraldic ornementée", [("heraldic_churburg_13_brass_tabard",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4950, weight(27)|abundance(100)|head_armor(0)|body_armor(60)|leg_armor(21)|difficulty(8), imodbits_plate, [(ti_on_init_item,[(store_trigger_param_1,":agent_no"),(store_trigger_param_2,":troop_no"),(call_script,"script_shield_item_set_banner","tableau_heraldic_churburg_13_brass_tabard",":agent_no",":troop_no"),])] ],

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


#tablier forgeron d'orleans
["orl_leather_apron", "Tablier de maitre forgeron", [("leather_vest_z",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#
["bb_armet", "Armet", [("armet_01",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1210, weight(2.85)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["bb_armet2", "Armet", [("flemish_armet",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1210, weight(2.85)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],

["bb_hounskull_bp", "Bascinet a plumes noires", [("hounskull_bascinet_02",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["bb_greathelm_bp", "Heaume lourd a plumes noires", [("hounskull_bascinet_04",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1480, weight(2.95)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["bb_massivehelm_bp", "Armet a plumes bleus", [("tournament_helmB",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1280, weight(2.85)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["bb_chivalhelm_vp", "Heaume a cloche a plumes rouges", [("tournament_helm_g",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1180, weight(2.75)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["bb_greathelm_rp", "Heaume lourd a plumes rouges", [("tournament_helmR",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1480, weight(2.95)|abundance(100)|head_armor(58)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["bb_hounskull_yp", "Bascinet a plumes jaunes", [("tournament_helmY",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["bb_complet_plates_b", "Armure de plates completes Francaise", [("plate_harness_blue",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],
["bb_complet_plates_bourg", "Armure de plates completes Bourgignone", [("plate_harness_bourg",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],
["bb_complet_plates_charles", "Armure de plates completes Francaise", [("plate_harness_charles",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],
["bb_complet_plates_r", "Armure de plates completes Anglaise", [("plate_harness_red",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],
["bb_complet_plates_rlyon", "Armure de plates completes Anglaise", [("plate_harness_red_lyon",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],
["breton_complet_plates", "Armure de plates completes Bretonne", [("plate_harness_breton",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(62)|leg_armor(24)|difficulty(9), imodbits_armor ],


["charger_blue_lanciers", "Cheval de guerre en plates completes", [("chargerplainblue",0)], itp_type_horse, 0, 2411, abundance(0)|hit_points(115)|body_armor(25)|difficulty(4)|horse_speed(38)|horse_maneuver(39)|horse_charge(29), imodbits_horse_basic ],

["weapon_lanceier_f1", "Grande Lance de Noble chevalier", [("weapon_lanceier_f1",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],
["weapon_lanceier_f2", "Grande Lance de Noble chevalier", [("weapon_lanceier_f2",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itc_great_lance_upstab, 560, weight(6.3)|difficulty(12)|spd_rtng(52)|weapon_length(251)|swing_damage(0,cut)|thrust_damage(35,pierce), imodbits_polearm ],

["bb_noble_hat", "Coiffe de noble a plumes", [("h_h2",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 200, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["bb_noble_hat_simple", "Coiffe de noble", [("h_h1",0)], itp_type_head_armor|itp_merchandise|itp_civilian, 0, 200, weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],

["chaudron", "Chaudron", [("cauldron_a",0)], itp_type_goods, 0, 230, weight(6)|abundance(0), imodbits_none ],
#["legum", "Panier de égumes", [("item_from_quest_21",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["ustensil", "Ustensiles de cuisine", [("item_from_quest_20",0)], itp_type_goods, 0, 30, weight(1)|abundance(0), imodbits_none ],


["joust_warhorse_f1", "Cheval de joutes", [("warhorse_f1",0)], itp_type_horse, 0, 1424, abundance(50)|hit_points(115)|body_armor(13)|difficulty(1)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],
["joust_warhorse_en1", "Cheval de joutes", [("warhorse_en1",0)], itp_type_horse, 0, 1424, abundance(50)|hit_points(115)|body_armor(12)|difficulty(1)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],

#mon epee
["bastard_sword_my_sword", "épée batarde de guerre", [("mon_epee",0),("scab_mon_epee",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 594, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(101)|swing_damage(37,cut)|thrust_damage(35,pierce), imodbits_sword_high ],

#epee du chevalier
["regent2", "épée de famille", [("mon_epee",0),("scab_mon_epee", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 594 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(38 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_high ],

["tab_shield_renfor", "Bouclier aux armoiries renforcé",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,416 , weight(3)|hit_points(410)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield, [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["war_shield3lys_renfor", "Bouclier Francais renforcé", [("war_shield_e1",0)], itp_merchandise|itp_type_shield , itcf_carry_kite_shield,  396 , weight(4)|hit_points(380)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],

["court_hat_two", "Coiffe de noble", [("court_hat_two",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,189, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["coiffe_soeur", "Coiffe", [("habit",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["coiffe_mere", "Coiffe", [("habit_flying",0)],itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

["rpg_anterroche_armor", "Cotte de mailles aux armoiries Anterroche", [("surcoat_over_mail_f4",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["rpg_armor_arloing", "Cotte de mailles aux Arloing", [("surcoat_over_mail_f4",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],


["templar_q_sword", "épée Maconique", [("templar_sword",0),], itp_type_two_handed_wpn|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip, 494, weight(2.0)|difficulty(9)|spd_rtng(98)|weapon_length(121)|swing_damage(35,cut)|thrust_damage(32,pierce), imodbits_sword_high ],
["maconique_armor", "Cotte de mailles Maconique", [("havrincourt_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
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


["newlance_joutes_training_enemi", "Lance de Joute", [("new_jousting_l",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(280)|swing_damage(0,cut)|thrust_damage(999,pierce), imodbits_polearm ],#350 / 220: trop court /250 semble bien
["newlance_joutes_training_joueur", "Lance de Joute", [("new_jousting_l",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(999,pierce), imodbits_polearm ],#mettre les memes valeures a lance joutes !!!!

["newlance_joutes_enemi", "Lance de Joute", [("new_l_joutes_rouge",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(280)|swing_damage(0,cut)|thrust_damage(999,pierce), imodbits_polearm ],#260  ### 350 / 220: trop court /250 semble bien
["newlance_joutes_joueur", "Lance de Joute", [("new_l_joutes_bleu",0)], itp_type_polearm|itp_primary|itp_offset_lance, itc_great_lance_upstab, 83, weight(5)|difficulty(0)|spd_rtng(68)|weapon_length(218)|swing_damage(0,cut)|thrust_damage(999,pierce), imodbits_polearm ],

["new_shynbaulds", "Shynbaulds", [("shynbaulds",0)], itp_type_foot_armor | itp_attach_armature,0, 1329 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0) ,imodbits_plate ],
["new_steel_greaves", "Greaves", [("steel_greaves",0)], itp_type_foot_armor | itp_attach_armature,0, 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0) ,imodbits_plate ],
["training_joute_saddle_horse", "Cheval de Joute", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["training_joute_saddle_horse_enemi", "Cheval de Joute", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_tilting_helmet", "Casque a tete de crapeau", [("tilting_helmet",0)], itp_type_head_armor,0, 1240 , weight(2.75)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],


["new_hourglass_gauntlets","Gantellets", [("hourglass_gauntlets_L",0)], itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(1)|difficulty(0),imodbits_armor],
["new_wisby_gauntlets_red","Gantellets", [("wisby_gauntlets_red_L",0)], itp_type_hand_armor,0, 860, weight(0.75)|abundance(100)|body_armor(1)|difficulty(0),imodbits_armor],

["new_helmet_tournament_blue_1", "Armet a plumes bleus", [("tournament_helmB",0)], itp_type_head_armor|itp_covers_head, 0, 1280, weight(2.85)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_plate ],
["new_helmet_tournament_blue_2", "Bascinet a plumes bleus", [("hounskull_bascinet_02",0)],  itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

["new_helmet_tournament_red_1", "Heaume lourd", [("tilting_helm_unicorn_tall",0)], itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["new_helmet_tournament_red_2", "Heaume lourd a plumes rouges", [("tournament_helmR",0)], itp_type_head_armor|itp_covers_head, 0, 1480, weight(2.95)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_plate ],

["new_churburg_13_brass_red", "Armure de joute", [("churburg_13_brass",0)], itp_type_body_armor|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1)|difficulty(0), imodbits_armor ],
["new_churburg_13_brass_blue", "Armure de joute", [("churburg_13_brass_f",0)], itp_type_body_armor|itp_covers_legs, 0, 3828, weight(27)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1)|difficulty(0), imodbits_armor ],

["new_joutes_horse_blue", "Cheval de Joute", [("warhorse_f3",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_joutes_horse_fr", "Cheval de Joute", [("warhorse_charles",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_joutes_horse_red", "Cheval de Joute", [("warhorse_edwardiii",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_breton_warhorse_2", "Cheval de Joute", [("war_horde_breton_2",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_bourgogne_warhorse", "Cheval de Joute", [("warhorse_f2",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(1)|difficulty(0)|horse_speed(25)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
["new_bb_complet_plates_charles", "Armure de plates completes Francaise", [("plate_harness_charles",0)], itp_type_body_armor|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(1)|difficulty(0), imodbits_armor ],
["new_bb_complet_plates_r", "Armure de plates completes Anglaise", [("plate_harness_red",0)], itp_type_body_armor|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(1)|difficulty(0), imodbits_armor ],
["new_bb_complet_plates_bourg", "Armure de plates completes Bourgignone", [("plate_harness_bourg",0)], itp_type_body_armor|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(1)|difficulty(0), imodbits_armor ],
["new_breton_complet_plates", "Armure de plates completes Bretonne", [("plate_harness_breton",0)], itp_type_body_armor|itp_covers_legs, 0, 4228, weight(29)|abundance(100)|head_armor(0)|body_armor(2)|leg_armor(1)|difficulty(0), imodbits_armor ],
["new_bb_hounskull_yp", "Bascinet a plumes jaunes", [("tilting_helmet",0)], itp_type_head_armor|itp_covers_head,0, 1180 , weight(2.75)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["new_bb_greathelm_bp", "Heaume lourd a plumes noires", [("hounskull_bascinet_04",0)], itp_type_head_armor|itp_covers_head, 0, 1480, weight(2.95)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_plate ],

["cidre", "Cidre", [("bierr",0)], itp_type_goods|itp_merchandise|itp_food|itp_consumable, 0, 120, weight(30)|abundance(70)|food_quality(50)|max_ammo(50), imodbits_none ],
["practice_sword_figurants","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(5,blunt)|thrust_damage(4,blunt),imodbits_none],

["cle_auberge_maison", "clé de la maison abandonnée", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],

["dedal_kufel","Kufel",[("dedal_kufelL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lutnia","Lutnia",[("dedal_lutniaL",0)],	itp_type_hand_armor,0,0,weight(1),0],
["dedal_lira","Lira",[("dedal_liraL",0)],		itp_type_hand_armor,0,0,weight(1),0],


["cavalier_invisible_casque", "Armet", [("cavalier_invisible_casque",0)], itp_type_head_armor|itp_merchandise|itp_covers_head, 0, 1210, weight(2.85)|abundance(100)|head_armor(57)|body_armor(0)|leg_armor(0)|difficulty(9), imodbits_plate ],
["cavalier_invisible_armor", "Light Mail and Plate", [("cavalier_invisible_armor",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["cavalier_invisible_bottes", "English Mail Chausses", [("cavalier_invisible_bottes",0)], itp_type_foot_armor | itp_attach_armature  ,0, 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["cavalier_invisible_gants","Plate Mittens", [("plate_mittens_trans_L",imodbit_reinforced)], itp_type_hand_armor,0, 1940, weight(1.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor],

["cheval_praire", "Cheval exceptionnel", [("hunting_horsef01",0)], itp_type_horse, 0, 730, abundance(70)|body_armor(12)|hit_points(130)|difficulty(4)|horse_speed(52)|horse_maneuver(54)|horse_charge(13)|horse_scale(106), imodbits_horse_basic|imodbit_champion ],
["cheval_praire_barder", "Cheval exceptionnel bardé", [("warhorse_f3",0)], itp_type_horse, 0, 1324, abundance(50)|hit_points(130)|body_armor(15)|difficulty(4)|horse_speed(50)|horse_maneuver(52)|horse_charge(28)|horse_scale(110), imodbits_horse_basic|imodbit_champion ],

["duke_joutes", "Duc", [("landgraf",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1000, weight(3)|difficulty(1)|spd_rtng(95) | weapon_length(135)|swing_damage(20 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],

["laisse_passer_lorges", "Laissé passé du Duc de Bretagne pour la foret de Lorges", [("lettres",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["cle_mine", "clé de la mine de la foret de Lorges", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],
["choppe_bier", "Chope de bierre", [("choppe",0)], itp_merchandise|itp_type_goods|itp_food|itp_consumable, 0, 5, weight(1)|abundance(110)|food_quality(20)|max_ammo(5), imodbits_none ],
["cle_de_grotte", "clé de l'ancienne mine de la foret de Lorges", [("item_from_quest_16",0)], itp_type_goods, 0, 0, weight(1)|abundance(0), imodbits_none ],

["quest_sniper_crossbow", "Arbalète du chasseur", [("crossbow_c",0)], itp_type_crossbow|itp_merchandise|itp_cant_reload_on_horseback|itp_two_handed|itp_primary, itcf_shoot_crossbow|itcf_carry_crossbow_back, 683, weight(3.75)|difficulty(10)|spd_rtng(82)|shoot_speed(90)|thrust_damage(60,pierce)|max_ammo(1), imodbits_crossbow ],

["fr_hourglass_gauntlets","Hourglass Gauntlets", [("fr_hourglass_gauntlets_L",0)], itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(1)|difficulty(0),imodbits_armor],
["eng_hourglass_gauntlets","Hourglass Gauntlets", [("eng_hourglass_gauntlets_L",0)], itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(1)|difficulty(0),imodbits_armor],
["bret_hourglass_gauntlets","Hourglass Gauntlets", [("bret_hourglass_gauntlets_L",0)], itp_type_hand_armor,0, 990, weight(1.0)|abundance(100)|body_armor(1)|difficulty(0),imodbits_armor],

["corrazina_breton", "Corrazina Bretone", [("corrazina_breton",0)], itp_type_body_armor  |itp_covers_legs ,0, 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(53)|leg_armor(18)|difficulty(6) ,imodbits_armor ],
["preuve_mort_pantievre", "Chevaliere de Pantièvre [preuve de sa mort]", [("item_from_quest_2",0)], itp_type_goods, 0, 2000, weight(2)|abundance(0), imodbits_none ],


["items_end", "Items End", [("small_shield",0)], 0, 0, 1, 0, 0],
]

#MOTO generate no-swing versions of weapons
#Warning: this makes additions to item table non-save compatible, as the system only reads in the "new" ones, effectively overwriting the real new ones
#It may be best to comment out until the table is set
#append_noswing_items(items)
