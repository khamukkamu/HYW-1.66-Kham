# -*- coding: utf-8 -*-
import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *
from compiler import *
####################################################################################################################
#  Each troop contains the following fields:   
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

######
#Troop Skills Templates
#lvl12
knows_common_kham = knows_weapon_master_5|knows_ironflesh_4|knows_athletics_5|knows_power_strike_3|knows_shield_1|knows_inventory_management_2|knows_power_throw_3|knows_power_draw_3 #40+12 / 2
#lvl18
knows_warrior_basic = knows_weapon_master_6|knows_ironflesh_5|knows_athletics_5|knows_riding_2|knows_power_strike_3|knows_shield_2|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3 #40+18 / 2 +2
#lvl23
knows_warrior_basic2 = knows_weapon_master_7|knows_ironflesh_7|knows_athletics_5|knows_riding_3|knows_power_strike_5|knows_shield_4|knows_inventory_management_4|knows_power_throw_3|knows_power_draw_3  #40+24 / 2 +4
#lvl26
knows_warrior_normal = knows_weapon_master_8|knows_ironflesh_8|knows_athletics_5|knows_riding_5|knows_power_strike_5|knows_shield_4|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 #40+26 / 2 +6
#lvl29
knows_warrior_veteran = knows_weapon_master_9|knows_ironflesh_9|knows_athletics_5|knows_riding_6|knows_power_strike_7|knows_shield_6|knows_inventory_management_5|knows_power_throw_4|knows_power_draw_4 ##40+30 / 2 +8
#lvl31
knows_warrior_elite = knows_weapon_master_10|knows_ironflesh_10|knows_athletics_5|knows_riding_7|knows_power_strike_8|knows_shield_6|knows_inventory_management_6|knows_power_throw_4|knows_power_draw_4 ###40+32 / 2 +12


knows_archer_basic = knows_weapon_master_3|knows_ironflesh_6|knows_athletics_5|knows_riding_3|knows_power_strike_2|knows_shield_2|knows_inventory_management_4|knows_power_throw_4|knows_power_draw_4 #cambiado chief
#special skirmishers & longbowmen
knows_archer_english = knows_weapon_master_5|knows_ironflesh_6|knows_athletics_6|knows_riding_4|knows_power_strike_4|knows_shield_2|knows_inventory_management_4|knows_power_throw_5|knows_power_draw_5 #cambiado chief

knows_archer_english_2 = knows_weapon_master_8|knows_ironflesh_6|knows_athletics_6|knows_riding_4|knows_power_strike_4|knows_shield_2|knows_inventory_management_4|knows_power_throw_5|knows_power_draw_8

#Attributes Templates
def_attrib =    str_16 | agi_8 | int_12 | cha_12|level(12)   #basic points 55
def_attrib_b =  str_16 | agi_8 | int_12 | cha_12|level(18) #basic points 55

def_attrib2 =   str_18 | agi_8 | int_12 | cha_12|level(23)   #+3 level med
def_attrib2_b = str_18 | agi_8 | int_12 | cha_12|level(26) #+3 level med

def_attrib3 =   str_20 | agi_8 | int_12 | cha_12|level(29)   #+5 level max
def_attrib3_b = str_20 | agi_8 | int_12 | cha_12|level(31)   #+5 level max

#######

#Skills (Old, replaced by above)
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2


### The below are all commented out and replaced with the VC system. I like the idea of having lords have the same attributes and skills, just like in VC.
### That system allows some internal consistency, that all lords are generally the same. I'm sure the VC team has a good reason for implementing it this way.

#lord_attrib = str_20|agi_20|int_20|cha_20|level(38)
#knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

#knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
#knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
#knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
#knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
#knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
#knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
#knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
#knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
#knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
#knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

### END Comment out of Old system

### Kings & Lords Template New System BEGIN
king_attrib = str_20|agi_19|int_18|cha_20|level(40)

king_skills = knows_weapon_master_10|knows_trainer_5|knows_riding_4|knows_ironflesh_10|knows_power_strike_10|knows_athletics_10|knows_shield_3|knows_tactics_10|knows_prisoner_management_9|knows_leadership_10|knows_wound_treatment_9|knows_first_aid_8|knows_surgery_8|knows_power_throw_5|knows_power_draw_6|knows_spotting_6|knows_pathfinding_5|knows_inventory_management_4|knows_persuasion_6|knows_engineer_6


lord_attrib = str_18|agi_17|int_16|cha_18|level(38)
knows_lord_1 = knows_weapon_master_8|knows_trainer_4|knows_riding_4|knows_ironflesh_8|knows_power_strike_8|knows_athletics_8|knows_shield_3|knows_tactics_8|knows_prisoner_management_9|knows_leadership_8|knows_wound_treatment_7|knows_first_aid_6|knows_surgery_6|knows_power_throw_4|knows_power_draw_4|knows_spotting_4|knows_pathfinding_4|knows_inventory_management_3|knows_persuasion_4|knows_engineer_4



#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes. 


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x000000003f00d00036db6db6db61b6db00000000001db6db0000000000000000
swadian_face_young_1   = 0x000000003f00700436db6db6db65b6db00000000001db6db0000000000000000
swadian_face_middle_1  = 0x000000000000a00636db6db6db65b6db00000000001db6db0000000000000000
swadian_face_old_1     = 0x000000002c00c00d36db6db6db65b6db00000000001db6db0000000000000000
swadian_face_older_1   = 0x000000003f00100d36db6db6db65b6db00000000001db6db0000000000000000

swadian_face_younger_2 = 0x000000003f00b01036db6db6db65b6db00000000001db6db0000000000000000
swadian_face_young_2   = 0x000000003f00001036db6db6db65b6db00000000001db6db0000000000000000
swadian_face_middle_2  = 0x000000003f00501036db6db6db65b6db00000000001db6db0000000000000000
swadian_face_old_2     = 0x000000003f00801236db6db6db65b6db00000000001db6db0000000000000000
swadian_face_older_2   = 0x000000003f00a01236db6db6db65b6db00000000001db6db0000000000000000

vaegir_face_younger_1 = 0x000000000000000536db6db6db65b6db00000000001db6db0000000000000000
vaegir_face_young_1   = 0x000000000000200534db6d36db61c91b00000000001da6e30000000000000000
vaegir_face_middle_1  = 0x000000000000500534db6d352461c91b00000000001da6db0000000000000000
vaegir_face_old_1     = 0x000000000000a00534db6d352461c91b00000000001da6db0000000000000000
vaegir_face_older_1   = 0x000000000000c00034db6d352461c91b00000000001da6db0000000000000000

vaegir_face_younger_2 = 0x000000001d00200134db6d35246dc91b00000000001da6db0000000000000000
vaegir_face_young_2   = 0x000000074300b00134db6d352469c91b00000000001da6db0000000000000000
vaegir_face_middle_2  = 0x000000074300100234db6d38dc61c91b00000000001da6db0000000000000000
vaegir_face_old_2     = 0x0000000b4010010136db6db6db6db6db00000000001db6db0000000000000000
vaegir_face_older_2   = 0x000000000000400034dc6d38dc61cb5b00000000001da6db0000000000000000

khergit_face_younger_1 = 0x000000000000714034db8d38dc61cb5b00000000001da6db0000000000000000
khergit_face_young_1   = 0x000000000000740034db8d38dc61cb5b00000000001da6db0000000000000000
khergit_face_middle_1  = 0x00000000000093c634db6d38dc61cb5b00000000001da6db0000000000000000
khergit_face_old_1     = 0x000000000000a44b34db6d38dc61cb5b00000000001da6db0000000000000000
khergit_face_older_1   = 0x0000000ac000a4cd34dc8a38dc61cb5b00000000001da6db0000000000000000

khergit_face_younger_2 = 0x000000000000b4cd34db8a38dc61cb5b00000000001da6db0000000000000000
khergit_face_young_2   = 0x000000001900d4d134db8a38dc61cb5b00000000001da6db0000000000000000
khergit_face_middle_2  = 0x000000001900101234db8a38dc61cb5b00000000001da6db0000000000000000
khergit_face_old_2     = 0x0000000c1900100034db8a38dc61cb5b00000000001da6db0000000000000000
khergit_face_older_2   = 0x000000001900400034db8a38dc61cb5b00000000001da6db0000000000000000

nord_face_younger_1 = 0x000000001900600036db6db6db6db6db00000000001db6db0000000000000000
nord_face_young_1   = 0x000000001900700036db6db6db6db6db00000000001db6db0000000000000000
nord_face_middle_1  = 0x000000001900800036db6db6db6db6db00000000001db6db0000000000000000
nord_face_old_1     = 0x000000001900a00036db6db6db6db6db00000000001db6db0000000000000000
nord_face_older_1   = 0x000000001900c00036db6db6db6db6db00000000001db6db0000000000000000

nord_face_younger_2 = 0x000000001900d04012db6d46db6db6db00000000001db6ec0000000000000000
nord_face_young_2   = 0x000000001900d04012db6d46db6db6db00000000001db6ec0000000000000000
nord_face_middle_2  = 0x000000000600004114db6d46db6db6db00000000001db6ec0000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x000000000600104114db8d46db6db6db00000000001db6ec0000000000000000

rhodok_face_younger_1 = 0x000000003b04359336db6db6db6db6db00000000001db6db0000000000000000
rhodok_face_young_1   = 0x000000000110600c39e4a43c762ad6e300000000001e4ca10000000000000000
rhodok_face_middle_1  = 0x000000003508201048d575db1c39d76400000000001cca950000000000000000
rhodok_face_old_1     = 0x000000000008501248d575db1c39d76400000000001cca950000000000000000
rhodok_face_older_1   = 0x0000000d0008500048d575db1c39d76400000000001cca950000000000000000

rhodok_face_younger_2 = 0x000000014008600248d575db1c39d76400000000001cca950000000000000000
rhodok_face_young_2   = 0x00000000380cb4d43a9a6ca396aa647400000000001ccb920000000000000000
rhodok_face_middle_2  = 0x00000000380c04d43a9a6ca396aa647400000000001ccb920000000000000000
rhodok_face_old_2     = 0x00000000380c14d33a9a6ca396aa647400000000001ccb920000000000000000
rhodok_face_older_2   = 0x00000000380c54d33a9a6ca396aa647400000000001ccb920000000000000000

man_face_younger_1 = 0x00000000380c64d33a9a6ca396aa647400000000001ccb920000000000000000
man_face_young_1   = 0x000000002608d00460a365484ca2151a00000000001f26560000000000000000
man_face_middle_1  = 0x000000001008100560a365484ca2151a00000000001f26560000000000000000
man_face_old_1     = 0x000000003208510460a365484ca2151a00000000001f26560000000000000000
man_face_older_1   = 0x000000001908c00d60a365484ca2151a00000000001f26560000000000000000

man_face_younger_2 = 0x000000003f10000f489c724ce16da71a00000000001d550c0000000000000000
man_face_young_2   = 0x00000000171060d0489c724ce16da71a00000000001d550c0000000000000000
man_face_middle_2  = 0x00000000171090d0489c724ce16da71a00000000001d550c0000000000000000
man_face_old_2     = 0x000000001710a153489c724ce16da71a00000000001d550c0000000000000000
man_face_older_2   = 0x000000089710a140489c724ce16da71a00000000001d550c0000000000000000

merchant_face_1    = 0x000000003f10108f489c724ce16da71a00000000001d550c0000000000000000
merchant_face_2    = 0x00000000171050d0489c724ce16da71a00000000001d550c0000000000000000

woman_face_1    = 0x000000001910500614ea6cb4e95146de000000000019d9330000000000000000
woman_face_2    = 0x0000000000001004391aca36dc12249300000000001da6db0000000000000000

swadian_woman_face_1 = 0x000000002d04500654e1722b8b2dbe1600000000000c97510000000000000000
swadian_woman_face_2 = 0x0000000a81045001389d29b96a89c7220000000000090b9a0000000000000000

khergit_woman_face_1 = 0x00000006c41020023aab764b1a30a69500000000000d32ca0000000000000000
khergit_woman_face_2 = 0x0000000ac400200424da81a6dd6ca6d200000000001dc7130000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x000000001710a040489c724ce16da71a00000000001d550c0000000000000000
mercenary_face_2 = 0x000000003f101085489c724ce16da71a00000000001d550c0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = 0x000000003f101145489c724ce16da71a00000000001d550c0000000000000000
bandit_face2  = 0x000000003f102189489c724ce16da71a00000000001d550c0000000000000000

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield


troops = [
["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,[],str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,[itm_leather_jerkin,itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,[itm_tribal_warrior_outfit,itm_leather_boots],0,0,0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,[itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,[itm_tutorial_sword,itm_leather_vest,itm_hide_boots],str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

["novice_fighter", "Novice Fighter", "Novice Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_6|agi_6|level(5), wp(110), knows_common, mercenary_face_1, mercenary_face_2 ],
["regular_fighter", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_8|agi_8|level(11), wp(120), knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2, mercenary_face_1, mercenary_face_2 ],
["veteran_fighter", "Veteran Fighter", "Veteran Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_10|agi_10|level(17), wp(130), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3, mercenary_face_1, mercenary_face_2 ],
["champion_fighter", "Champion Fighter", "Champion Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_mail_chausses], str_12|agi_11|level(22), wp(160), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4, mercenary_face_1, mercenary_face_2 ],

["arena_training_fighter_1", "Novice Fighter", "Novice Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_6|agi_6|level(5), wp(60), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_2", "Novice Fighter", "Novice Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_7|agi_6|level(7), wp(70), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_3", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_8|agi_7|level(9), wp(80), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_4", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_8|agi_8|level(11), wp(90), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_5", "Regular Fighter", "Regular Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_9|agi_8|level(13), wp(100), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_6", "Veteran Fighter", "Veteran Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_10|agi_9|level(15), wp(110), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_7", "Veteran Fighter", "Veteran Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_10|agi_10|level(17), wp(120), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_8", "Veteran Fighter", "Veteran Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_11|agi_10|level(19), wp(130), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_9", "Champion Fighter", "Champion Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_12|agi_11|level(21), wp(140), knows_common, mercenary_face_1, mercenary_face_2 ],
["arena_training_fighter_10", "Champion Fighter", "Champion Fighters", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose], str_12|agi_12|level(23), wp(150), knows_common, mercenary_face_1, mercenary_face_2 ],

["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#### EXCEL TEMPLATE CODE STARTS ######
#### Troop Stats modified by Kham - Comments and commented out troops removed.

#soldiers:
#This troop is the troop marked as soldiers_begin
["farmer","Farmer","Farmers",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_commoners,[itm_straw_hat,itm_leather_cap,itm_coarse_tunic,itm_leather_apron,itm_linen_tunic,itm_blue_hose,itm_wrapping_boots,itm_club,itm_hammer,itm_pickaxe,itm_sickle,itm_cleaver,itm_knife,itm_butchering_knife,itm_hatchet,itm_pitch_fork,itm_boar_spear,itm_scythe,itm_staff,],def_attrib,wp(60),knows_common_kham,swadian_face_young_1,swadian_face_old_2],
["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_coif_new_e1,itm_skullcap,itm_leather_armor,itm_leather_vestgreen,itm_hide_boots,itm_nomad_boots,itm_1mace,itm_2mace,itm_4mace,itm_1club,itm_fighting_pick,itm_gaddhjalt,itm_ritter,itm_reeve,itm_hand_axe,itm_military_fork,itm_battle_fork,itm_spear,itm_pike,itm_3polehammer,],def_attrib_b,wp(75),knows_warrior_basic,swadian_face_young_1,swadian_face_old_2],
#Farmer Troop Tree continues after mercenaries.

#Mercenaries Begin
["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_nasal_helmet,itm_segmented_helmet,itm_mail_coif,itm_padded_cloth,itm_padded_leatherblack,itm_leather_jerkingreen,itm_leather_boots,itm_mail_chausses,itm_squire,itm_laird,itm_caithness,itm_fighting_axe,itm_woodenbuckler,itm_tab_shield_round_b,],def_attrib_b,wp(85),knows_warrior_basic2,swadian_face_young_1,swadian_face_old_2],
["caravan_guard","Caravan_Guard","Caravan_Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,[itm_kettle_hat,itm_nasal_helmet,itm_mail_coif_full,itm_mail_shirtdeer,itm_mail_shirtgreen,itm_mail_hauberk,itm_leather_gloves,itm_splinted_greaves,itm_mail_boots,itm_hersir,itm_huskarl,itm_nordic_shield,itm_tab_shield_kite_c,itm_courser,itm_hunter,],def_attrib2,wp(95),knows_warrior_basic2,swadian_face_young_1,swadian_face_old_2],
["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_commoners,[itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_padded_cloth,itm_leather_jerkin,itm_nomad_boots,itm_wrapping_boots,itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_round_b,],def_attrib2_b,wp(90)|wp_crossbow(120),knows_warrior_normal,mercenary_face_1,mercenary_face_2],
["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,[itm_norman_helmet,itm_mail_coif,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_saddle_horse,itm_courser,itm_hunter,],def_attrib2_b,wp(105),knows_warrior_normal,mercenary_face_1,mercenary_face_2],
["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,[itm_kettle_hat,itm_mail_coif,itm_mail_hauberk,itm_banded_armor,itm_hide_boots,itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_saddle_horse,itm_courser,itm_hunter,],def_attrib3,wp(125),knows_warrior_veteran,mercenary_face_1,mercenary_face_2],
["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_commoners,[itm_kettle_hat,itm_mail_coif,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,],def_attrib2_b,wp(105),knows_warrior_normal,0x000000000710701036d26cbb59a5e6db00000000001db6db0000000000000000,0x000000000710801236d26cbb59a5e6db00000000001db6db0000000000000000],
["genoese_crossbowman","Genoese Crossbowman","Genoese Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,[itm_kettle_hat,itm_kettle_hat,itm_brigandine_g,itm_leather_gloves,itm_mail_chausses,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d,],def_attrib3,wp(160),knows_warrior_elite,0x000000000710a05236d26cbb59a5e6db00000000001db6db0000000000000000,0x000000003e10b0d236d26cbb59a5e6db00000000001db6db0000000000000000],
["german_knight","German Mercenary","German Mercenaries",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_commoners,[itm_mail_coif_full,itm_black_cuir_bouilli,itm_mail_mittens,itm_mail_chausses,itm_senlac,itm_bastard_sword_a,itm_bastard_sword_b,itm_great_bardiche,itm_heavy_lance,itm_heavy_lance,itm_heavy_lance,itm_heavy_lance,itm_tab_shield_kite_cav_b,itm_warhorseboar,],def_attrib3,wp(140),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],
["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,[itm_guard_helmet,itm_great_helmet,itm_haubergeon,itm_leather_gloves,itm_mail_chausses,itm_iron_greaves,itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,],def_attrib3,wp(130),knows_warrior_veteran,mercenary_face_1,mercenary_face_2],

["swiss_veteran_halberdier","Swiss Halberdier","Swiss Halberdiers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,[itm_open_sallet,itm_visored_sallet,itm_arming_cap,itm_leather_cap,itm_early_transitional_teu,itm_early_transitional_teu,itm_plate_mittens,itm_plate_mittens,itm_mail_mittens,itm_steel_greaves,itm_shynbaulds,itm_shynbaulds,itm_lui_vaegirhallberd,itm_pop_halberd,],def_attrib3_b,wp_melee(220),knows_warrior_elite,swadian_face_young_1,man_face_young_2],

#,itm_byrnie_swiss1

["coulveriners","Couleuvrinier","Couleuvriniers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,[itm_mail_coif,itm_corrazina_green,itm_splinted_greaves_nospurs,itm_woolen_hose,itm_matchlock_2,itm_cartridges,itm_sword_medieval_b_small,itm_sword_medieval_a,],def_attrib3,wp(160),knows_warrior_elite,0x000000003e1010d236d26cbb59a5e6db00000000001db6db0000000000000000,0x000000000010311236d26cbb59a5e6db00000000001db6db0000000000000000],
["arquebusier","Arquebusier","Arquebusiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,[itm_mail_coif,itm_corrazina_green,itm_splinted_greaves_nospurs,itm_woolen_hose,itm_matchlock_2,itm_cartridges,itm_sword_medieval_b_small,itm_sword_medieval_a,],def_attrib2_b,wp(160),knows_warrior_veteran,0x000000000010419236d26cbb59a5e6db00000000001db6db0000000000000000,0x000000000010521236d26cbb59a5e6db00000000001db6db0000000000000000],
["sang_lysrecruit","Mercenaire du SansLys","Mercenaire du SansLys",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_commoners,[itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_brigandine_sl,itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_templar,itm_bastard_sword_a,itm_battle_shieldcharlesv,],def_attrib2_b,wp(130),knows_warrior_veteran,0x000000000010614036d26cbb59a5e6db00000000001db6db0000000000000000,0x000000000010714036d26cbb59a5e6db00000000001db6db0000000000000000],

["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,[],def_attrib|level(4),wp(60),knows_common,mercenary_face_1,mercenary_face_2],
#Mercenaries END

#Not used
["recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1,swadian_face_old_2],

#Farmer Upgrades
["monk","Millicien","Millicien",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_shirt,itm_hunter_boots,itm_club,itm_knife,itm_staff,itm_staff,],def_attrib_b,wp(75),knows_warrior_basic,man_face_young_1,man_face_older_2],
["lumberman","Boureau","Boureau",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_leather_cap,itm_pilgrim_disguise,itm_rawhide_coat,itm_rawhide_coatwhite,itm_leather_gloves,itm_leather_gloves,itm_hunter_boots,itm_leather_boots,itm_hand_axe,itm_fighting_axe,itm_axe,],def_attrib2,wp(80),knows_warrior_basic2,swadian_face_young_1,swadian_face_old_2],
["priest","Piquier millicien","Piquiers milliciens",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_long_mail_coat,itm_mail_shirt,itm_leather_boots,itm_mail_chausses,itm_club,itm_knife,itm_staff,itm_staff,itm_voulge_3,itm_voulge_1,itm_2glaive,],def_attrib2,wp(80),knows_warrior_basic2,man_face_young_1,man_face_older_2],
["executioner","Executioner","Executioners",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_mail_chausses,itm_robeblack,itm_common_hoodblack,itm_leather_gloves,itm_leather_boots,itm_mail_chausses,itm_battle_axe,itm_war_axe,],def_attrib2,wp(95),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
["sentry","Sentry","Sentries",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_kettle_hat,itm_nasal_helmet,itm_mail_coif_full,itm_mail_shirtdeer,itm_mail_shirtgreen,itm_mail_hauberk,itm_splinted_greaves,itm_mail_boots,itm_templar,itm_bayeux,itm_hospitaller,itm_nordic_shield,itm_tab_shield_kite_c,],def_attrib2,wp(95),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
["chaplain","Piquier millicien lourd","Piquiers milliciens lourds",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_long_mail_coat,itm_mail_shirt,itm_mail_hauberk,itm_leather_gloves,itm_mail_mittens,itm_mail_gauntlets,itm_mail_chausses,itm_mail_boots,itm_knife,itm_bill,itm_fauchard_fork_2,itm_bardiche_5,],def_attrib2,wp(95),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
["torturer","Tortionaire","Tortionaires",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_robeblack,itm_common_hoodblack,itm_leather_gloves,itm_mail_boots,itm_great_axe,],def_attrib2_b,wp(110),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],
["city_guard","City_Guard","City_Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_guard_helmet,itm_black_helmetgrey,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_gothic_armour,itm_early_transitional_boar,itm_early_transitional_teu,itm_early_transitional_horse,itm_leather_gloves,itm_mail_boots,itm_iron_greaves,itm_senlac,itm_knight,itm_count,itm_castellan,itm_sempach,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_tab_shield_kite_c,],def_attrib2_b,wp(110),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],
["bishop","Hallbardier","Hallbardiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves,0,0,fac_commoners,[itm_chapel_de_fer,itm_chapel_de_fer,itm_nasal_helmet,itm_gothic_armour,itm_milanese_armour,itm_shynbaulds,itm_steel_greaves,itm_lui_vaegirhallberd,itm_lui_vaegirhallberd,itm_lui_smallhallberda,],def_attrib2_b,wp(110),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],
["rider","Rider","Riders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,[itm_kettle_hat,itm_nasal_helmet,itm_mail_coif_full,itm_mail_shirtdeer,itm_mail_shirtgreen,itm_mail_hauberk,itm_splinted_greaves,itm_mail_boots,itm_templar,itm_bayeux,itm_hospitaller,itm_nordic_shield,itm_tab_shield_kite_c,itm_sumpter_horse,itm_saddle_horse,itm_steppe_horse,],def_attrib2,wp(95),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],
["master_rider","Master_Rider","Master_Riders",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_commoners,[itm_guard_helmet,itm_black_helmetgrey,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_gothic_armour,itm_mail_mittens,itm_mail_boots,itm_iron_greaves,itm_clontarf,itm_jarl,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_courser,itm_hunter,],def_attrib2_b,wp(110),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],
#Farmer Upgrades END

########## 1429 Faction Troops BEGIN - Kham ###################
## French Main Troops

#Infantry Line
["swadian_recruit","French_Paysan","French_Paysans",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,[itm_straw_hat,itm_coarse_tunic,itm_peasant_man_f2,itm_wrapping_boots,itm_blue_hose,itm_pitch_fork,itm_awlpike_4,itm_ashwood_pike,itm_fauchard_2,itm_stones,itm_hatchet,itm_cleaver,],def_attrib,wp(60),knows_common_kham,swadian_face_younger_1,swadian_face_middle_2],

["swadian_militia","French_Milice","French_Milices",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,[itm_mail_coif,itm_mail_coif,itm_bascinet_3,itm_bascinet_3,itm_haubergeon_f1,itm_haubergeon_f2,itm_mail_mittens,itm_mail_chausses_f1,itm_mail_chausses,itm_sword_medieval_a,itm_sword_medieval_c,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib_b,wp(75),knows_warrior_basic,swadian_face_young_1,swadian_face_old_2],

["swadian_footman","French_Homme_d'Armes","French_Hommes_d'Armes",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,[itm_kettlehat2_painted,itm_kettlehat2,itm_surcoat_over_mail_f1,itm_surcoat_over_mail_f2,itm_mail_mittens,itm_leather_gloves,itm_mail_chausses_f1,itm_blue_hose,itm_sword_medieval_c,itm_sword_medieval_a,itm_bayeux,itm_mace_4,itm_tab_shield_round_e,itm_tab_shield_heater_b,itm_tab_shield_round_e,],def_attrib2,wp_melee(85),knows_warrior_basic2,swadian_face_young_1,swadian_face_old_2],

#Has shield guarantee but no shield. To Study
["french_spearmen","French_Piquier","French_Piquiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_kettlehat2,itm_leather_cap,itm_skullcap,itm_leather_vest_f1,itm_leather_vest_f2,itm_leather_gloves,itm_leather_gloves,itm_blue_hose,itm_splinted_greaves_f1,itm_woolen_hose,itm_spetum_3,itm_awlpike_5,itm_spetum_3,],def_attrib2,wp(85),knows_warrior_basic2,swadian_face_young_1,swadian_face_old_2],

["swadian_infantry","Infanterie lourde Francaise","Infanteries lourdes Francaise",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_full_helm,itm_kettlehat2,itm_open_sallet,itm_coat_of_plates_f2,itm_coat_of_plates_f1,itm_shynbaulds,itm_steel_greaves,itm_shynbaulds,itm_steel_greaves,itm_bayeux,itm_one_handed_war_axe_a,itm_bastard_sword_a,itm_bastard_sword_b,],def_attrib2_b,wp_melee(105),knows_warrior_normal,swadian_face_middle_1,swadian_face_old_2],

#Has shield guarantee but no shield. To Study
["swadian_sergent","Sergent Francais","Sergents Francais",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_hounskull,itm_klappvisier,itm_pigface_klappvisor,itm_heraldic_churburg_13_brass_tabard,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_landgraf,itm_1mace,itm_lui_knightaxeonehe,itm_bayeux,itm_one_handed_battle_axe_c,itm_one_handed_battle_axe_c,itm_bastard_sword_b,itm_bastard_sword_a,],def_attrib3,wp_melee(155),knows_warrior_veteran,swadian_face_middle_1,swadian_face_old_2],

#two handed pollearms
["french_hallebardier","French_Sergent_Vougier","French_Sergent_Vougiers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,[itm_chapel_de_fer,itm_kettlehat2,itm_churburg_13,itm_heraldic_churburg_13_brass_tabard,itm_splinted_greaves_f1,itm_splinted_leather_greaves,itm_splinted_greaves_f1,itm_splinted_leather_greaves,itm_1halberd,itm_2halberd,itm_6halberd,itm_lui_smallhallberdb,],def_attrib2_b,wp(115),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],

#shield/spear - Currently no shield, but has guarantee. To Study
["french_pikemen","French_Sergent_Lourd","French_Sergent_Lourds",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_kettlehat2,itm_kettlehat2,itm_kettlehat2_painted,itm_brigandine_f2,itm_brigandine_f1,itm_plate_mittens,itm_mail_mittens,itm_splinted_greaves_f1,itm_splinted_leather_greaves,itm_mail_chausses_f1,itm_voulge_long,itm_spetum_3,itm_2glaive,itm_jam_scorpion,itm_fauchard_fork_2,],def_attrib2_b,wp(110),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],

["swadian_sergeant","Massier Francais","Massier Francais",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_bb_hounskull_bp,itm_gothic_armour,itm_milanese_armour,itm_hourglass_gauntlets,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_1mace,itm_2hammer,itm_4mace,itm_mace_2,itm_mace_4,itm_one_handed_battle_axe_c,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib3,wp_melee(110),knows_warrior_veteran,swadian_face_middle_1,swadian_face_old_2],

#Ranged line

["french_javelinier","French_Archer_Paysen","French_Archer_Paysens",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_leather_cap,itm_white_gambeson_f1,itm_hide_boots,itm_hide_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_sword_medieval_c,itm_sword_medieval_a,],def_attrib_b,wp(75),knows_common_kham,swadian_face_young_1,swadian_face_old_2],

["swadian_skirmisher","French_Homme_de_Traits","French_Homme_de_Traits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_skullcap,itm_nasal_helmet,itm_mail_coif,itm_leather_vest_f2,itm_padded_cloth_f1,itm_leather_boots,itm_leather_boots,itm_hunting_crossbow,itm_bolts,itm_sword_medieval_a,itm_gaddhjalt,itm_ritter,itm_reeve,itm_mace_2,itm_mace_4,],def_attrib2,wp(80),knows_archer_basic,swadian_face_young_1,swadian_face_middle_2],

["french_bowmen","French_Archer","French_Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_skullcap,itm_nasal_helmet,itm_leather_cap,itm_padded_cloth_b_f1,itm_padded_cloth_f1,itm_blue_hose,itm_leather_boots,itm_blue_hose,itm_leather_boots,itm_war_bow,itm_arrows,itm_sword_medieval_a,itm_sword_medieval_c,itm_bayeux,],def_attrib2,wp(80),knows_archer_basic,swadian_face_young_1,swadian_face_old_2],

["swadian_crossbowman","French_Arbaletrier_Paysen","French_Arbaletrier_Paysens",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_kettlehat2,itm_kettlehat2,itm_kettlehat2_painted,itm_tattered_leather_armor_f1,itm_tattered_leather_armor_f2,itm_leather_gloves,itm_blue_hose,itm_blue_hose,itm_leather_boots,itm_heavy_crossbow,itm_heavy_crossbow,itm_bolts,itm_sword_medieval_a,itm_sword_medieval_a,itm_tab_shield_pavise_a,itm_tab_shield_pavise_b,itm_mace_2,itm_mace_4,],def_attrib2_b,wp(100),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],

["swadian_sharpshooter","French_Arbaletrier","French_Arbaletriers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_neutral,[itm_kettlehat2,itm_kettlehat2,itm_kettlehat2_painted,itm_brigandine_f1,itm_brigandine_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_sniper_crossbow,itm_bolts,itm_tab_shield_pavise_c,itm_sword_medieval_c,itm_sword_medieval_a,itm_sword_medieval_a,itm_mace_2,itm_mace_4,],def_attrib3,wp(120),knows_warrior_veteran,swadian_face_middle_2,swadian_face_old_2],

#Noble line
#French lances itm_banner_kite_plain_diamonds,itm_banner_kite_plain_lys,itm_banner_kite_plain_ermine,itm_banner_war_blue,itm_banner_war_horses,itm_banner_war_cross,itm_banner_war_eagle,itm_banner_heraldric_lys

["swadian_man_at_arms","French_Ecuyer","French_Ecuyers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_full_helm,itm_visored_sallet,itm_mail_coif,itm_open_sallet,itm_early_transitional_f2,itm_early_transitional_f3,itm_mail_chausses_f1,itm_splinted_greaves_nospurs,itm_splinted_leather_greaves,itm_mail_chausses_f1,itm_splinted_greaves_nospurs,itm_splinted_leather_greaves,itm_sword_medieval_a,itm_sword_medieval_c,itm_bastard_sword_a,itm_one_handed_battle_axe_c,itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b,itm_horse1f01,],def_attrib2_b,wp_melee(95),knows_warrior_normal,swadian_face_middle_1,swadian_face_older_2],

["swadian_knight","French_Chevalier_Bachelier","French_Chevalier_Bacheliers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_hounskull,itm_pigface_klappvisor,itm_pigface_klappvisor_open,itm_hounskull,itm_heraldic_churburg_13_brass_tabard,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_mittens,itm_hourglass_gauntlets,itm_shynbaulds,itm_mail_chausses,itm_mail_chausses_f1,itm_great_lance,itm_great_lanceblueyellow,itm_great_lanceblueyellow,itm_bastard_sword_a,itm_bayeux,itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b,itm_warhorse_f1,itm_warhorse_f2,itm_warhorse_f3,],def_attrib3,wp_melee(110),knows_warrior_veteran,swadian_face_middle_1,swadian_face_older_2],

["french_chevalier_banneret","French_Chevalier_Banneret","French_Chevalier_Bannerets",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_great_helmet,itm_hounskull,itm_pigface_klappvisor_open,itm_pigface_klappvisor,itm_bb_complet_plates_b,itm_bb_complet_plates_charles,itm_shynbaulds,itm_steel_greaves,itm_shynbaulds,itm_steel_greaves,itm_great_lance,itm_great_lanceblueyellow,itm_great_lancebluewhite,itm_lance_banner_f1,itm_bastard_sword_a,itm_bayeux,itm_agincourt,itm_great_lanceblueyellow,itm_great_lancebluewhite,itm_tab_shield_heater_cav_b,itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b,itm_warhorse_f2,itm_warhorse_f3,itm_warhorsechandos,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,swadian_face_middle_1,swadian_face_older_2],

["french_chevalier_lancier","Lancier_francais","Lancier_francais",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_bb_massivehelm_bp,itm_bb_armet2,itm_bb_armet,itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_steel_greaves,itm_steel_greaves,itm_weapon_lanceier_f1,itm_great_lancebluewhite,itm_great_lancebluewhite,itm_great_lanceblueyellow,itm_great_lanceblueyellow,itm_bastard_sword_b,itm_bayeux,itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b,itm_tab_shield_heater_cav_b,itm_chargerplainblue,itm_chargerred,],def_attrib3_b,wp_melee(140),knows_warrior_elite,swadian_face_middle_1,swadian_face_older_2],

["french_chevalier_bachelier_a_pied","French_Chevalier_Bachelier_a_Pied","French_Chevalier_Bachelier_a_Pieds",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_hounskull,itm_pigface_klappvisor,itm_klappvisier,itm_heraldic_churburg_13_brass_tabard,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_mittens,itm_hourglass_gauntlets,itm_shynbaulds,itm_mail_chausses,itm_lui_knightaxeonehe,itm_bastard_sword_a,itm_bastard_sword_b,itm_agincourt,itm_great_axe,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib3,wp_melee(110),knows_warrior_normal,swadian_face_young_1,swadian_face_old_2],

["french_chevalier_banneret_a_pied","French_Chevalier_Banneret_a_Pieds","French_Chevalier_Banneret_a_Pieds",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_pigface_klappvisor,itm_pigface_klappvisor_open,itm_hounskull,itm_great_helmet,itm_bb_complet_plates_b,itm_bb_complet_plates_charles,itm_steel_greaves,itm_shynbaulds,itm_steel_greaves,itm_shynbaulds,itm_agincourt,itm_bastard_sword_a,itm_one_handed_battle_axe_c,itm_tab_shield_heater_b,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,swadian_face_young_1,swadian_face_old_2],

["french_chevalier_lancier_a_pied","Lancier_francais_a_pieds","Lancier_francais_a_pieds",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_bb_armet,itm_bb_armet2,itm_bb_massivehelm_bp,itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_hourglass_gauntlets,itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_steel_greaves,itm_shynbaulds,itm_one_handed_war_axe_a,itm_lui_knightaxeonehe,itm_bastard_sword_a,itm_bastard_sword_b,itm_tab_shield_heater_b,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib3_b,wp_melee(140),knows_warrior_elite,swadian_face_young_1,swadian_face_old_2],

## END French Main Troops


["swadian_messenger", "French Messenger", "Swadian Messengers", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5, swadian_face_young_1, swadian_face_old_2 ],
["swadian_deserter", "French Deserter", "Swadian Deserters", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_deserters, [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet], def_attrib|level(14), wp(80), knows_common|knows_riding_2|knows_ironflesh_1, swadian_face_young_1, swadian_face_old_2 ],
["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,[itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_guard_helmet,itm_leather_gloves],def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1,swadian_face_old_2],
["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_neutral,[itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_guard_helmet,itm_leather_gloves],def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1,swadian_face_old_2],

["coulveriners_f", "Couleuvrinier Francais", "Couleuvriniers Francais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_matchlock_1,itm_cartridges,itm_woolen_hose,itm_brigandine_f1,itm_sword_medieval_a,itm_skullcap], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_power_draw_4|knows_athletics_4, 0x000000000010814036d26cbb59a5e6db00000000001db6db0000000000000000, 0x000000000010a20036d26cbb59a5e6db00000000001db6db0000000000000000 ],
["arquebusier_f", "Arquebusier Francais", "Arquebusiers Francais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_matchlock_2,itm_cartridges,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_brigandine_f1,itm_mail_chausses_f1,itm_woolen_hose,itm_mail_coif], def_attrib|level(22), wp(160), knows_common|knows_ironflesh_2|knows_power_draw_4|knows_athletics_3, 0x000000057f00c04436db6db6db6db6db00000000001db6db0000000000000000, 0x000000002210c00036d26cbb59a5e6db00000000001db6db0000000000000000 ],


## English Main Troops

#Infantry Line
["vaegir_recruit","English_Peasant","English_Peasants",tf_guarantee_boots|tf_guarantee_armor|tf_english,0,0,fac_neutral,[itm_straw_hat,itm_hood_e1,itm_coarse_tunic,itm_peasant_man_e1,itm_wrapping_boots,itm_woolen_hose,itm_pitch_fork,itm_awlpike_4,itm_ashwood_pike,itm_fauchard_2,itm_stones,itm_knife,itm_hatchet,itm_cleaver,],def_attrib,wp(60),knows_common_kham,0x000000000010000136d26cbb59a5e6db00000000001db6db0000000000000000,vaegir_face_middle_2],

["vaegir_footman","English_Town_Militia","English_Town_Militia",tf_guarantee_boots|tf_guarantee_armor|tf_english,0,0,fac_neutral,[itm_mail_coif,itm_mail_coif,itm_haubergeon_e1,itm_haubergeon_e2,itm_mail_mittens,itm_mail_mittens,itm_mail_chausses_e1,itm_mail_chausses_e1,itm_sword_medieval_a,itm_sword_medieval_c_small,itm_sword_medieval_c,itm_sword_medieval_c,itm_tab_shield_round_c,itm_tab_shield_kite_c,itm_tab_shield_kite_c,],def_attrib_b,wp(75),knows_warrior_basic,vaegir_face_young_1,vaegir_face_middle_2],

#has shield guarantee but no shield. To study.
["english_spearman","English_Levy_Spearman","English_Levy_Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_bascinet_3,itm_coif_new_e1,itm_hood_e1,itm_padded_cloth_b_e1,itm_padded_cloth_b_e2,itm_leather_gloves,itm_leather_boots,itm_woolen_hose,itm_woolen_hose,itm_spetum_3,itm_awlpike_5,itm_spetum_3,],def_attrib2,wp(80),knows_warrior_basic2,vaegir_face_younger_1,vaegir_face_middle_1],

["vaegir_veteran","English_Man-at-Arms","English_Men-at-Arms",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_kettlehat1,itm_kettlehat1_painted,itm_surcoat_over_mail_e4,itm_surcoat_over_mail_e4,itm_surcoat_over_mail_e1,itm_mail_mittens,itm_mail_mittens,itm_mail_chausses_e1,itm_mail_chausses_e1,itm_one_handed_war_axe_a,itm_bastard_sword_a,itm_bastard_sword_b,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_tab_shield_kite_c,],def_attrib2,wp(80),knows_warrior_basic2,vaegir_face_young_1,vaegir_face_older_2],

["english_pikeman","English_Armored_Sergeant","English_Armored_Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_kettlehat1_painted,itm_kettlehat1,itm_kettle_hat,itm_padded_cloth_b_e2,itm_padded_cloth_b_e1,itm_surcoat_over_mail_e4,itm_mail_mittens,itm_mail_mittens,itm_mail_chausses_e1,itm_mail_chausses_e1,itm_splinted_greaves_e1,itm_voulge_long,itm_voulge_long,itm_voulge_long,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib2_b,wp(140),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_2],

["english_halberdier","English_Billman","English_Billmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_english,0,0,fac_neutral,[itm_kettle_hat,itm_kettlehat1,itm_mail_coif,itm_churburg_13_mail,itm_churburg_13_e,itm_plate_mittens,itm_mail_mittens,itm_plate_mittens,itm_steel_greaves,itm_mail_chausses_e1,itm_spetum_3,itm_voulge_long,itm_fauchard_fork_2,itm_3glaive,itm_awlpike_5,],def_attrib2_b,wp(140),knows_warrior_normal,vaegir_face_younger_1,vaegir_face_older_1],

["vaegir_guard","English_Sergeant_At_Arms","English_Sergeants_At_Arms",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_bb_chivalhelm_vp,itm_bb_greathelm_rp,itm_greatbascinet1,itm_bb_complet_plates_r,itm_bb_complet_plates_rlyon,itm_wisby_gauntlets_red,itm_plate_mittens,itm_mail_mittens,itm_shynbaulds,itm_steel_greaves,itm_iron_greaves,itm_1halberd,itm_2halberd,itm_6halberd,itm_lui_smallhallberdb,],def_attrib2_b,wp(130),knows_warrior_normal,vaegir_face_young_1,vaegir_face_older_2],

["vaegir_infantry","Infanterie lourde Anglaise","Infanteries lourdes Anglaise",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_kettlehat1,itm_visored_sallet,itm_mail_coif,itm_open_sallet,itm_coat_of_plates_e1,itm_coat_of_plates_e2,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_chausses_e1,itm_splinted_greaves_e1,itm_one_handed_war_axe_a,itm_bastard_sword_a,itm_1mace,itm_one_handed_battle_axe_c,itm_tab_shield_small_round_c,itm_tab_shield_small_round_c,],def_attrib2_b,wp_melee(105),knows_warrior_normal,vaegir_face_young_1,0x000000000600004114db6d46db6db6db00000000001db6ec0000000000000000],

["vaegir_sergent","Sergent Anglais","Sergents Anglais",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_klappvisier,itm_pigface_klappvisor,itm_hounskull,itm_pigface_klappvisor,itm_sugarloaf,itm_bb_complet_plates_rlyon,itm_bb_complet_plates_rlyon,itm_bb_complet_plates_r,itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets,itm_shynbaulds,itm_steel_greaves,itm_4mace,itm_2hammer,itm_lui_knightaxeonehe,itm_one_handed_battle_axe_c,itm_bastard_sword_a,itm_tab_shield_heater_a,itm_tab_shield_heater_b,itm_battle_shieldedwardiii,itm_tab_shield_heater_a,itm_tab_shield_heater_a,],def_attrib3,wp_melee(155),knows_warrior_veteran,vaegir_face_middle_2,vaegir_face_older_2],



#Archer line
["english_peasant_crossbowman","English_Peasant_Crossbowman","English_Peasant_Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_english,0,0,fac_neutral,[itm_kettlehat2,itm_kettlehat1_painted,itm_brigandine_e1_c,itm_brigandine_e1,itm_leather_gloves,itm_splinted_greaves_e1,itm_light_crossbow,itm_bolts,itm_agincourt,itm_mace_4,itm_mace_3,],def_attrib_b,wp(75),knows_archer_basic,vaegir_face_young_2,vaegir_face_older_1],

["vaegir_skirmisher","English_Peasant_Archer","English_Peasant_Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_english,0,0,fac_neutral,[itm_leather_cap,itm_hood_e1,itm_padded_cloth_b_e1,itm_white_gambeson_e1,itm_leather_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_1mace,itm_spiked_club,itm_4mace,itm_1club,itm_fighting_pick,itm_agincourt,itm_mace_4,],def_attrib_b,wp(80),knows_archer_basic,0x000000000010504036d26cbb59a5e6db00000000001db6db0000000000000000,vaegir_face_middle_2],

["vaegir_archer","English_Yeomen_Archer","English_Yeomen_Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_english,0,0,fac_neutral,[itm_coif_new_e1,itm_hood_e1,itm_kettle_hat,itm_kettlehat1_painted,itm_guard_helmet,itm_padded_cloth_b_e1,itm_padded_cloth_b_e2,itm_leather_gloves,itm_leather_boots,itm_woolen_hose,itm_woolen_hose,itm_war_bow,itm_war_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_sword_medieval_b_small,itm_agincourt,itm_bayeux,itm_mace_4,],def_attrib2,wp(110),knows_archer_english,vaegir_face_younger_1,vaegir_face_old_2],

["vaegir_marksman","English_Longbowman","English_Longbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_english,0,0,fac_neutral,[itm_kettle_hat,itm_kettlehat1,itm_kettlehat2,itm_padded_jack_e,itm_padded_jack,itm_padded_jack_e,itm_leather_gloves,itm_splinted_greaves_e1,itm_splinted_greaves_nospurs,itm_long_bow,itm_khergit_arrows,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux,itm_bayeux,itm_bastard_sword_b],def_attrib3,wp(140),knows_archer_english_2,0x000000000010b0c036d26cbb59a5e6db00000000001db6db0000000000000000,vaegir_face_older_2],

# English Noble Line
#English lances >>> ,itm_banner_kite_metal_rose,itm_banner_kite_metal_squares,itm_banner_kite_plain_cross,itm_banner_war_red,itm_banner_war_trees,itm_banner_war_flowers,itm_banner_war_wales,itm_banner_heraldric_lions,itm_banner_heraldric_stripes

["vaegir_horseman","English_Squire","English_Squires",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_bascinet_2, itm_bascinet_3, itm_oniontop_bascinet, itm_open_sallet, itm_open_sallet_coif,itm_heraldic_mail_with_tunic_b, itm_heraldic_mail_with_tabard, itm_brigandine_e1, itm_brigandine_e1_c, itm_brigandine_e2,itm_leather_gloves, itm_mail_mittens,itm_splinted_leather_greaves, itm_mail_chausses, itm_mail_chausses_e1,itm_squire, itm_light_lance, itm_tab_shield_kite_cav_a,itm_horse6e01, itm_horse7e01, itm_horse8e01, itm_hunting_horsee01, itm_horse_bardede01, itm_horse_bardede02, itm_horse_bardede03,],def_attrib2_b,wp_melee(95),knows_warrior_normal,vaegir_face_young_2,vaegir_face_older_1],
["vaegir_knight","English_Knight","English_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_greatbascinet1, itm_klappvisier, itm_pigface_klappvisor_open,itm_early_transitional_e1,itm_early_transitional_e4,itm_early_transitional_heraldic,itm_early_transitional_orange,itm_wisby_gauntlets_red,itm_shynbaulds,itm_steel_greaves,itm_great_lanceredyellow,itm_great_lanceredwhite,itm_banner_kite_metal_rose,itm_banner_kite_metal_squares,itm_breton_lance,itm_sword_medieval_c,itm_heraldric_shieldred3lions,itm_heraldric_shieldredstripes,itm_heraldric_shieldredblack,itm_tab_shield_heater_cav_a,itm_warhorse_en1,itm_warhorse_en2,itm_warhorse_en3,],def_attrib3,wp_melee(110),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_older_2],
["english_heavy_knight","English_Heavy_Knight","English_Heavy_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_pigface_klappvisor,itm_bb_chivalhelm_vp,itm_corrazina_red,itm_churburg_13_e,itm_heraldic_churburg_13_tabard,itm_hourglass_gauntlets,itm_shynbaulds,itm_steel_greaves,itm_lance_e1,itm_lance_e2,itm_lance_banner_e1,itm_lance_banner_e2,itm_lance_banner_f2,itm_lance_banner_tut,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_warhorse3lions,itm_warhorseredwhite,itm_warhorseredyellow,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_old_2],
["saint_georges_knight","Order_Of_Saint_Georges_Knight","Order_Of_Saint_Georges_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_hounskull,itm_bb_chivalhelm_vp,itm_bb_greathelm_rp,itm_churburg_13_brass,itm_churburg_13_mail,itm_heraldic_churburg_13_brass_tabard,itm_bb_complet_plates_r,itm_bb_complet_plates_rlyon,itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets,itm_shynbaulds,itm_steel_greaves,itm_lance_6,itm_lance_e1,itm_lance_e2,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_chargerred,itm_chargerplainred,],def_attrib3_b,wp_melee(140),knows_warrior_elite,vaegir_face_middle_2,vaegir_face_older_2],
["english_longbowman_captain","English_Longbowman_Captain","English_Longbowman_Captains",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_english,0,0,fac_neutral,[itm_bb_noble_hat,itm_padded_jack,itm_padded_jack_e,itm_leather_armor_e2,itm_leather_gloves,itm_leather_boots,itm_khergit_arrows,itm_long_bow,itm_military_cleaver_c,itm_sarranid_mace_1,itm_steel_buckler1,],def_attrib3_b,wp(155),knows_weapon_master_10|knows_ironflesh_7|knows_athletics_7|knows_riding_4|knows_power_strike_6|knows_shield_4|knows_inventory_management_4|knows_power_throw_5|knows_power_draw_10,vaegir_face_middle_2,vaegir_face_older_2],
["english_captain","English_Captain","English_Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_open_sallet_coif,itm_heraldic_mail_with_tunic_b, itm_heraldic_mail_with_tabard, itm_early_transitional_e4,itm_mail_gauntlets,itm_iron_greaves,itm_splinted_greaves_spurs,itm_knight,itm_tab_shield_kite_cav_b,itm_horse1e01,],def_attrib3,wp_melee(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_2],
["three_lions_guard","Three_Lions_Guard","Three_Lions_Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_klappvisier,itm_early_transitional_e3,itm_mail_gauntlets,itm_iron_greaves,itm_knighthammerbastard,itm_sword_medieval_c,itm_heraldric_shieldred3lions,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_older_1],


## END English Main Troops


["vaegir_messenger","English Messenger","Vaegir Messengers",tf_english|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,[itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_deserter","English Deserter","Vaegir Deserters",tf_english|tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,[itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_prison_guard", "Prison Guard", "Prison Guards", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_coat_of_plates_e1,itm_mail_chausses,itm_iron_greaves,itm_open_sallet_coif,itm_leather_gloves], def_attrib|level(24), wp(130), knows_athletics_3|knows_shield_2|knows_ironflesh_3, 0x000000000f10214036db6db6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["vaegir_castle_guard", "Castle Guard", "Castle Guards", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english, no_scene, reserved, fac_neutral, [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_churburg_13_brass,itm_mail_chausses,itm_iron_greaves,itm_pigface_klappvisor,itm_leather_gloves], def_attrib|level(24), wp(130), knows_athletics_3|knows_shield_2|knows_ironflesh_3, 0x000000000010244036db6db6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["coulveriners_anglais", "Couleuvrinier anglais", "Couleuvrinier anglais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_english, no_scene, reserved, fac_neutral, [itm_matchlock_1,itm_cartridges,itm_woolen_hose,itm_brigandine_e2,itm_sword_medieval_a,itm_skullcap], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_power_draw_4|knows_athletics_4, 0x00000000001043c036db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],

## Burgandy Main Troops
#Infantry Line

["bourg_recruit","Recrue_Bourguignonne","Recrues_Bourguignonnes",tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon,0,0,fac_neutral,[itm_common_hood,itm_common_hood,itm_straw_hat,itm_coarse_tunic,itm_shirt,itm_woolen_hose,itm_leather_boots,itm_pitch_fork,itm_boar_spear,itm_scythe,itm_hammer,itm_pickaxe,itm_cleaver,itm_knife,itm_butchering_knife,itm_hatchet,itm_stones,],def_attrib,wp(60),knows_common_kham,0x000000000010640036db6db6db6db6db00000000001db6db0000000000000000,0x00000000001074c136db6db6db6db6db00000000001db6db0000000000000000],

["bourg_veteran","Veteran_Bourguignon","Veteran_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_mail_coif,itm_ragged_outfit,itm_leather_armor,itm_leather_gloves,itm_leather_boots,itm_mail_boots,itm_squire,itm_laird,itm_caithness,itm_fighting_axe,itm_one_handed_battle_axe_a,itm_tab_shield_kite_a,itm_tab_shield_kite_b,],def_attrib2,wp(80),knows_warrior_basic2,vaegir_face_young_1,vaegir_face_old_2],

["bourg_spearman","Vougier_Bourguignon","Vougiers_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_open_sallet_coif,itm_mail_coif,itm_leather_vest,itm_leather_armor,itm_leather_gloves,itm_leather_boots,itm_hunter_boots,itm_spear,itm_war_spear,itm_tab_shield_kite_a,itm_tab_shield_kite_b,],def_attrib2,wp(110),knows_warrior_normal,vaegir_face_younger_1,vaegir_face_older_1],

["bourg_pikeman","Piquier long Bourguignons","Piquiers long Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_nasal_helmet,itm_heraldic_churburg_13_tabard,itm_heraldic_churburg_13_tabard,itm_mail_gauntlets,itm_steel_greaves,itm_mail_boots,itm_voulge_long,itm_voulge_long,itm_voulge_long,],def_attrib2_b,wp(150),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_old_2],

["bourg_halberdier","Hallbardier_Bourguignon","Hallbardiers_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon,0,0,fac_neutral,[itm_open_sallet,itm_chapel_de_fer,itm_visored_sallet,itm_guard_helmet,itm_churburg_13_mail,itm_mail_mittens,itm_plate_mittens,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_2halberd,itm_6halberd,itm_lui_smallhallberda,],def_attrib2_b,wp(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_1],

["bourg_footman","Millicien_bourguignon","Milliciens_bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon,0,0,fac_neutral,[itm_skullcap,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_hunter_boots,itm_1mace,itm_1club,itm_1hammer,itm_2hammer,itm_fighting_pick,itm_gaddhjalt,itm_battle_fork,itm_spear,itm_iron_staff,itm_tab_shield_kite_a,itm_tab_shield_kite_b,],def_attrib2,wp(75),knows_warrior_basic2,vaegir_face_younger_1,vaegir_face_young_1],

["bourg_infantry","Infanterie lourde bourguignone","Infanteries lourdes bourguignones",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_visored_sallet,itm_nasal_helmet,itm_kettlehat1_painted,itm_open_sallet_coif,itm_heraldic_churburg_13_tabard,itm_heraldic_churburg_13_tabard,itm_plate_mittens,itm_hourglass_gauntlets,itm_shynbaulds,itm_mail_chausses,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib2_b,wp_melee(105),knows_warrior_normal,vaegir_face_young_1,vaegir_face_older_2],

["bourg_guard","Garde_Bourguignon","Gardes_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_bb_hounskull_yp,itm_greathelm1,itm_great_helmet,itm_bb_complet_plates_bourg,itm_bb_complet_plates_bourg,itm_bb_complet_plates_bourg,itm_churburg_13_mail,itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets_ornate,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_tab_shield_heater_b,itm_tab_shield_heater_b,],def_attrib2_b,wp_melee(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_middle_1],

["bourg_sergent","Garde du Duc","Gardes du Duc",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_bb_hounskull_yp,itm_greatbascinet1,itm_bb_complet_plates_bourg,itm_churburg_13_mail,itm_hourglass_gauntlets_ornate,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_bardiche,itm_great_bardiche,itm_long_axe_c,],def_attrib3,wp_melee(155),knows_warrior_veteran,vaegir_face_middle_2,vaegir_face_older_2],


#Ranged Line
["bourg_skirmisher","Archer_paysan_Borguignon","Archers_paysans_Borguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bourgignon,0,0,fac_neutral,[itm_leather_cap,itm_common_hood,itm_straw_hat,itm_shirt,itm_coarse_tunic,itm_leather_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_1mace,itm_spiked_club,itm_4mace,itm_1club,itm_fighting_pick,itm_agincourt,itm_mace_4],def_attrib_b,wp(80),knows_common_kham,vaegir_face_young_2,vaegir_face_old_1],

["bourg_peasant_crossbowman","Arbalitier_Bourguignon","Arbalitiers_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_bourgignon,0,0,fac_neutral,[itm_padded_cloth,itm_gambeson,itm_leather_gloves,itm_splinted_greaves_nospurs,itm_light_crossbow,itm_bolts,itm_agincourt,itm_mace_4,itm_mace_3,],def_attrib2,wp(75),knows_archer_basic,vaegir_face_younger_1,vaegir_face_middle_2],

["bourg_archer","Archer_Bourguignon","Archers_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bourgignon,0,0,fac_neutral,[itm_common_hood,itm_mail_coif,itm_mail_hauberk,itm_shirt,itm_leather_gloves,itm_ankle_boots,itm_leather_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_sword_medieval_b_small,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_bayeux,itm_mace_4,],def_attrib2_b,wp(110),knows_archer_english,vaegir_face_middle_2,vaegir_face_older_2],

["bourg_marksman","Archer_lourd_Bourguignon","Archers_lourds_Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon,0,0,fac_neutral,[itm_visored_sallet,itm_open_sallet,itm_surcoat_over_mail_brg1,itm_surcoat_over_mail_brg1,itm_leather_gloves,itm_steel_greaves,itm_mail_boots,itm_war_bow,itm_hunting_bow,itm_arrows,itm_templar,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux,itm_mace_4,],def_attrib3,wp(130),knows_archer_english,vaegir_face_young_1,vaegir_face_old_2],


#Burgandy Noble Line
["bourg_horseman","Burgundian_Horseman","Burgundian_Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_open_sallet_coif,itm_black_studded_leather_coat,itm_mail_mittens,itm_splinted_leather_greaves,itm_sword_medieval_b,itm_lance,itm_tab_shield_kite_cav_a,itm_horse1,itm_horse7,itm_horse8,],def_attrib2_b,wp_melee(95),knows_warrior_normal,vaegir_face_young_2,vaegir_face_older_1],
["bourg_knight","Burgundian Knight","Burgundian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_klappvisier,itm_visored_sallet_coif,itm_banded_armor,itm_cuir_bouilli,itm_heraldic_mail_with_tunic,itm_heraldic_mail_with_tabard,itm_surcoat_over_mail_brg1,itm_wisby_gauntlets_black,itm_shynbaulds,itm_steel_greaves,itm_sword_medieval_c,itm_breton_lance,itm_tab_shield_heater_cav_a,itm_warhorse,],def_attrib3,wp_melee(110),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_older_2],
["burgandy_heavy_knight","Burgandian_Heavy_Knight","Burgandian_Heavy_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_pigface_klappvisor,itm_visored_sallet_coif,itm_gothic_armour,itm_heraldic_churburg_13_tabard,itm_hourglass_gauntlets,itm_shynbaulds,itm_steel_greaves,itm_great_lance,itm_lance_3,itm_lance_5,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_warhorse,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_old_2],
["burgandy_iron_knight","Burgandian_Iron_Knight","Burgandian_Iron_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_hounskull,itm_bb_hounskull_yp,itm_churburg_13_mail,itm_heraldic_churburg_13_brass_tabard,itm_bb_complet_plates_bourg,itm_hourglass_gauntlets_ornate,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_great_lance,itm_lance_3,itm_lance_5,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_charger],def_attrib3_b,wp_melee(140),knows_warrior_elite,vaegir_face_middle_2,vaegir_face_older_2],
["burgandy_mounted_crossbowman_captain","Burgandian_Mounted_Crossbowman_Captain","Burgandian_Mounted_Crossbowman_Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon,0,0,fac_neutral,[itm_open_sallet_coif,itm_black_studded_leather_coat,itm_leather_gloves,itm_leather_boots,itm_light_crossbow,itm_steel_bolts,itm_steel_bolts,itm_sword_medieval_b,itm_steel_buckler1,itm_horse1,itm_horse7,itm_horse8,],def_attrib3_b,wp(155),knows_weapon_master_10|knows_ironflesh_7|knows_athletics_7|knows_riding_6|knows_power_strike_6|knows_shield_4|knows_inventory_management_4|knows_power_throw_5|knows_power_draw_10,vaegir_face_middle_2,vaegir_face_older_2],
["burgandy_captain","Burgundian_Captain","Burgundian_Captains",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_visored_sallet_coif,itm_black_brigandine,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_sword_medieval_c,itm_tab_shield_kite_cav_b,itm_warhorse,],def_attrib3,wp_melee(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_2],
["burgandy_elite_guard","Burgandian_Elite_Guard","Burgandian_Elite_Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_klappvisier,itm_visored_sallet_coif,itm_surcoat_over_mail_brg1,itm_wisby_gauntlets_black,itm_iron_greaves,itm_7halberd,itm_sword_medieval_c,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_older_1],


## END Burgandy Main Troops

["bourg_messenger", "Messager_Bourguignon", "Messagers Bourguignons", tf_bourgignon|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_deserter", "Deserteur_Bourguignon", "Deserteurs Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_deserters, [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_leather_vest,itm_leather_vest,itm_nomad_boots,itm_hunter_boots], def_attrib|str_10|level(14), wp(80), knows_ironflesh_1|knows_power_draw_1, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_prison_guard", "Garde_du_cachot_Bourguignon", "Gardes_du_cachot_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_bourgignon, no_scene, reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_coat_of_plates,itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_mail_chausses,itm_iron_greaves,itm_open_sallet_coif,itm_leather_gloves], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_2, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_castle_guard", "Garde_du_Donjon_Bourguignon", "Gardes du Donjon_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_bourgignon, no_scene, reserved, fac_neutral, [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_mail_chausses,itm_iron_greaves,itm_pigface_klappvisor,itm_surcoat_over_mail_brg1,itm_rawhide_coat,itm_leather_gloves], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],


##Breton Main Troops
#Infantry Line

["breton_recruit","Recrue_Bretonne","Recrues_Bretonnes",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,[itm_common_hood,itm_common_hood,itm_straw_hat,itm_breton_peasant_man,itm_breton_peasant_man,itm_woolen_hose,itm_leather_boots,itm_hammer,itm_pickaxe,itm_cleaver,itm_knife,itm_butchering_knife,itm_hatchet,itm_pitch_fork,itm_boar_spear,itm_scythe,itm_stones,],def_attrib,wp(60),knows_common_kham,0x000000000010640036db6db6db6db6db00000000001db6db0000000000000000,0x00000000001074c136db6db6db6db6db00000000001db6db0000000000000000],

["breton_veteran","Fantassin Breton","Fantassins Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,[itm_mail_coif,itm_chapel_de_fer,itm_mail_coif_full,itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_leather_gloves,itm_leather_boots,itm_splinted_greaves_nospurs,itm_mail_boots,itm_caithness,itm_squire,itm_laird,itm_caithness,itm_fighting_axe,itm_one_handed_battle_axe_a,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_heraldric_shieldblue3lys,itm_heraldric_shieldblue3lys,],def_attrib2,wp(110),knows_warrior_basic2,vaegir_face_young_1,vaegir_face_old_2],

["breton_spearman","Piquier Breton","Piquiers Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_neutral,[itm_mail_coif,itm_breton_mail_and_plate,itm_leather_vest,itm_breton_mail_and_plate,itm_leather_armor,itm_leather_gloves,itm_leather_boots,itm_hunter_boots,itm_spear,itm_war_spear,itm_tab_shield_kite_c,itm_tab_shield_kite_c,itm_heraldric_shieldblue3lys,itm_heraldric_shieldblue3lys,],def_attrib2,wp(110),knows_warrior_normal,vaegir_face_younger_1,vaegir_face_older_1],

["breton_pikeman","Coutillier Breton","Coutilliers Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_nasal_helmet,itm_chapel_de_fer,itm_klappvisier,itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_mail_gauntlets,itm_steel_greaves,itm_mail_boots,itm_voulge_long,itm_2glaive,itm_3glaive,itm_6halberd,],def_attrib2_b,wp(150),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_old_2],

["breton_halberdier","Fauchard Breton","Fauchard Breton",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves,0,0,fac_neutral,[itm_bb_greathelm_bp,itm_klappvisier,itm_pigface_klappvisor,itm_heraldic_churburg_13_tabard,itm_heraldic_churburg_13_tabard,itm_churburg_13_mail,itm_mail_mittens,itm_plate_mittens,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_bill,itm_fauchard_fork_2,itm_voulge_1,itm_voulge_3,],def_attrib2_b,wp(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_1],

["breton_footman","Millicien_Breton","Milliciens_Bretons",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_neutral,[itm_mail_coif_full,itm_skullcap,itm_breton_mail_and_plate,itm_leather_vest,itm_breton_mail_and_plate,itm_hide_boots,itm_nomad_boots,itm_hunter_boots,itm_agincourt,itm_1mace,itm_1club,itm_1hammer,itm_2hammer,itm_gaddhjalt,itm_battle_fork,itm_spear,itm_iron_staff,itm_agincourt,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_tab_shield_round_d,],def_attrib_b,wp(85),knows_warrior_basic,vaegir_face_younger_1,vaegir_face_young_1],

["breton_guard","Fantassin lourd Breton","Fantassins lourds Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_klappvisier,itm_corrazina_breton,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight,itm_tab_shield_heater_a,itm_tab_shield_heater_a,],def_attrib2_b,wp(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_middle_1],

["breton_infantry","Epeiste Breton","Epeistes Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_klappvisier,itm_pigface_klappvisor,itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_hourglass_gauntlets,itm_plate_mittens,itm_hourglass_gauntlets,itm_shynbaulds,itm_mail_chausses,itm_baron,itm_duke,itm_count,],def_attrib2_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_1,vaegir_face_older_2],

["breton_sergent","Sergent Breton","Sergents Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_bb_armet2,itm_pigface_klappvisor,itm_heraldic_churburg_13_tabard,itm_heraldic_churburg_13_tabard,itm_churburg_13_mail,itm_hourglass_gauntlets_ornate,itm_shynbaulds,itm_steel_greaves,itm_plate_mittens,itm_baron,itm_count,itm_duke,itm_duke,itm_duke,],def_attrib3,wp_melee(155),knows_warrior_veteran,vaegir_face_middle_2,vaegir_face_older_2],


#Ranged Line

["breton_skirmisher","Archer_paysan_Breton","Archers_paysans_Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_leather_cap,itm_common_hood,itm_straw_hat,itm_breton_peasant_man,itm_coarse_tunic,itm_breton_peasant_man,itm_leather_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_1mace,itm_spiked_club,itm_4mace,itm_1club,itm_fighting_pick,itm_agincourt,itm_mace_4,],def_attrib_b,wp(85),knows_common_kham,vaegir_face_young_2,vaegir_face_old_1],

["breton_peasant_crossbowman","Archer Breton lourd","Archers Bretons lourds",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_neutral,[itm_breton_peasant_man,itm_padded_cloth,itm_breton_peasant_man,itm_splinted_greaves_nospurs,itm_leather_gloves,itm_short_bow,itm_short_bow,itm_arrows,itm_arrows,itm_agincourt,itm_mace_4,itm_mace_3,itm_gaddhjalt,itm_gaddhjalt,],def_attrib2,wp(125),knows_archer_basic,vaegir_face_younger_1,vaegir_face_middle_2],

["breton_archer","Archer_Breton","Archers_Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_neutral,[itm_common_hood,itm_mail_coif,itm_breton_mail_and_plate,itm_breton_mail_and_plate,itm_leather_gloves,itm_ankle_boots,itm_leather_boots,itm_hunting_bow,itm_short_bow,itm_arrows,itm_caithness,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_bayeux,itm_caithness,itm_mace_4,],def_attrib2_b,wp(115),knows_archer_english,vaegir_face_middle_2,vaegir_face_older_2],

["breton_marksman","Franc Archer Breton","Francs Archers Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,[itm_chapel_de_fer,itm_chapel_de_fer,itm_nasal_helmet,itm_mail_coif_full,itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_heraldric_shieldblue3lys,itm_wisby_gauntlets_black,itm_mail_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_mail_boots,itm_war_bow,itm_hunting_bow,itm_arrows,itm_templar,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux,],def_attrib3,wp(125),knows_archer_english_2,0x000000000010b0c036d26cbb59a5e6db00000000001db6db0000000000000000,vaegir_face_older_2],



#Breton Noble Line
["breton_horseman","Breton_Squire","Breton_Squires",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_footman_helmet,itm_mail_coif_full,itm_breton_mail_and_plate,itm_leather_gloves,itm_splinted_leather_greaves,itm_lance,itm_sword_medieval_b,itm_tab_shield_kite_cav_a,itm_horse1,itm_horse6,itm_horse7,itm_horse8,],def_attrib2_b,wp_melee(95),knows_warrior_normal,vaegir_face_young_2,vaegir_face_older_1],
["breton_knight","Breton_Knight","Breton_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_greatbascinet1,itm_klappvisier,itm_pigface_klappvisor_open,itm_early_transitional_teu,itm_early_transitional_heraldic,itm_wisby_gauntlets_black,itm_shynbaulds,itm_steel_greaves,itm_breton_lance,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,itm_warhorse,itm_breton_war_horse,],def_attrib3,wp_melee(110),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_older_2],
["breton_heavy_knight","Breton_Heavy_Knight","Breton_Heavy_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_greatbascinet1,itm_klappvisier,itm_pigface_klappvisor,itm_pigface_klappvisor_open,itm_early_transitional_heraldic,itm_heraldic_churburg_13_tabard,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_shynbaulds,itm_steel_greaves,itm_lance_2,itm_lance_3,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_a,itm_breton_warhorse_2,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_old_2],
["breton_hermine_knight","Order_Of_The_Ermine_Knight","Order_Of_The_Ermine_Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_pigface_klappvisor,itm_bb_greathelm_bp,itm_heraldic_churburg_13_tabard,itm_breton_complet_plates,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_shynbaulds,itm_steel_greaves,itm_weapon_lanceier_f2,itm_sword_medieval_d_long,itm_tab_shield_heater_cav_b,itm_warhorse_sarranid,],def_attrib3_b,wp_melee(140),knows_warrior_elite,vaegir_face_middle_2,vaegir_face_older_2],
["breton_noble_swordsman","Breton_Noble_Swordsman","Breton_Noble_Swordsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_splinted_greaves_nospurs,itm_baron,],def_attrib3_b,wp(155),knows_warrior_elite,vaegir_face_middle_2,vaegir_face_older_2],
["breton_noble","Breton_Noble","Breton_Nobles",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_neutral,[itm_bascinet_2,itm_bascinet_3,itm_oniontop_bascinet,itm_breton_mail_and_plate,itm_mail_mittens,itm_mail_chausses,itm_heavy_lance,itm_sword_medieval_b,itm_tab_shield_kite_cav_b,itm_breton_war_horse,],def_attrib3,wp_melee(120),knows_warrior_normal,vaegir_face_young_2,vaegir_face_old_2],
["breton_honour_guard","Breton_Honour_Guard","Breton_Honour_Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_bascinet_2,itm_bascinet_3,itm_oniontop_bascinet,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_splinted_greaves_nospurs,itm_boar_spear,itm_sword_medieval_c,itm_kite_shieldreddragon,],def_attrib3_b,wp_melee(120),knows_warrior_veteran,vaegir_face_young_2,vaegir_face_older_1],


## END Breton Main Troops


["breton_messenger", "Messager_Breton", "Messagers Bretons", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5, vaegir_face_young_1, vaegir_face_older_2 ],
["breton_deserter", "Deserteur_Breton", "Deserteurs Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_deserters, [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_leather_vest,itm_leather_vest,itm_nomad_boots,itm_hunter_boots], def_attrib|str_10|level(14), wp(80), knows_ironflesh_1|knows_power_draw_1, vaegir_face_young_1, vaegir_face_older_2 ],
["breton_prison_guard", "Garde_du_cachot_Breton", "Gardes_du_cachot_Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_heraldric_shieldblue3lys,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_mail_gauntlets,itm_mail_gauntlets,itm_mail_boots,itm_mail_boots,itm_caithness,itm_caithness,itm_gaddhjalt], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_2, vaegir_face_young_1, vaegir_face_older_2 ],
["breton_castle_guard", "Garde_du_Donjon_Breton", "Gardes du Donjon_Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],

########## 1429 Faction Troops END - Kham ###################

## Crane de Fer Troops
["crane_de_fer_sergent","Sergent de la Compagnie des Cranes de Fer","Sergents de la Compagnie des Cranes de Fer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_klappvisier,itm_corrazina_breton,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight,itm_tab_shield_heater_a,itm_tab_shield_heater_a,],def_attrib3,wp(130),knows_warrior_veteran,vaegir_face_young_1,vaegir_face_older_2],

["crane_de_fer_archer","Archer de la Compagnie des Cranes de Fer","Archers de la Compagnie des Cranes de Fer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_neutral,[itm_chapel_de_fer,itm_chapel_de_fer,itm_nasal_helmet,itm_mail_coif_full,itm_corrazina_breton,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_mail_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_mail_boots,itm_war_bow,itm_hunting_bow,itm_arrows,itm_templar,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux,],def_attrib3_b,wp(135),knows_archer_english_2,vaegir_face_middle_2,vaegir_face_older_2],

["crane_de_fer_fantassin","Fantassin de la Compagnie des Cranes de Fer","Fantassins de la Compagnie des Cranes de Fer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_klappvisier,itm_corrazina_breton,itm_corrazina_breton,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight,itm_tab_shield_heater_a,itm_tab_shield_heater_a,],def_attrib3,wp(130),knows_warrior_veteran,vaegir_face_younger_1,vaegir_face_middle_2],


## Bandits
["looter","Looter","Looters",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_woolen_cap,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_rawhide_coat,itm_tabard,itm_ragged_outfit,itm_wrapping_boots,itm_woolen_hose,itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_stones,],def_attrib_b,wp(20),knows_common_kham,bandit_face1,bandit_face2],
["bandit","Bandit","Bandits",tf_bandit|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_outlaws,[itm_leather_cap,itm_rawhide_coat,itm_leather_jerkin,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_arrows,itm_nordic_shield,itm_saddle_horse],def_attrib_b,wp(60),knows_warrior_basic,bandit_face1,bandit_face2],
["brigand","Brigand","Brigands",tf_bandit|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,[itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_arrows,itm_wooden_shield,itm_woodenbuckler,itm_long_bow,itm_saddle_horse,],def_attrib2,wp(90),knows_warrior_basic,bandit_face1,bandit_face2],
###
["mountain_bandit","écorcheur","écorcheurs",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_klappvisier,itm_greathelm1,itm_mail_coif,itm_banded_armor,itm_coat_of_plates,itm_early_transitional_teu,itm_haubergeon,itm_cuir_bouilli,itm_plate_mittens,itm_mail_gauntlets,itm_mail_chausses,itm_splinted_greaves_nospurs,itm_mace_4,itm_bastard_sword_c,itm_sword_medieval_c_long,itm_heraldric_shieldredblack,itm_tab_shield_kite_c,itm_war_shieldeagle,],def_attrib2_b,wp(90),knows_warrior_basic,0x000000000000000026db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000],
["mountain_bandit_2","écorcheur Archer","écorcheurs Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bandit,0,0,fac_outlaws,[itm_mail_coif,itm_leather_gloves,itm_wrapping_boots,itm_woolen_hose,itm_short_bow,itm_hunting_bow,itm_arrows,itm_khergit_arrows,itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_sword_medieval_c_small,],def_attrib2_b,wp(90),knows_archer_basic,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000],
["mountain_bandit_3","écorcheur Vougier","écorcheurs Vougiers",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_mail_coif,itm_nasal_helmet,itm_mail_hauberk,itm_studded_leather_coat,itm_leather_jerkin,itm_plate_mittens,itm_mail_mittens,itm_mail_chausses,itm_mail_boots,itm_leather_boots,itm_voulge_long,itm_voulge_long,itm_jam_scorpion,itm_spetum_3,itm_voulge_long,],def_attrib2,wp(90),knows_warrior_basic,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000],
###
["forest_bandit","routier","routiers",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_guard_helmet,itm_visored_sallet,itm_kettle_hat,itm_kettlehat2,itm_visored_sallet,itm_aketon_green,itm_aketon_green,itm_padded_jack,itm_leather_gloves,itm_plate_mittens,itm_woolen_hose,itm_woolen_hose,itm_awlpike_5,itm_awlpike_5,itm_awlpike_5,itm_sword_medieval_c,],def_attrib2,wp(90),knows_warrior_basic,swadian_face_young_1,swadian_face_old_2],
["forest_bandit_2","routier Archer","routiers Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bandit,0,0,fac_outlaws,[itm_visored_sallet,itm_open_sallet,itm_skullcap,itm_padded_jack,itm_padded_jack,itm_white_gambeson_f1,itm_aketon_green,itm_plate_mittens,itm_hourglass_gauntlets_ornate,itm_woolen_hose,itm_mail_boots,itm_ankle_boots,itm_crossbow,itm_heavy_crossbow,itm_short_bow,itm_hunting_bow,itm_bolts,itm_arrows,itm_sword_medieval_a,itm_bayeux,itm_1mace,itm_heraldric_shieldredblack,itm_heraldric_shieldredblack,itm_heraldric_shieldblue3lys,],def_attrib2,wp(90),knows_archer_basic,0x0000000d0008500048d575db1c39d76400000000001cca950000000000000000,swadian_face_old_2],
###
["sea_raider","Sea Raider","Sea Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_bandit,0,0,fac_outlaws,[itm_leather_cap,itm_skullcap,itm_common_hood,itm_leather_vest,itm_leather_jerkin,itm_leather_armor,itm_leather_gloves,itm_leather_boots,itm_hunter_boots,itm_hide_boots,itm_bastard_sword_a,itm_bastard_sword_b,itm_sword_medieval_c,itm_wooden_buckler1,itm_woodenbuckler,],def_attrib2,wp(110),knows_warrior_basic2,nord_face_young_1,0x000000003010a5cb48ad724ce16da71a00000000001d550c0000000000000000],
["sea_raider_2","retondeur Archer","retondeurs Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_bandit,0,0,fac_outlaws,[itm_common_hood,itm_leather_cap,itm_kettlehat2,itm_leather_armor,itm_leather_jerkin,itm_leather_vest,itm_leather_gloves,itm_hide_boots,itm_hunter_boots,itm_leather_boots,itm_short_bow,itm_short_bow,itm_arrows,itm_cleaver,itm_military_cleaver_c,],def_attrib2,wp(110),knows_archer_basic,nord_face_young_1,0x000000003010a5cb48ad724ce16da71a00000000001d550c0000000000000000],
###
["steppe_bandit","Plundering Bandit","Plundering Bandits",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_nasal_helmet,itm_mail_coif,itm_leather_vest,itm_padded_jack,itm_mail_hauberk,itm_padded_jack,itm_shirt,itm_hide_boots,itm_nomad_boots,itm_ashwood_pike,itm_voulge_long,itm_voulge_long,itm_voulge_long,itm_ashwood_pike,],def_attrib2,wp(140),knows_warrior_basic2,0x000000089710a580489c724ce16da71a00000000001d550c0000000000000000,0x0000000d0008500048d575db1c39d76400000000001cca950000000000000000],
###
["taiga_bandit","Tard Venu","Tard Venus",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_bascinet_3,itm_common_hood,itm_guard_helmet,itm_head_wrappings,itm_kettlehat1,itm_padded_jack,itm_banded_armor,itm_haubergeon,itm_haubergeon,itm_leather_jerkin,itm_mail_gauntlets,itm_leather_gloves,itm_woolen_hose,itm_ankle_boots,itm_nomad_boots,itm_sword_medieval_a,itm_one_handed_war_axe_a,itm_great_axe,itm_wooden_buckler1,itm_woodenbuckler,itm_tab_shield_round_d,],def_attrib2,wp(110),knows_warrior_basic2,0x000000000d045482298c84bb0db0c92200000000001ec49b0000000000000000,0x000000000d046589298c84bb0db0c92200000000001ec49b0000000000000000],
["taiga_bandit_2","Tard Venu Archer","Tard Venu Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bandit,0,0,fac_outlaws,[itm_guard_helmet,itm_head_wrappings,itm_kettle_hat,itm_mail_coif,itm_tabard,itm_short_tunic,itm_mail_hauberk,itm_leather_jerkin,itm_leather_armor,itm_woolen_hose,itm_nomad_boots,itm_hide_boots,itm_woolen_hose,itm_woolen_hose,itm_war_bow,itm_light_crossbow,itm_crossbow,itm_short_bow,itm_barbed_arrows,itm_arrows,itm_bolts,itm_bolts,itm_sword_medieval_a,itm_wooden_buckler1,],def_attrib2,wp(110),knows_archer_basic,0x000000000004758a36db6db6db6db6db00000000001db6db0000000000000000,vaegir_face_old_2],
["taiga_bandit_3","Tard Venu Vougier","Tard Venus Vougiers",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_outlaws,[itm_leather_cap,itm_head_wrappings,itm_common_hood,itm_mail_hauberk,itm_linen_tunic,itm_coarse_tunic,itm_aketon_green,itm_leather_gloves,itm_woolen_hose,itm_woolen_hose,itm_blue_hose,itm_voulge_long,itm_voulge_long,itm_voulge_long,itm_spetum_3,],def_attrib2,wp(110),knows_warrior_basic2,vaegir_face_young_1,0x00000000000485cb36db6db6db6db6db00000000001db6db0000000000000000],
###
["desert_bandit","Desert Bandit","Desert Bandits",tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,[itm_leather_steppe_cap_b,itm_arabian_sword_a,itm_winged_mace,itm_spear,itm_light_lance,itm_jarid,itm_arrows,itm_nomad_bow,itm_short_bow,itm_jarid,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a,],def_attrib_b,wp(100),knows_archer_basic,khergit_face_young_1,khergit_face_old_2],
###
["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemans",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,[itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_hide_boots,itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a,itm_saddle_horse,itm_steppe_horse,],def_attrib2_b,wp(100),knows_warrior_basic2,khergit_face_young_1,khergit_face_old_2],
###
["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,[itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_nomad_boots,itm_wrapping_boots,itm_mace_3,itm_winged_mace,itm_wooden_shield,itm_sumpter_horse,],def_attrib_b,wp(50),knows_warrior_basic,bandit_face1,bandit_face2],

### Bandits END

## Slave Driver
["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_slavers,[itm_segmented_helmet,itm_tribal_warrior_outfit,itm_leather_gloves,itm_khergit_leather_boots,itm_leather_boots,itm_club_with_spike_head,itm_nordic_shield,itm_steppe_horse,],def_attrib2,wp(80),knows_warrior_normal,bandit_face1,bandit_face2],
["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_slavers,[itm_kettle_hat,itm_mail_shirt,itm_leather_gloves,itm_leather_boots,itm_winged_mace,itm_maul,itm_tab_shield_round_c,itm_courser,itm_hunter,],def_attrib2_b,wp(90),knows_warrior_normal,bandit_face1,bandit_face2],
["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_slavers,[itm_bascinet_2,itm_bascinet_3,itm_mail_hauberk,itm_mail_mittens,itm_mail_chausses,itm_splinted_leather_greaves,itm_sledgehammer,itm_spiked_mace,itm_tab_shield_round_d,itm_hunter,],def_attrib2_b,wp(110),knows_warrior_veteran,bandit_face1,bandit_face2],
["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,[itm_guard_helmet,itm_brigandine_red,itm_scale_gauntlets,itm_mail_mittens,itm_plate_boots,itm_mail_boots,itm_military_hammer,itm_warhammer,itm_steel_shield,itm_warhorse,],def_attrib3,wp(130),knows_warrior_veteran,bandit_face1,bandit_face2],



## Avenger Line
["follower_woman","Apprenti combattant","Apprenti combattants",tf_male|tf_guarantee_armor,0,0,fac_commoners,[itm_skullcap,itm_shirt,itm_leather_vest,itm_nomad_boots,itm_wrapping_boots,itm_bolts,itm_crossbow,itm_hand_axe,itm_voulge,itm_nordic_shield,itm_woodenbuckler,],def_attrib,wp(70),knows_common_kham,0x00000000140453c5275949b75566b56600000000001dc2da0000000000000000,man_face_young_2],
["hunter_woman","deffenseur","deffenseurs",tf_male|tf_guarantee_armor,0,0,fac_commoners,[itm_skullcap,itm_leather_jerkin,itm_leather_armor,itm_nomad_boots,itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_nordic_shield,itm_woodenbuckler,],def_attrib_b,wp(85),knows_warrior_basic,0x000000003f04d14536db6db6db6db6db00000000000db6db0000000000000000,man_face_young_2],
["fighter_woman","Vengeur","Vengeurs",tf_male|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_skullcap,itm_mail_shirt,itm_mail_hauberk,itm_wrapping_boots,itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_hatchet,itm_voulge,itm_woodenbuckler,],def_attrib2,wp(100),knows_warrior_basic2,0x000000003f0404c5275949b75566356600000000001dc2da0000000000000000,man_face_young_2],
["sword_sister","heros incoruptible","heros incoruptibles",tf_male|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_commoners,[itm_greatbascinet1,itm_pigface_klappvisor_open,itm_gothic_armour,itm_hourglass_gauntlets,itm_steel_greaves,itm_bolts,itm_darkknightsword,itm_estoc,itm_sword_of_war,itm_crossbow,itm_tab_shield_kite_cav_a,itm_warhorse,],def_attrib2_b,wp(140),knows_warrior_normal,0x000000003f0414c5275949b75566356600000000001dc2da0000000000000000,man_face_young_2],



["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,[itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress,itm_headcloth,itm_wrapping_boots],def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
["peasant_woman", "paysant revolte", "paysant revolte", tf_male|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_wrapping_boots,itm_hide_boots,itm_woolen_hose], def_attrib|level(1), wp(40), knows_common, 0x000000087210419067648cdd736da52c00000000001ee5220000000000000000 ],


["caravan_master", "Caravan Master", "Caravan Masters", tf_mounted|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_leather_apron,itm_leather_apron,itm_leather_boots,itm_leather_boots,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_sword_medieval_c,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_arrows,itm_arrows,itm_book_weapon_mastery,itm_sword_of_war,itm_sword_of_war,itm_sword_medieval_a,itm_cheese,itm_cheese,itm_cheese,itm_raw_olives,itm_raw_olives,itm_butter,itm_butter,itm_smoked_fish,itm_smoked_fish,itm_leather_boots,itm_leather_boots,itm_torch,itm_torch,itm_torch], def_attrib|level(9), wp(100), knows_common|knows_riding_4|knows_ironflesh_3|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,[itm_dress,itm_leather_boots],def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1,woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
["town_walker_1", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_short_tunic,itm_g_tw_shirt,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, 0x000000003f04018556db6d35244636db00000000001db69b0000000000000000, man_face_old_2 ],
["town_walker_2", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_blue_dress,itm_blue_dress_tw,itm_blue_dress_tw2,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
["khergit_townsman", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_kingdom_1, [itm_wrapping_boots,itm_khergit_leather_boots,itm_short_tunic,itm_short_tunic], def_attrib|level(4), wp(60), knows_common, 0x000000003f04118756db6d35244636db00000000001db69b0000000000000000, 0x000000002404230d56db6d35244636db00000000001db69b0000000000000000 ],
["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_blue_dress,itm_dress,itm_woolen_dress,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,[itm_wrapping_boots,itm_short_tunic,itm_tabard],def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1,swadian_face_middle_2],
["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_green_dress,itm_green_dress,itm_woolen_hose],def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as town_walkers_end and village_walkers_begin
["village_walker_1", "Villager", "Villagers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_leather_vest,itm_leather_apron,itm_shirt,itm_tabard,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, man_face_younger_1, man_face_older_2 ],
["village_walker_2", "Villager", "Villagers", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_blue_dress,itm_blue_dress_tw2,itm_peasant_dress,itm_blue_dress_tw,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood], def_attrib|level(2), wp(40), knows_common, 0x000000000400200324da81a6dd6ca6d200000000001dc7130000000000000000, 0x000000000608300137774ab79a6a18c4000000000008c4e10000000000000000 ],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
["spy_walker_1", "Townsman", "Townsmen", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, [itm_short_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, man_face_middle_1, man_face_old_2 ],
["spy_walker_2", "Townswoman", "Townswomen", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, [itm_blue_dress,itm_peasant_dress,itm_blue_dress_tw2,itm_blue_dress_tw,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
["tournament_master", "Tournament Master", "Tournament Master", tf_hero, scn_zendar_center|entry(1), reserved, fac_commoners, [itm_nomad_armor,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x000000002404530f56db6d35244636db00000000001db69b0000000000000000 ],
["trainer", "Trainer", "Trainer", tf_hero, scn_zendar_center|entry(2), reserved, fac_commoners, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x0000000a240473cf56db6d35244636db00000000001db69b0000000000000000 ],
["Constable_Hareck", "Constable Hareck", "Constable Hareck", tf_hero, scn_zendar_center|entry(5), reserved, fac_commoners, [itm_leather_jacket,itm_hide_boots], def_attrib|level(5), wp(20), knows_common, 0x000000002404844f56db6d35244636db00000000001db69b0000000000000000 ],

# Ryan BEGIN
["Ramun_the_slave_trader", "Ramun, the slave trader", "Ramun, the slave trader", tf_hero, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_hide_boots], def_attrib|level(5), wp(20), knows_common, 0x000000002404a59056db6d35244636db00000000001db69b0000000000000000 ],

["guide", "Quick Jimmy", "Quick Jimmy", tf_hero, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000002404b59056db6d35244636db00000000001db69b0000000000000000 ],
# Ryan END

["Xerina", "Xerina", "Xerina", tf_female|tf_hero, scn_the_happy_boar|entry(5), reserved, fac_commoners, [itm_leather_jerkin,itm_hide_boots], def_attrib|str_15|agi_30|level(39), wp(312), knows_power_strike_5|knows_ironflesh_10|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_10, 0x0000000023102007408b49f95b48bb8c0000000000199ccb0000000000000000 ],
["Dranton", "Dranton", "Dranton", tf_hero, scn_the_happy_boar|entry(2), reserved, fac_commoners, [itm_leather_vest,itm_hide_boots], def_attrib|str_25|agi_20|level(42), wp(324), knows_power_strike_5|knows_ironflesh_10|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_10, 0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000 ],
["Kradus", "Kradus", "Kradus", tf_hero, scn_the_happy_boar|entry(3), reserved, fac_commoners, [itm_padded_leather,itm_hide_boots], def_attrib|str_30|agi_17|level(43), wp(270), knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3, 0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000 ],


#Tutorial
["tutorial_trainer", "Training Ground Master", "Training Ground Master", tf_hero, no_scene, reserved, fac_commoners, [itm_robe,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003604c00f56db6d35244636db00000000001db69b0000000000000000 ],
["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_sword,itm_practice_shield,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_sword,itm_practice_shield,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_staff,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],
["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,[itm_practice_staff,itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],def_attrib|level(2),wp(20),knows_common,swadian_face_young_1,swadian_face_old_2],

#Sargoth
#halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
["Galeas", "Galeas", "Galeas", tf_hero, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_hide_boots], def_attrib|level(5), wp(20), knows_common, 0x000000003604d04f56db6d35244636db00000000001db69b0000000000000000 ],

#Dhorak keep

["farmer_from_bandit_village", "Farmer", "Farmers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(4), wp(60), knows_common, 0x000000003604004f56db6d35244636db00000000001db69b0000000000000000, man_face_older_2 ],

["trainer_1", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_1|entry(6), reserved, fac_commoners, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003604104f56db6d35244636db00000000001db69b0000000000000000 ],
["trainer_2", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_2|entry(6), reserved, fac_commoners, [itm_nomad_vest,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000360420c956db6d35244636db00000000001db69b0000000000000000 ],
["trainer_3", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_3|entry(6), reserved, fac_commoners, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003604818056db6e35244636db00000000001db69b0000000000000000 ],
["trainer_4", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_4|entry(6), reserved, fac_commoners, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000057604535356db6e35244636db00000000001db69b0000000000000000 ],
["trainer_5", "Trainer", "Trainer", tf_hero, scn_training_ground_ranged_melee_5|entry(6), reserved, fac_commoners, [itm_leather_vest,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000037604839356db6e35244636db00000000001db69b0000000000000000 ],

# Ransom brokers.
["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,itm_book_tactics,itm_book_persuasion,itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_training_reference,itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,itm_book_wound_treatment_reference,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_engineering,itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern minstrel.
["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dedal_lira,itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dedal_lutnia,itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dedal_lutnia,itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dedal_lutnia,itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_dedal_lira,itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

#["musican_male","H","Habitant du bourg",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_dedal_lutnia,itm_short_tunic,itm_g_tw_shirt,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat],def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
#["musican_female","Villageois","Villageois",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_dedal_lutnia,itm_short_tunic,itm_linen_tunic,itm_tabard,itm_woolen_hose,itm_blue_hose],def_attrib|level(2),wp(40),knows_common,man_face_young_1,man_face_young_2],
#["musicans_end","Villageois","Villageois",tf_inactive|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_dedal_lira,itm_shirt,itm_linen_tunic,itm_tabard,itm_woolen_hose,itm_blue_hose],def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
#NPC system changes begin
#Companions
["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(380),knows_lord_1, 0x000000000010918a01f248377289467d],

["npc1", "Ulrich", "Ulrich", tf_hero|tf_mounted, no_scene, reserved, fac_commoners, [itm_horse1f01,itm_caithness,itm_heraldric_shieldblue3lys,itm_woolen_hose,itm_red_shirt], str_10|agi_7|int_9|cha_7|level(7), wp(80), knows_warrior_npc|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2|knows_riding_3, 0x000000001b00b504251b893ae265249b00000000001e36db0000000000000000 ],
["npc2", "Roland de Paris", "Roland de Paris", tf_hero, no_scene, reserved, fac_commoners, [itm_early_transitional_heraldic,itm_light_leather_boots,itm_sword_medieval_a,itm_courser], str_9|agi_9|int_6|cha_6|level(6), wp(100), knows_warrior_npc|knows_riding_3|knows_weapon_master_1|knows_ironflesh_1|knows_power_strike_2|knows_athletics_2|knows_tactics_1|knows_leadership_1, 0x00000009ff01218a251b89c6dca6491a00000000001e36db0000000000000000 ],
["npc3", "Enguerrand", "Enguerrand", tf_hero|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_squire,itm_blue_gambeson], str_8|agi_9|int_12|cha_6|level(6), wp(70), knows_warrior_npc|knows_power_strike_1|knows_tactics_4|knows_first_aid_2|knows_athletics_1|knows_riding_2, 0x000000077f00104f24dc71bb6bc548db00000000001da7240000000000000000 ],
["npc4", "Gaspard", "Gaspard", tf_hero, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_nomad_boots,itm_sword_medieval_a], str_10|agi_9|int_13|cha_10|level(10), wp(110), knows_warrior_npc|knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2, 0x000000095b008380251b8a3ae265249b00000000001e36db0000000000000000 ],
["npc5", "Hermance de Bordeaux", "Hermance de Bordeaux", tf_hero, no_scene, reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_sword_of_war], str_9|agi_9|int_12|cha_7|level(5), wp(90), knows_warrior_npc|knows_riding_2|knows_horse_archery_3|knows_power_draw_3|knows_leadership_2|knows_weapon_master_1|knows_trade_5, 0x000000001000310826db8dbce5a9a2cb00000000001e36eb0000000000000000 ],
["npc6", "Guillaume", "Guillaume", tf_hero, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_woolen_hose,itm_knight], str_10|agi_12|int_12|cha_5|level(6), wp(70), knows_tracker_npc|knows_riding_1|knows_pathfinding_2|knows_tracking_2|knows_athletics_3|knows_power_draw_2, 0x00000001ab0074c736db6db6db6db6db00000000001db6e30000000000000000 ],
["npc7", "Pierrick", "Pierrick", tf_hero, no_scene, reserved, fac_commoners, [itm_ragged_outfit,itm_wrapping_boots,itm_hunting_bow,itm_arrows,itm_quarter_staff], str_8|agi_9|int_10|cha_6|level(2), wp(80), knows_tracker_npc|knows_tracking_4|knows_athletics_2|knows_spotting_1|knows_pathfinding_1|knows_power_draw_2|knows_tracking_2, 0x000000001000210638dc6ebb148a46e300000000001d291c0000000000000000 ],
["npc8", "Renaud", "Renaud", tf_hero, no_scene, reserved, fac_commoners, [itm_cuir_bouilli,itm_mail_chausses,itm_saddle_horse,itm_two_handed_battle_axe_2], str_17|agi_10|int_9|cha_10|level(9), wp(100), knows_warrior_npc|knows_weapon_master_3|knows_power_strike_2|knows_leadership_1|knows_athletics_4, 0x000000003f00518036db6db6db6db6db00000000001db6db0000000000000000 ],
["npc9", "Gael", "Gael", tf_hero, no_scene, reserved, fac_commoners, [itm_early_transitional_blue,itm_splinted_greaves,itm_knight,itm_hunter], str_12|agi_12|int_7|cha_8|level(7), wp(100), knows_warrior_npc|knows_weapon_master_2|knows_riding_4|knows_athletics_1|knows_leadership_1|knows_tactics_1|knows_power_strike_2, 0x000000003d00e01144dc8dbb2361b6db00000000001d571b0000000000000000 ],
["npc10", "Gauvin", "Gauvin", tf_hero, no_scene, reserved, fac_commoners, [itm_light_mail_and_plate,itm_leather_boots,itm_sword_medieval_a,itm_tab_shield_heater_a], str_12|agi_8|int_9|cha_11|level(9), wp(105), knows_warrior_npc|knows_weapon_master_3|knows_tactics_2|knows_leadership_1|knows_ironflesh_3|knows_trainer_3|knows_riding_2, 0x000000095b0093c0251b8a3ae265249b00000000001e36db0000000000000000 ],
["npc11", "Florentin", "Florentin", tf_hero, no_scene, reserved, fac_commoners, [itm_leather_apron,itm_wrapping_boots,itm_dagger_medievale,itm_sword_medieval_a], str_8|agi_11|int_10|cha_10|level(8), wp(70), knows_merchant_npc|knows_weapon_master_1|knows_first_aid_1|knows_wound_treatment_2|knows_ironflesh_3|knows_inventory_management_5, 0x000000003d01209244dc8dbb2361b6db00000000001d571b0000000000000000 ],
["npc12", "Nortimer", "Nortimer", tf_hero, no_scene, reserved, fac_commoners, [itm_dagger_medievale,itm_woolen_hose,itm_bb_noble_hat,itm_red_gambeson], str_8|agi_7|int_13|cha_7|level(5), wp(70), knows_merchant_npc|knows_ironflesh_1|knows_power_strike_1|knows_pathfinding_4|knows_inventory_management_3|knows_first_aid_3|knows_wound_treatment_2, 0x000000000000a10f38dc8cb92c8e36db00000000001dd6e30000000000000000 ],
["npc13", "mathieu", "mathieu", tf_hero, no_scene, reserved, fac_commoners, [itm_black_brigandine,itm_splinted_leather_greaves,itm_bastard_sword_b], str_9|agi_8|int_12|cha_8|level(3), wp(90), knows_warrior_npc|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_1|knows_weapon_master_1, 0x000000003f00900b14dc72372cad44dc00000000001e592b0000000000000000 ],
["npc14", "Michel", "Michel", tf_hero, no_scene, reserved, fac_commoners, [itm_shirt,itm_nomad_boots,itm_sword_medieval_b_small,itm_hunting_bow,itm_arrows], str_12|agi_10|int_9|cha_8|level(9), wp(100), knows_warrior_npc|knows_weapon_master_3|knows_leadership_2|knows_power_strike_1|knows_inventory_management_3|knows_tactics_2|knows_ironflesh_3|knows_trainer_2, 0x0000000ac00ce18744db6db6db6db6db00000000001dc6d30000000000000000 ],
["npc15", "Godefroi de Cherbourg", "Godefroi de Cherbourg", tf_hero, no_scene, reserved, fac_commoners, [itm_tabard,itm_woolen_hose,itm_dagger], str_9|agi_9|int_12|cha_8|level(7), wp(40), knows_warrior_npc|knows_surgery_4|knows_trade_3|knows_spotting_1|knows_engineer_3|knows_tactics_1, 0x000000095b007180251b8a3ae465249b00000000001e36db0000000000000000 ],
["npc16", "Blanche", "Blanche", tf_female|tf_hero, no_scene, reserved, fac_commoners, [itm_blue_hose,itm_ribaude_dress6bluues,itm_throwing_daggers,itm_throwing_daggers_poison], str_7|agi_11|int_8|cha_7|level(2), wp(80), knows_tracker_npc|knows_power_throw_3|knows_athletics_2|knows_power_strike_1|knows_surgery_8, 0x00000000000040060558b239244d94d100000000001d98e30000000000000000 ],
#NPC system changes end


#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwaer
["kingdom_1_lord", "Charles_VII,", "King of France", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_nobleman_outfit_charles,itm_blue_hose,itm_iron_greaves,itm_bb_complet_plates_charles,itm_bastard_sword_b,itm_battle_shieldcharlesv,itm_pigface_klappvisor_open,itm_shynbaulds,itm_tab_shield_heater_a], king_attrib, wp(420), king_skills, 0x000000063608200156dbc68dcb3226a400000000001c39320000000000000000, 0 ],

["kingdom_2_lord", "John_Lancaster, Duke of Bedford", "Edward_lll, King of England", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_nobleman_outfit_anglais,itm_courtly_outfitred,itm_woolen_hose,itm_iron_greaves,itm_bb_complet_plates_r,itm_battle_shieldedwardiii,itm_landgraf,itm_bayeux,itm_mail_coif,itm_hourglass_gauntlets,itm_nobleman_outfit_charles], king_attrib, wp(420), king_skills, 0x0000000e8000d00d271b6d371a4a36dc00000000001db6e30000000000000000, 0 ],

["kingdom_3_lord", "Philip the Good", "Duke of Burgandy", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en3,itm_nobleman_outfit_charles,itm_woolen_hose,itm_iron_greaves,itm_sword_two_handed_a,itm_sugarloaf,itm_mail_coif,itm_churburg_13_mail,itm_hourglass_gauntlets_ornate], king_attrib, wp(420), king_skills, 0x00000003ff01150422db8e3b1c8db91b00000000001db6db0000000000000000, 0 ],

["kingdom_4_lord", "Jean V", "Duke of Brittany", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_breton_warhorse_2,itm_nobleman_out_fr,itm_woolen_hose,itm_breton_complet_plates,itm_pigface_klappvisor_open,itm_wisby_gauntlets_black,itm_steel_greaves,itm_tab_shield_heater_a,itm_agincourt], king_attrib, wp(420), king_skills, 0x00000009ff01118a251b89c6dca6491a00000000001e36db0000000000000000, 0x00000009ff01118a251b89c6dca6491a00000000001e36db0000000000000000 ],

#  ["kingdom_5_lord",  "King Graveth",  "Graveth",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_warhorse,  itm_tabard,             itm_leather_boots,              itm_splinted_leather_greaves,   itm_heraldic_mail_with_tabard,  itm_gauntlets,         itm_bastard_sword_b,         itm_tab_shield_heater_cav_b,        itm_spiked_helmet],         knight_attrib_4,wp(220),knight_skills_4|knows_trainer_5, 0x0000000efc04119225848dac5d50d62400000000001d48b80000000000000000, rhodok_face_old_2],
#  ["kingdom_6_lord",  "Sultan Hakim",  "Hakim",  tf_hero, 0,reserved,  fac_kingdom_6,[itm_warhorse_sarranid,     itm_mamluke_mail,          itm_sarranid_boots_c,       itm_sarranid_mail_coif,  itm_mail_mittens,      itm_sarranid_cavalry_sword,    itm_tab_shield_small_round_c],         knight_attrib_4,wp(220),knight_skills_5|knows_trainer_5, 0x0000000a4b103354189c71d6d386e8ac00000000001e24eb0000000000000000, rhodok_face_old_2],


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina
# Dunga        Agatha     Dibus Crahask

#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
#Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
["knight_1_1", "Jean II d'Alençon", "Duc d'Alençon", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_pigface_klappvisor_open,itm_nobleman_out_fr,itm_blue_hose,itm_bayeux,itm_4mace,itm_hourglass_gauntlets,itm_shynbaulds,itm_tab_shield_heater_cav_a,itm_bb_complet_plates_charles], 
  lord_attrib,wp(380),knows_lord_1, 
    0x000000002400e00f49255229948d172300000000001d551a0000000000000000, 0x000000002400e00f49255229948d172300000000001d551a0000000000000000 ],

["knight_1_2", "La Hire", "Seigneur de Vignolles", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_pigface_klappvisor_open,itm_gambeson,itm_blue_hose,itm_bastard_sword_a,itm_hourglass_gauntlets,itm_shynbaulds,itm_tab_shield_heater_cav_a,itm_bb_complet_plates_b], 
  lord_attrib,wp(380),knows_lord_1, 
    0x0000000a0d00620d36db6db6db6db6db00000000001e5afb0000000000000000, 0x0000000a0d00620d36db6db6db6db6db00000000001e5afb0000000000000000 ],

["knight_1_3", "Gilles de Rais", "Baron de Rais", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_pigface_klappvisor_open,itm_nobleman_out_fr,itm_blue_hose,itm_bayeux,itm_4mace,itm_hourglass_gauntlets,itm_shynbaulds,itm_tab_shield_heater_cav_a,itm_bb_complet_plates_charles], 
  lord_attrib,wp(380),knows_lord_1, 
    0x000000002b0c600946dc8e391c69c8db00000000001db6eb0000000000000000, 0x000000002b0c600946dc8e391c69c8db00000000001db6eb0000000000000000 ],

["knight_1_4", "Charles II d'Albret", "Vicomte de Tartas", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out,itm_woolen_hose,itm_churburg_13_mail,itm_iron_greaves,itm_pigface_klappvisor_open,itm_bastard_sword_a,itm_tab_shield_heater_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000000240850140cf485c59720494b00000000001d76a40000000000000000, 0x00000000240850140cf485c59720494b00000000001d76a40000000000000000 ],

["knight_1_5", "Jeanne la Pucelle", "Jeanne la Pucelle", tf_hero|tf_jeanne, no_scene, reserved, fac_kingdom_1, [itm_warhorseduguesclin,itm_nobleman_outfit,itm_pigface_klappvisor_open,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_banner_jhoan, itm_prince, itm_tab_shield_kite_cav_b], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000400200324da81a6dd6ca6d200000000001dc7130000000000000000, 0x000000000400200324da81a6dd6ca6d200000000001dc7130000000000000000 ],

["knight_1_6", "Jean Poton de Xaintrailles", "Capitaine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000009ba08c14f4b22cad5527297a400000000001e66a30000000000000000, 0x00000009ba08c14f4b22cad5527297a400000000001e66a30000000000000000 ],

["knight_1_7", "Louis d'Amboise", "Vicomte de Thouars", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse2lys,itm_rich_outfitblue,itm_churburg_13_mail,itm_woolen_hose,itm_steel_greaves,itm_sword_medieval_c,itm_sword_two_handed_a,itm_tab_shield_heater_c,itm_great_helmet,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a3f05100c359b6dd8e46e44e400000000001db4a90000000000000000, 0x0000000a3f05100c359b6dd8e46e44e400000000001db4a90000000000000000 ],

["knight_1_8", "Pierre d'Amboise", "Seigneur de Chaumont", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_rich_outfitblue,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,itm_hourglass_gauntlets,itm_hounskull], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000003ff051011359b6dd8e46e44e400000000001db4a90000000000000000, 0x00000003ff051011359b6dd8e46e44e400000000001db4a90000000000000000 ],

["knight_1_9", "Jean de Dunois", "Comte de Dunois", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_rich_outfit,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_4hammer,itm_sword_two_handed_a,itm_tab_shield_heater_cav_a,itm_hourglass_gauntlets,itm_mail_coif_full], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000001dc106010194d52491d65bb6600000000001ec8ee0000000000000000, 0x00000001dc106010194d52491d65bb6600000000001ec8ee0000000000000000 ],

["knight_1_10", "Louis de Culant", "Baron de Culant", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_tabard,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_bastard_sword_b,itm_sword_two_handed_b,itm_tab_shield_heater_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1, 
    0x0000000ee004f50444e98a28e38f48e300000000001d98ea0000000000000000, 0x0000000ee004f50444e98a28e38f48e300000000001d98ea0000000000000000 ],

["knight_1_11", "Jean de Culant", "Seigneur de la Crête", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_courtly_outfit,itm_gothic_armour,itm_woolen_hose,itm_steel_greaves,itm_sugarloaf,itm_sword_medieval_c,itm_tab_shield_heater_c,itm_hourglass_gauntlets,itm_mail_coif], 
  lord_attrib,wp(380),knows_lord_1, 
    0x0000000a2004f5c544e98a28e38f48e300000000001d98ea0000000000000000, 0x0000000a2004f5c544e98a28e38f48e300000000001d98ea0000000000000000 ],

["knight_1_12", "Charles de Culant", "Capitaine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_hounskull,itm_blue_gambeson,itm_woolen_hose,itm_iron_greaves,itm_sugarloaf,itm_two_handed_axe,itm_bastard_sword_b,itm_tab_shield_heater_cav_b,itm_bb_complet_plates_charles,itm_shynbaulds,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000009fa0515cf44e98a28e38f48e300000000001d98ea0000000000000000, 0x00000009fa0515cf44e98a28e38f48e300000000001d98ea0000000000000000 ],

["knight_1_13", "Philippe de Culant", "Seigneur de Jalognes", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_blue_gambeson,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_sword_two_handed_a,itm_tab_shield_heater_cav_a,itm_hourglass_gauntlets,itm_mail_coif], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000002bf05101044e98a28a38f48da00000000001da8ea0000000000000000, 0x00000002bf05101044e98a28a38f48da00000000001da8ea0000000000000000 ],

["knight_1_14", "Raoul VI de Gaucourt", "Seigneur de Gaucourt", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_red_gambeson,itm_bb_complet_plates_charles,itm_woolen_hose,itm_iron_greaves,itm_bastard_sword_a,itm_tab_shield_heater_cav_b,itm_hourglass_gauntlets,itm_great_helmet], 
  lord_attrib,wp(380),knows_lord_1, 
  0x0000000e8e00300f14db6e36dcae46db00000000001e26e30000000000000000, 0x0000000e8e00300f14db6e36dcae46db00000000001e26e30000000000000000 ],

["knight_1_15", "Jean de Brosse", "Seigneur de Boussac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_outfit,itm_woolen_hose,itm_churburg_13_mail,itm_steel_greaves,itm_steel_greaves,itm_bastard_sword_b,itm_tab_shield_heater_d,itm_hourglass_gauntlets,itm_great_helmet], 
  lord_attrib,wp(380),knows_lord_1,
  0x0000000efd0114c114db6e36dcae46db00000000001e26e30000000000000000, 0x0000000efd0114c114db6e36dcae46db00000000001e26e30000000000000000 ],

["knight_1_16", "Charles I de Bourbon", "Comte de Clermont", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_out,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_4hammer,itm_sword_two_handed_a,itm_tab_shield_heater_cav_a,itm_hounskull,itm_hourglass_gauntlets,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000007a710e5cf395b4e251c65d72200000000001e4b230000000000000000, 0x00000007a710e5cf395b4e251c65d72200000000001e4b230000000000000000 ],

["knight_1_17", "Louis I de Bourbon", "Comte de Montpensier", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_rich_outfitblue,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_visored_sallet_coif,itm_sword_medieval_c,itm_sword_two_handed_a,itm_tab_shield_heater_cav_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002710e004695b4e24dc65d72200000000001e4b240000000000000000, 0x000000002710e004695b4e24dc65d72200000000001e4b240000000000000000 ],

["knight_1_18", "Arthur de Richemont", "Connétable de Richemont", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_charles,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000010400b12dd4db7547238dc00000000001eb8da0000000000000000, 0x000000000010400b12dd4db7547238dc00000000001eb8da0000000000000000 ],

["knight_1_19", "Antoine de Toulongeon", "Seigneur de Buxy, La Bastie, Montrichard et de Traves", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_hunter,itm_rich_outfit,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_bb_hounskull_yp,itm_sword_medieval_c,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000006a708e5c55c2c6627db6ecb9d00000000001dc4ca0000000000000000, 0x00000006a708e5c55c2c6627db6ecb9d00000000001dc4ca0000000000000000 ],

["knight_1_20", "André de Toulongeon", "Seigneur de Mornay", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_hunter,itm_tabard,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_bb_hounskull_yp,itm_bastard_sword_b,itm_sword_two_handed_b,itm_tab_shield_heater_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000012708e0065c2ca637db6ecaed00000000001dc6ca0000000000000000, 0x000000012708e0065c2ca637db6ecaed00000000001dc6ca0000000000000000 ],

#England
["knight_2_1", "John Talbot", "Earl of Shrewsbury", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredyellow,itm_nobleman_out,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_steel_greaves,itm_klepp_helmet,itm_bastard_sword_b,itm_tab_shield_kite_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1, 
    0x000000085c082181356b29b95395d7ad00000000001d34eb0000000000000000, 0x000000085c082181356b29b95395d7ad00000000001d34eb0000000000000000 ],

["knight_2_2", "John Fastolf", "Governor of Anjou", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_rich_outfit,itm_milanese_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000007f008c102499c8e185b3a5a2400000000001deaae0000000000000000, 0x00000007f008c102499c8e185b3a5a2400000000001deaae0000000000000000 ],

["knight_2_3", "William de la Pole", "Duke of Suffolk", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit_anglais,itm_milanese_armour,itm_woolen_hose,itm_iron_greaves,itm_great_helm_joust,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000071610e5cf341ba99d6369aba500000000001ddb6d0000000000000000, 0x000000071610e5cf341ba99d6369aba500000000001ddb6d0000000000000000 ],

["knight_2_4", "Pierre de Beauvau", "Seigneur de Beauvau", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_nobleman_out_fr,itm_churburg_13_mail,itm_blue_hose,itm_iron_greaves,itm_4hammer,itm_tab_shield_heater_cav_b,itm_hounskull,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000089108a01037ae8716e492eb6300000000001d68ed0000000000000000, 0x000000089108a01037ae8716e492eb6300000000001d68ed0000000000000000 ],

["knight_2_5", "Thomas de Scales", "Baron de Scales", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_rich_outfit,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_bastard_sword_b,itm_tab_shield_kite_d,itm_bb_chivalhelm_vp,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008aa00c5015713adc98cad18d500000000001ee4b00000000000000000, 0x00000008aa00c5015713adc98cad18d500000000001ee4b00000000000000000 ],

["knight_2_6", "John Tiptoft", "Baron Tiptoft", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredyellow,itm_nobleman_outfit_anglais,itm_milanese_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_kite_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1, 
    0x00000009e60425c4612aa69761cea35e00000000001d98ea0000000000000000, 0x00000009e60425c4612aa69761cea35e00000000001d98ea0000000000000000 ],

["knight_2_7", "Humphrey of Lancaster", "Duke of Gloucester", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_nobleman_outfit_anglais,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_sugarloaf,itm_great_bardiche,itm_battle_shieldedwardiii,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000440003101171b6d371a4a36e500000000001db6fb0000000000000000, 0x0000000440003101171b6d371a4a36e500000000001db6fb0000000000000000 ],

["knight_2_8", "John Beaufort", "Earl of Somerset", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_tab_shield_heater_cav_a,itm_lui_knightaxeonehe,itm_bb_greathelm_rp,itm_hourglass_gauntlets,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008e210d5d4429b91b855d1c6e400000000001edb0c0000000000000000, 0x00000008e210d5d4429b91b855d1c6e400000000001edb0c0000000000000000 ],

["knight_2_9", "Jean V de Bueil", "Seigneur de Bueil, Capitaine de Tours", tf_hero|tf_english, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out,itm_bb_complet_plates_b,itm_woolen_hose,itm_iron_greaves,itm_great_bardiche,itm_tab_shield_kite_d,itm_mail_coif_full,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000003ec0c50014af3323d6c41c76900000000001d448f0000000000000000, 0x00000003ec0c50014af3323d6c41c76900000000001d448f0000000000000000 ],

["knight_2_10", "Thomas Beaufort", "Count of Perche", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000028910d4cf429b91b855d1c6e400000000001edb0c0000000000000000, 0x000000028910d4cf429b91b855d1c6e400000000001edb0c0000000000000000 ],

["knight_2_11", "Edmund Beaufort", "Earl of Dorset", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_out,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_kite_cav_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000a10d001429b91b855d1c6e400000000001edb0c0000000000000000, 0x000000000a10d001429b91b855d1c6e400000000001edb0c0000000000000000 ],

["knight_2_12", "Richard of York", "Duke of York", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000007f05000f255c91b4da2e36dc00000000001cd8a20000000000000000, 0x000000007f05000f255c91b4da2e36dc00000000001cd8a20000000000000000 ],

["knight_2_13", "John Mowbray ", "Duke of Norfolk ", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_out,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000cc10c129455548d4a67b5b2e400000000001eca9a0000000000000000, 0x0000000cc10c129455548d4a67b5b2e400000000001eca9a0000000000000000 ],

["knight_2_14", "Richard le Strange", "Baron Strange", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_courtly_outfit,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a401035c466db50c86496a8da00000000001daa590000000000000000, 0x0000000a401035c466db50c86496a8da00000000001daa590000000000000000 ],

["knight_2_15", "Reginald Grey", "Baron Grey de Ruthyn", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_bastard_sword_b,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000003304e18b251c6cc3a5b9e75b00000000001dca6a0000000000000000, 0x000000003304e18b251c6cc3a5b9e75b00000000001dca6a0000000000000000 ],

["knight_2_16", "John Grey", "Lord Grey de Ruthyn", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_outfit,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000003504e010251c6cc395a4e71b00000000001dc26a0000000000000000, 0x000000003504e010251c6cc395a4e71b00000000001dc26a0000000000000000 ],

["knight_2_17", "Jean de Penhoët", "Seigneur de Penhoët", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_anglais,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000b670051cc12db8db6d482b6db00000000001db6db0000000000000000, 0x0000000b670051cc12db8db6d482b6db00000000001db6db0000000000000000 ],

["knight_2_18", "Thomas Stanley", "Baron Stanley", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_nobleman_outfit,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_poitiers,itm_hourglass_gauntlets,itm_tab_shield_heater_cav_a], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000d08159328a570cacc66b4dc00000000001e65250000000000000000, 0x000000000d08159328a570cacc66b4dc00000000001e65250000000000000000 ],

["knight_2_19", "Bertrand III de Montferrand", "Baron of Guyenne", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseblackprince,itm_nobleman_outfit_anglais,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_iron_greaves,itm_4hammer,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_a,itm_bayeux,itm_hourglass_gauntlets],
  lord_attrib,wp(380),knows_lord_1,
    0x000000003f04f5074863ae199a9a56da00000000001e39130000000000000000, 0x000000003f04f5074863ae199a9a56da00000000001e39130000000000000000 ],

["knight_2_20", "James Berkeley", "Baron Berkeley", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_nobleman_outfit,itm_churburg_13_mail,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000001d0c219458936e4ce692cb2900000000001cd92d0000000000000000, 0x000000001d0c219458936e4ce692cb2900000000001cd92d0000000000000000 ],

#France
["knight_3_1", "Jean IV D'Armagnac", "Comte d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out_fr,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000005990c60856b4d46c952ae375b00000000001d68920000000000000000, 0x00000005990c60856b4d46c952ae375b00000000001d68920000000000000000 ],

["knight_3_2", "Bernard VIII D'Armagnac", "Comte de Pardiac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_out_fr,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001990c60106b4d46c955acb75b00000000001d68920000000000000000, 0x00000001990c60106b4d46c955acb75b00000000001d68920000000000000000 ],

["knight_3_3", "Jean IV de Termes d’Armagnac", "Seigneur de Termes", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_nobleman_out_fr,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehe,itm_war_shield3lys,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000e2208e3c4491d2e17594a36db00000000001dc6ad0000000000000000, 0x0000000e2208e3c4491d2e17594a36db00000000001dc6ad0000000000000000 ],

["knight_3_4", "Géraud de Termes d'Armagnac", "Géraud de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out_fr,itm_mail_and_plate,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a2208e007491d2e17594a375b00000000001dc6ad0000000000000000, 0x0000000a2208e007491d2e17594a375b00000000001dc6ad0000000000000000 ],

["knight_3_5", "Thilbault de Termes d'Armagnac", "Thilbault de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_out,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000032208e001650d7a172645c79400000000001dca9d0000000000000000, 0x000000032208e001650d7a172645c79400000000001dca9d0000000000000000 ],

["knight_3_6", "Renaud de Termes d'Armagnac", "Renaud de Termes d'Armagnac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_nobleman_out,itm_bb_complet_plates_charles,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehc,itm_tab_shield_heater_cav_a,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a2208e009490d7a171d4a579400000000001dca9d0000000000000000, 0x0000000a2208e009490d7a171d4a579400000000001dca9d0000000000000000 ],

["knight_3_7", "Jacques de Chabannes", "Seigneur de La Palice", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_out,itm_churburg_13_mail,itm_woolen_hose,itm_blue_hose,itm_klappvisier,itm_tilting_helmet,itm_lui_knightaxeonehd,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000009e60480013b1c69a95277389e00000000001cb6e30000000000000000, 0x00000009e60480013b1c69a95277389e00000000001cb6e30000000000000000 ],

["knight_3_8", "Christophe d'Harcourt", "Baron D'Avrech", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_out_fr,itm_churburg_13_mail,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008b504100f4cdb6696f3d6545e00000000001d476a0000000000000000, 0x00000008b504100f4cdb6696f3d6545e00000000001d476a0000000000000000 ],

["knight_3_9", "Charles II de Poitiers", "Seigneur de Saint-Vallier", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_nobleman_outfit,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_hounskull,itm_lui_knightaxeonehe,itm_battle_shieldcharlesv,itm_hourglass_gauntlets_ornate,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000007f30cd05448d46a47132dc77200000000001f28cc0000000000000000, 0x00000007f30cd05448d46a47132dc77200000000001f28cc0000000000000000 ],

["knight_3_10", "Jean de Gamaches", "Seigneur de Gamaches", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_outfit,itm_churburg_13_mail,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehd,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001800c40106b4d46c955acb75b00000000001d68920000000000000000, 0x00000001800c40106b4d46c955acb75b00000000001d68920000000000000000 ],

["knight_3_11", "Tanneguy III Du Chastel", "Seigneur Du Chastel", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_out_fr,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000003df00e014271b6d371a4a36dc00000000001db6e30000000000000000, 0x00000003df00e014271b6d371a4a36dc00000000001db6e30000000000000000 ],

["knight_3_12", "Nicolas de Giresme", "Chevalier Hospitalier de Rhodes, commandeur de la Croix-en-Brie", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_nobleman_outfit,itm_milanese_armour,itm_blue_hose,itm_iron_greaves,itm_hounskull,itm_lui_knightaxeonehc,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000004f604e188325b924722961b5400000000001cc6760000000000000000, 0x00000004f604e188325b924722961b5400000000001cc6760000000000000000 ],

["knight_3_13", "Louis I de Bourbon-Vendôme", "Comte de Vendôme", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_outfit,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehd,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000001004800127792659238d3bb100000000001ee85b0000000000000000, 0x000000001004800127792659238d3bb100000000001ee85b0000000000000000 ],

["knight_3_14", "Jean de Linières", "Baron de Linières", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_out_fr,itm_gothic_armour,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000000110035cb519bb1b75b7a216a00000000001cc8eb0000000000000000, 0x00000000110035cb519bb1b75b7a216a00000000001cc8eb0000000000000000],

["knight_3_15", "Jean Malet de Graville", "Seigneur de Graville, Grand Maître des Arbalétriers", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_nobleman_out_fr,itm_bb_complet_plates_charles,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehc,itm_shortened_military_scythe,itm_hourglass_gauntlets_ornate,itm_tab_shield_kite_cav_a,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002708f001366daa331d68a7ac00000000001cb8830000000000000000, 0x000000002708f001366daa331d68a7ac00000000001cb8830000000000000000 ],

["knight_3_16", "Louis III d'Anjou", "Duc d'Anjou, Comte de Provence", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_nobleman_out_fr,itm_bb_complet_plates_b,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehc,itm_hourglass_gauntlets_ornate,itm_tab_shield_heater_cav_a,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000006c00c900c168b51aaa389b49e00000000001e3c540000000000000000, 0x00000006c00c900c168b51aaa389b49e00000000001e3c540000000000000000 ],

["knight_3_17", "René D'Anjou", "Duc de Bar et de Lorraine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out_fr,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000000400c900b168b51aaa389b49e00000000001e3a540000000000000000, 0x00000000400c900b168b51aaa389b49e00000000001e3a540000000000000000 ],

["knight_3_18", "Jean de La Trémoille", "Seigneur de Jonvelle", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_warhorse2lys,itm_nobleman_outfit,itm_milanese_armour,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_war_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a1f0071c2271b4d371a4a36db00000000001db6e30000000000000000, 0x0000000a1f0071c2271b4d371a4a36db00000000001db6e30000000000000000 ],

["knight_3_19", "Walter Hungerford", "Baron Hungerford", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_warhorse_f3,itm_nobleman_out,itm_milanese_armour,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehc,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets,itm_bayeux],
  lord_attrib,wp(380),knows_lord_1,
    0x00000009d004358d58db4e096b66396400000000001e675b0000000000000000, 0x00000009d004358d58db4e096b66396400000000001e675b0000000000000000 ],

["knight_3_20", "Richard de Beauchamp", "Earl of Warwick", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_warhorseblackprince,itm_nobleman_out,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_lui_knightaxeonehd,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets_ornate,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000a7600c44b26d392351c4a36db00000000001db6e30000000000000000, 0x0000000a7600c44b26d392351c4a36db00000000001db6e30000000000000000 ],

#England
["knight_4_1", "Thomas Montacute", "Earl of Salisbury", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseblackprince,itm_nobleman_out,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_axe,itm_hourglass_gauntlets_ornate,itm_tab_shield_heater_cav_a], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008c9043186249a77268da5a92b00000000001e4b2c0000000000000000, 0x00000008c9043186249a77268da5a92b00000000001e4b2c0000000000000000 ],

["knight_4_2", "John Holland", "Duke of Exeter", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_one_handed_battle_axe_c,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
  0x000000090a04d5d038e18e12dc9944db00000000001ecb330000000000000000, 0x000000090a04d5d038e18e12dc9944db00000000001ecb330000000000000000 ],

["knight_4_3", "James Tuchet", "Baron Tuchet", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredyellow,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_great_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000006b700119036626756eb8dea7500000000001e98520000000000000000, 0x00000006b700119036626756eb8dea7500000000001e98520000000000000000 ],

["knight_4_4", "William Glasdale", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_outfit,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000007af00d5c12ad392351b4a36db00000000001db6e30000000000000000, 0x00000007af00d5c12ad392351b4a36db00000000001db6e30000000000000000 ],

["knight_4_5", "Thomas Kyriell", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredyellow,itm_rich_outfit,itm_gothic_armour,itm_woolen_hose,itm_steel_greaves,itm_greatbascinet1,itm_bastard_sword_b,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets],
  lord_attrib,wp(380),knows_lord_1,
    0x0000000000103001470c72ba6b31c90e00000000001e47210000000000000000, 0x0000000000103001470c72ba6b31c90e00000000001e47210000000000000000 ],

["knight_4_6", "James Fiennes", "Lord Say and Sele", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_rich_outfit,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_war_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000009180021052ad392351b4a36da00000000001db6e30000000000000000, 0x00000009180021052ad392351b4a36da00000000001db6e30000000000000000 ],

["knight_4_7", "Richard Neville", "Earl of Salisbury", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_outfit,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_4hammer,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001460030092ad372351b4a36d900000000001db6e30000000000000000, 0x00000001460030092ad372351b4a36d900000000001db6e30000000000000000 ],

["knight_4_8", "Edward Neville", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_outfit_anglais,itm_mail_and_plate,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_war_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001460040492ad372351b4a36d900000000001db6e30000000000000000, 0x00000001460040492ad372351b4a36d900000000001db6e30000000000000000 ],

["knight_4_9", "Baron Bonville", "Baron Bonville", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_greathelm1,itm_one_handed_battle_axe_c,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000003de0060131924b2265a75451400000000001d58540000000000000000, 0x00000003de0060131924b2265a75451400000000001d58540000000000000000 ],

["knight_4_10", "William Fitzhugh", "Baron Fitzhugh", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_out,itm_coat_of_plates,itm_woolen_hose,itm_steel_greaves,itm_great_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets,itm_bb_greathelm_rp], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008810433c1249a97268da5a92b00000000001e4b2c0000000000000000, 0x00000008810433c1249a97268da5a92b00000000001e4b2c0000000000000000 ],

["knight_4_11", "Richard Woodville", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_nobleman_out,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_great_bardiche,itm_tab_shield_kite_cav_b,itm_mail_coif,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000080f0c65863922d6549546c53500000000001e6a920000000000000000, 0x000000080f0c65863922d6549546c53500000000001e6a920000000000000000 ],

["knight_4_12", "Richard II Woodville", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_nobleman_out,itm_gothic_armour,itm_blue_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_one_handed_battle_axe_c,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000024f0c60083924d2249546c53500000000001e68920000000000000000, 0x000000024f0c60083924d2249546c53500000000001e68920000000000000000 ],

["knight_4_13", "Thomas Dacre", "Baron Dacre", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseedwardiii,itm_nobleman_out,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_war_axe,itm_battle_shieldedwardiii,itm_hourglass_gauntlets_ornate,itm_bayeux], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000bb200159422da8e3b1c81b91b00000000001db6db0000000000000000, 0x0000000bb200159422da8e3b1c81b91b00000000001db6db0000000000000000 ],

["knight_4_14", "John De Vere", "Earl of Oxford", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_out,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_kite_cav_b,itm_bayeux,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002508e581271a74277432675e000000000019b2f60000000000000000, 0x000000002508e581271a74277432675e000000000019b2f60000000000000000 ],

["knight_4_15", "John Radckliff", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_steel_greaves,itm_greatbascinet1,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000049408204b18c29526943aaca500000000001f34b40000000000000000, 0x000000049408204b18c29526943aaca500000000001f34b40000000000000000 ],

["knight_4_16", "Pierre Ier de Luxembourg", "Comte de Brienne", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_bb_hounskull_yp,itm_war_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000001800e00436d415bcd6664b2600000000001e56cd0000000000000000, 0x000000001800e00436d415bcd6664b2600000000001e56cd0000000000000000 ],

["knight_4_17", "Jean II de Luxembourg", "Comte de Guise", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorseblackprince,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_4hammer,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000075800e0c636d415bcd6664b2600000000001e58e00000000000000000, 0x000000075800e0c636d415bcd6664b2600000000001e58e00000000000000000 ],

["knight_4_18", "Jean de Luxembourg", "Seigneur d’Haubourdin et d'Ailly", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorseblackprince,itm_rich_outfit,itm_mail_and_plate,itm_woolen_hose,itm_iron_greaves,itm_bb_hounskull_yp,itm_4hammer,itm_shortened_military_scythe,itm_tab_shield_kite_cav_b], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000004ff01000636d415bcd6664b2600000000001e58e80000000000000000, 0x00000004ff01000636d415bcd6664b2600000000001e58e80000000000000000 ],

["knight_4_19", "Baudot de Noyelles", "Seigneur de Noyelles", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse,itm_nobleman_outfit,itm_gothic_armour,itm_blue_hose,itm_iron_greaves,itm_greathelm1,itm_one_handed_battle_axe_c,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000003f0104c234db8e38ada5d53300000000001db6db0000000000000000, 0x000000003f0104c234db8e38ada5d53300000000001db6db0000000000000000 ],

["knight_4_20", "Pierre de Bauffremont", "Comte de Charny et Seigneur de Montfort", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse3lions,itm_courtly_outfit,itm_coat_of_plates,itm_woolen_hose,itm_steel_greaves,itm_bb_hounskull_bp,itm_great_axe,itm_tab_shield_kite_cav_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000007ff0004c034dbae38ada5d53300000000001db6db0000000000000000, 0x00000007ff0004c034dbae38ada5d53300000000001db6db0000000000000000 ],

["knight_5_1", "Henry Percy", "Earl of Northumberland", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_tabard,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_klappvisier,itm_4hammer,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008f80c10013ad56d972296c76d00000000001ea96b0000000000000000, 0x00000008f80c10013ad56d972296c76d00000000001ea96b0000000000000000 ],

["knight_5_2", "John Sutton de Dudley", "Baron Dudley", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit,itm_bb_complet_plates_r,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_lui_vaegirhallberd,itm_sword_two_handed_a,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000091408100628ca9a5764ae59d200000000001d290b0000000000000000, 0x000000091408100628ca9a5764ae59d200000000001d290b0000000000000000 ],

["knight_5_3", "John Fitzalan", "Earl of Arundel", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit_anglais,itm_bb_complet_plates_rlyon,itm_woolen_hose,itm_steel_greaves,itm_klappvisier,itm_shortened_military_scythe,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000041041190249a77268da5a92b00000000001e4b2c0000000000000000, 0x0000000041041190249a77268da5a92b00000000001e4b2c0000000000000000 ],

["knight_5_4", "Henry Bourchier", "Lord Bourchier", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit,itm_gothic_armour,itm_woolen_hose,itm_steel_greaves,itm_greatbascinet1,itm_bastard_sword_a,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000091408100628ca9a5764ae59d200000000001d290b0000000000000000, 0x000000091408100628ca9a5764ae59d200000000001d290b0000000000000000 ],

["knight_5_5", "John Seymour", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_great_helmet,itm_shortened_military_scythe,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000090c042010249a77268da5a92b00000000001e4b2c0000000000000000, 0x000000090c042010249a77268da5a92b00000000001e4b2c0000000000000000 ],

["knight_5_6", "Guy III de Chauvigny", "Baron de Châteauroux", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_charger,itm_nobleman_outfit,itm_gothic_armour,itm_woolen_hose,itm_steel_greaves,itm_klappvisier,itm_sword_two_handed_b,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000003a0ce010066992b55c4a38a400000000001da8da0000000000000000, 0x000000003a0ce010066992b55c4a38a400000000001da8da0000000000000000 ],

["knight_5_7", "William Trussell", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseredwhite,itm_nobleman_outfit,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_bastard_sword_a,itm_tab_shield_heater_c,itm_hourglass_gauntlets,itm_bastard_sword_a], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000093f0501904ceb92936389596b00000000001dc6e40000000000000000, 0x000000093f0501904ceb92936389596b00000000001dc6e40000000000000000 ],

["knight_5_8", "William ap Thomas", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorseblackprince,itm_nobleman_outfit_anglais,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_lui_vaegirhallberd,itm_sword_two_handed_b,itm_tab_shield_heater_c,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000005120c158b27136237166d5dab00000000001dc45a0000000000000000, 0x00000005120c158b27136237166d5dab00000000001dc45a0000000000000000 ],

["knight_5_9", "Robert Howard of Tendring", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_nobleman_outfit,itm_milanese_armour,itm_woolen_hose,itm_steel_greaves,itm_klappvisier,itm_great_bardiche,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000006dd00d408369a51275575e2b300000000001d456b0000000000000000, 0x00000006dd00d408369a51275575e2b300000000001d456b0000000000000000 ],

# ["knight_5_10", "Lord Falsevor", "knight_5_0", tf_hero, 0, reserved,  fac_kingdom_2,[itm_warhorse,           itm_rich_outfit,  itm_milanese_armour,     itm_blue_hose,  itm_iron_greaves,       itm_great_helmet,       itm_bastard_sword_a,   itm_tab_shield_heater_d],  knight_attrib_5,wp(130),knight_skills_5|knows_trainer_4, 0x00000008e20011063d9b6d4a92ada53500000000001cc1180000000000000000, rhodok_face_older_2],

#France
["knight_5_11", "Guy XIV de Montfort-Laval", "Baron de Laval", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_tabard,itm_milanese_armour,itm_woolen_hose,itm_iron_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000003ee10d5d40c9c71275529c89d00000000001e24610000000000000000, 0x00000003ee10d5d40c9c71275529c89d00000000001e24610000000000000000 ],

["knight_5_12", " André de Lohéac", "Seigneur de Lohéac", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_red_gambeson,itm_bb_complet_plates_charles,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_lui_vaegirhallberd,itm_tab_shield_heater_c,itm_hourglass_gauntlets,itm_bastard_sword_a], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002e10d0010c9c71275529c89d00000000001e24610000000000000000, 0x000000002e10d0010c9c71275529c89d00000000001e24610000000000000000 ],

["knight_5_13", "Gilbert Motier de La Fayette", "Seigneur de La Fayette", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_outfit_anglais,itm_milanese_armour,itm_woolen_hose,itm_steel_greaves,itm_klappvisier,itm_sword_two_handed_a,itm_tab_shield_heater_d,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000073f0d1010331d85a5546d5b6500000000001e54cb0000000000000000, 0x000000073f0d1010331d85a5546d5b6500000000001e54cb0000000000000000 ],

["knight_5_14", "Bertrand V de La Tour d'Auvergne", "Seigneur de La Tour", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_leather_jacket,itm_milanese_armour,itm_woolen_hose,itm_steel_greaves,itm_greatbascinet1,itm_bastard_sword_a,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000727005009409b6eb56e70e4ec00000000001d37090000000000000000, 0x0000000727005009409b6eb56e70e4ec00000000001d37090000000000000000 ],

["knight_5_15", "Ambroise de Loré", "Capitaine de Sainte-Suzanne", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsecharlesv,itm_nobleman_outfit_charles,itm_bb_complet_plates_charles,itm_woolen_hose,itm_iron_greaves,itm_great_helmet,itm_sword_two_handed_a,itm_hourglass_gauntlets_ornate,itm_tab_shield_heater_cav_a], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000009bd05114f2b9b723789ce2ae200000000001cb6650000000000000000, 0x00000009bd05114f2b9b723789ce2ae200000000001cb6650000000000000000 ],

["knight_5_16", "Jean Foucault", "Seigneur de Saint-Germain", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorsechandos,itm_nobleman_outfit_charles,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_klappvisier,itm_4hammer,itm_bastard_sword_a,itm_war_shield3lys], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002a0c10104b43d9571b51272b00000000001d352c0000000000000000, 0x000000002a0c10104b43d9571b51272b00000000001d352c0000000000000000 ],

["knight_5_17", "Théodore de Valpergue", "Comte de Valpergue", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_outfit_charles,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_bastard_sword_a,itm_tab_shield_heater_c,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000bef04c51422a66dd6dd9a28d200000000001dd9750000000000000000, 0x0000000bef04c51422a66dd6dd9a28d200000000001dd9750000000000000000 ],

["knight_5_18", "Robert de Baudricourt", "Seigneur de Baudricourt", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_outfit_charles,itm_gothic_armour,itm_woolen_hose,itm_iron_greaves,itm_greatbascinet1,itm_lui_vaegirhallberd,itm_tab_shield_heater_d,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000eca0c958f569a89c51a4d396d00000000001d5adb0000000000000000, 0x0000000eca0c958f569a89c51a4d396d00000000001d5adb0000000000000000 ],

["knight_5_19", "Bertrand de Poulengy", "Seigneur de Gondrecourt", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_outfit_charles,itm_bb_complet_plates_b,itm_woolen_hose,itm_steel_greaves,itm_pigface_klappvisor_open,itm_4hammer,itm_sword_two_handed_a,itm_war_shield3lys,itm_hourglass_gauntlets_ornate], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000edf087209799c8ea92c75c74e00000000001d49a20000000000000000, 0x0000000edf087209799c8ea92c75c74e00000000001d49a20000000000000000 ],

["knight_5_20", "Guillaume Bellier", "Seigneur de Chérelles, Grand Veneur du Roi", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f2,itm_nobleman_outfit_charles,itm_bb_complet_plates_b,itm_blue_hose,itm_iron_greaves,itm_great_helmet,itm_bastard_sword_b,itm_tab_shield_heater_d,itm_hourglass_gauntlets_ornate,itm_bastard_sword_b], 
  lord_attrib,wp(380),knows_lord_1,
     0x0000000bef04c51422a66dd6dd9a28d200000000001dd9750000000000000000, 0x0000000bef04c51422a66dd6dd9a28d200000000001dd9750000000000000000 ],

["knight_6_1", "Pierre Bessonneau", "Maître de l'Artillerie", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_blue_tourney_armor,itm_iron_greaves,itm_pigface_klappvisor,itm_bastard_sword_a,itm_tab_shield_heater_d,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000bc008f0024694c6534d65d51d00000000001eb56c0000000000000000, 0x0000000bc008f0024694c6534d65d51d00000000001eb56c0000000000000000 ],

["knight_6_2", "Guillaume de Chaumont-Quitry", "Capitaine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f3,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_blue_tourney_armor,itm_iron_greaves,itm_pigface_klappvisor,itm_bastard_sword_b,itm_tab_shield_heater_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008030c72c568d3aad71d92375b00000000001d649c0000000000000000, 0x00000008030c72c568d3aad71d92375b00000000001d649c0000000000000000 ],

["knight_6_3", "Bernard de Comminges", "Capitaine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_blue_tourney_armor,itm_iron_greaves,itm_pigface_klappvisor,itm_bastard_sword_b,itm_tab_shield_heater_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000003bf1115c126938a32e5ab476300000000001ddba4000000000000000, 0x00000003bf1115c126938a32e5ab476300000000001ddba4000000000000000 ],

["knight_6_4", "Girault de La Paillière", "Capitaine", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out_fr,itm_blue_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_bastard_sword_b,itm_tab_shield_heater_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000009170c350b4ac92d2663cdb0fc00000000001e1ae20000000000000000, 0x00000009170c350b4ac92d2663cdb0fc00000000001e1ae20000000000000000 ],

["knight_6_5", "Régnier Pot", "Seigneur de la Prugne", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit,itm_woolen_hose,itm_milanese_armour,itm_iron_greaves,itm_hounskull,itm_sword_two_handed_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000097a04218338dbc8dd9b8f445300000000001dc6e40000000000000000, 0x000000097a04218338dbc8dd9b8f445300000000001dc6e40000000000000000 ],

["knight_6_6", "Jean de Villiers de l'Isle-Adam", "Seigneur de L'Isle-Adam", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit,itm_woolen_hose,itm_milanese_armour,itm_iron_greaves,itm_hounskull,itm_sword_two_handed_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000097a04318238dbc8dd9b8f445300000000001dc6e40000000000000000, 0x000000097a04318238dbc8dd9b8f445300000000001dc6e40000000000000000 ],

["knight_6_7", "David de Brimeu", "Seigneur de Ligny", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_greatbascinet1,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000087a10f5cf4b129b4a636da69d00000000001da89b0000000000000000, 0x000000087a10f5cf4b129b4a636da69d00000000001da89b0000000000000000 ],

["knight_6_8", "Jacques de Brimeu", "Seigneur de Grigny", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit,itm_woolen_hose,itm_milanese_armour,itm_iron_greaves,itm_great_helm_wings_teut,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000021041584189c731b5991e50e00000000001e1ea20000000000000000, 0x0000000021041584189c731b5991e50e00000000001e1ea20000000000000000 ],

["knight_6_9", "Colart de Brimeu", "Seigneur de Maizicourt", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_outfit,itm_woolen_hose,itm_milanese_armour,itm_iron_greaves,itm_greathelm1,itm_sword_two_handed_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000000210425c4189c731b5991e50e00000000001e1ea20000000000000000, 0x00000000210425c4189c731b5991e50e00000000001e1ea20000000000000000 ],

#ANGLAIS+
["knight_6_10", "Walter Fitzwalter", "Lord Fitzwalter", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_hounskull,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets],
   lord_attrib,wp(380),knows_lord_1,
    0x00000006d304f04142e4aca3296976d400000000001dd8540000000000000000, 0x00000006d304f04142e4aca3296976d400000000001dd8540000000000000000 ],

["knight_6_11", "Owen Tudor", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_hounskull,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000000210450c5189c931b5991e50e00000000001e1ea20000000000000000, 0x00000000210450c5189c931b5991e50e00000000001e1ea20000000000000000 ],

["knight_6_12", "Prigent VII de Coëtivy", "Seigneur de Coëtivy", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_out,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000040010330922dd31c8e38dc8cb00000000001dbb8a0000000000000000, 0x000000040010330922dd31c8e38dc8cb00000000001dbb8a0000000000000000 ],

["knight_6_13", "Matthew Gough", "Hugues andres", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_rich_outfit,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001000020451493d54d1a661aae00000000001e34910000000000000000, 0x00000001000020451493d54d1a661aae00000000001e34910000000000000000 ],

["knight_6_14", "Tugdual de Kermoysan", "Seigneur de Kermoysan et de Goasmap", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_out,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000010000b0061493d54d1a661aae00000000001e34910000000000000000, 0x000000010000b0061493d54d1a661aae00000000001e34910000000000000000 ],

["knight_6_15", "Henri Penmarc'h", "Seigneur de Penmarc'h", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_out_fr,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000008dd043105368e6e045290a69b00000000001db8930000000000000000, 0x00000008dd043105368e6e045290a69b00000000001db8930000000000000000 ],

["knight_6_16", "Alain Penmarc'h", "", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_out_fr,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000001d0430104a8e6e045290a69b00000000001db8830000000000000000, 0x000000001d0430104a8e6e045290a69b00000000001db8830000000000000000 ],

["knight_6_17", "Thomas de Courtenay", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_outfit_anglais,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000077504c084368e6e045290a69b00000000001db8930000000000000000, 0x000000077504c084368e6e045290a69b00000000001db8930000000000000000 ],

["knight_6_18", "John Willoughby", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_outfit_anglais,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000708140b38da44c8aab5252a00000000001dc9530000000000000000, 0x000000000708140b38da44c8aab5252a00000000001dc9530000000000000000 ],

["knight_6_19", "William Oldhall", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_a,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000004600013cc26a378d35bd358a700000000001d95290000000000000000, 0x00000004600013cc26a378d35bd358a700000000001d95290000000000000000 ],

["knight_6_20", "Thomas Blount", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000000a0cd4cf3892d1acdb7328d600000000001e4aeb0000000000000000, 0x000000000a0cd4cf3892d1acdb7328d600000000001e4aeb0000000000000000 ],

#bourgs+
["knight_6_21", "Thomas Clifford", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000079600d51434e28e48ca2636aa00000000001dbcfb0000000000000000, 0x000000079600d51434e28e48ca2636aa00000000001dbcfb0000000000000000 ],

["knight_6_22", "Thomas Rempston", "Sir", tf_hero|tf_english, no_scene, reserved, fac_kingdom_2, [itm_warhorse3lions,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000086504e0106322a9d56429daea00000000001e469c0000000000000000, 0x000000086504e0106322a9d56429daea00000000001e469c0000000000000000 ],

["knight_6_23", "Alain IX de Rohan", "Jean de Derval", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight,itm_nobleman_outfit_charles], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000096e00d11036db6db6db6db6db00000000001dbadb0000000000000000, 0x000000096e00d11036db6db6db6db6db00000000001dbadb0000000000000000 ],

["knight_6_24", "Alain de Rohan", "Jean du Boschet", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_charles,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000002d00d0cf36db6db6db6db6db00000000001db6db0000000000000000, 0x000000002d00d0cf36db6db6db6db6db00000000001db6db0000000000000000 ],

["knight_6_25", "Charles de Rohan-Guéméné", "Albert du Boschet", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_charles,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000058600d4c636db6db6db6db6db00000000001db6db0000000000000000, 0x000000058600d4c636db6db6db6db6db00000000001db6db0000000000000000 ],

["knight_6_26", "Antoine de Vergy", "Comte de Dammartin", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_greatbascinet1,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000063300d00b37a26eb6ea4dc8d900000000001e331d0000000000000000, 0x000000063300d00b37a26eb6ea4dc8d900000000001e331d0000000000000000 ],

["knight_6_27", "Jean IV de Vergy", "Seigneur de Fouvent-Saint-Andoche", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_greatbascinet1,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x00000001b300d0103b8a6eb79c4a48d900000000001e331d0000000000000000, 0x00000001b300d0103b8a6eb79c4a48d900000000001e331d0000000000000000 ],

["knight_6_28", "Guillaume IV de Vienne", "Seigneur de Saint-Georges et de Sainte-Croix", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_nobleman_out,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_greatbascinet1,itm_tab_shield_kite_cav_b,itm_bastard_sword_b,itm_hourglass_gauntlets], 
  lord_attrib,wp(380),knows_lord_1,
    0x0000000ecb0013d431226ab6ea4dc8e400000000001e371d0000000000000000, 0x0000000ecb0013d431226ab6ea4dc8e400000000001e371d0000000000000000 ],

["knight_6_29", "Guillaume de Rosmadec", "Baron de Rosmadec", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_charles,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000066d10d01034a38234dc86475a00000000001f370a0000000000000000, 0x000000066d10d01034a38234dc86475a00000000001f370a0000000000000000 ],

["knight_6_30", "Pierre de Rochefort", "Seigneur de Rieux et de Rochefort", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_charles,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000095700e5d0251b7259536d36dc00000000001e36db0000000000000000, 0x000000095700e5d0251b7259536d36dc00000000001e36db0000000000000000 ],

#["knight_6_31", "EmirX Raddoun", "Raddoun", tf_hero, no_scene, reserved, fac_kingdom_3, [itm_warhorse_en2,itm_rich_outfit,itm_woolen_hose,itm_gothic_armour,itm_iron_greaves,itm_greatbascinet1,itm_tab_shield_kite_cav_b,itm_bastard_sword_b], knight_attrib_2, wp(150), knight_skills_2|knows_riding_5, 0x000000007f0462c32419f47a1aba8bcf00000000001e7e090000000000000000, rhodok_face_old_2 ],

#bretagne_edition_acier
["knight_6_31", "Richard de Montfort", "Comte d'Etampes", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_charles,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000018000000236db8e495b6db6db00000000001d46db0000000000000000, 0x000000018000000236db8e495b6db6db00000000001d46db0000000000000000 ],

["knight_6_32", "Bertrand de Dinan", "", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_anglais,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000099b003186251b7259536d36dc00000000001e36db0000000000000000, 0x000000099b003186251b7259536d36dc00000000001e36db0000000000000000 ],

["knight_6_33", "Jacques de Dinan", "Seigneur de Beaumanoir", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_anglais,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000001b0030c5251b7259536d36db00000000001e36db0000000000000000, 0x000000001b0030c5251b7259536d36db00000000001e36db0000000000000000 ],

["knight_6_34", "Jean II de Châteaubriant", "Baron de Châteaubriant", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_anglais,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000070f00600f251b6a3ae465249b00000000001e36db0000000000000000, 0x000000070f00600f251b6a3ae465249b00000000001e36db0000000000000000 ],

["knight_6_35", "Olivier de Blois", "Comte de Penthievre", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_woolen_hose,itm_nobleman_outfit_anglais,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight],
  lord_attrib,wp(380),knows_lord_1,
    0x000000079b00514f251b8a3ae465249b00000000001e36db0000000000000000, 0x000000079b00514f251b8a3ae465249b00000000001e36db0000000000000000 ],

["knight_6_36", "Rolland de Coëtmen", "", tf_hero, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_charles,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], 
  lord_attrib,wp(380),knows_lord_1,
    0x000000079b006150251b8a3ae465249b00000000001e36db0000000000000000, 0x000000079b006150251b8a3ae465249b00000000001e36db0000000000000000 ],

#["knight_6_37", "Seigneur breton 7", "Albert de Macon", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_4, [], knight_attrib_1, wp(120), knight_skills_1|knows_riding_5, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000 ],
#["knight_6_38", "Seigneur breton 8", "Albert de Macon", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_4, [], knight_attrib_1, wp(120), knight_skills_1|knows_riding_5, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000 ],
#["knight_6_39", "Seigneur breton 9", "Albert de Macon", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_4, [], knight_attrib_1, wp(120), knight_skills_1|knows_riding_5, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000 ],
#["knight_6_40", "Seigneur breton 10", "Albert de Macon", tf_hero|tf_bourgignon, no_scene, reserved, fac_kingdom_4, [], knight_attrib_1, wp(120), knight_skills_1|knows_riding_5, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000, 0x00000006fd10a29034a38234dc86475900000000001f370a0000000000000000 ],


["kingdom_1_pretender", "Francois de Navarre", "Francois de Navarre", tf_hero, no_scene, reserved, fac_kingdom_1, [itm_warhorse_f1,itm_nobleman_out_fr,itm_blue_hose,itm_gothic_armour,itm_iron_greaves,itm_pigface_klappvisor_open,itm_bastard_sword_b,itm_tab_shield_heater_b,itm_hourglass_gauntlets], lord_attrib,wp(380),knows_lord_1, 0x000000001b00b504251b893ae265249b00000000001e36db0000000000000000 ],
#claims pre-salic descent

["kingdom_2_pretender", "Owain Lawgoch", "Owain Lawgoch", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_warhorse,itm_rich_outfit,itm_blue_hose,itm_iron_greaves,itm_mail_shirt,itm_bastard_sword_a,itm_tab_shield_small_round_b,itm_pigface_klappvisor], lord_attrib,wp(380),knows_lord_1, 0x000000048010b29034a38234dc86475900000000001f370a0000000000000000, 0x000000048010b29034a38234dc86475900000000001f370a0000000000000000 ],
#had his patrimony falsified

["kingdom_3_pretender", "Hugues de Lannoy", "Hugues de Lannoy", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_3, [itm_warhorse,itm_rich_outfit,itm_blue_hose,itm_iron_greaves,itm_mail_shirt,itm_bastard_sword_a,itm_tab_shield_small_round_b,itm_pigface_klappvisor], lord_attrib,wp(380),knows_lord_1, 0x0000000a7f10e31234a38234dc86475900000000001f370a0000000000000000, 0x0000000a7f10e31234a38234dc86475900000000001f370a0000000000000000 ],
#of the family

["kingdom_4_pretender", "Lethwin Far-Seeker", "Lethwin", tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_nobleman_outfit_anglais,itm_woolen_hose,itm_breton_warhorse_2,itm_breton_warhorse_2,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_wisby_gauntlets_black,itm_plate_mittens,itm_shynbaulds,itm_steel_greaves,itm_tab_shield_heater_a,itm_tab_shield_heater_cav_a,itm_caithness,itm_agincourt,itm_knight], lord_attrib,wp(380),knows_lord_1, 0x000000001000210638dc6ebb148a46e300000000001d291c0000000000000000, 0x000000001000210638dc6ebb148a46e300000000001d291c0000000000000000 ],


#Royal family members

["knight_1_1_wife", "Error - knight_1_1_wife should not appear in game", "knight_1_1_wife", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_commoners, [itm_lady_dress_ruby,itm_turret_hat_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000 ],

#Swadian ladies - eight mothers, eight daughters, four sisters
["kingdom_1_lady_1", "Lady Beatrice de Clisson", "Beatrice de Clisson", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["kingdom_1_lady_2", "Joan of Kent", "Joan of Kent", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000005002469b6e24e44e324b00000000001da6d30000000000000000 ],
["knight_1_lady_3", "Lady Beatrice de Chalon", "Beatrice de Chalon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000 ],
["knight_1_lady_4", "Lady Margaret of Bourbon", "Margaret of Bourbon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000000100436d8a236db6db6db00000000001dc6db0000000000000000 ],
["kingdom_l_lady_5", "Lady Constanis", "Constanis", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_6", "Philippa of Hainault", "Philippa of Hainault", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000017002003391aca36dc12249300000000001da6db0000000000000000 ],
["kingdom_1_lady_7", "Lady Isabella de Coucy", "Isabella de Coucy", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_8", "Lady Violante", "Violante", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000014002004391aca36dc12249300000000001da6db0000000000000000 ],
["kingdom_1_lady_9", "Infanta Isabella of Castile", "Isabella of Castile", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_10", "Catherine de Vernon", "Catherine de Vernon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001200300236d9edb6dc41379800000000001db6db0000000000000000 ],
["kingdom_1_lady_11", "Lady Alice Holland", "Alice Holland", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_12", "Joanna of Bourbon", "Joanna of Bourbon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000095400400224db8a18db7136d300000000001db6eb0000000000000000 ],
["kingdom_l_lady_13", "Lady Isabella of Valois", "Isabella of Valois", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_14", "Lady Tiphaine", "Tiphaine", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000095400500524db8a18db7136d300000000001db6eb0000000000000000 ],
["kingdom_1_lady_15", "Lady Isabelle de Bourbon", "Isabelle de Bourbon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_green_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_1_lady_16", "Lady Jeanne de Coucy", "Jeanne de Coucy", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000c3c00000524db8a18db7136d300000000001db6eb0000000000000000 ],
["kingdom_1_lady_17", "Lady Petronille ou Pernelle de Villiers", "Petronille ou Pernelle de Villiers", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003c00100424db6218db7136d300000000001db6eb0000000000000000 ],
["kingdom_1_lady_18", "Lady Isabeau de Craon", "Isabeau de Craon", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000400000224da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_1_lady_19", "Lady Cecily de Weyland", "Cecily de Weyland", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_3, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1 ],
["kingdom_1_lady_20","Lady Elizabeth Burghersh","Elizabeth Burghersh",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],

#Vaegir ladies
["kingdom_2_lady_1", "Lady Cicely", "Cicely", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_3, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000400100324da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_2", "Lady Katia", "Katia", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_3, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000400200324da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_3", "Lady Seomis", "Seomis", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000ac400200424da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_4", "Lady Drina", "Drina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000400300424da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_5", "Lady Nesha", "Nesha", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000400400424da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_6", "Lady Tabath", "Tabath", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000094400400624da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_7", "Lady Pelaeka", "Pelaeka", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000094400500724da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_8", "Lady Haris", "Haris", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000094400000124da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_9", "Lady Vayen", "Vayen", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000d4400400124da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_10", "Lady Joaka", "Joaka", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000003ff00500124da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_2_lady_11", "Lady Tejina", "Tejina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000002d04500654e1722b8b2dbe1600000000000c97510000000000000000 ],
["kingdom_2_lady_12", "Lady Olekseia", "Olekseia", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001c1030012722c6cba169b69300000000001daca90000000000000000 ],
["kingdom_2_lady_13", "Lady Myntha", "Myntha", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000b080004593385a723755cdd00000000000c9b640000000000000000 ],
["kingdom_2_lady_14", "Lady Akilina", "Akilina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000f10300528cd44c88a7138eb000000000000a54a0000000000000000 ],
["kingdom_2_lady_15", "Lady Sepana", "Sepana", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000023102007408b49f95b48bb8c0000000000199ccb0000000000000000 ],
["kingdom_2_lady_16", "Lady Iarina", "Iarina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003e0c10032d53a54b2668c83600000000001e14e20000000000000000 ],
["kingdom_2_lady_17", "Lady Sihavan", "Sihavan", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003d00200368ee75c65ac54515000000000011bce30000000000000000 ],
["kingdom_2_lady_18", "Lady Erenchina", "Erenchina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_green_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003500200638e2c6b9346f9724000000000005a7af0000000000000000 ],
["kingdom_2_lady_19", "Lady Tamar", "Tamar", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_2, [itm_green_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f04000645a13b379251b6de00000000001d92a30000000000000000 ],
["kingdom_2_lady_20","Lady Valka","Valka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000e0000013b178a366cf6c8db00000000001724890000000000000000],


["kingdom_3_lady_1","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_2","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001000500556d991bcd53248f1000000000011c30c0000000000000000],
["kingdom_3_lady_3","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
["kingdom_3_lady_4","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006e60c400169a341bae38e37a400000000001ed6550000000000000000],
["kingdom_3_lady_5","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006df0c10033aeb6a24a2995b1800000000000c14ee0000000000000000],
["kingdom_3_lady_6","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006f8045007451aa1b51169cc44000000000018c31a0000000000000000],
["kingdom_3_lady_7","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c41020023aab764b1a30a69500000000000d32ca0000000000000000],
["kingdom_3_lady_8","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006d508200763a2b538a2c93ad500000000001639550000000000000000],
["kingdom_3_lady_9","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c50000012b7b7218eed5a6a300000000001de85a0000000000000000],
["kingdom_3_lady_10","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006db1010063ae491e6632a389a00000000000e54e20000000000000000],
["kingdom_3_lady_11","Lady Selik","Selik",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c30c5001464c6ddb2c95a6d900000000001ce8b30000000000000000],
["kingdom_3_lady_12","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006ea04300336ec9749624f28e5000000000002d5040000000000000000],
["kingdom_3_lady_13","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006d91010053c338cb51b6cccc9000000000009b6d10000000000000000],
["kingdom_3_lady_14","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
["kingdom_3_lady_15","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
["kingdom_3_lady_16", "Lady Arjis", "Zenur", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_1, [itm_brown_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000006c30440015b156dd8cd72d29d00000000000e4bab0000000000000000 ],
["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006e0043004399f4e9710ad988900000000000ee7120000000000000000],
["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c20820053849a5a92d6dd93300000000000d36240000000000000000],
["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006f41050051d35c8c70a4f371300000000001356690000000000000000],
["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006fd101003459b6bb8ac8ef663000000000011cae70000000000000000],


#1429
["kingdom_4_lady_1","Lady Jadeth","Jadeth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress , itm_court_hat ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c0044003235cacbef38ea8d600000000001e08dd0000000000000000],
["kingdom_4_lady_2","Lady Miar","Miar",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress ,  itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006c50850022d1b86b674cd3d4900000000001cc6550000000000000000],
["kingdom_4_lady_3","Lady Dria","Dria",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006e404200537968e4ead8e2d1a00000000001d279f0000000000000000],
["kingdom_4_lady_4","Lady Glunde","Glunde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006e210200116dc22d91e57351000000000000a46db0000000000000000],
["kingdom_4_lady_5","Lady Loeka","Loeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress ,  itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006df08300428d5adbae949395500000000000dd72b0000000000000000],
["kingdom_4_lady_6","Lady Bryn","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress ,  itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000006f80030020ba3763c9369595300000000000ebd4e0000000000000000],
["kingdom_4_lady_7","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ab904100628cd95175b73336100000000001dba950000000000000000],
["knight_4_2b_daughter_1","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a830c30046adbd6b8e486b6a600000000000ec76b0000000000000000],
["kingdom_4_lady_9","Lady Hild","Hild",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress , itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a9b00200547a475589b75e924000000000009990b0000000000000000],
["knight_4_2c_wife_1","Lady Endegrid","Endegrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress , itm_court_hat ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000abd10000228d4922b726a98e400000000001f57330000000000000000],
["kingdom_4_lady_11","Lady Herjasa","Herjasa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a8f0c2004575caa2b1e92494c0000000000066b640000000000000000],
["knight_4_2c_daughter","Lady Svipul","Svipul",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000a81045001389d29b96a89c7220000000000090b9a0000000000000000],
["knight_4_1b_wife","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress ,  itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c004300268a4819524652c5b00000000001cd9530000000000000000],
["kingdom_4_lady_14","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_court_dress , itm_court_hat ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e600100524d4d25b9ca8c4d500000000001614640000000000000000],
["knight_4_1b_daughter","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000000136db6db6db6db6db00000000001db6db0000000000000000],
["knight_4_2b_daughter_2","Lady Gudrun","Gudrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002400100138dca6b8dd8d36d200000000001ca72b0000000000000000],
["kingdom_4_lady_17","Lady Bergit","Bergit",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_court_dress ,  itm_court_hat ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001200200538dca6b8dd8d36d200000000001ca72b0000000000000000],
["knight_4_2c_wife_2","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_court_dress ,  itm_court_hat , itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001200300236d9edb6dc41379800000000001db6db0000000000000000],
["knight_4_1c_daughter","Lady Alfrun","Alfrun",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000],
["kingdom_4_lady_20","Lady Afrid","Afrid",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000005002469b6e24e44e324b00000000001da6d30000000000000000],


["kingdom_5_lady_1","Lady Brina","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000],
["kingdom_5_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000017002003391aca36dc12249300000000001da6db0000000000000000],
["kingdom_5_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000014002004391aca36dc12249300000000001da6db0000000000000000],
["kingdom_5_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008940030063918ea36dc12249300000000001da6db0000000000000000],
["kingdom_5_5_wife","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
["kingdom_5_2b_wife_1","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000095400400224db8a18db7136d300000000001db6eb0000000000000000],
["kingdom_5_1c_daughter_1","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000c3c00000524db8a18db7136d300000000001db6eb0000000000000000],
["kingdom_5_2c_daughter_1","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003c00100424db6218db7136d300000000001db6eb0000000000000000],
["kingdom_5_1c_wife_1","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400000224da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_2c_wife_1","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400100324da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_1c_daughter_2","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400200324da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_2c_daughter_2","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ac400200424da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_1b_wife","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400300424da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_2b_wife_2","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400400424da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_1c_daughter_3","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000094400400624da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000094400500724da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_1c_wife_2","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ac400200424da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_2c_wife_2","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000400400424da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_1c_daughter_4","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000094400000124da81a6dd6ca6d200000000001dc7130000000000000000],
["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000d4400100324da81a6dd6ca6d200000000001dc7130000000000000000],

#Sarranid ladies
["kingdom_6_lady_1", "Lady Rayma", "Rayma", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000d4400200524da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_6_lady_2", "Lady Thanaikha", "Thanaikha", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000d4400400124da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_6_lady_3", "Lady Sulaha", "Sulaha", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x00000003ff00500124da81a6dd6ca6d200000000001dc7130000000000000000 ],
["kingdom_6_lady_4", "Lady Shatha", "Shatha", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001c1030012722c6cba169b69300000000001daca90000000000000000 ],
["kingdom_6_lady_5", "Lady Bawthan", "Bawthan", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_6", "Lady Mahayl", "Mahayl", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000b080004593385a723755cdd00000000000c9b640000000000000000 ],
["kingdom_6_lady_7", "Lady Isna", "Isna", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_blue,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_8", "Lady Siyafan", "Siyafan", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000f10300528cd44c88a7138eb000000000000a54a0000000000000000 ],
["kingdom_6_lady_9", "Lady Ifar", "Ifar", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_10", "Lady Yasmin", "Yasmin", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x0000000023102007408b49f95b48bb8c0000000000199ccb0000000000000000 ],
["kingdom_6_lady_11", "Lady Dula", "Dula", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_12", "Lady Ruwa", "Ruwa", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003e0c10032d53a54b2668c83600000000001e14e20000000000000000 ],
["kingdom_6_lady_13", "Lady Luqa", "Luqa", tf_female|tf_hero|tf_randomize_face|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_14", "Lady Zandina", "Zandina", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003500200638e2c6b9346f9724000000000005a7af0000000000000000 ],
["kingdom_6_lady_15", "Lady Lulya", "Lulya", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_kingdom_4, [itm_lady_dress_ruby,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2 ],
["kingdom_6_lady_16", "Lady Zahara", "Zahara", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_player_supporters_faction, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000003f04000645a13b379251b6de00000000001d92a30000000000000000 ],
["kingdom_6_lady_17", "Lady Safiya", "Safiya", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_player_supporters_faction, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000000608300137774ab79a6a18c4000000000008c4e10000000000000000 ],
["kingdom_6_lady_18", "Lady Khalisa", "Khalisa", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_player_supporters_faction, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, 0x000000001000500556d991bcd53248f1000000000011c30c0000000000000000 ],
["kingdom_6_lady_19", "Lady Janab", "Janab", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_player_supporters_faction, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_1 ],
["kingdom_6_lady_20", "Lady Sur", "Sur", tf_female|tf_hero|tf_unmoveable_in_party_window, no_scene, reserved, fac_player_supporters_faction, [itm_lady_dress_green,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, swadian_woman_face_2 ],




#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],


#Seneschals
["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00159222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000005bf00259222da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003f0025c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000400246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000410146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_red_gambeson,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x000000000000810146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000910146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_red_gambeson,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x000000000000a0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000000000b0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000e0c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000000100c146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001901110146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001901210146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900114046da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900214146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900218146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900318146da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900418246da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900518346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900818346da8e3b1c81b91b00000000001db6db0000000000000000 ],
["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190081c436db6db6db6db6db00000000001db6db0000000000000000 ],
["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],

["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000190091c436db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_nomad_armor,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900920536db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900a20536db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900b20546db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900c24546db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900e24646db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001901028646db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001901128746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001901228746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190012c746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190022c746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_nomad_armor,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190032c746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000190042c746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000190052c746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900630746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900830746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900930746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900a30746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900b30746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900c30746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900e34746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001901034746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001901134746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001901234746db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900138846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900238846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900338846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900438846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900538846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900838846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900938846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_nomad_armor,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900a38846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900b38846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000001900c38846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000001900e38846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000000001038846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000001138846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000000001238846db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000000013cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000023cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000033cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000043cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000053cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000083cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000093cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000a3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000b3cb46db6db6db6db6db00000000001db6db0000000000000000 ],
["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000000000c3cb46db6db6db6db6db00000000001db6db0000000000000000 ],

#Arena Masters
["town_1_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_1_arena|entry(52), reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots,itm_bb_noble_hat_simple], def_attrib|level(2), wp(20), knows_common, 0x000000003901044b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_2_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_2_arena|entry(52), reserved, fac_commoners, [itm_g_tw_shirt,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_3_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_3_arena|entry(52), reserved, fac_commoners, [itm_shirt,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_4_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_4_arena|entry(52), reserved, fac_commoners, [itm_shirt,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003901148b46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_5_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_5_arena|entry(52), reserved, fac_commoners, [itm_g_tw_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_6_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_6_arena|entry(52), reserved, fac_commoners, [itm_leather_jerkin,itm_leather_boots,itm_bb_noble_hat_simple], def_attrib|level(2), wp(20), knows_common, 0x000000003900148d46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_8_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_8_arena|entry(52), reserved, fac_commoners, [itm_g_tw_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000044cf46db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_10_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_10_arena|entry(52), reserved, fac_commoners, [itm_g_tw_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000000000054d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
["town_20_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_20_arena|entry(52), reserved, fac_commoners, [itm_fur_coat,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x00000000000084c046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_21_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_21_arena|entry(52), reserved, fac_commoners, [itm_shirt,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],
["town_22_arena_master", "Tournament Master", "{!}Tournament Master", tf_hero|tf_randomize_face, scn_town_22_arena|entry(52), reserved, fac_commoners, [itm_padded_leather,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, man_face_middle_1, man_face_older_2 ],



# Underground

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
#arena_masters_end = zendar_armorer

["town_1_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_short_tunic,itm_leather_boots,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000094c046db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_2_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_peasant_dress,itm_straw_hat,itm_enclume], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000006db1010063ae491e6632a389a00000000000e54e20000000000000000, 0x00000006db1010063ae491e6632a389a00000000000e54e20000000000000000 ],
["town_3_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_hide_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_4_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_red_gambeson,itm_leather_boots,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0114c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_6_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_nomad_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0124c146db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_7_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_blue_hose,itm_enclume], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_8_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_padded_leather,itm_leather_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f0014c246db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_9_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_blue_gambeson,itm_nomad_boots,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_10_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_hide_boots,itm_enclume], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_12_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_red_gambeson,itm_nomad_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00850346db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_13_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_hide_boots,itm_cuir,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_14_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_peasant_dress,itm_headcloth], def_attrib|level(5), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_16_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_nomad_boots,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_18_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_peasant_dress,itm_headcloth,itm_cuir,itm_cuir,itm_enclume], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006c30c5001464c6ddb2c95a6d900000000001ce8b30000000000000000, 0x00000006c30c5001464c6ddb2c95a6d900000000001ce8b30000000000000000 ],
["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
["town_20_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_hide_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_21_armorer", "Armorer", "{!}Armorer", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_hide_boots,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_enclume], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00950446db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_22_armorer", "Armorer", "{!}Armorer", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_woolen_hose], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006f41050051d35c8c70a4f371300000000001356690000000000000000, 0x00000006f41050051d35c8c70a4f371300000000001356690000000000000000 ],

# Weapon merchants

["town_1_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_straw_hat,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_3,itm_plan_7,itm_plan_7,itm_plan_7,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_bois,itm_enclume,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_tools,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_2_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_nomad_boots,itm_plan_2,itm_plan_2,itm_plan_4,itm_plan_4,itm_plan_4,itm_plan_4,itm_plan_4,itm_plan_5,itm_bois,itm_bois,itm_bois,itm_enclume,itm_enclume,itm_corde,itm_corde,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000003f00c00546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_3_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_hide_boots,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_7,itm_plan_7,itm_plan_7,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00e08546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_4_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_2,itm_plan_2,itm_plan_2,itm_bois,itm_bois,itm_bois,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_5_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_wrapping_boots,itm_plan_3,itm_plan_3,itm_plan_4,itm_plan_4,itm_plan_4,itm_plan_4,itm_plan_7,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_6_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_5,itm_corde], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_7_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000bbf00f18546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_8_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_blue_dress,itm_wrapping_boots,itm_straw_hat,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_6,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000006e210200116dc22d91e57351000000000000a46db0000000000000000, 0x00000006e210200116dc22d91e57351000000000000a46db0000000000000000 ],
["town_9_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_leather_boots,itm_plan_7,itm_plan_7,itm_plan_7,itm_plan_2,itm_plume,itm_plume,itm_plume,itm_plume], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_10_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_4,itm_plan_4,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_enclume,itm_enclume,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_11_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_woolen_hose,itm_plan_7,itm_plan_6,itm_plan_1,itm_plan_1,itm_plume,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_12_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_5,itm_plan_5,itm_plan_5,itm_plan_5], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_13_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_wrapping_boots,itm_plan_6,itm_plan_6,itm_plan_6,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_14_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_wrapping_boots,itm_plan_7,itm_plan_7,itm_plan_2,itm_plan_1,itm_enclume,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_15_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_woolen_hose,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_4,itm_bois,itm_bois,itm_bois,itm_enclume,itm_tools,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_16_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_7,itm_corde,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000043f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_17_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_wrapping_boots,itm_plan_6,itm_plan_5,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_18_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_wrapping_boots,itm_plan_1,itm_plan_2,itm_plan_4,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_enclume,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_19_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jacket,itm_woolen_hose,itm_plan_5,itm_plan_2,itm_plan_2,itm_enclume,itm_corde,itm_corde,itm_corde,itm_tools], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_20_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_hide_boots,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_6,itm_plan_7,itm_plan_7,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_21_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_woolen_hose,itm_plan_6,itm_plan_5,itm_enclume,itm_cuir,itm_cuir,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_22_weaponsmith", "Weaponsmith", "{!}Weaponsmith", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_woolen_hose,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_2,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier], def_attrib|level(5), wp(20), knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

#Tavern keepers

["town_1_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_1_tavern|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_wrapping_boots,itm_fesan,itm_fesan,itm_rhumm,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_wine,itm_wine,itm_cattle_meat,itm_cattle_meat,itm_cattle_meat,itm_cattle_meat,itm_chicken,itm_chicken,itm_chicken,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_cabbages,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bread,itm_rhumm,itm_rhumm,itm_rhumm,itm_bier,itm_bier,itm_bier,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_torch,itm_fesan,itm_fesan,itm_fesan,itm_pate2,itm_pate2,itm_pate3,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01018546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_2_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_2_tavern|entry(9), reserved, fac_commoners, [itm_tavern_shirt,itm_leather_boots,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_cheese,itm_cheese,itm_dried_meat,itm_dried_meat,itm_cattle_meat,itm_cattle_meat,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_chicken,itm_chicken,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_rhumm,itm_rhumm,itm_rhumm,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_fesan,itm_fesan,itm_fesan,itm_fesan], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f01114546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_3_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_3_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress,itm_hide_boots,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_cattle_meat,itm_cattle_meat,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_cheese,itm_cheese,itm_raw_grapes,itm_raw_grapes,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_rhumm,itm_rhumm,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_fesan,itm_fesan,itm_pate3,itm_pate3,itm_pate1,itm_pate1,itm_pate1,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006df08300428d5adbae949395500000000000dd72b0000000000000000, 0x00000006df08300428d5adbae949395500000000000dd72b0000000000000000 ],
["town_4_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_4_tavern|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_fesan,itm_pate1,itm_pate1,itm_pate1,itm_pate2,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0120c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_5_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_5_tavern|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_hide_boots,itm_cattle_meat,itm_cattle_meat,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_wine,itm_dried_meat,itm_dried_meat,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_6_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_6_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress,itm_hide_boots,itm_bier,itm_bier,itm_fesan,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cattle_meat,itm_cattle_meat,itm_chicken,itm_chicken,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_pate2,itm_pate2,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x00000006f80030020ba3763c9369595300000000000ebd4e0000000000000000, 0x00000006f80030020ba3763c9369595300000000000ebd4e0000000000000000 ],
["town_7_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_7_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_leather_boots,itm_headcloth,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_rhumm,itm_rhumm,itm_rhumm,itm_rhumm,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x0000000ab904100628cd95175b73336100000000001dba950000000000000000, 0x0000000ab904100628cd95175b73336100000000001dba950000000000000000 ],
["town_8_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_8_tavern|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_bier,itm_bier,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_dried_meat,itm_dried_meat,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_fesan,itm_torch,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000003f0010c546db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_9_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_9_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_nomad_boots,itm_bread,itm_bread,itm_bread,itm_bread,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_torch,itm_fesan], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_10_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_10_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_hide_boots,itm_vinn,itm_vinn,itm_vinn,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x0000000abd10000228d4922b726a98e400000000001f57330000000000000000, 0x0000000abd10000228d4922b726a98e400000000001f57330000000000000000 ],
["town_11_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_11_tavern|entry(9), reserved, fac_commoners, [itm_woolen_dress,itm_nomad_boots,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_wine,itm_wine,itm_wine,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_rhumm,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_fesan,itm_fesan], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0101c746db6db6db6db6db00000000001db6db0000000000000000, woman_face_2 ],
["town_12_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_12_tavern|entry(9), reserved, fac_commoners, [itm_tavern_shirt,itm_hide_boots,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_13_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_13_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_hide_boots,itm_headcloth,itm_fesan,itm_fesan,itm_fesan,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_cattle_meat,itm_cattle_meat,itm_cattle_meat,itm_cattle_meat,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_sausages,itm_sausages,itm_sausages,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_rhumm,itm_rhumm,itm_rhumm,itm_rhumm,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_torch,itm_torch,itm_fesan,itm_fesan,itm_pate1,itm_pate1,itm_pate1,itm_pate1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x0000000a81045001389d29b96a89c7220000000000090b9a0000000000000000, 0x0000000a81045001389d29b96a89c7220000000000090b9a0000000000000000 ],
["town_14_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_14_tavern|entry(9), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_cattle_meat,itm_cattle_meat,itm_rhumm,itm_rhumm,itm_rhumm,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_olives,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_rhumm,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_pate1,itm_pate1,itm_pate3], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0111cd46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_15_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_15_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress,itm_nomad_boots,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_fesan,itm_fesan,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_16_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_16_tavern|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_hide_boots,itm_bier,itm_bier,itm_bier,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_bread,itm_bread,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_fesan,itm_pate3,itm_pate3,itm_pate2,itm_pate2], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_17_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_17_tavern|entry(9), reserved, fac_commoners, [itm_blue_dress,itm_hide_boots,itm_headcloth,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_cheese,itm_cheese,itm_cheese,itm_cabbages,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_torch,itm_torch,itm_torch,itm_torch,itm_torch,itm_torch,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_18_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", 0|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_18_tavern|entry(9), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_wine,itm_wine,itm_wine,itm_wine,itm_wine,itm_cattle_meat,itm_cattle_meat,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_rhumm,itm_rhumm,itm_fesan,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan,itm_pate1,itm_pate1,itm_pate1,itm_pate1], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000033f0121cf46db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_19_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_19_tavern|entry(9), reserved, fac_commoners, [itm_peasant_dress,itm_leather_boots,itm_cattle_meat,itm_cattle_meat,itm_cattle_meat,itm_chicken,itm_chicken,itm_cabbages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_fesan], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, 0x000000000000100436d8a236db6db6db00000000001dc6db0000000000000000, 0x000000000000100436d8a236db6db6db00000000001dc6db0000000000000000 ],
["town_20_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_20_tavern|entry(9), reserved, fac_commoners, [itm_tavern_shirt,itm_leather_boots,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bread,itm_bread,itm_bread,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_dried_meat,itm_dried_meat,itm_bier,itm_bier,itm_bier,itm_bier,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_torch,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],
["town_21_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_21_tavern|entry(9), reserved, fac_commoners, [itm_peasant_dress,itm_leather_boots,itm_headcloth,itm_cheese,itm_cheese,itm_cheese,itm_fesan,itm_cheese,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_cabbages,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_22_tavernkeeper", "Tavern_Keeper", "{!}Tavern_Keeper", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_22_tavern|entry(9), reserved, fac_commoners, [itm_tavern_shirt,itm_leather_boots,itm_fesan,itm_fesan,itm_bier,itm_bread,itm_bread,itm_bread,itm_dried_meat,itm_dried_meat,itm_dried_meat,itm_cheese,itm_vinn,itm_vinn,itm_vinn,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_rhumm,itm_rhumm,itm_vinn,itm_fesan,itm_fesan,itm_pate3,itm_pate3,itm_pate3,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_cidre,itm_torch,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, mercenary_face_1, mercenary_face_2 ],

#Goods Merchants

["town_1_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_1_store|entry(9), reserved, fac_commoners, [itm_leather_jacket,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f01221046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_3_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_3_store|entry(9), reserved, fac_commoners, [itm_blue_dress,itm_leather_boots,itm_straw_hat], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_4_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_4_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000093f00125046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_5_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_5_store|entry(9), reserved, fac_commoners, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_6_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_6_store|entry(9), reserved, fac_commoners, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_7_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_7_store|entry(9), reserved, fac_commoners, [itm_leather_jerkin,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00229046db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_8_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_8_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f0052d246db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_11_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_11_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00830146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_12_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_12_store|entry(9), reserved, fac_commoners, [itm_red_dress,itm_leather_boots,itm_female_hood], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_13_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_13_store|entry(9), reserved, fac_commoners, [itm_red_dress,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_14_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_14_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00b34146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_15_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_15_store|entry(9), reserved, fac_commoners, [itm_leather_jacket,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_16_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_16_store|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_leather_boots,itm_female_hood], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_17_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_17_store|entry(9), reserved, fac_commoners, [itm_blue_dress_tw,itm_leather_boots,itm_straw_hat], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_18_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_18_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00c40146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_20_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_20_store|entry(9), reserved, fac_commoners, [itm_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_21_merchant", "Merchant", "{!}Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_town_21_store|entry(9), reserved, fac_commoners, [itm_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, woman_face_1, woman_face_2 ],
["town_22_merchant", "Merchant", "{!}Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_town_22_store|entry(9), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000aff00e44146db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],

["salt_mine_merchant", "Barezan", "Barezan", tf_hero|tf_is_merchant, scn_salt_mine|entry(1), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6 ],

# Horse Merchants

["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000002400100138dca6b8dd8d36d200000000001ca72b0000000000000000, 0x000000002400100138dca6b8dd8d36d200000000001ca72b0000000000000000],
["town_2_horse_merchant", "Horse Merchant", "{!}Town 2 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_linen_tunic,itm_nomad_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00f44148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_3_horse_merchant", "Horse Merchant", "{!}Town 3 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_g_tw_shirt,itm_hide_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_4_horse_merchant", "Horse Merchant", "{!}Town 4 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_nomad_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01044148db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_5_horse_merchant", "Horse Merchant", "{!}Town 5 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_peasant_dress,itm_woolen_hose,itm_woolen_hood], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x000000000400300424da81a6dd6ca6d200000000001dc7130000000000000000, 0x000000000400300424da81a6dd6ca6d200000000001dc7130000000000000000 ],
["town_6_horse_merchant", "Horse Merchant", "{!}Town 6 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01148248db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_9_horse_merchant", "Horse Merchant", "{!}Town 9 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff01248348db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000],
["town_11_horse_merchant", "Horse Merchant", "{!}Town 11 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_vest,itm_leather_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_13_horse_merchant", "Horse Merchant", "{!}Town 13 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_nomad_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff00148448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
["town_15_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_leather_vest,itm_leather_boots], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000aff0025c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000008940030063918ea36dc12249300000000001da6db0000000000000000, 0x00000008940030063918ea36dc12249300000000001da6db0000000000000000],
["town_19_horse_merchant", "Horse Merchant", "{!}Town 15 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_fur_coat], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x00000000000115c448db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["town_20_horse_merchant", "Horse Merchant", "{!}Town 16 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_shirt], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_21_horse_merchant", "Horse Merchant", "{!}Town 17 Horse Merchant", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_woolen_hose], def_attrib|level(5), wp(20), knows_inventory_management_10, man_face_young_1, man_face_older_2 ],
["town_22_horse_merchant", "Horse Merchant", "{!}Town 18 Horse Merchant", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_shirt,itm_blue_hose], def_attrib|level(5), wp(20), knows_inventory_management_10, 0x0000000c3c00000524db8a18db7136d300000000001db6eb0000000000000000, 0x0000000c3c00000524db8a18db7136d300000000001db6eb0000000000000000 ],


#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_court_hat_two,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000008de0115c448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_gambeson,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e01208448db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x0000000b1e00110548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_fur_coat,itm_blue_hose,itm_bb_noble_hat], def_attrib|level(2), wp(20), knows_common, 0x00000008de00210748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_court_hat_two,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000008de00318748db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_red_gambeson,itm_woolen_hose,itm_bb_noble_hat], def_attrib|level(2), wp(20), knows_common, 0x00000008c000410648db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_g_tw_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000010000918548db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_red_gambeson,itm_woolen_hose,itm_bb_noble_hat_simple], def_attrib|level(2), wp(20), knows_common, 0x00000001310cb0cc5664a943216a231a00000000001638660000000000000000, mercenary_face_2 ],
["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000011400e0c036db6db6db6db6db00000000000db6db0000000000000000, mercenary_face_2 ],
["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000006000100c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_woolen_hose,itm_bb_noble_hat], def_attrib|level(2), wp(20), knows_common, 0x00000006140110c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_red_gambeson,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x0000000a5401218036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_court_hat_two], def_attrib|level(2), wp(20), knows_common, 0x0000000a540001c036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose,itm_bb_noble_hat], def_attrib|level(2), wp(20), knows_common, 0x0000000a4000120036db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_leather_jacket,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x0000000c4000220136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_fur_coat,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000084000328136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_court_hat_two], def_attrib|level(2), wp(20), knows_common, 0x00000008760052c136db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_blue_gambeson,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x000000087600830236db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_fur_coat,itm_hide_boots], def_attrib|level(2), wp(20), knows_common, 0x000000087600934336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_shirt], def_attrib|level(2), wp(20), knows_common, 0x000000087600a38336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_fur_coat,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000087600b3c336db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],
["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, no_scene, reserved, fac_neutral, [itm_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000087600e40536db6db6db6db6db00000000001db6db0000000000000000, mercenary_face_2 ],


#Village stores
["village_1_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots,itm_felt_hat], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff601040536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_3_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600140536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_9_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots,itm_leather_cap], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600250536db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_24_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_robe,itm_wrapping_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600354636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_31_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600454636db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_37_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_robe,itm_wrapping_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600458736db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_46_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff60045c836db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_65_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_fur_coat,itm_wrapping_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600400966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_73_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_hide_boots,itm_felt_hat], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500966db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_90_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_tabard,itm_wrapping_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000e7600500b66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_91_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_furs], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["village_92_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_shirt], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["village_93_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_shirt], def_attrib|level(2), wp(20), knows_inventory_management_10, man_face_old_1, man_face_older_2 ],
["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_98_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_short_tunic,itm_hide_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600400c66db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
["village_104_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_coarse_tunic,itm_nomad_boots,itm_fur_hat], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600401266db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_short_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_tabard, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_tabard, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
["village_110_elder", "Village_Elder", "{!}village_1_elder", tf_hero|tf_is_merchant|tf_randomize_face, no_scene, reserved, fac_commoners, [itm_robe,itm_wrapping_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000ff600701366db6db6db6db6db00000000001db6db0000000000000000, man_face_older_2 ],
# Place extra merchants before this point
["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

#Used for player enterprises
["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003600b01336db6db6db6db6db00000000001db6db0000000000000000 ],
["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_padded_leather,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000003600c01236db6db6db6db6db00000000001db6db0000000000000000 ],
["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x000000003600e04130db6db6db6db6db00000000001db6db0000000000000000 ],
["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007f601008230db6db6db6db6db00000000001db6db0000000000000000 ],
["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007f601108230db6db6db6db6db00000000001db6db0000000000000000 ],
["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x00000007f60110c338db6db6db6db6db00000000001db6db0000000000000000 ],
["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007f60120c338db6db6db6db6db00000000001db6db0000000000000000 ],
["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x00000007f600114438db6db6db61b6db00000000001db6db0000000000000000 ],
["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x00000007e800214438db6db6db61b6db00000000001db6db0000000000000000 ],
["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800314438db6db6db61b6db00000000001db6db0000000000000000 ],
["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common, 0x00000007e800514538db6db6db61b6db00000000001db6db0000000000000000 ],
["town_12_master_craftsman", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_coarse_tunic,itm_leather_boots], def_attrib|level(2), wp(20), knows_common, 0x00000007e800614638db6db6db61b6db00000000001db6db0000000000000000 ],
["town_13_master_craftsman", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800714638db6db6db61b6db00000000001db6db0000000000000000 ],
["town_14_master_craftsman", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800814738db6db6db61b6db00000000001db6db0000000000000000 ],
["town_15_master_craftsman", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800914838db6db6db61b6db00000000001db6db0000000000000000 ],
["town_16_master_craftsman", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800b14938db6db6db61b6db00000000001db6db0000000000000000 ],
["town_17_master_craftsman", "{!}Town 17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800c18b38db6db6db61b6db00000000001db6db0000000000000000 ],
["town_18_master_craftsman", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_leather_apron,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000007e800e1cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["town_19_master_craftsman", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_hide_boots,itm_fur_coat], def_attrib|level(2), wp(20), knows_common, 0x00000004e80101cd38db6db6db61b6db00000000001db6db0000000000000000 ],
["town_20_master_craftsman", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_blue_hose,itm_shirt], def_attrib|level(2), wp(20), knows_common, 0x00000004e801020f38db6db6db61b6db00000000001db6db0000000000000000 ],
["town_21_master_craftsman", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_nobleman_outfit,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000004e801120f38db6db6db61b6db00000000001db6db0000000000000000 ],
["town_22_master_craftsman", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, no_scene, reserved, fac_neutral, [itm_shirt,itm_blue_hose], def_attrib|level(2), wp(20), knows_common, 0x00000004e801220f38db6db6db61b6db00000000001db6db0000000000000000 ],



# Chests
["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common,0],
["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_4","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_5","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_chevaliere,],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_6","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_espee_ecuyer,],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_7","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_torch,itm_woolen_hose,itm_dress,itm_red_shirt,itm_bois],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_8","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_torch,itm_bois,itm_ustensil, itm_plan_5],def_attrib|level(18),wp(60),knows_common, 0],

["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],

["chest_4toul","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_plis_toul,itm_dagger_medievale],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_5cat","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_epee_jeanne_charles],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_6rennes","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_grimoire_rennes_chat],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_7orleans","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_grimoire_orleans],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_8chateaux","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_torch, itm_one_handed_battle_axe_c],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_9_logesecrete","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_grimoire_orleans],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],
["chest_10_logerouen","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[itm_tresort_1,itm_tresort_2,itm_tresort_3,itm_tresort_4,itm_tresort_5,itm_tresort_6, itm_templar_q_sword],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],


["tutorial_chest_9","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_torch,itm_lui_knightaxeoneh,itm_ustensil, itm_mail_gauntlets],def_attrib|level(18),wp(60),knows_common, 0],

["tutorial_chest_10","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_hourglass_gauntlets,itm_bois,itm_mail_coif_full, itm_nasal_helmet],def_attrib|level(18),wp(60),knows_common, 0],

["tutorial_chest_11","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_torch,itm_full_helm,itm_bayeux, itm_caithness],def_attrib|level(18),wp(60),knows_common, 0],

["tutorial_chest_12","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_1mace,itm_flamberge,itm_common_hood],def_attrib|level(18),wp(60),knows_common, 0],

["tutorial_chest_13","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_haubergeon,itm_woolen_cap,itm_woodenbuckler],def_attrib|level(18),wp(60),knows_common, 0],

["tutorial_chest_14","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_breton_peasant_man,itm_g_tw_shirt,itm_mail_hauberk, itm_plan_5],def_attrib|level(18),wp(60),knows_common, 0],
#RPG village mine
["tutorial_chest_15","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_torch,itm_bois,itm_bois],def_attrib|level(18),wp(60),knows_common, 0],
#ENTREE GROTTE avec tentes
["tutorial_chest_16","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_gaddhjalt,itm_heraldric_shieldblue3lys],def_attrib|level(18),wp(60),knows_common, 0],

#bois des cerfs
["tutorial_chest_17","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_bolts,itm_quest_sniper_crossbow,],def_attrib|level(18),wp(60),knows_common, 0],
["tutorial_chest_18","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_klappvisier,itm_mail_gauntlets,itm_mail_boots,itm_1mace,itm_agincourt],def_attrib|level(18),wp(60),knows_common, 0],

# These are used as arrays in the scripts.
["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point

["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,[itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,vaegir_face1,vaegir_face2],
["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,[itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,vaegir_face1,vaegir_face2],
["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_medieval_b,itm_throwing_daggers],def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1,man_face_old_2],

["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_viking_1],def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,bandit_face1,bandit_face2],

["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_viking_1],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],

["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,[itm_short_tunic,itm_linen_tunic,itm_coarse_tunic,itm_tabard,itm_leather_vest,itm_woolen_hose,itm_nomad_boots,itm_blue_hose,itm_wrapping_boots,itm_fur_hat,itm_leather_cap,itm_sword_viking_1],def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,bandit_face1,bandit_face2],



["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1,man_face_older_2],

["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,[itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1,vaegir_face2],

["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,[itm_robe,itm_black_hood,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,woman_face_1,woman_face_2],
["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,[itm_rich_outfit,itm_wrapping_boots],def_attrib|level(4),wp(60),knows_common,man_face_middle_1,man_face_older_2],


##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_tab_shield_heater_cav_a],    
  lord_attrib,wp(380),knows_lord_1,
    0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops
["swadian_crossbowman_multiplayer_ai", "Swadian Crossbowman", "Swadian Crossbowmen", tf_guarantee_all, no_scene, reserved, fac_kingdom_1, [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet], def_attrib|level(19), wp_melee(90), knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3, swadian_face_young_1, swadian_face_old_2 ],
["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,[itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,itm_studded_leather_coat,itm_ankle_boots],def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1,swadian_face_old_2],
["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,[itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1,swadian_face_old_2],
["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,[itm_arrows,itm_scimitar,itm_nomad_bow,itm_leather_vest,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,[itm_padded_leather,itm_nomad_boots,itm_spear,itm_tab_shield_kite_b,itm_mace_1],def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_horseman_multiplayer_ai", "Vaegir Horseman", "Vaegir Horsemen", tf_guarantee_all_wo_ranged|tf_mounted, no_scene, reserved, fac_kingdom_2, [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse], def_attrib|level(19), wp(100), knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3, vaegir_face_young_1, vaegir_face_older_2 ],
# ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
# [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
# itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c],
# def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
# ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
# [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
# itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
# def_attrib|level(21),wp(90)|wp_archery(150),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
# ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
# [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
# itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
# def_attrib|level(23),wp(130),knows_riding_7|knows_power_strike_5|knows_power_draw_4|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
# ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
# [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
# itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
# def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
# ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
# [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
# itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
# def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
# ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
# [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
# itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
# def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
# ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
# [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
# itm_leather_cap,itm_padded_leather,itm_nomad_boots],
# def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
# ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
# [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
# itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
# def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
# ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
##   TODO: Change weapons, copied from Nord Scout
# [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
# itm_skullcap,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
# def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
#  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_woolen_hose,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
#   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
#  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_woolen_hose,itm_sarranid_helmet1,itm_desert_turban],
#   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
#  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
#   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
#    itm_sarranid_mail_shirt,itm_woolen_hose,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
#   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],



#Multiplayer troops (they must have the base items only, nothing else)
["swadian_crossbowman_multiplayer","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,[itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_tab_shield_heater_a,itm_red_shirt,itm_ankle_boots],def_attrib_multiplayer|level(19),wpe(90,60,180,90),knows_common|knows_ironflesh_2|knows_athletics_5|knows_shield_5|knows_power_strike_2|knows_riding_1,swadian_face_young_1,swadian_face_old_2],
["swadian_infantry_multiplayer","Swadian Infantry","Swadian Infantry",tf_guarantee_all,0,0,fac_kingdom_1,[itm_sword_medieval_a,itm_tab_shield_heater_a,itm_ankle_boots],def_attrib_multiplayer|level(20),wpex(105,130,110,40,60,110),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_6|knows_riding_1,swadian_face_middle_1,swadian_face_old_2],
["swadian_man_at_arms_multiplayer","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,[itm_lance,itm_sword_medieval_a,itm_tab_shield_heater_a,itm_ankle_boots,itm_saddle_horse],def_attrib_multiplayer|level(20),wp_melee(110),knows_common|knows_riding_5|knows_ironflesh_3|knows_shield_2|knows_power_throw_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1,swadian_face_old_2],
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
["vaegir_archer_multiplayer","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,[itm_arrows,itm_scimitar,itm_nomad_bow,itm_linen_tunic,itm_hide_boots],def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_6|knows_athletics_4|knows_shield_2|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_spearman_multiplayer","Vaegir Spearman","Vaegir spearman",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,[itm_spear,itm_tab_shield_kite_a,itm_mace_1,itm_linen_tunic,itm_hide_boots],def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1,vaegir_face_older_2],
["vaegir_horseman_multiplayer", "Vaegir Horseman", "Vaegir Horsemen", tf_guarantee_all|tf_mounted, no_scene, reserved, fac_kingdom_2, [itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,itm_linen_tunic,itm_hide_boots,itm_saddle_horse], def_attrib_multiplayer|level(19), wpe(110,90,60,110), knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2, vaegir_face_young_1, vaegir_face_older_2 ],
# ["khergit_veteran_horse_archer_multiplayer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
# [itm_sword_khergit_1,itm_nomad_bow,itm_arrows,itm_tab_shield_small_round_a,
# itm_khergit_armor,_a,itm_hide_boots,itm_steppe_horse],
# def_attrib_multiplayer|level(21),wpe(80,150,60,100),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5|knows_athletics_3,khergit_face_middle_1, khergit_face_older_2],
# ["khergit_lancer_multiplayer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
# [itm_sword_khergit_1,itm_lance,itm_tab_shield_small_round_a,
# itm_khergit_armor,itm_hide_boots,itm_steppe_horse],
# def_attrib_multiplayer|level(21),wp(115),knows_riding_6|knows_ironflesh_3|knows_power_throw_3|knows_shield_2|knows_horse_archery_1|knows_power_strike_2|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
# ["nord_archer_multiplayer","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
# [itm_arrows,itm_sword_viking_2_small,itm_short_bow,
# itm_blue_tunic,itm_leather_boots],
# def_attrib_multiplayer|str_11|level(15),wpe(90,150,60,80),knows_ironflesh_2|knows_power_strike_2|knows_shield_2|knows_power_draw_5|knows_athletics_4|knows_riding_1,nord_face_young_1, nord_face_old_2],
# ["nord_veteran_multiplayer","Nord Huscarl","Nord Huscarls",tf_guarantee_all,0,0,fac_kingdom_4,
# [itm_sword_viking_1,itm_one_handed_war_axe_a,itm_tab_shield_round_a,
# itm_blue_tunic,itm_leather_boots],
# def_attrib_multiplayer|level(24),wpex(110,135,100,40,60,140),knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_athletics_6|knows_shield_3|knows_riding_1,nord_face_young_1, nord_face_older_2],
# ["nord_scout_multiplayer","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
# [itm_javelin,itm_sword_viking_1,itm_spear,itm_tab_shield_small_round_a,
# itm_blue_tunic,itm_leather_boots,itm_saddle_horse],
# def_attrib_multiplayer|level(19),wp(105),knows_riding_6|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3|knows_athletics_3,vaegir_face_young_1, vaegir_face_older_2],
# ["rhodok_veteran_crossbowman_multiplayer","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
# [itm_crossbow,itm_bolts,itm_fighting_pick,itm_tab_shield_pavise_a,
# itm_tunic_with_green_cape,itm_ankle_boots],
# def_attrib_multiplayer|level(20),wpe(100,60,180,90),knows_common|knows_ironflesh_2|knows_shield_2|knows_power_strike_2|knows_athletics_5|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
# ["rhodok_sergeant_multiplayer","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_all,0,0,fac_kingdom_5,
# [itm_fighting_pick,itm_tab_shield_pavise_a,itm_spear,
# itm_green_tunic,itm_ankle_boots],
# def_attrib_multiplayer|level(20),wpex(110,100,140,30,50,110),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_6|knows_riding_1,rhodok_face_middle_1, rhodok_face_older_2],
# ["rhodok_horseman_multiplayer","Rhodok Horseman","Rhodok Horsemen",tf_guarantee_all,0,0,fac_kingdom_5,
# [itm_sword_medieval_a,itm_tab_shield_heater_cav_a, itm_light_lance,
# itm_green_tunic,itm_ankle_boots,itm_saddle_horse],
# def_attrib_multiplayer|level(20),wp(100),knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_3,rhodok_face_middle_1, rhodok_face_older_2],
#  ["sarranid_archer_multiplayer","Sarranid Archer","Sarranid Archers",tf_guarantee_all,0,0,fac_kingdom_6,
#   [itm_arrows,itm_arabian_sword_a,itm_nomad_bow,
#    itm_sarranid_cloth_robe, itm_woolen_hose],
#   def_attrib_multiplayer|str_12|level(19),wpe(80,150,60,80),knows_ironflesh_2|knows_power_draw_5|knows_athletics_5|knows_shield_2|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
#  ["sarranid_footman_multiplayer","Sarranid Footman","Sarranid footman",tf_guarantee_all,0,0,fac_kingdom_6,
#   [itm_bamboo_spear, itm_tab_shield_kite_a, itm_arabian_sword_a,
#    itm_sarranid_cloth_robe, itm_woolen_hose],
#   def_attrib_multiplayer|str_12|level(19),wpex(110,100,130,30,50,120),knows_ironflesh_4|knows_shield_2|knows_power_throw_3|knows_power_strike_3|knows_athletics_6|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
#  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
#   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
#    itm_sarranid_cloth_robe, itm_woolen_hose,itm_saddle_horse],
#   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_2, [], 0, 0, 0, 0, 0],

#replacable troop, not used
["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000ab904100628cd95175b73336100000000001dba950000000000000000],
#erase later added to avoid errors

#Player history array
["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

["quick_battle_troop_1","Rodrigo de Braganca","Rodrigo de Braganca", tf_hero,0,0,fac_kingdom_1,[itm_long_hafted_knobbed_mace,itm_wooden_shield,itm_iron_staff,itm_throwing_daggers,itm_felt_hat,itm_fur_coat,itm_leather_gloves],str_9|agi_15|int_12|cha_12|level(15),wpex(109,33,132,15,32,100),knows_riding_3|knows_athletics_5|knows_shield_3|knows_weapon_master_3|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_3,0x0000000e240070cd598bb02b9556428c00000000001eabce0000000000000000,swadian_face_old_2],
["quick_battle_troop_2","Usiatra","Usiatra", tf_hero|tf_female,0,0,fac_kingdom_1,[itm_nomad_bow,itm_barbed_arrows,itm_scimitar,itm_tab_shield_small_round_c,itm_sumpter_horse,itm_leather_armor,itm_splinted_greaves],str_12|agi_14|int_11|cha_18|level(22),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_3|knows_athletics_4|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_1|knows_power_strike_3|knows_ironflesh_4,0x000000007f004000719b69422165b71300000000001d5d1d0000000000000000,swadian_face_old_2],
["quick_battle_troop_3","Hegen","Hegen", tf_hero,0,0,fac_kingdom_1,[itm_heavy_lance,itm_sword_two_handed_b,itm_sword_medieval_c,itm_tab_shield_heater_c,itm_warhorse,itm_guard_helmet,itm_coat_of_plates,itm_mail_mittens,itm_mail_boots],str_18|agi_16|int_12|cha_11|level(24),wpex(90,152,102,31,33,34),knows_riding_5|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_strike_6|knows_ironflesh_6,0x000000018000324428db8a431491472400000000001e44a90000000000000000,swadian_face_old_2],
["quick_battle_troop_4","Konrad","Konrad", tf_hero,0,0,fac_kingdom_1,[itm_sword_two_handed_a,itm_mace_4,itm_tab_shield_kite_d,itm_bascinet_3,itm_leather_armor,itm_mail_mittens,itm_mail_boots],str_18|agi_15|int_12|cha_12|level(24),wpex(130,150,130,30,50,90),knows_riding_2|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_throw_3|knows_power_strike_6|knows_ironflesh_6,0x000000081700205434db6df4636db8e400000000001db6e30000000000000000,swadian_face_old_2],
["quick_battle_troop_5","Sverre","Sverre", tf_hero,0,0,fac_kingdom_1,[itm_long_axe,itm_sword_viking_1,itm_light_throwing_axes,itm_tab_shield_round_d,itm_mail_hauberk,itm_leather_gloves,itm_leather_boots],str_15|agi_15|int_12|cha_12|level(21),wpex(110,130,110,80,15,110),knows_riding_1|knows_athletics_5|knows_shield_4|knows_weapon_master_5|knows_power_draw_2|knows_power_throw_4|knows_power_strike_5|knows_ironflesh_5,0x000000048a00024723134e24cb51c91b00000000001dc6aa0000000000000000,swadian_face_old_2],
["quick_battle_troop_6","Borislav","Borislav", tf_hero,0,0,fac_kingdom_1,[itm_strong_bow,itm_barbed_arrows,itm_barbed_arrows,itm_shortened_spear,itm_leather_jerkin,itm_leather_gloves,itm_ankle_boots],str_12|agi_15|int_15|cha_9|level(18),wpex(70,70,100,140,15,100),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_weapon_master_3|knows_power_draw_4|knows_power_throw_3|knows_power_strike_2|knows_ironflesh_2,0x000000089e00444415136e36e34dc8e400000000001d46d90000000000000000,swadian_face_old_2],
["quick_battle_troop_7","Stavros","Stavros", tf_hero,0,0,fac_kingdom_1,[itm_heavy_crossbow,itm_bolts,itm_sword_medieval_b_small,itm_tab_shield_pavise_c,itm_nasal_helmet,itm_padded_leather,itm_leather_gloves,itm_leather_boots],str_12|agi_15|int_15|cha_12|level(21),wpex(100,70,70,30,140,80),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_3|knows_weapon_master_5|knows_power_throw_2|knows_power_strike_4|knows_ironflesh_4,0x0000000e1400659226e34dcaa46e36db00000000001e391b0000000000000000,swadian_face_old_2],
["quick_battle_troop_8","Gamara","Gamara", tf_hero|tf_female,0,0,fac_kingdom_1,[itm_throwing_spears,itm_throwing_spears,itm_scimitar,itm_leather_covered_round_shield,itm_leather_gloves,itm_woolen_hose],str_12|agi_15|int_12|cha_12|level(18),wpex(100,40,100,85,15,130),knows_horse_archery_2|knows_riding_2|knows_athletics_5|knows_shield_2|knows_weapon_master_4|knows_power_draw_2|knows_power_throw_4|knows_power_strike_2|knows_ironflesh_2,0x000000015400300118d36636db6dc8e400000000001db6db0000000000000000,swadian_face_old_2],
["quick_battle_troop_9","Aethrod","Aethrod", tf_hero,0,0,fac_kingdom_1,[itm_nomad_bow,itm_barbed_arrows,itm_barbed_arrows,itm_scimitar_b,itm_splinted_greaves],str_16|agi_21|int_12|cha_14|level(26),wpex(182,113,112,159,82,115),knows_horse_archery_2|knows_riding_2|knows_athletics_7|knows_shield_2|knows_weapon_master_4|knows_power_draw_7|knows_power_throw_3|knows_power_strike_3|knows_ironflesh_4,0x000000000000210536db6db6db6db6db00000000001db6db0000000000000000,swadian_face_old_2],
["quick_battle_troop_10","Zaira","Zaira", tf_hero|tf_female,0,0,fac_kingdom_1,[itm_sarranid_cavalry_sword,itm_strong_bow,itm_bodkin_arrows,itm_bodkin_arrows,itm_arabian_horse_b,itm_green_dress,itm_woolen_hose],str_13|agi_18|int_15|cha_9|level(18),wpex(126,19,23,149,41,26),knows_horse_archery_6|knows_riding_6|knows_weapon_master_2|knows_power_draw_4|knows_power_throw_1|knows_power_strike_4|knows_ironflesh_1,0x0000000502003001471a6a24dc6594cb00000000001da4840000000000000000,swadian_face_old_2],
["quick_battle_troop_11","Argo Sendnar","Argo Sendnar", tf_hero,0,0,fac_kingdom_1,[itm_morningstar,itm_tab_shield_round_d,itm_war_spear,itm_courser,itm_leather_gloves,itm_fur_hat,itm_leather_boots,itm_leather_jacket],str_15|agi_12|int_14|cha_20|level(28),wpex(101,35,136,15,17,19),knows_riding_4|knows_athletics_2|knows_shield_4|knows_weapon_master_4|knows_power_strike_5|knows_ironflesh_5,0x0000000e800015125adb702de3459a9c00000000001ea6d00000000000000000,swadian_face_old_2],
["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_2, [], 0, 0, 0, 0, 0],

["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000,vaegir_face_older_2],
["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000,vaegir_face_older_2],
["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000,vaegir_face_older_2],
["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000,vaegir_face_older_2],
["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,[itm_leather_jerkin,itm_leather_vest,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1,vaegir_face_older_2],
["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000,vaegir_face_older_2],
["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,[itm_linen_tunic,itm_hunter,itm_saddle_horse,itm_leather_gloves],def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1,vaegir_face_older_2],
["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_2,[itm_tribal_warrior_outfit,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1,khergit_face_older_2],
["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,[itm_leather_vest,itm_nomad_boots],def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000,vaegir_face_older_2],

["swadian_merchant", "Monk", "{!}Prominent", tf_hero, no_scene, reserved, fac_kingdom_2, [itm_sword_two_handed_a,itm_robe,itm_woolen_hose], def_attrib|level(2), wp(20), knows_common, 0x000000099300500e36db6db6dbcdb6db00000000001e391b0000000000000000 ],
["vaegir_merchant", "Merchant", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
#  ["khergit_merchant", "Merchant of Tulga", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
#  ["nord_merchant", "Merchant of Sargoth", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
#  ["rhodok_merchant", "Merchant of Jelkala", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
#  ["sarranid_merchant", "Merchant of Shariz", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,[itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_throwing_axes,itm_nasal_helmet,itm_nasal_helmet,itm_nasal_helmet,itm_mail_shirt,itm_mail_hauberk,itm_mail_hauberk,itm_leather_boots,itm_nomad_boots],def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1,nord_face_old_2],

["looter_leader", "Robber", "Looters", tf_hero, no_scene, reserved, fac_outlaws, [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots], def_attrib|level(8), wp(20), knows_common, 0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2 ],

["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

["relative_of_merchant", "Monk's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,[itm_linen_tunic,itm_nomad_boots],def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000000320410022d2595495491afa400000000001d9ae30000000000000000,mercenary_face_2],

["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
["paris_merchant", "Marchand des bas cartiers", "Marchand des bas cartiers", tf_hero|tf_is_merchant, scn_town_1_alley|entry(2), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_sumpter_horse_paris,itm_saddle_horseparis,itm_saddle_horseparis2], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000004c000620f38db6db6db61b6db00000000001db6db0000000000000000 ],
["paris_mendiant1", "Mendiant des bas cartiers", "Mendiant des bas cartiers", tf_hero, scn_town_1_alley|entry(3), reserved, fac_commoners, [itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000bbf00120f38db6db6db61b6db00000000001db6db0000000000000000 ],
["paris_formateurch", "Instructeur", "Instructeur", tf_hero, scn_town_paris6_alley|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_tabard], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000007bf00925038db6db6db61b6db00000000001db6db0000000000000000 ],
["paris_vendeurchevauxtop", "Maitre dresseur", "Maitre dresseur", tf_hero|tf_is_merchant, scn_town_paris6_alley|entry(3), reserved, fac_commoners, [itm_linen_shirt,itm_leather_boots,itm_warhorse,itm_warhorse_en2,itm_warhorse_f1,itm_horse7,itm_horse_bardedf01,itm_chargerplainblue,itm_chargerplainblue,itm_chargerplainred,itm_chargershinyblue,itm_charger], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000007bf00b28f38db6db6db61b6db00000000001db6db0000000000000000 ],
["paris_ecuyer", "Ecuyer", "Ecuyer", tf_hero, scn_town_paris6_alley|entry(4), reserved, fac_commoners, [itm_milanese_armour,itm_steel_greaves,itm_bastard_sword_b], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f01200f38db6db6db61b6db00000000001db6db0000000000000000 ],

### 1429 Special Troops

#npc dijon hospices
["dijon_moine_guer_troup", "Pere Jacob", "Pere Jacob", tf_hero, scn_town_6_fleuve|entry(2), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f00105238db6db6db61b6db00000000001db6db0000000000000000 ],
["dijon_moine_discut_troup", "Pretre", "Pretre", tf_hero, scn_town_6_fleuve|entry(3), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f0055ce38db6db6db61b6db00000000001db6db0000000000000000 ],
["dijon_blesse_troop", "Blesse de guerre", "Blesse de guerre", tf_hero, scn_town_6_fleuve|entry(4), reserved, fac_commoners, [itm_hunter_boots,itm_shirt], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000000834b38db6db6db61b6db00000000001db6db0000000000000000 ],

#jacobins
["jacobin_gueris", "pere Michel", "pere Michel", tf_hero, scn_town_13_alley|entry(2), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000000934038db6db6db61b6db00000000001db6db0000000000000000 ],
["jacobin_vendor", "pere Jaques", "pere Jaques", tf_hero|tf_is_merchant, scn_town_13_alley|entry(3), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a4000a58e38db6db6db61b6db00000000001db6db0000000000000000 ],
["jacobin_chief", "pere Mathieu", "pere Mathieu", tf_hero, scn_town_13_alley|entry(4), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a4000b5ce38db6db6db61b6db00000000001db6db0000000000000000 ],
["jacobin_benis", "pere Guillaume", "pere Guillaume", tf_hero, scn_town_13_alley|entry(5), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a6200e01338db6db6db61b6db00000000001db6db0000000000000000 ],

#soeurs
["soeur_1d", "Soeur", "Soeur", tf_female|tf_hero, scn_town_8_alley|entry(2), reserved, fac_commoners, [itm_coiffe_soeur,itm_woolen_hose,itm_robe], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000 ],
["soeur_2d", "Soeur", "Soeur", tf_female|tf_hero, scn_town_8_alley|entry(4), reserved, fac_commoners, [itm_coiffe_soeur,itm_woolen_hose,itm_robe], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000 ],
["soeur_3d", "Mere superieure", "Mere superieure", tf_female|tf_hero, scn_town_8_alley|entry(3), reserved, fac_commoners, [itm_coiffe_mere,itm_woolen_hose,itm_robe], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000 ],
["soeur_4d", "Soeur", "Soeur", tf_female|tf_hero, scn_town_8_alley|entry(5), reserved, fac_commoners, [itm_coiffe_soeur,itm_woolen_hose,itm_robe], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000 ],
#

["limoge_artisant1", "Ingenieur", "Ingenieur", tf_hero, scn_town_10_alley|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_shirt], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a6200e05338db6db6db61b6db00000000001db6db0000000000000000 ],
["limoge_artisant2", "Cordier", "Cordier", tf_hero, scn_town_10_alley|entry(3), reserved, fac_commoners, [itm_wrapping_boots,itm_shirt], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a6201009438db6db6db61b6db00000000001db6db0000000000000000 ],
["limoge_artisant3", "Chef Ingenieur", "Chef Ingenieur", tf_hero|tf_is_merchant, scn_town_10_alley|entry(4), reserved, fac_commoners, [itm_leather_boots,itm_linen_shirt,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_cartridges,itm_matchlock_1,itm_matchlock_1,itm_matchlock_1,itm_matchlock_2,itm_matchlock_1,itm_matchlock_2,itm_matchlock_2], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a620110c038db6db6db61b6db00000000001db6db0000000000000000 ],

#caserne tours

["tour_caserne_1", "Soldat en garnison", "Soldat en garnison", tf_hero, scn_town_16_alley|entry(5), reserved, fac_commoners, [itm_leather_boots,itm_leather_vest,itm_bastard_sword_b], def_attrib|level(2)|str_16, wp(20), knows_common, 0x00000001e20120c038db6db6db61b6db00000000001db6db0000000000000000 ],
["tour_caserne_2", "Soldat en garnison", "Soldat en garnison", tf_hero, scn_town_16_alley|entry(6), reserved, fac_commoners, [itm_wrapping_boots,itm_leather_vest,itm_bastard_sword_a], def_attrib|level(2)|str_16, wp(20), knows_common, 0x00000001e200008038db6db6db61b6db00000000001db6db0000000000000000 ],
["tour_caserne_3", "Soldat en garnison", "Soldat en garnison", tf_hero, scn_town_16_alley|entry(7), reserved, fac_commoners, [itm_leather_boots,itm_tabard,itm_bastard_sword_a,itm_wooden_shield], def_attrib|level(2)|str_16, wp(20), knows_common, swadian_face_middle_2 ],
["tour_caserne_4", "Instructeur", "Instructeur", tf_hero, scn_town_16_alley|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_black_brigandine,itm_baron], def_attrib|level(22)|str_16|agi_20, wp(220), knows_common|knows_ironflesh_8, 0x00000001e200100038db6db6db61b6db00000000001db6db0000000000000000 ],
["tour_caserne_5", "Soldat en garnison", "Soldat en garnison", tf_hero, scn_town_16_alley|entry(40), reserved, fac_commoners, [itm_wrapping_boots,itm_leather_vest,itm_duke], def_attrib|level(2)|str_16, wp(20), knows_common, swadian_face_younger_1 ],
["tour_caserne_6", "Soldat en garnison", "Soldat en garnison", tf_hero, scn_town_16_alley|entry(41), reserved, fac_commoners, [itm_leather_boots,itm_leather_vest,itm_duke], def_attrib|level(2)|str_16, wp(20), knows_common, swadian_face_young_2 ],
#forgerons orleans

["orleans_maitre", "Maistre forgeron", "Maistre forgeron", tf_hero|tf_is_merchant, scn_town_15_alley|entry(2), reserved, fac_commoners, [itm_wrapping_boots,itm_dagger,itm_estoc,itm_estoc,itm_realclaymore,itm_realflambergeb,itm_realflambergeb,itm_realflambergeb,itm_baron,itm_baron,itm_baron,itm_duke,itm_duke,itm_darkknightsword,itm_darkknightsword,itm_estoc,itm_realclaymore,itm_realclaymore,itm_realclaymore,itm_agincourt,itm_agincourt,itm_agincourt,itm_agincourt,itm_agincourt,itm_flamberge,itm_realflambergeb,itm_realespadona,itm_realespadona,itm_realespadona,itm_realespadona,itm_realespadona,itm_mercenary,itm_mercenary,itm_flamberge,itm_flamberge,itm_realflambergeb,itm_realespadon,itm_realespadon,itm_realespadona,itm_realespadona,itm_bb_complet_plates_b,itm_plan_1,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_3,itm_plan_3,itm_plan_4,itm_plan_5,itm_plan_5,itm_plan_6,itm_plan_7,itm_plan_7,itm_plan_7,itm_bb_complet_plates_b,itm_bb_complet_plates_r], def_attrib|level(2)|str_16, wp(20), knows_common|knows_inventory_management_10, 0x00000001e200514238db6db6db61b6db00000000001db6db0000000000000000 ],
["orleans_aprentis", "Compagnon Forgeron", "Compagnon Forgeron", tf_hero, scn_town_15_alley|entry(3), reserved, fac_commoners, [itm_leather_boots,itm_leather_vest], def_attrib|level(2)|str_16, wp(20), knows_common, 0x00000001e200214038db6db6db61b6db00000000001db6db0000000000000000 ],

#vendeurs bordeau
["bordeau_artisant1", "Fabriquant de Bannieres", "Fabriquant de Bannieres", tf_hero, scn_town_14_alley|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_shirt,itm_dagger], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000001e200714238db6db6db61b6db00000000001db6db0000000000000000 ],
["bordeau_artisant2", "Sommelier", "Sommelier", tf_hero|tf_is_merchant, scn_town_14_alley|entry(3), reserved, fac_commoners, [itm_wrapping_boots,itm_shirt,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn,itm_vinn], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000ae200818338db6db6db61b6db00000000001db6db0000000000000000 ],
["bordeau_artisant3", "Vendeur de Livres", "Vendeur de Livres", tf_hero|tf_is_merchant, scn_town_14_alley|entry(4), reserved, fac_commoners, [itm_leather_boots,itm_linen_shirt,itm_book_tactics,itm_book_persuasion,itm_book_leadership,itm_book_leadership,itm_book_intelligence,itm_book_trade,itm_book_weapon_mastery,itm_book_engineering,itm_book_wound_treatment_reference,itm_book_wound_treatment_reference,itm_book_training_reference,itm_book_surgery_reference,itm_book_surgery_reference], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000ae20091c538db6db6db61b6db00000000001db6db0000000000000000 ],
["bordeau_artisant4", "Potier", "Potier", tf_hero|tf_is_merchant, scn_town_14_alley|entry(5), reserved, fac_commoners, [itm_leather_boots,itm_shirt,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000ae200a20738db6db6db61b6db00000000001db6db0000000000000000 ],

#vendeurs fleuve
["provence", "Paysan", "Paysan", tf_hero|tf_is_merchant, scn_town_6_alley|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_shirt,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003c01220738db6db6db61b6db00000000001db6db0000000000000000, 0x000000003c01220738db6db6db61b6db00000000001db6db0000000000000000 ],
["provence2", "Marchant itinerant", "Marchant itinerant", tf_hero|tf_is_merchant, scn_town_6_alley|entry(3), reserved, fac_commoners, [itm_gambeson,itm_woolen_hose,itm_bastard_sword_a,itm_bastard_sword_b,itm_sword_medieval_a,itm_short_bow,itm_arrows,itm_crossbow,itm_bolts,itm_crossbow,itm_light_crossbow,itm_bolts,itm_gambeson,itm_leather_jacket,itm_battle_shieldcharlesv,itm_heraldric_shieldblueerminestripes,itm_heraldric_shieldblueerminestripes,itm_tab_shield_round_a,itm_wooden_buckler1,itm_hand_axe,itm_dagger_medievale,itm_mail_coif,itm_torch], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003c0042c838db6db6db61b6db00000000001db6db0000000000000000, 0x000000003c0042c838db6db6db61b6db00000000001db6db0000000000000000 ],
["provence3", "Marchant de chevaux", "Marchant de chevaux", tf_hero|tf_is_merchant, scn_town_6_alley|entry(4), reserved, fac_commoners, [itm_leather_apron,itm_wrapping_boots,itm_saddle_horse,itm_horse1], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000001200630a38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence4", "Passager", "Passager", tf_male|tf_guarantee_boots|tf_guarantee_armor, scn_town_6_alley|entry(5), reserved, fac_commoners, [itm_leather_boots,itm_ragged_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000000120083cb38db6db6db61b6db00000000001db6db0000000000000000, 0x00000000120083cb38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence5", "Passager", "Passager", tf_hero, scn_town_6_alley|entry(6), reserved, fac_commoners, [itm_shirt,itm_nomad_boots,itm_sword_medieval_b,itm_hunting_bow,itm_arrows], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000001200940b38db6db6db61b6db00000000001db6db0000000000000000, 0x000000001200940b38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence6", "Capitaine", "Capitaine", tf_male|tf_guarantee_boots|tf_guarantee_armor, scn_town_6_alley|entry(7), reserved, fac_commoners, [itm_wrapping_boots,itm_red_gambeson], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000000350015cf38db6db6db61b6db00000000001db6db0000000000000000, 0x00000000350015cf38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence7", "Equipage", "Equipage", tf_male|tf_guarantee_boots|tf_guarantee_armor, scn_town_6_alley|entry(8), reserved, fac_commoners, [itm_leather_boots,itm_leather_vest], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003500c59038db6db6db61b6db00000000001db6db0000000000000000, 0x000000003500c59038db6db6db61b6db00000000001db6db0000000000000000 ],

#vendeur baniere anger
["anger_baner", "Fabriquant de bannieres", "Fabriquant de bannieres", tf_hero, scn_town_3_alley|entry(4), reserved, fac_commoners, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000000060890d258db70b913a2192400000000001dd6d40000000000000000 ],

#garde ducal de caen
["caen_spec_guard", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_9_alley|entry(2), reserved, fac_neutral, [itm_morningstar,itm_battle_shieldedwardiii,itm_fighting_axe,itm_churburg_13_brass_f,itm_mail_chausses,itm_hounskull,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608c01258db70b913a2192400000000001dd6d40000000000000000 ],

#garde ducal de caen interieur!
["caen_spec_guard_int1", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english, scn_town_9bis_alley|entry(2), reserved, fac_neutral, [itm_morningstar,itm_fighting_axe,itm_battle_shieldedwardiii,itm_surcoat_over_mail_e4,itm_mail_chausses,itm_hounskull,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000609001258db70b913a2192400000000001dd6d40000000000000000 ],
["caen_spec_guard_int2", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english, scn_town_9bis_alley|entry(3), reserved, fac_neutral, [itm_fighting_axe,itm_bastard_sword_a,itm_surcoat_over_mail_e4,itm_mail_chausses,itm_hounskull,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000609100058db70b913a2192400000000001dd6d40000000000000000 ],
#pnj de chateau caen interieur!
["caen_chateau_conte", "Comte", "Comte", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(4), reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_dagger_medievale,itm_bb_noble_hat], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608100158db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_garde1", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english, scn_town_9bis_alley|entry(5), reserved, fac_neutral, [itm_bastard_sword_a,itm_battle_shieldedwardiii,itm_surcoat_over_mail_e4,itm_mail_coif,itm_mail_chausses,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608300158db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_garde2", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(6), reserved, fac_neutral, [itm_morningstar,itm_fighting_axe,itm_surcoat_over_mail_e4,itm_mail_chausses,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608500058db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_armurier", "Armurier du chateau", "Armurier du chateau", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(7), reserved, fac_neutral, [itm_surcoat_over_mail_e2,itm_mail_chausses,itm_iron_greaves,itm_sword_of_war], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a4608910558db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_archer", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english, scn_town_9bis_alley|entry(8), reserved, fac_neutral, [itm_fighting_axe,itm_surcoat_over_mail_e4,itm_mail_coif,itm_mail_chausses,itm_iron_greaves,itm_long_bow,itm_arrows], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10|knows_power_draw_8, 0x0000000a4608a08558db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_garde3", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english, scn_town_9bis_alley|entry(9), reserved, fac_neutral, [itm_surcoat_over_mail_e4,itm_bastard_sword_a,itm_mail_coif,itm_battle_shieldedwardiii,itm_mail_chausses,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000a4608b08518db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_garde4", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english, scn_town_9bis_alley|entry(10), reserved, fac_neutral, [itm_morningstar,itm_fighting_axe,itm_surcoat_over_mail_e4,itm_mail_chausses,itm_hounskull,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608e14518db70b913a2192400000000001dd6d40000000000000000 ],
["caen_chateau_garde5", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_english, scn_town_9bis_alley|entry(11), reserved, fac_neutral, [itm_bastard_sword_a,itm_battle_shieldedwardiii,itm_surcoat_over_mail_e4,itm_mail_chausses,itm_iron_greaves], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000608e14524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_gardecour", "Garde du Chateau", "Garde du Chateau", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english, scn_town_9bis_alley|entry(12), reserved, fac_neutral, [itm_bastard_sword_a,itm_surcoat_over_mail_e4,itm_mail_coif,itm_mail_chausses,itm_iron_greaves,itm_long_bow,itm_arrows], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10|knows_power_throw_8, 0x000000000609014524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitespec", "Convive", "Convive", tf_english|tf_guarantee_boots|tf_guarantee_armor, scn_town_9bis_alley|entry(13), reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose], def_attrib|level(2)|str_16, wp(20), 0, 0x00000000000011c516db8db6db6db6db00000000001db6db0000000000000000 ],
["caen_chateau_rebel", "Rebelle", "Rebelle", tf_unkillable|tf_guarantee_boots|tf_guarantee_armor, scn_town_9bis_alley|entry(14), reserved, fac_neutral, [itm_bastard_sword_b,itm_hide_boots,itm_shirt], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f09218524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitee1", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(15), reserved, fac_neutral, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000609114524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitee2", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(16), reserved, fac_neutral, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f08018524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitee3", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(17), reserved, fac_neutral, [itm_woolen_hose,itm_linen_tunic], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f08018524db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitee4", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(18), reserved, fac_neutral, [itm_woolen_hose,itm_linen_tunic], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000003f08320624db6db6db6136db00000000001db6db0000000000000000 ],
["caen_chateau_invitee5", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_english, scn_town_9bis_alley|entry(19), reserved, fac_neutral, [itm_woolen_hose,itm_linen_shirt], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x0000000fc008424624db6db6db6136db00000000001db6db0000000000000000 ],

#acteurs ferme mathieu
["mathieu_farm", "Mathieu", "Mathieu", tf_hero|tf_is_merchant, scn_ferm_mat|entry(2), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000043f08e2462cdb6db6db6136db00000000001db6db0000000000000000 ],
["femme_farm", "Femme de Mathieu", "Femme de Mathieu", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_ferm_mat|entry(3), reserved, fac_commoners, [itm_peasant_dress,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_woman_face_2 ],

#acteurs camp de chasse
["chasse_camp_gouv", "Gouverneur", "Gouverneur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_english, scn_camp_chasseur|entry(2), reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_sword_medieval_a,itm_horse6e01], def_attrib|level(2)|agi_6, wp(20), knows_inventory_management_10|knows_riding_3, 0x000000003f09000620db6db6db6136db00000000001db6db0000000000000000 ],
["chasse_camp_1", "Garde du gouverneur", "Garde du gouverneur", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_english, scn_camp_chasseur|entry(40), reserved, fac_neutral, [itm_early_transitional_e1,itm_early_transitional_e3,itm_early_transitional_e5,itm_early_transitional_e7,itm_splinted_greaves_spurs,itm_mail_chausses_e1,itm_hunter_e,itm_mail_mittens,itm_mail_gauntlets,itm_templar,itm_bayeux,itm_hospitaller,itm_mercenary,itm_regent,itm_mail_coif], def_attrib|level(19), wp(90), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_riding_2, 0x000000003f09100620db6db6db6136db00000000001db6db0000000000000000 ],
["chasse_camp_2", "Garde du gouverneur", "Garde du gouverneur", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_english, scn_camp_chasseur|entry(41), reserved, fac_neutral, [itm_early_transitional_e1,itm_early_transitional_e3,itm_early_transitional_e5,itm_early_transitional_e7,itm_splinted_greaves_spurs,itm_mail_chausses_e1,itm_hunter_e,itm_mail_mittens,itm_mail_gauntlets,itm_templar,itm_bayeux,itm_hospitaller,itm_mercenary,itm_regent,itm_mail_coif], def_attrib|level(19), wp(90), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_riding_2, 0x000000003f08108020db6db6db6136db00000000001db6db0000000000000000 ],
["chasse_camp_cond", "Paysan", "Paysan", tf_guarantee_boots|tf_guarantee_armor, scn_camp_chasseur|entry(3), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_wooden_stick], def_attrib|level(12)|str_10|agi_10, wp(20), knows_inventory_management_10|knows_ironflesh_8|knows_power_strike_3, 0x00000003bf0840012adb6db6db6136db00000000001db6db0000000000000000 ],
["chasse_camp_bour", "Paysan", "Paysan", tf_guarantee_boots|tf_guarantee_armor, scn_camp_chasseur|entry(4), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_knife], def_attrib|level(12), wp(20), knows_inventory_management_10|knows_ironflesh_8, 0x00000009bf0850022adb6db6db6136db00000000001db6db0000000000000000 ],

#acteurs manoire assassinat
["banquier", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon, scn_assa_manoire|entry(2), reserved, fac_neutral, [itm_linen_tunic,itm_woolen_hose,itm_dagger_medievale], def_attrib|level(2), wp(20), 0, 0x00000009bf0850022adb6db6db6136db00000000001db6db0000000000000000 ],
["manoire_conviv_invit1", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon, scn_assa_manoire|entry(40), reserved, fac_neutral, [itm_woolen_hose,itm_linen_tunic,itm_dagger_medievale], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008f804e3873b0ba9d72031acec00000000001cfb6e0000000000000000 ],
["manoire_conviv_invit2", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon, scn_assa_manoire|entry(41), reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_sword_medieval_a], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008f804f38732db6db6db6db6db00000000001db6db0000000000000000 ],
["manoire_conviv_medic", "Convive", "Convive", tf_guarantee_boots|tf_guarantee_armor|tf_bourgignon, scn_assa_manoire|entry(42), reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008f80503c832db6d37646db6db00000000001db6db0000000000000000 ],
["manoire_chevalier", "Chevalier de Bourgogne", "Chevalier de Bourgogne", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield|tf_bourgignon, scn_assa_manoire|entry(43), reserved, fac_neutral, [itm_churburg_13_brass,itm_splinted_greaves_spurs,itm_shynbaulds,itm_hourglass_gauntlets_ornate,itm_senlac,itm_sovereign,itm_baron], def_attrib|level(24), wp(115), knows_common|knows_shield_1|knows_ironflesh_1|knows_power_strike_3|knows_athletics_3|knows_riding_3, 0x00000008f80513cb32db6d37646db6db00000000001db6db0000000000000000, 0x00000008f80513cb32db6d37646db6db00000000001db6db0000000000000000 ],
["manoire_halberdier1", "Hallbardier_Bourguignon", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon, scn_assa_manoire|entry(44), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_visored_sallet,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x00000008f805214b32db6d37646db6db00000000001db6db0000000000000000 ],
["manoire_halberdier2", "Hallbardier_Bourguignon", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon, scn_assa_manoire|entry(45), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_visored_sallet,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x00000008f804014c32db6d37646db6db00000000001db6db0000000000000000 ],
["manoire_cuistot", "Cuisinier", "Cuisinier", tf_hero|tf_is_merchant|tf_bourgignon, scn_assa_manoire|entry(46), reserved, fac_neutral, [itm_leather_apron,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000008f804114d32db6d37646db6db00000000001db6db0000000000000000 ],

#milicien ouvreur catas paris
["cata_miliceparis", "Milicien de Paris", "Milicien de Paris", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, scn_town_paris_cataentry|entry(40), reserved, fac_neutral, [itm_heraldic_mail_with_surcoat,itm_heraldic_mail_with_tunic,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_lui_smallhallberda], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x000000003804218f32db6d37646db6db00000000001db6db0000000000000000, 0x000000003804218f32db6d37646db6db00000000001db6db0000000000000000 ],

#rebels des catas
["catarebel_dsentinel", "Sentinele", "Sentinele", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_reservoir|entry(2), reserved, fac_black_khergits, [itm_shirt,itm_wrapping_boots,itm_dagger_medievale,itm_spiked_mace], def_attrib|level(14), wp(80), knows_common, 0x000000003804618f32db6d37646db6db00000000001db6db0000000000000000, 0x000000003804618f32db6d37646db6db00000000001db6db0000000000000000 ],
["catarebel_redid1", "Rebelle de Paris", "Rebelle de Paris", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_catacomb_reservoir|entry(3), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14), wp(80), knows_common|knows_power_draw_6, 0x000000003804919232db6d37646db6db00000000001db6db0000000000000000, 0x000000003804919232db6d37646db6db00000000001db6db0000000000000000 ],
["catarebel_redid2", "Rebelle de Paris", "Rebelle de Paris", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, scn_catacomb_reservoir|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluelysstripes,itm_crossbow,itm_bolts], def_attrib|level(14)|str_6|agi_6, wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x000000003804a1d232db6d37646db6db00000000001db6db0000000000000000, 0x000000003804a1d232db6d37646db6db00000000001db6db0000000000000000 ],
["catarebel_rvend", "Rebelle de Paris", "Rebelle de Paris", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, scn_catacomb_reservoir|entry(5), reserved, fac_black_khergits, [itm_wrapping_boots,itm_shirt,itm_bastard_sword_a,itm_battle_shieldbluecross,itm_crossbow,itm_bolts,itm_wooden_shield,itm_wooden_shield,itm_arrows,itm_arrows,itm_bolts,itm_crossbow,itm_pottery,itm_pottery,itm_iron,itm_iron,itm_iron_greaves], def_attrib|level(14)|str_6|agi_6, wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x000000003804b29332db6d37646db6db00000000001db6db0000000000000000, 0x000000003804b29332db6d37646db6db00000000001db6db0000000000000000 ],
["catarebel_rchef", "Chef des Rebelles de Paris", "Chef des Rebelles de Paris", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, scn_catacomb_reservoir|entry(6), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows,itm_woodenbuckler,itm_templar], def_attrib|level(19)|str_8|agi_7, wp(180), knows_common|knows_power_draw_6, 0x000000003805028128db6d37646db6db00000000001db6cb0000000000000000, 0x000000003805028128db6d37646db6db00000000001db6cb0000000000000000 ],
["catarebel_womanrebel", "Rebelle de Paris", "Rebelle de Paris", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reservoir|entry(7), reserved, fac_black_khergits, [itm_peasant_dress,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood,itm_templar,itm_wooden_shield], def_attrib|level(12)|str_6|agi_6, wp(140), knows_common|knows_athletics_6|knows_shield_5|knows_ironflesh_5, 0x0000000a830c30046adbd6b8e486b6a600000000000ec76b0000000000000000, 0x0000000a830c30046adbd6b8e486b6a600000000000ec76b0000000000000000 ],
["catarebel_womanresid", "Rebelle de Paris", "Rebelle de Paris", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reservoir|entry(8), reserved, fac_black_khergits, [itm_dress,itm_woolen_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood,itm_templar,itm_wooden_shield], def_attrib|level(12)|str_6|agi_3, wp(70), knows_common|knows_ironflesh_3, 0x00000007c004300268a4819524652c5b00000000001cd9530000000000000000, 0x00000007c004300268a4819524652c5b00000000001cd9530000000000000000 ],

#rebels des catas attack
["catacomando_dsentinel", "Sentinele", "Sentinele", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_reperteng|entry(2), reserved, fac_black_khergits, [itm_shirt,itm_wrapping_boots,itm_dagger_medievale,itm_spiked_mace], def_attrib|level(14), wp(80), knows_common, 0x000000018000200136db6db6db6db6db00000000001db6db0000000000000000, 0x000000018000200136db6db6db6db6db00000000001db6db0000000000000000 ],
["catacomando_redid1", "Rebelle de Paris", "Rebelle de Paris", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_catacomb_reperteng|entry(3), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14), wp(80), knows_common|knows_power_draw_6, 0x000000074000300336db8db6db6db4db00000000001db6db0000000000000000, 0x000000074000300336db8db6db6db4db00000000001db6db0000000000000000 ],
["catacomando_redid2", "Rebelle de Paris", "Rebelle de Paris", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, scn_catacomb_reperteng|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluecross,itm_crossbow,itm_bolts], def_attrib|level(14)|str_6|agi_6, wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000003da00518336db8db6db6d94dd00000000001db6db0000000000000000, 0x00000003da00518336db8db6db6d94dd00000000001db6db0000000000000000 ],
["catacomando", "Chef des Rebelles de Paris", "Chef des Rebelles de Paris", tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged, scn_catacomb_reperteng|entry(5), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows,itm_woodenbuckler,itm_templar], def_attrib|level(19)|str_8|agi_7, wp(180), knows_common|knows_power_draw_6, 0x00000005ff00120736db6db6db6d94dd00000000001db6db0000000000000000, 0x00000005ff00120736db6db6db6d94dd00000000001db6db0000000000000000 ],
["catacomando_womanrebel", "Rebelle de Paris", "Rebelle de Paris", tf_female|tf_hero|tf_unkillable|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reperteng|entry(6), reserved, fac_black_khergits, [itm_peasant_dress,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood,itm_templar,itm_wooden_shield], def_attrib|level(12)|str_6|agi_6, wp(140), knows_common|knows_athletics_6|knows_shield_5|knows_ironflesh_5, 0x00000007e600100524d4d25b9ca8c4d500000000001614640000000000000000, 0x00000007e600100524d4d25b9ca8c4d500000000001614640000000000000000 ],

#rebels des catas attack ANGLAIS
["catacom_serg", "Sergent Anglais", "Sergent Anglais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_english, scn_catacomb_reperteng|entry(40), reserved, fac_neutral, [itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e1,itm_splinted_greaves_e1,itm_mail_chausses_e1,itm_kettlehat1_painted,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_heater_cav_a,itm_kite_shieldreddragon,itm_tab_shield_heater_a,itm_battle_shieldedwardiii,itm_heraldric_shieldred3lions,itm_heraldric_shieldredlys,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_war_shieldwales,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_shield_3|knows_athletics_5, 0x00000008b805248428db6d37646db6db00000000001db6e30000000000000000, vaegir_face_older_2 ],
["catacom_serg2", "Sergent Anglais", "Sergent Anglais", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_catacomb_reperteng|entry(40), reserved, fac_neutral, [itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e1,itm_splinted_greaves_e1,itm_mail_chausses_e1,itm_kettlehat1_painted,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_c,itm_kite_shieldreddragon,itm_tab_shield_heater_a,itm_battle_shieldedwardiii,itm_heraldric_shieldredlys,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldredlys,itm_war_shieldwales,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["catacom1", "Millice Anglaise", "Millice Anglaise", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reperteng|entry(41), reserved, fac_neutral, [itm_leather_vest_e2,itm_leather_armor_e1,itm_leather_boots,itm_mail_chausses_e1,itm_leather_gloves,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],
["catacom2", "Millice Anglaise", "Millice Anglaise", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reperteng|entry(42), reserved, fac_neutral, [itm_leather_vest_e2,itm_leather_armor_e1,itm_leather_boots,itm_mail_chausses_e1,itm_coif_new_e1,itm_mail_coif,itm_leather_gloves,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],
["catacom3", "Millice Anglaise", "Millice Anglaise", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_catacomb_reperteng|entry(42), reserved, fac_neutral, [itm_leather_vest_e2,itm_leather_armor_e1,itm_leather_boots,itm_mail_chausses_e1,itm_coif_new_e1,itm_mail_coif,itm_leather_gloves,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],

#troupes du camp
["campement_troupe_1", "Soldat", "Soldat", tf_hero, scn_camp_19_alley|entry(2), reserved, fac_commoners, [itm_fur_coat,itm_leather_vest,itm_leather_boots,itm_nomad_boots,itm_sword_of_war], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_younger_1, swadian_face_middle_2 ],
["campement_troupe_2", "Soldat", "Soldat", tf_hero, scn_camp_19_alley|entry(3), reserved, fac_commoners, [itm_coarse_tunic,itm_nomad_vest,itm_leather_boots,itm_wrapping_boots,itm_sniper_crossbow], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000008b804058436db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["campement_troupe_3", "Soldat", "Soldat", tf_hero, scn_camp_19_alley|entry(4), reserved, fac_commoners, [itm_mail_shirt,itm_nomad_vest,itm_leather_boots,itm_coarse_tunic,itm_mail_boots,itm_bastard_sword_a], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_middle_2 ],
["campement_troupe_4", "Soldat", "Soldat", tf_hero, scn_camp_22_alley|entry(2), reserved, fac_commoners, [itm_leather_vest,itm_padded_cloth,itm_leather_boots,itm_wrapping_boots,itm_fauchard_1], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000380415c736db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["campement_troupe_5", "Soldat", "Soldat", tf_hero, scn_camp_22_alley|entry(3), reserved, fac_commoners, [itm_mail_shirt,itm_leather_vest,itm_padded_cloth,itm_wrapping_boots,itm_leather_boots,itm_dagger], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2 ],
["campement_troupe_6", "Soldat", "Soldat", tf_hero, scn_camp_22_alley|entry(4), reserved, fac_commoners, [itm_leather_vest,itm_padded_cloth,itm_leather_boots,itm_wrapping_boots,itm_dagger], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_middle_1, swadian_face_old_2 ],
["campement_troupe_7", "Soldat", "Soldat", tf_hero, scn_camp_20_alley|entry(2), reserved, fac_commoners, [itm_leather_armor,itm_leather_vest,itm_padded_cloth,itm_leather_boots,itm_mail_boots,itm_dagger,itm_bastard_sword_a], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2 ],
["campement_troupe_8", "Soldat", "Soldat", tf_hero, scn_camp_20_alley|entry(3), reserved, fac_commoners, [itm_mail_shirt,itm_leather_vest,itm_tabard,itm_leather_boots,itm_mail_boots,itm_bastard_sword_a], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000000004900736db6db6db6db6db00000000001db6db0000000000000000, swadian_face_older_2 ],
["campement_troupe_9", "Soldat", "Soldat", tf_hero, scn_camp_20_alley|entry(4), reserved, fac_commoners, [itm_leather_vest,itm_tabard,itm_leather_boots,itm_hunter_boots,itm_fauchard_1], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_old_2 ],
["campement_troupe_10", "Soldat", "Soldat", tf_hero, scn_camp_21_alley|entry(2), reserved, fac_commoners, [itm_tabard,itm_leather_vest,itm_hunter_boots,itm_leather_boots,itm_bastard_sword_a], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_middle_1, swadian_face_older_2 ],
["campement_troupe_11", "Soldat", "Soldat", tf_hero, scn_camp_21_alley|entry(3), reserved, fac_commoners, [itm_shirt,itm_leather_vest,itm_tabard,itm_leather_boots,itm_hunter_boots,itm_dagger], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000000004a04a36db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["campement_troupe_12", "Soldat", "Soldat", tf_hero, scn_camp_21_alley|entry(4), reserved, fac_commoners, [itm_leather_armor,itm_tabard,itm_leather_boots,itm_hunter_boots,itm_bastard_sword_b], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000087f0500cb36db6db6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["campement_troupe_chant_1", "Soldat", "Soldat", tf_hero, scn_camp_19_alley|entry(5), reserved, fac_commoners, [itm_gambeson,itm_fur_coat,itm_leather_vest,itm_mail_boots,itm_mail_boots,itm_leather_boots,itm_sword_of_war], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000087f05118f36db6db6db6db6db00000000001db6db0000000000000000, swadian_face_middle_2 ],
["campement_troupe_chant_2", "Soldat", "Soldat", tf_hero, scn_camp_22_alley|entry(5), reserved, fac_commoners, [itm_tabard,itm_leather_vest,itm_leather_boots,itm_nomad_boots,itm_sword_of_war], def_attrib|level(2), wp(20), knows_inventory_management_10, swadian_face_old_1, swadian_face_middle_2 ],
["campement_troupe_chant_3", "Soldat", "Soldat", tf_hero, scn_camp_20_alley|entry(5), reserved, fac_commoners, [itm_tabard,itm_fur_coat,itm_leather_boots,itm_nomad_boots,itm_sword_of_war], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000087f0521cf36db6db6db6db6db00000000001db6db0000000000000000, vaegir_face_younger_1 ],
["campement_troupe_chant_4", "Soldat", "Soldat", tf_hero, scn_camp_21_alley|entry(5), reserved, fac_commoners, [itm_tabard,itm_fur_coat,itm_leather_boots,itm_nomad_boots,itm_sword_of_war], def_attrib|level(2), wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],
#
["campement_troupe_serg_1", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_19_alley|entry(6), reserved, fac_commoners, [itm_templar,itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_steel_greaves,itm_iron_greaves,itm_shynbaulds,itm_mail_boots], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_young_1 ],
["campement_troupe_spec_1", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_19_alley|entry(7), reserved, fac_commoners, [itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_steel_greaves,itm_bastard_sword_b], def_attrib|level(2)|str_18, wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],
#
["campement_troupe_serg_2", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_22_alley|entry(6), reserved, fac_commoners, [itm_templar,itm_bb_complet_plates_b,itm_bb_complet_plates_charles,itm_steel_greaves,itm_iron_greaves,itm_shynbaulds,itm_mail_boots], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_young_1 ],
["campement_troupe_spec_2", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_22_alley|entry(7), reserved, fac_commoners, [itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_steel_greaves,itm_bastard_sword_b], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],
#
["campement_troupe_serg_3", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_20_alley|entry(6), reserved, fac_commoners, [itm_templar,itm_bb_complet_plates_b,itm_bb_complet_plates_charles,itm_steel_greaves,itm_iron_greaves,itm_shynbaulds,itm_mail_boots], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_young_1 ],
["campement_troupe_spec_3", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_20_alley|entry(7), reserved, fac_commoners, [itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_steel_greaves,itm_bastard_sword_b], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],
#
["campement_troupe_serg_4", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_21_alley|entry(6), reserved, fac_commoners, [itm_templar,itm_bb_complet_plates_charles,itm_bb_complet_plates_b,itm_steel_greaves,itm_iron_greaves,itm_shynbaulds,itm_mail_boots], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, swadian_face_young_1, swadian_face_young_1 ],
["campement_troupe_spec_4", "Sergent", "Sergent", tf_guarantee_boots|tf_guarantee_armor, scn_camp_21_alley|entry(7), reserved, fac_commoners, [itm_bb_complet_plates_b,itm_bb_complet_plates_charles,itm_steel_greaves,itm_bastard_sword_b], def_attrib|level(12)|str_18, wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],



["ribaude_1", "Ribaude", "Ribaude", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_town_1_alley|entry(4), reserved, fac_commoners, [itm_ribaude_dress6bluues,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000001200200538dca6b8dd8d36d200000000001ca72b0000000000000000 ],
["ribaude_2", "Ribaude", "Ribaude", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_town_1_alley|entry(5), reserved, fac_commoners, [itm_ribaude_dresss,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000000050010558b239244d94d100000000001d98e30000000000000000 ],
["ribaude_3", "Ribaude", "Ribaude", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_town_1_alley|entry(6), reserved, fac_commoners, [itm_ribaude_dress6bluues,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000000000000136db6db6db6db6db00000000001db6db0000000000000000 ],

#
["rebel_montpelier_tower_1", "Sentinelle", "Sentinelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(2), reserved, fac_black_khergits, [itm_shirt,itm_wrapping_boots,itm_dagger_medievale,itm_spiked_mace], def_attrib|level(14)|str_12, wp(80), knows_common, 0x000000003f0401cf36db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f0401cf36db6db6db6db6db00000000001db6db0000000000000000 ],
["rebel_montpelier_tower_2", "Archer Rebelle", "Archer Rebelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(3), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14)|str_12, wp(80), knows_common|knows_power_draw_6, 0x000000003f04120f36db6db6db6db6db00000000001cb6db0000000000000000, bandit_face2 ],
["rebel_montpelier_tower_3", "Fantassin Rebelle", "Fantassin Rebelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluecross,itm_heavy_crossbow,itm_bolts], def_attrib|level(14)|str_12, wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x000000003f04224f36db6db6db6db6db00000000001d36db0000000000000000, bandit_face2 ],
["rebel_montpelier_tower_4", "Archer Rebelle", "Archer Rebelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(5), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_nasal_helmet,itm_templar,itm_short_bow,itm_arrows], def_attrib|level(14)|str_12, wp(80), knows_common|knows_shield_5, 0x000000003f04629336db6db6db6db6db00000000001d36db0000000000000000, bandit_face2 ],
["rebel_montpelier_tower_5", "Arbaletier Rebelle", "Arbaletier Rebelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(6), reserved, fac_black_khergits, [itm_gambeson,itm_mail_boots,itm_templar,itm_bolts,itm_sniper_crossbow], def_attrib|level(14)|str_12, wp(80), knows_common|knows_shield_6|knows_power_throw_8, 0x000000003f0472c936db6db6db6db6db00000000001d36d30000000000000000, bandit_face2 ],
["rebel_montpelier_tower_6", "Arbaletier Rebelle", "Arbaletier Rebelle", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(7), reserved, fac_black_khergits, [itm_haubergeon_f1,itm_templar,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_sniper_crossbow,itm_bolts], def_attrib|level(14)|str_12, wp(80), knows_common|knows_riding_5|knows_power_throw_8, 0x000000003f0482c936db6db6db6db6db00000000001d36d30000000000000000, bandit_face2 ],
["rebel_montpelier_tower_7", "Francis", "Francis", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(8), reserved, fac_black_khergits, [itm_gambeson,itm_hide_boots,itm_templar], def_attrib|level(14)|str_12, wp(80), knows_common|knows_shield_6, 0x000000003f04934936db6db6db6db6db00000000001d36d30000000000000000, bandit_face2 ],
["rebel_montpelier_tower_8", "Chef Rebelle", "Chef Rebelle", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_tour_pins|entry(9), reserved, fac_black_khergits, [itm_mail_with_surcoat,itm_wrapping_boots,itm_dagger_medievale,itm_templar], def_attrib|level(14)|str_14, wp(80), knows_common, 0x00000007ba05218716db6db6db61b6db00000000001d36e30000000000000000, 0x00000007ba05218716db6db6db61b6db00000000001d36e30000000000000000 ],

#Excel Generated
["covoy_english_guard","Garde du convoi Anglais","Garde du convoi Anglais",tf_hero|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english,0,0,fac_convoi_weapons,[itm_hounskull,itm_churburg_13_mail,itm_splinted_greaves_spurs,itm_shynbaulds,itm_mail_boots,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_warhorse_en1,],def_attrib3,wp(110),knows_warrior_veteran,0x000000003f05100636db6db6db6db6db00000000001d36d30000000000000000,0x000000003f05100636db6db6db6db6db00000000001d36d30000000000000000],
["covoy_english_guard2","Fantassin du convoi Anglais","Fantassin du convoi Anglais",tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_convoi_weapons,[itm_coat_of_plates_e1,itm_coat_of_plates_e2,itm_mail_mittens,itm_wisby_gauntlets_red,itm_splinted_greaves_nospurs,itm_shynbaulds,itm_mail_boots,itm_mail_chausses,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,],def_attrib3,wp(110),knows_warrior_veteran,vaegir_face_young_1,bandit_face2],
["covoy_english_guard3","Archer du convoi Anglais","Archer du convoi Anglais",tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_convoi_weapons,[itm_kettlehat1,itm_kettlehat2,itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_padded_jack_e,itm_splinted_greaves_e1,itm_mail_boots,itm_long_bow,itm_arrows,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_long_bow,itm_sword_medieval_a,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,itm_arrows,],def_attrib3,wp(110),knows_archer_english,vaegir_face_young_1,bandit_face2],
["covoy_english_guard_end","Garde du convoi Anglais","Garde du convoi Anglais",tf_hero|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_english,0,0,fac_convoi_weapons,[itm_hounskull,itm_churburg_13_mail,itm_splinted_greaves_spurs,itm_shynbaulds,itm_mail_boots,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_templar,itm_warhorse_en1,],def_attrib3,wp(110),knows_warrior_veteran,bandit_face2,bandit_face2],

#Excel Generated END

#pirates du fleuve
["pirate_troupe_1", "Chef des pirates", "Chef des pirates", tf_hero|tf_bandit, scn_town_6_pirates|entry(40), reserved, fac_commoners, [itm_mail_hauberk,itm_hide_boots,itm_hunting_bow,itm_arrows,itm_dagger,itm_bastard_sword_a,itm_wooden_shield], def_attrib|level(2)|level(28)|str_14, wp(20), knows_inventory_management_10, 0x00000007ba04014616db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04014616db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_2", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_bastard_sword_a], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04118716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04118716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_3", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_bastard_sword_a], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04218616db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04218616db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_4", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_sword_medieval_a], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba0431c716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba0431c716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_5", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_sword_medieval_a], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba0451c716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba0451c716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_6", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_bastard_sword_b,itm_head_wrappings], def_attrib|level(25), wp(20), knows_inventory_management_10, 0x00000007ba04820716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04820716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_7", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_sword_of_war], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04920716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04920716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_8", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_sword_medieval_a,itm_wooden_shield], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04a20716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04a20716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_9", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_lui_battleaxeb,itm_bastard_sword_b], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04b20716db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04b20716db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_10", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_wooden_shield,itm_bastard_sword_b], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba0492c916db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba0492c916db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_11", "Pirate", "Pirate", tf_hero|tf_bandit, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_one_handed_war_axe_a,itm_wooden_shield], def_attrib|level(20), wp(20), knows_inventory_management_10, 0x00000007ba04a2c916db6db6db61b6db00000000001db6eb0000000000000000, 0x00000007ba04a2c916db6db6db61b6db00000000001db6eb0000000000000000 ],
["pirate_troupe_12", "Pirate", "Pirate", tf_bandit|tf_hero, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_one_handed_war_axe_a,itm_wooden_shield], def_attrib|level(20), wp(20), knows_inventory_management_10, rhodok_face_younger_1, rhodok_face_young_1 ],
["pirate_troupe_13", "Pirate", "Pirate", tf_bandit|tf_hero, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_falchion], def_attrib|level(20), wp(20), knows_inventory_management_10, rhodok_face_younger_1 ],
#["pirate_troupe_14", "Pirate", "Pirate", tf_hero, scn_town_6_pirates|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_sword_of_war,itm_wooden_shield,itm_mail_shirt], def_attrib|level(20), wp(20), knows_inventory_management_10, rhodok_face_young_1 ],


["provence2_p", "Marchant itinerant", "Marchant itinerant", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_6_pirates|entry(2), reserved, fac_commoners, [itm_gambeson,itm_woolen_hose,itm_bastard_sword_b,itm_crossbow,itm_bolts,itm_gambeson,itm_heraldric_shieldblueerminestripes,itm_dagger_medievale,itm_mail_coif], def_attrib|level(20)|str_16, wp(20), knows_inventory_management_10, 0x000000003c0042c838db6db6db61b6db00000000001db6db0000000000000000, 0x000000003c0042c838db6db6db61b6db00000000001db6db0000000000000000 ],
["provence3_p", "Marchant de chevaux", "Marchant de chevaux", tf_male|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_ranged, scn_town_6_pirates|entry(3), reserved, fac_commoners, [itm_leather_apron,itm_wrapping_boots,itm_saddle_horse,itm_horse1,itm_dagger], def_attrib|level(6)|str_16, wp(20), knows_inventory_management_10, 0x000000001200630a38db6db6db61b6db00000000001db6db0000000000000000, 0x000000001200630a38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence4_p", "Passager", "Passager", tf_male|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_6_pirates|entry(4), reserved, fac_commoners, [itm_leather_boots,itm_ragged_outfit,itm_bastard_sword_a], def_attrib|level(12)|str_16, wp(20), knows_inventory_management_10, 0x00000000120083cb38db6db6db61b6db00000000001db6db0000000000000000, 0x00000000120083cb38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence5_p", "Passager", "Passager", tf_hero, scn_town_6_pirates|entry(5), reserved, fac_commoners, [itm_shirt,itm_nomad_boots,itm_sword_medieval_b,itm_hunting_bow,itm_khergit_arrows], def_attrib|level(20)|str_16, wp(20), knows_inventory_management_10, 0x000000001200940b38db6db6db61b6db00000000001db6db0000000000000000, 0x000000001200940b38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence6_p", "Capitaine", "Capitaine", tf_male|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_town_6_pirates|entry(6), reserved, fac_commoners, [itm_wrapping_boots,itm_red_gambeson,itm_bastard_sword_a], def_attrib|level(20)|str_16, wp(20), knows_inventory_management_10, 0x00000000350015cf38db6db6db61b6db00000000001db6db0000000000000000, 0x00000000350015cf38db6db6db61b6db00000000001db6db0000000000000000 ],
["provence7_p", "Equipage", "Equipage", tf_male|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_town_6_pirates|entry(7), reserved, fac_commoners, [itm_leather_boots,itm_leather_vest,itm_dagger], def_attrib|level(12)|str_16, wp(20), knows_inventory_management_10, 0x000000003500c59038db6db6db61b6db00000000001db6db0000000000000000, 0x000000003500c59038db6db6db61b6db00000000001db6db0000000000000000 ],

#SANG LYS
["sang_lysbateau", "Soldat", "Soldat", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_6_alley|entry(9), reserved, fac_commoners, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(22)|str_16, wp(20), knows_inventory_management_10, 0x000000003f00000136db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00000136db6db6db6db6db00000000001db6db0000000000000000 ],
["sang_lysbateau_p", "Soldat", "Soldat", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_6_pirates|entry(7), reserved, fac_commoners, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x000000003f00000136db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00000136db6db6db6db6db00000000001db6db0000000000000000 ],

#Gordaine SANG LYS
["gordaine_sang_lys1", "Instructeur", "Instructeur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(2), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(25)|str_30|agi_30, wp(220), knows_shield_10|knows_ironflesh_10|knows_weapon_master_10|knows_power_strike_10, 0x000000003f00118222db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00118222db6db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys2", "Soldat", "Soldat", tf_hero|tf_unkillable|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_heraldric_shieldblueerminestripes,itm_sword_medieval_a], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x000000003f00018222db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00018222db6db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys3", "Soldat", "Soldat", tf_hero|tf_unkillable|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(41), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_pigface_klappvisor,itm_heraldric_shieldblueerminestripes,itm_sword_medieval_a], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x000000003f00618122db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00618122db6db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys4", "Soldat", "Soldat", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(16), reserved, fac_sang_lys, [itm_brigandine_sl,itm_steel_greaves,itm_templar], def_attrib|level(25)|str_24|agi_28, wp(20), knows_inventory_management_10|knows_shield_10|knows_ironflesh_8, 0x000000003f00718122db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f00718122db6db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys5", "Soldat", "Soldat", tf_hero|tf_unkillable|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(17), reserved, fac_sang_lys, [itm_brigandine_sl,itm_steel_greaves,itm_sword_medieval_a], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x000000003f00818422db8db6db6db6db00000000001db6db0000000000000000, 0x000000003f00818422db8db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys6", "Soldat", "Soldat", tf_hero|tf_unkillable|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(18), reserved, fac_sang_lys, [itm_brigandine_sl,itm_steel_greaves,itm_sword_medieval_a], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x000000003f00919222db8db6db6db6db00000000001db6db0000000000000000, 0x000000003f00919222db8db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys7", "Garde", "Garde", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_alley|entry(19), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_pigface_klappvisor_open,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(25)|str_24|agi_28, wp(20), knows_inventory_management_10|knows_shield_10|knows_ironflesh_8, 0x000000003f00a18022db8db6db6db6db00000000001db6db0000000000000000, 0x000000003f00a18022db8db6db6db6db00000000001db6db0000000000000000 ],
["gordaine_sang_lys8", "Maitre de la Compagnie du SansLys", "Maitre de la Compagnie du SansLys", tf_hero|tf_unkillable|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged|tf_unmoveable_in_party_window, scn_town_4_alley|entry(20), reserved, fac_sang_lys, [itm_brigandine_sl,itm_steel_greaves,itm_templar], def_attrib|level(22)|str_16|agi_12, wp(20), knows_inventory_management_10, 0x00000004ff01018022db8db6db6db6db00000000001db6db0000000000000000, 0x00000004ff01018022db8db6db6db6db00000000001db6db0000000000000000 ],

#marchand ressources
["ressource_merchant_paris", "Marchand de matières premières de Paris", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_paris6_alley|entry(5), reserved, fac_commoners, [itm_nobleman_outfit,itm_woolen_hose,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_enclume,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_tools,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_plan_1,itm_alchimi,itm_alchimi,itm_alchimi,itm_torch,itm_torch,itm_torch,itm_plan_12,itm_plan_12,itm_oil], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000004ff01218022db8db6db6db6db00000000001db6db0000000000000000, 0x00000004ff01218022db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_roen", "Marchand de matières premières de Rouen", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_12_alley|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_plan_12], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000004ff0011c022db8db6db6db6db00000000001db6db0000000000000000, 0x00000004ff0011c022db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_caen", "Marchand de matières premières de Caen", "Marchand de matières premières", tf_is_merchant, scn_town_9_alley|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_iron,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_torch,itm_torch,itm_torch,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000fff0021c134db8db6db6db6db00000000001db6db0000000000000000, 0x0000000fff0021c134db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_anger", "Marchand de matières premières de Nantes", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_3_alley|entry(5), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_iron,itm_iron,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_plan_2,itm_alchimi,itm_alchimi,itm_alchimi,itm_alchimi,itm_alchimi,itm_alchimi], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000fff00320134db8db6db6db6db00000000001db6db0000000000000000, 0x0000000fff00320134db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_orleans", "Marchand de matières premières d'Orléans", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_15_alley|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_plume,itm_plume,itm_plume,itm_plume,itm_corde,itm_corde,itm_corde,itm_corde,itm_torch,itm_plan_12,itm_plan_12,itm_plan_12], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f00420134db8db6db6db6db00000000001db6db0000000000000000, 0x000000003f00420134db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_tours", "Marchand de matières premières de Tours", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_16_alley|entry(13), reserved, fac_commoners, [itm_linen_shirt,itm_woolen_hose,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_pier,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_iron,itm_iron,itm_iron,itm_tools,itm_tools,itm_tools,itm_corde,itm_corde,itm_corde,itm_plume,itm_plume,itm_plume,itm_plume,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000003f00524234db8db6db6db6db00000000001db6db0000000000000000, 0x000000003f00524234db8db6db6db6db00000000001db6db0000000000000000 ],
["ressource_merchant_bordeau", "Marchand de matières premières de Bordeau", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_14_alley|entry(13), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_corde,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_bois,itm_bois,itm_bois,itm_bois,itm_bois,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plan_3,itm_alchimi,itm_alchimi,itm_alchimi], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_3, swadian_face_young_1, swadian_face_old_2 ],
["ressource_merchant_dijon", "Marchand de matières premières de Dijon", "Marchand de matières premières", tf_hero|tf_is_merchant, scn_town_6_fleuve|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_corde,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_cuir,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_plume,itm_enclume,itm_enclume,itm_enclume,itm_enclume,itm_enclume,itm_enclume,itm_enclume,itm_alchimi,itm_alchimi,itm_alchimi,itm_cuir,itm_cuir,itm_torch,itm_torch,itm_torch], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, swadian_face_middle_1, swadian_face_old_2 ],

#BANDITS ENTRPOS BOURGESS
["entrepot_bandit_1", "Brigand", "Brigand", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_bandit, scn_town_4_etpalley|entry(40), reserved, fac_commoners, [itm_hide_boots,itm_tribal_warrior_outfit,itm_bastard_sword_a,itm_wooden_shield], def_attrib|level(16), wp(80), knows_shield_5, 0x0000000b3f00824434db8db6db6db6db00000000001db6db0000000000000000, 0x0000000b3f00824434db8db6db6db6db00000000001db6db0000000000000000 ],
["entrepot_bandit_2", "Brigand", "Brigand", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bandit, scn_town_4_etpalley|entry(41), reserved, fac_commoners, [itm_hide_boots,itm_shirt,itm_two_handed_battle_axe_2,itm_bastard_sword_a], def_attrib|level(16), wp(90), knows_inventory_management_10, 0x000000003f0113c434db8db6db6db6db00000000001db6eb0000000000000000, 0x000000003f0113c434db8db6db6db6db00000000001db6eb0000000000000000 ],
["entrepot_contremaitre", "Contremaitre", "Contremaitre", tf_male|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_4_etpalley|entry(8), reserved, fac_commoners, [itm_leather_boots,itm_ragged_outfit], def_attrib|level(12)|str_16, wp(20), knows_inventory_management_10, 0x000000000000440736db6db6db6db6db00000000001db6db0000000000000000, 0x000000000000440736db6db6db6db6db00000000001db6db0000000000000000 ],

#acteurs scene taverne bourges 3lys
["tlys_bookseller", "Book_Merchant", "Book_Merchant", tf_hero|tf_is_merchant|tf_randomize_face, scn_tavern_3lys|entry(9), reserved, fac_commoners, [itm_fur_coat,itm_hide_boots], def_attrib|level(5), wp(20), knows_common, 0x000000000000444936db6db6db6db6db00000000001db6db0000000000000000, 0x000000000000444936db6db6db6db6db00000000001db6db0000000000000000 ],
["sang_lysivretlys", "Mercenaire ivre", "Mercenaire ivre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_tavern_3lys|entry(40), reserved, fac_commoners, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000520a16db6db6db6db6db00000000001db6e30000000000000000, 0x000000000000520a16db6db6db6db6db00000000001db6e30000000000000000 ],
["tlys_tavernkeeper", "Tavernier", "Tavernier", tf_female|tf_hero|tf_is_merchant|tf_randomize_face, scn_tavern_3lys|entry(8), reserved, fac_commoners, [itm_peasant_dress,itm_nomad_boots], def_attrib|level(2), wp(20), knows_common|knows_inventory_management_10, woman_face_1, woman_face_2 ],


## EXCEL Templates here too - Kham
##1429 troupes rebels !!!!!!!!!!!!!!!!!!!!!

["rebel_paysan","Paysan Rebelle","Paysans Rebelles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_black_khergits,[itm_shirt,itm_wrapping_boots,itm_wrapping_boots,itm_dagger_medievale,itm_spiked_mace],def_attrib2,wp(80),knows_warrior_basic2,0x00000000000054cb16db6db6db6db6db00000000001db6e30000000000000000,0x00000000000054cb16db6db6db6db6db00000000001db6e30000000000000000],

["rebel_archer","Archer Rebelle","Archers Rebelles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows],def_attrib2,wp(80),knows_archer_basic,0x000000000000800b36db6db6db6db6db00000000001db6d30000000000000000,0x000000000000900b36db6db6db6db6db00000000001db6d30000000000000000],

["rebel_arbaletier","Arbaletier Rebelle","Arbaletiers Rebelles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_wrapping_boots,itm_wrapping_boots,itm_crossbow,itm_bolts,itm_templar,itm_battle_shieldcharlesv,itm_wooden_buckler1,],def_attrib2,wp(80),knows_archer_basic,0x000000000001200b36db6db6db61b6db00000000001db6d30000000000000000,bandit_face2],

["rebel_fantassin","Fantassin Rebelle","Fantassins Rebelles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_black_khergits,[itm_nasal_helmet,itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_hide_boots,itm_wrapping_boots,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_templar,],def_attrib2,wp(80),knows_warrior_basic2,0x000000000001200b36db6db6db61b6db00000000001db6d30000000000000000,bandit_face2],

["rebel_piquier","Piquier Rebelle","Piquiers Rebelles",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_black_khergits,[itm_mail_coif,itm_segmented_helmet,itm_gambeson,itm_haubergeon,itm_hide_boots,itm_mail_boots,itm_voulge,itm_halberd_1,itm_halberd_6,itm_3halberd,itm_templar,itm_battle_shieldcharlesv,itm_wooden_buckler1,itm_templar,itm_battle_shieldcharlesv,itm_wooden_buckler1,],def_attrib2,wp(80),knows_warrior_basic2,0x000000003601001236db6db6db61b6db00000000001db6d30000000000000000,bandit_face2],

["rebel_heros","Heros de la Rebellion","Heros de la Rebellion",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_black_khergits,[itm_segmented_helmet,itm_haubergeon_f1,itm_tribal_warrior_outfit,itm_leather_gloves,itm_leather_boots,itm_khergit_leather_boots,itm_great_lance,itm_templar,itm_warhorse,itm_steppe_horse,],def_attrib2_b,wp(100),knows_warrior_normal,0x000000003600b01036db6db6db61b6db00000000001db6d30000000000000000,bandit_face2],


#troupe sl 
["sang_lysbasetroop","Mercenaire du SansLys","Mercenaires du SansLys",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_brigandine_sl,itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_templar,itm_bastard_sword_a,itm_battle_shieldcharlesv,],def_attrib3,wp(130),knows_warrior_veteran,0x000000003600a01036db6db6db61b6db00000000001db6d30000000000000000,0x000000003600a01036db6db6db61b6db00000000001db6d30000000000000000],

["serg_sang_lysbasetroop","Sergent Mercenaire du SansLys","Sergents Mercenaire du SansLys",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_brigandine_sl,itm_hourglass_gauntlets_ornate,itm_steel_greaves,itm_templar,itm_bastard_sword_a,itm_battle_shieldcharlesv,],def_attrib3_b,wp(130),knows_warrior_veteran,0x000000003600901036db6db6db61b6db00000000001db6d30000000000000000,0x000000003600901036db6db6db61b6db00000000001db6d30000000000000000],


#bandits vilandrandro quete de bourges
["vilandrandro_quest_fanta","Fantassin de Vilandrandro","Fantassin de Vilandrandro",tf_bandit|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_viland_quest_bourges,[itm_hounskull,itm_mail_shirt,itm_coat_of_plates,itm_surcoat_over_mail,itm_mail_gauntlets,itm_leather_boots,itm_mail_boots,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,],def_attrib_b,wp(100),knows_warrior_basic,bandit_face1,bandit_face2],

["vilandrandro_quest_fanta2","Fantassin de Vilandrandro","Fantassin de Vilandrandro",tf_bandit|tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_viland_quest_bourges,[itm_hounskull,itm_mail_shirt,itm_surcoat_over_mail,itm_coat_of_plates,itm_mail_gauntlets,itm_leather_boots,itm_mail_boots,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,],def_attrib_b,wp(100),knows_warrior_basic,bandit_face1,bandit_face2],

["vilandrandro_quest_arbaletier","Archer de Vilandrandro","Archer de Vilandrandro",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit,0,0,fac_viland_quest_bourges,[itm_surcoat_over_mail,itm_shirt,itm_aketon_green,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts,itm_war_axe,itm_bastard_sword_a,],def_attrib_b,wp(100),knows_archer_basic,bandit_face1,bandit_face2],

["vilandrandro_quest_fanta_end","Archer de Vilandrandro","Archer de Vilandrandro",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit,0,0,fac_viland_quest_bourges,[itm_surcoat_over_mail,itm_shirt,itm_aketon_green,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts,itm_war_axe,itm_bastard_sword_a,],def_attrib_b,wp(100),knows_archer_basic,bandit_face1,bandit_face2],


## EXCEL Templates here END - Kham

#bataille entrepots
#sl
["sang_lysbatb1", "Sergent Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(2), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_20|agi_10, wp(130), knows_common|knows_shield_6|knows_power_strike_2|knows_ironflesh_2, 0x000000003600801036db6db6db61b6db00000000001db6d30000000000000000, 0x000000003600801036db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb2", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(3), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003600701036db6db6db61b6db00000000001db6d30000000000000000, 0x000000003600701036db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb3", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(4), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003600601036db6db6db61b6db00000000001db6d30000000000000000, 0x000000003600601036db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb4", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(5), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003600401036db6db6db61b6db00000000001db6d30000000000000000, 0x000000003600401036db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb5", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(6), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000300a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000000000300a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb6", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(7), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000200a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000000000200a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb7", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000100a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000000000100a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb8", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000000a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000000000000a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb9", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000001200a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000000001200a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb10", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003f01100a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000003f01100a36db6db6db61b6db00000000001db6d30000000000000000 ],
["sang_lysbatb11", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_town_4_battle_v|entry(40), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003f01000a36db6db6db61b6db00000000001db6d30000000000000000, 0x000000003f01000a36db6db6db61b6db00000000001db6d30000000000000000 ],


#brigands
["vilandrandro_bat_bourg1", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(41), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_jam_scorpion,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_coat_of_plates], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg2", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(41), reserved, fac_vilandrandro, [itm_jam_scorpion,itm_bastard_sword_b,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_coat_of_plates], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg3", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(41), reserved, fac_vilandrandro, [itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_coat_of_plates], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg4", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(41), reserved, fac_vilandrandro, [itm_jam_scorpion,itm_bastard_sword_b,itm_sword_medieval_b,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg5", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bandit, scn_town_4_battle_v|entry(42), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["vilandrandro_bat_bourg6", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(42), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg7", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(42), reserved, fac_vilandrandro, [itm_bastard_sword_b,itm_sword_medieval_b,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_mail_hauberk], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg8", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(43), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg9", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(43), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_jam_scorpion,itm_woodenbuckler,itm_wooden_shield,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_coat_of_plates], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg10", "Fantassin de Vilandrandro", "Fantassin de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_4_battle_v|entry(43), reserved, fac_vilandrandro, [itm_one_handed_war_axe_a,itm_one_handed_battle_axe_b,itm_bastard_sword_b,itm_sword_medieval_b,itm_leather_boots,itm_mail_boots,itm_hounskull,itm_mail_gauntlets,itm_mail_shirt,itm_surcoat_over_mail,itm_mail_hauberk,itm_coat_of_plates], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg11", "Archer de Vilandrandro", "Archer de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_4_battle_v|entry(43), reserved, fac_vilandrandro, [itm_war_axe,itm_bastard_sword_a,itm_surcoat_over_mail,itm_shirt,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts], def_attrib|level(12)|str_16|agi_10, wp(100), knows_common|knows_power_draw_4, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg12", "Archer de Vilandrandro", "Archer de Vilandrandro", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, scn_town_4_battle_v|entry(44), reserved, fac_vilandrandro, [itm_war_axe,itm_bastard_sword_a,itm_surcoat_over_mail,itm_aketon_green,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts], def_attrib|level(12)|str_16|agi_10, wp(100), knows_common|knows_power_draw_4, 0x000000086900c0003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["vilandrandro_bat_bourg13", "Archer de Vilandrandro", "Archer de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_4_battle_v|entry(44), reserved, fac_vilandrandro, [itm_war_axe,itm_bastard_sword_a,itm_surcoat_over_mail,itm_shirt,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts], def_attrib|level(12)|str_16|agi_10, wp(100), knows_common|knows_power_draw_4, bandit_face1, bandit_face2 ],
["vilandrandro_bat_bourg14", "Archer de Vilandrandro", "Archer de Vilandrandro", tf_bandit|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_4_battle_v|entry(44), reserved, fac_vilandrandro, [itm_war_axe,itm_bastard_sword_a,itm_surcoat_over_mail,itm_shirt,itm_aketon_green,itm_hide_boots,itm_nomad_boots,itm_short_bow,itm_war_bow,itm_crossbow,itm_arrows,itm_bolts], def_attrib|level(12)|str_16|agi_10, wp(100), knows_common|knows_power_draw_4, bandit_face1, bandit_face2 ],

#sl bataille pont benezet

["sang_lyspont1", "Sergent du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(2), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000000290010403adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290010403adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont2", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(3), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_pigface_klappvisor_open,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont3", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(4), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000008690124033adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690124033adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont4", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(5), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000003f0040443adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f0040443adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont5", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(6), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000000000084043adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000000084043adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont6", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(7), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000000290060053adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290060053adbadb6db6db6db00000000001db6db0000000000000000 ],
["sang_lyspont7", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(8), reserved, fac_sang_lys, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_hounskull,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar,itm_bastard_sword_a], def_attrib|level(22)|str_16|agi_10, wp(130), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],
#benezt troupes du pape
["pontbenezet_troop1", "Inquisiteur", "Inquisiteur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(40), reserved, fac_commoners, [itm_robepurple,itm_woolen_hose,itm_sword_medieval_a], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, 0x00000000290063013adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290063013adbadb6db6db6db00000000001db6db0000000000000000 ],
["pontbenezet_troop2", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(41), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],
["pontbenezet_troop3", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(42), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["pontbenezet_troop4", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(42), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],
["pontbenezet_troop5", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(42), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],
["pontbenezet_troop6", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(43), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],
["pontbenezet_troop7", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_18_alley|entry(43), reserved, fac_commoners, [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_hide_boots,itm_kettle_hat,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_2 ],
["pontbenezet_troop8", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(44), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop9", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(44), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop10", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(45), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop11", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(45), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop12", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(46), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop13", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(47), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop14", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(47), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop15", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(47), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["pontbenezet_troop16", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_alley|entry(47), reserved, fac_commoners, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["pontbenezet_troop17","Hallbardier Suisse","Hallbardier Suisse",tf_guarantee_boots|tf_guarantee_armor, scn_town_18_alley|entry(46), reserved,fac_commoners,[itm_woolen_hose,itm_byrnie_swiss1,itm_swiss_armor,itm_swiss_armor,itm_swiss_armor,itm_linen_tunic_swiss,itm_linen_tunic_swiss,itm_arming_cap,itm_leather_cap,itm_lui_vaegirhallberd,itm_pop_halberd],def_attrib|level(28),wp_melee(220),knows_common|knows_ironflesh_5|knows_shield_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1,man_face_young_2],
["pontbenezet_troop18","Hallbardier Suisse","Hallbardier Suisse",tf_guarantee_boots|tf_guarantee_armor, scn_town_18_alley|entry(46), reserved,fac_commoners,[itm_woolen_hose,itm_byrnie_swiss1,itm_swiss_armor,itm_swiss_armor,itm_swiss_armor,itm_linen_tunic_swiss,itm_linen_tunic_swiss,itm_arming_cap,itm_leather_cap,itm_lui_vaegirhallberd,itm_pop_halberd],def_attrib|level(28),wp_melee(220),knows_common|knows_ironflesh_5|knows_shield_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1,man_face_young_2],
["pontbenezet_troop19","Hallbardier Suisse","Hallbardier Suisse",tf_guarantee_boots|tf_guarantee_armor, scn_town_18_alley|entry(46), reserved,fac_commoners,[itm_woolen_hose,itm_byrnie_swiss1,itm_swiss_armor,itm_swiss_armor,itm_swiss_armor,itm_linen_tunic_swiss,itm_linen_tunic_swiss,itm_arming_cap,itm_leather_cap,itm_lui_vaegirhallberd,itm_pop_halberd],def_attrib|level(28),wp_melee(220),knows_common|knows_ironflesh_5|knows_shield_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1,man_face_young_2],
["pontbenezet_troop20","Hallbardier Suisse","Hallbardier Suisse",tf_guarantee_boots|tf_guarantee_armor, scn_town_18_alley|entry(46), reserved,fac_commoners,[itm_woolen_hose,itm_byrnie_swiss1,itm_swiss_armor,itm_swiss_armor,itm_swiss_armor,itm_linen_tunic_swiss,itm_linen_tunic_swiss,itm_arming_cap,itm_leather_cap,itm_lui_vaegirhallberd,itm_pop_halberd],def_attrib|level(28),wp_melee(220),knows_common|knows_ironflesh_5|knows_shield_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1,man_face_young_2],
["pontbenezet_troop21","Hallbardier Suisse","Hallbardier Suisse",tf_guarantee_boots|tf_guarantee_armor, scn_town_18_alley|entry(46), reserved,fac_commoners,[itm_woolen_hose,itm_byrnie_swiss1,itm_swiss_armor,itm_swiss_armor,itm_swiss_armor,itm_linen_tunic_swiss,itm_linen_tunic_swiss,itm_arming_cap,itm_leather_cap,itm_lui_vaegirhallberd,itm_pop_halberd],def_attrib|level(28),wp_melee(220),knows_common|knows_ironflesh_5|knows_shield_2|knows_power_strike_6|knows_athletics_3,swadian_face_young_1,man_face_young_2],


#milliciens neutres benezet
["milliceneutre1", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_benezet_end|entry(2), reserved, fac_neutral, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["milliceneutre2", "Mercenaire", "Mercenaire", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, scn_town_18_benezet_end|entry(3), reserved, fac_neutral, [itm_brigandine_g,itm_mail_chausses,itm_byzantion,itm_byzantion_painted,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_sword_medieval_a,itm_laird,itm_caithness,itm_tab_shield_pavise_d], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_draw_4|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],

#troupe camp anglais quete rebels
#rebels
["rebel_quest_ca1", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(2), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluelysstripes,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca2", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(3), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluelysstripes,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca3", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluecross,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000008690124033adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca4", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(5), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_heraldric_shieldblueerminestripes,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000008690024843adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca5", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(6), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldbluelysstripes,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x00000008690034c53adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca6", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(7), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldcharlesv,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca7", "Archer Rebelle", "Archers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(40), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14), wp(80), knows_common|knows_power_draw_6, 0x00000008690020003adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca8", "Archer Rebelle", "Archers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(40), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14), wp(80), knows_common|knows_power_draw_6, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca9", "Fantassin Rebelle", "Fantassins Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_camp_brit_alley|entry(40), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(14), wp(80), knows_common|knows_shield_5, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca10", "Fantassin Rebelle", "Fantassins Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_camp_brit_alley|entry(40), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(14), wp(80), knows_common|knows_shield_5, 0x00000008690065873adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_quest_ca11", "Arbaletier Rebelle", "Arbaletiers Rebelles", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_camp_brit_alley|entry(40), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldcharlesv,itm_crossbow,itm_bolts], def_attrib|level(14), wp(80), knows_common|knows_shield_5|knows_power_draw_6, 0x000000086900b5ca3adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],

#anglais
["eng_quest_ca1", "Sentinele", "Sentinele", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_english, scn_camp_brit_alley|entry(41), reserved, fac_kingdom_2, [itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_padded_jack_e,itm_splinted_greaves_e1,itm_mail_chausses_e1,itm_leather_gloves,itm_long_bow,itm_khergit_arrows,itm_mace_4,itm_mace_3,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_4, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["eng_quest_ca2", "Archer long Anglais", "Archer long Anglais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_english, scn_camp_brit_alley|entry(42), reserved, fac_kingdom_2, [itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_padded_jack_e,itm_splinted_greaves_e1,itm_mail_chausses_e1,itm_leather_gloves,itm_long_bow,itm_khergit_arrows,itm_templar,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_4, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["eng_quest_ca3", "Guisarmier Anglais", "Guisarmier Anglais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_english, scn_camp_brit_alley|entry(42), reserved, fac_kingdom_2, [itm_coat_of_plates_e2,itm_coat_of_plates_e3,itm_surcoat_over_mail_e4,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_bill_1,itm_guisarme,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_open_sallet_coif,itm_visored_sallet_coif,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["eng_quest_ca4", "Guisarmier Anglais", "Guisarmier Anglais", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_english, scn_camp_brit_alley|entry(43), reserved, fac_kingdom_2, [itm_coat_of_plates_e2,itm_coat_of_plates_e3,itm_surcoat_over_mail_e4,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_bill_1,itm_guisarme,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x00000008690024843adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["eng_quest_ca5", "Sergent Anglais", "Sergent Anglais", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_brit_alley|entry(43), reserved, fac_kingdom_2, [itm_haubergeon_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e2,itm_surcoat_over_mail_e1,itm_splinted_greaves_e1,itm_mail_chausses_e1,itm_kettlehat1_painted,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_c,itm_kite_shieldreddragon,itm_tab_shield_heater_a,itm_battle_shieldedwardiii,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldred3lions,itm_heraldric_shieldredlys,itm_war_shieldwales,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["eng_quest_ca6", "Chevalier Anglais", "Chevalier Anglais", tf_english|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_brit_alley|entry(44), reserved, fac_kingdom_2, [itm_gothic_armour,itm_steel_greaves,itm_shynbaulds,itm_bec_de_corbin,itm_templar,itm_heraldric_shieldred3lions,itm_hourglass_gauntlets_ornate], def_attrib|level(25), wp(125), knows_common|knows_shield_8|knows_ironflesh_8|knows_power_strike_4|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],

#acteurs foret vervy
["rebel_verzy1", "Chef Rebelle", "Chef Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_verzy_camp|entry(2), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(24)|str_13|agi_14, wp(180), knows_common|knows_shield_5|knows_weapon_master_5|knows_power_strike_4|knows_ironflesh_6, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000 ],
["rebel_verzy2", "Antoine", "Antoine", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_verzy_camp|entry(3), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_12, wp(180), knows_common|knows_shield_5, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000 ],
["rebel_verzy3", "Poignard", "Poignard", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_verzy_camp|entry(4), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_13, wp(180), knows_common|knows_shield_5, 0x000000003f00e0043adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_verzy4", "La Ripaille", "La Ripaille", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_verzy_camp|entry(5), reserved, fac_black_khergits, [itm_gambeson,itm_haubergeon,itm_hide_boots,itm_mail_boots,itm_mail_coif,itm_segmented_helmet,itm_templar,itm_voulge,itm_halberd_1,itm_halberd_6,itm_3halberd,itm_battle_shieldcharlesv,itm_wooden_buckler1], def_attrib|level(18), wp(180), knows_common|knows_shield_6, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000 ],
["rebel_verzy5", "Tibaut", "Tibaut", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_verzy_camp|entry(6), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14)|str_10|agi_12, wp(180), knows_common|knows_power_draw_6, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000 ],
["rebel_verzy6", "Foureau", "Foureau", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_verzy_camp|entry(7), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_crossbow,itm_bolts], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x000000000000114006db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000114006db6e375b61b6db00000000001db6eb0000000000000000 ],

#copie avec casque si dessous!!! attaques entrepot METZ
["rebel_verzentrep1", "Chef Rebelle", "Chef Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_5_batetp|entry(3), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(24)|str_13|agi_14, wp(180), knows_common|knows_shield_5|knows_weapon_master_5|knows_power_strike_4|knows_ironflesh_6, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000 ],
["rebel_verzentrep2", "Antoine", "Antoine", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_5_batetp|entry(4), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_12, wp(180), knows_common|knows_shield_5, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000 ],
["rebel_verzentrep3", "Poignard", "Poignard", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_5_batetp|entry(5), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_13, wp(180), knows_common|knows_shield_5, 0x000000003f00e0043adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_verzentrep4", "La Ripaille", "La Ripaille", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_town_5_batetp|entry(6), reserved, fac_black_khergits, [itm_gambeson,itm_haubergeon,itm_hide_boots,itm_mail_boots,itm_mail_coif,itm_segmented_helmet,itm_templar,itm_voulge,itm_halberd_1,itm_halberd_6,itm_3halberd,itm_battle_shieldbluecross,itm_wooden_buckler1], def_attrib|level(18), wp(180), knows_common|knows_shield_6, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000 ],
["rebel_verzentrep5", "Tibaut", "Tibaut", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_5_batetp|entry(7), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14)|str_10|agi_12, wp(180), knows_common|knows_power_draw_6, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000 ],
#["rebel_verzentrep6", "Foureau", "Foureau", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_5_batetp|entry(7), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_battle_shieldcharlesv,itm_crossbow,itm_bolts], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x000000085000d407171b8d36db65b6db00000000001d16db0000000000000000, 0x000000085000d407171b8d36db65b6db00000000001d16db0000000000000000 ],

#SOLDATS BOURG
["bourg_entrep_metz1", "Hallbardier", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon, scn_town_5_alley|entry(40), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_visored_sallet,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_metz2", "Piquier", "Piquiers_lourds_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon, scn_town_5_alley|entry(41), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_mail_hauberk,itm_steel_greaves,itm_mail_boots,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_b,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_metz3", "Piquier", "Piquiers_lourds_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon, scn_town_5_alley|entry(42), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_mail_hauberk,itm_steel_greaves,itm_mail_boots,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_b,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_2, 0x000000000000624406db6e375b61b6db00000000001db6eb0000000000000000, vaegir_face_older_2 ],
["bourg_entrep_metz4", "Hallbardier", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon, scn_town_5_alley|entry(43), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_visored_sallet,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_metz5", "Vougier", "Vougiers_Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_town_5_alley|entry(44), reserved, fac_neutral, [itm_leather_vest,itm_leather_armor,itm_leather_boots,itm_hunter_boots,itm_open_sallet_coif,itm_mail_coif,itm_leather_gloves,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_metz6", "Vougier", "Vougiers_Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_town_5_alley|entry(45), reserved, fac_neutral, [itm_leather_vest,itm_leather_armor,itm_leather_boots,itm_hunter_boots,itm_open_sallet_coif,itm_mail_coif,itm_leather_gloves,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_metz7", "Archer", "Archers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bourgignon, scn_town_5_alley|entry(46), reserved, fac_neutral, [itm_mail_hauberk,itm_shirt,itm_common_hood,itm_mail_coif,itm_ankle_boots,itm_sword_medieval_b_small,itm_leather_boots,itm_leather_gloves,itm_hunting_bow,itm_short_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_bayeux], def_attrib|level(18), wp(110), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_power_draw_3, 0x00000000000084043adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_entrep_metz8", "Archer", "Archers_Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_town_5_alley|entry(47), reserved, fac_neutral, [itm_mail_hauberk,itm_shirt,itm_common_hood,itm_mail_coif,itm_ankle_boots,itm_sword_medieval_b_small,itm_leather_boots,itm_leather_gloves,itm_hunting_bow,itm_short_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_bayeux], def_attrib|level(18), wp(110), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_power_draw_3, vaegir_face_young_1, vaegir_face_older_2 ],

#copie soldats metz
["bourg_entrep_copie1", "Hallbardier", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_bourgignon, scn_town_5_batetp|entry(40), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_copie2", "Piquier", "Piquiers_lourds_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon, scn_town_5_batetp|entry(41), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_mail_hauberk,itm_steel_greaves,itm_mail_boots,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_b,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_2, 0x000000003f0110043adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_entrep_copie3", "Piquier", "Piquiers_lourds_Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon, scn_town_5_batetp|entry(42), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_mail_hauberk,itm_steel_greaves,itm_mail_boots,itm_nasal_helmet,itm_mail_gauntlets,itm_tab_shield_kite_b,itm_pike,itm_war_spear], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_copie4", "Hallbardier", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_bourgignon, scn_town_5_batetp|entry(43), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork,itm_open_sallet,itm_visored_sallet,itm_guard_helmet], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_copie5", "Vougier", "Vougiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_bourgignon, scn_town_5_batetp|entry(44), reserved, fac_neutral, [itm_leather_vest,itm_leather_armor,itm_leather_boots,itm_hunter_boots,itm_open_sallet_coif,itm_mail_coif,itm_leather_gloves,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, 0x000000003f0120043adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_entrep_copie6", "Vougier", "Vougiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_bourgignon, scn_town_5_batetp|entry(45), reserved, fac_neutral, [itm_leather_vest,itm_leather_armor,itm_leather_boots,itm_hunter_boots,itm_open_sallet_coif,itm_mail_coif,itm_leather_gloves,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,itm_war_spear], def_attrib|level(15), wp(80), knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_4, 0x00000008690010003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_entrep_copie7", "Archer", "Archers_Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_town_5_batetp|entry(46), reserved, fac_neutral, [itm_mail_hauberk,itm_shirt,itm_common_hood,itm_mail_coif,itm_ankle_boots,itm_sword_medieval_b_small,itm_leather_boots,itm_leather_gloves,itm_hunting_bow,itm_short_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_bayeux], def_attrib|level(18), wp(110), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_power_draw_3, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_entrep_copie8", "Archer", "Archers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bourgignon, scn_town_5_batetp|entry(47), reserved, fac_neutral, [itm_mail_hauberk,itm_shirt,itm_common_hood,itm_mail_coif,itm_ankle_boots,itm_sword_medieval_b_small,itm_leather_boots,itm_leather_gloves,itm_hunting_bow,itm_short_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_caithness], def_attrib|level(18), wp(110), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_power_draw_3, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],

#fossoyeur de Caen
["caen_foss", "Fossoyeur de Calais", "Fossoyeur de Calais", tf_guarantee_boots|tf_guarantee_armor, scn_town_11_alley|entry(2), reserved, fac_commoners, [itm_leather_apron,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000 ],

#troupes place forte
["rebel_pfort1", "Antoine", "Antoine", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_forte|entry(2), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_12, wp(180), knows_common|knows_shield_5, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000 ],
["rebel_pfort2", "Poignard", "Poignard", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_forte|entry(3), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_13, wp(180), knows_common|knows_shield_5, 0x000000003f00e0043adbadb6db6db6db00000000001db6db0000000000000000, bandit_face2 ],
["rebel_pfort3", "La Ripaille", "La Ripaille", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_forte|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_haubergeon,itm_hide_boots,itm_mail_boots,itm_mail_coif,itm_segmented_helmet,itm_templar,itm_voulge,itm_halberd_1,itm_halberd_6,itm_3halberd,itm_battle_shieldbluecross,itm_wooden_buckler1], def_attrib|level(18), wp(180), knows_common|knows_shield_6, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000, 0x000000003f01000a36db6db6db61b6db00000000001db6eb0000000000000000 ],
["rebel_pfort4", "Tibaut", "Tibaut", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_p_forte|entry(5), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14)|str_10|agi_12, wp(180), knows_common|knows_power_draw_6, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000 ],
["rebel_pfort5", "Foureau", "Foureau", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_p_forte|entry(6), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_crossbow,itm_bolts], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x000000000000114006db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000114006db6e375b61b6db00000000001db6eb0000000000000000 ],

#bourg
["bourg_pfort1", "Arbaletier lourd Bourguignon", "Arbaletier lourd Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon, scn_p_forte|entry(40), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_steel_greaves,itm_mail_boots,itm_visored_sallet,itm_open_sallet,itm_leather_gloves,itm_heavy_crossbow,itm_bolts,itm_bolts,itm_templar,itm_bolts,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_1, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_pfort2", "Arbaletier lourd Bourguignon", "Arbaletier lourd Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon, scn_p_forte|entry(41), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_wooden_buckler1,itm_woodenbuckler,itm_steel_greaves,itm_mail_boots,itm_visored_sallet,itm_open_sallet,itm_leather_gloves,itm_heavy_crossbow,itm_bolts,itm_bolts,itm_templar,itm_bolts,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_1, 0x00000008690060003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_pfort3", "Arbaletier Lourd Bourguignon", "Arbaletier lourd Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon, scn_p_forte|entry(42), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_steel_greaves,itm_mail_boots,itm_visored_sallet,itm_open_sallet,itm_leather_gloves,itm_heavy_crossbow,itm_bolts,itm_templar,itm_bolts,itm_bolts,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_1, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_pfort4", "Arbaletier lourd Bourguignon", "Arbaletier lourd Bourguignon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged|tf_bourgignon, scn_p_forte|entry(43), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_steel_greaves,itm_mail_boots,itm_visored_sallet,itm_open_sallet,itm_leather_gloves,itm_heavy_crossbow,itm_bolts,itm_templar,itm_bolts,itm_bolts,itm_mace_4,itm_mace_3,itm_one_handed_war_axe_a,itm_one_handed_battle_axe_c,itm_bayeux], def_attrib|str_13|level(24), wp(90), knows_ironflesh_2|knows_power_draw_6|knows_athletics_1, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_pfort5", "Garde Bourguignon", "Gardes Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon, scn_p_forte|entry(44), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_splinted_greaves_nospurs,itm_shynbaulds,itm_mail_mittens,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_senlac,itm_knight,itm_count,itm_castellan,itm_sempach,itm_bayeux,itm_lui_knightaxeonehd,itm_open_sallet_coif,itm_visored_sallet_coif], def_attrib|level(23), wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000008690050003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["bourg_pfort6", "Archer Bourguignons", "Archers_Bourguignons", tf_bourgignon|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, scn_p_forte|entry(45), reserved, fac_neutral, [itm_mail_hauberk,itm_shirt,itm_common_hood,itm_mail_coif,itm_ankle_boots,itm_sword_medieval_b_small,itm_leather_boots,itm_leather_gloves,itm_hunting_bow,itm_short_bow,itm_arrows,itm_one_handed_battle_axe_a,itm_sword_medieval_c_small,itm_agincourt,itm_caithness], def_attrib|level(18), wp(110), knows_common|knows_ironflesh_2|knows_shield_3|knows_athletics_5|knows_power_draw_3, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_pfort7", "Hallbardier Bourguignons", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_bourgignon, scn_p_forte|entry(46), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, vaegir_face_young_1, vaegir_face_older_2 ],
["bourg_pfort8", "Hallbardier Bourguignons", "Hallbardiers_Bourguignons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_bourgignon, scn_p_forte|entry(47), reserved, fac_neutral, [itm_surcoat_over_mail_brg1,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_mail_mittens,itm_wisby_gauntlets_red,itm_pop_bill,itm_lui_smallhallberda,itm_voulge_2,itm_lochaber_axe_3,itm_glaive_fork], def_attrib|level(23), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_shield_3|knows_athletics_5, 0x00000008690010003adbadb6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],

#troupes place forte neutre
["pfrebel_neutre1", "Chef Rebelle", "Chef Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_fneutral|entry(2), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_12, wp(180), knows_common|knows_shield_5, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900e0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["pfrebel_neutre2", "Fantassin Rebelle", "Fantassin Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_fneutral|entry(3), reserved, fac_black_khergits, [itm_mail_shirtdeer,itm_mail_shirt,itm_haubergeon,itm_hide_boots,itm_wrapping_boots,itm_nasal_helmet,itm_templar,itm_sword_medieval_a,itm_sword_two_handed_a,itm_manhuntermaul,itm_mace_1,itm_battle_shieldcharlesv,itm_tab_shield_heater_a], def_attrib|level(18)|str_14|agi_13, wp(180), knows_common|knows_shield_5, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000 ],
["pfrebel_neutre3", "Fantassin Rebelle", "Fantassin Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_p_fneutral|entry(4), reserved, fac_black_khergits, [itm_gambeson,itm_haubergeon,itm_hide_boots,itm_mail_boots,itm_mail_coif,itm_segmented_helmet,itm_templar,itm_voulge,itm_halberd_1,itm_halberd_6,itm_3halberd,itm_heraldric_shieldblueerminestripes,itm_wooden_buckler1], def_attrib|level(18), wp(180), knows_common|knows_shield_6, 0x000000086900f3c23adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900f3c23adbadb6db6db6db00000000001db6db0000000000000000 ],
["pfrebel_neutre4", "Archer Rebelle", "Archer Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_p_fneutral|entry(5), reserved, fac_black_khergits, [itm_padded_cloth_b_f1,itm_wrapping_boots,itm_dagger_medievale,itm_war_bow,itm_arrows], def_attrib|level(14)|str_10|agi_12, wp(180), knows_common|knows_power_draw_6, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000 ],
["pfrebel_neutre5", "Arbaletier Rebelle", "Arbaletier Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_p_fneutral|entry(6), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_crossbow,itm_bolts], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x00000000290050043adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290050043adbadb6db6db6db00000000001db6db0000000000000000 ],
["pfrebel_neutre6", "Arbaletier Rebelle", "Arbaletier Rebelle", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_p_fneutral|entry(7), reserved, fac_black_khergits, [itm_gambeson,itm_wrapping_boots,itm_wrapping_boots,itm_bastard_sword_a,itm_crossbow,itm_bolts], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],

#
["rebel_licorn", "La Licorne", "La Licorne", tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_town_17_alley|entry(2), reserved, fac_black_khergits, [itm_nobleman_outfit,itm_woolen_hose], def_attrib|level(18)|str_15|agi_12, wp(180), knows_common|knows_shield_5|knows_power_draw_6, 0x00000001bf0110c436db6db6db6db6db00000000001db6db0000000000000000, 0x00000001bf0110c436db6db6db6db6db00000000001db6db0000000000000000 ],

# bandits de paris troupe passages catacombes !!!
["parisvilan_entry", "Homme louche", "Homme louche", tf_guarantee_boots|tf_guarantee_armor, scn_town_1_alley|entry(7), reserved, fac_vilandrandro, [itm_sword_medieval_b,itm_leather_boots,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000520306db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000520306db6e375b61b6db00000000001db6eb0000000000000000 ],
["parisvilan_guide", "Guide", "Guide", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_entry|entry(2), reserved, fac_vilandrandro, [itm_templar,itm_mail_boots,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, bandit_face2, bandit_face2 ],
#rodrigo villandrandro
["rodrigo_villandrandro", "Rodrigo de Villandrandro", "Rodrigo de Villandrandro", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_crypte|entry(2), reserved, fac_vilandrandro, [itm_templar,itm_nobleman_outfit,itm_hide_boots], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000420206db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000420206db6e375b61b6db00000000001db6eb0000000000000000 ],
#
["cata_vilain1", "Brigand", "Brigand", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_crypte|entry(3), reserved, fac_vilandrandro, [itm_sword_medieval_b,itm_leather_boots,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000, 0x00000000000031c206db6e375b61b6db00000000001db6eb0000000000000000 ],
#ribaude
["cata_ribaude1", "Ribaude", "Ribaude", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_crypte|entry(4), reserved, fac_commoners, [itm_woolen_hose,itm_red_dress], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000001200300236d9edb6dc41379800000000001db6db0000000000000000, 0x000000001200300236d9edb6dc41379800000000001db6db0000000000000000 ],
["cata_gard1", "Garde du corp", "Garde du corp", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_crypte|entry(5), reserved, fac_vilandrandro, [itm_bastard_sword_a,itm_leather_boots,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x000000000000218206db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000218206db6e375b61b6db00000000001db6eb0000000000000000 ],
["cata_gard2", "Garde du corp", "Garde du corp", tf_guarantee_boots|tf_guarantee_armor, scn_catacomb_crypte|entry(6), reserved, fac_vilandrandro, [itm_sword_medieval_b,itm_leather_boots,itm_surcoat_over_mail], def_attrib|level(12)|str_16|agi_8, wp(100), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, 0x00000008690110003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690110003adbadb6db6db6db00000000001db6db0000000000000000 ],

#les trois sirenes
["sirene_1", "Lady Laura", "Lady Laura", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(2), reserved, fac_commoners, [itm_lady_dress_ruby,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000002400100138dca6b8dd8d36d200000000001ca72b0000000000000000, 0x000000002400100138dca6b8dd8d36d200000000001ca72b0000000000000000 ],
["sirene_2", "Dame Catherine", "Dame Catherine", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(3), reserved, fac_commoners, [itm_lady_dress_green,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000, 0x0000000000000003469b6e24e44e324b00000000001da6d30000000000000000 ],
["sirene_3", "La belle Beatrice", "La belle Beatrice", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(4), reserved, fac_commoners, [itm_lady_dress_blue,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x000000000000100436d8a236db6db6db00000000001dc6db0000000000000000, 0x000000000000100436d8a236db6db6db00000000001dc6db0000000000000000 ],
["sirene_client", "Client", "Client", tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(5), reserved, fac_neutral, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008690024843adbadb6db6db6db00000000001db6db0000000000000000 ],
["sirene_chambellan", "Chambellan", "Chambellan", tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(6), reserved, fac_neutral, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000 ],
["sirene_4", "Georgia", "Georgia", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_t_sirenes|entry(7), reserved, fac_commoners, [itm_red_dress,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x00000008940030063918ea36dc12249300000000001da6db0000000000000000, 0x00000008940030063918ea36dc12249300000000001da6db0000000000000000 ],

#Vieux chateau de tours
#
["chateautours_1", "Sergent d'Arme", "Sergent d'Arme", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_16_vchateau|entry(41), reserved, fac_neutral, [itm_haubergeon_f2,itm_surcoat_over_mail_f2,itm_surcoat_over_mail_f1,itm_coat_of_plates_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_visored_sallet,itm_nasal_helmet,itm_kettlehat1_painted,itm_open_sallet_coif,itm_mail_gauntlets,itm_battle_shieldcharlesv,itm_tab_shield_heater_a,itm_battle_shieldcharlesv,itm_heraldric_shieldred3lions,itm_war_shield3lys,itm_battle_shieldbluecross,itm_heraldric_shieldblueerminestripes,itm_war_shieldeagle,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3, swadian_face_middle_1, swadian_face_old_2 ],
["chateautours_2", "Sergent d'Arme", "Sergent d'Arme", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_16_vchateau|entry(42), reserved, fac_neutral, [itm_haubergeon_f2,itm_surcoat_over_mail_f2,itm_surcoat_over_mail_f1,itm_coat_of_plates_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_visored_sallet,itm_mail_coif_full,itm_kettlehat1_painted,itm_open_sallet_coif,itm_mail_gauntlets,itm_battle_shieldcharlesv,itm_tab_shield_heater_a,itm_battle_shieldcharlesv,itm_heraldric_shieldred3lions,itm_war_shield3lys,itm_battle_shieldbluecross,itm_heraldric_shieldblueerminestripes,itm_war_shieldeagle,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3, 0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
#["chateautours_3", "Sergent d'Arme", "Sergent d'Arme", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_16_vchateau|entry(43), reserved, fac_neutral, [itm_haubergeon_f2,itm_surcoat_over_mail_f2,itm_surcoat_over_mail_f1,itm_coat_of_plates_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_visored_sallet,itm_mail_coif_full,itm_kettlehat1_painted,itm_open_sallet_coif,itm_mail_gauntlets,itm_battle_shieldcharlesv,itm_tab_shield_heater_a,itm_battle_shieldcharlesv,itm_heraldric_shieldred3lions,itm_war_shield3lys,itm_battle_shieldbluecross,itm_heraldric_shieldblueerminestripes,itm_war_shieldeagle,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3, swadian_face_middle_1, swadian_face_old_2 ],
["chateautours_4", "Sergent d'Arme", "Sergent d'Arme", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_16_vchateau|entry(44), reserved, fac_neutral, [itm_haubergeon_f2,itm_surcoat_over_mail_f2,itm_surcoat_over_mail_f1,itm_coat_of_plates_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_visored_sallet,itm_mail_coif_full,itm_kettlehat1_painted,itm_open_sallet_coif,itm_mail_gauntlets,itm_battle_shieldcharlesv,itm_tab_shield_heater_a,itm_battle_shieldcharlesv,itm_heraldric_shieldred3lions,itm_war_shield3lys,itm_battle_shieldbluelysstripes,itm_battle_shieldbluelysstripes,itm_war_shieldeagle,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3, swadian_face_middle_1, swadian_face_old_2 ],
["chateautours_5", "Arbaletrier", "Arbaletriers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_16_vchateau|entry(45), reserved, fac_neutral, [itm_surcoat_over_mail_f2,itm_brigandine_f1,itm_brigandine_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_templar,itm_bayeux,itm_hospitaller,itm_kettle_hat,itm_kettlehat1_painted,itm_kettlehat1,itm_tab_shield_pavise_c], def_attrib|level(24), wp_melee(100), knows_common|knows_ironflesh_3|knows_power_draw_4|knows_athletics_5, swadian_face_young_1, swadian_face_old_2 ],
["chateautours_6", "Arbaletrier", "Arbaletriers", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, scn_town_16_vchateau|entry(46), reserved, fac_neutral, [itm_surcoat_over_mail_f2,itm_brigandine_f1,itm_brigandine_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_templar,itm_bayeux,itm_hospitaller,itm_kettle_hat,itm_kettlehat1_painted,itm_kettlehat1,itm_tab_shield_pavise_c], def_attrib|level(24), wp_melee(100), knows_common|knows_ironflesh_3|knows_power_draw_4|knows_athletics_5, 0x00000008690040003adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["chateautours_7", "Sergent d'Arme", "Sergent d'Arme", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_16_vchateau|entry(40), reserved, fac_neutral, [itm_haubergeon_f2,itm_surcoat_over_mail_f2,itm_surcoat_over_mail_f1,itm_coat_of_plates_f2,itm_splinted_greaves_f1,itm_mail_chausses_f1,itm_visored_sallet,itm_mail_coif_full,itm_kettlehat1_painted,itm_open_sallet_coif,itm_mail_gauntlets,itm_battle_shieldcharlesv,itm_tab_shield_heater_a,itm_battle_shieldcharlesv,itm_heraldric_shieldredlys,itm_war_shield3lys,itm_battle_shieldcharlesv,itm_battle_shieldbluelysstripes,itm_war_shieldeagle,itm_one_handed_battle_axe_a,itm_templar,itm_one_handed_battle_axe_b,itm_hospitaller,itm_lui_knightaxeonehe], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2|knows_shield_3|knows_power_strike_3, swadian_face_middle_1, swadian_face_old_2 ],

#rebels aussaut paris
["parisassau_rchef","Chef des Rebelles de Paris","Chef des Rebelles de Paris",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_padded_cloth_b_f1,itm_wrapping_boots,itm_war_bow,itm_arrows,itm_dagger_medievale,itm_woodenbuckler,itm_templar,],def_attrib2_b,wp(180),knows_archer_english,0x000000003805028128db6d37646db6db00000000001db6cb0000000000000000,0x000000003805028128db6d37646db6db00000000001db6cb0000000000000000],

["parisassau_troop1","Rebelle de Paris","Rebelles de Paris",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_padded_cloth_b_f1,itm_wrapping_boots,itm_hunter_boots,itm_mail_chausses,itm_war_bow,itm_arrows,itm_crossbow,itm_bolts,itm_bastard_sword_a,itm_sword_medieval_a,itm_templar,itm_dagger_medievale,itm_woodenbuckler,itm_heraldric_shieldblueerminestripes,itm_battle_shieldcharlesv,],def_attrib2,wp(80),knows_archer_basic,0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000,0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000],

["parisassau_troop2","Rebelle de Paris","Rebelles de Paris",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_shirt,itm_gambeson,itm_leather_vestblue,itm_wrapping_boots,itm_hide_boots,itm_hunter_boots,itm_crossbow,itm_bolts,itm_bastard_sword_a,itm_heraldric_shieldblueerminestripes,itm_woodenbuckler,itm_battle_shieldbluecross,itm_bastard_sword_a,itm_bastard_sword_b,],def_attrib_b,wp(80),knows_archer_basic,swadian_face_middle_2,0x00000008690020003adbadb6db6db6db00000000001db6db0000000000000000],

["parisassau_troop_wo","Rebelle de Paris","Rebelles de Paris",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_ranged,0,0,fac_black_khergits,[itm_wimple_a,itm_wimple_with_veil,itm_female_hood,itm_dress,itm_woolen_hose,itm_crossbow,itm_bolts,itm_steel_bolts,itm_templar,itm_wooden_shield,itm_templar,],def_attrib,wp(70),knows_archer_basic,0x00000008690040003adbadb6db6db6db00000000001db6db0000000000000000,0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000],


#troops de fierbois
["pretre_fierbois1", "pretre", "pretre", tf_guarantee_boots|tf_guarantee_armor, scn_fierbois_cha|entry(2), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000007bf0120c636db6db6db6db6db00000000001db6db0000000000000000 ],
["pretre_fierbois2", "pretre", "pretre", tf_guarantee_boots|tf_guarantee_armor, scn_fierbois_cha|entry(3), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000007bf0010ce36db6db6db6db6db00000000001db6db0000000000000000 ],
["pretre_fierbois3", "pretre", "pretre", tf_guarantee_boots|tf_guarantee_armor, scn_fierbois_cha|entry(4), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000000400100324da81a6dd6ca6d200000000001dc7130000000000000000 ],

#quete marchand de rouen /fille
["rouen_merchantquest", "Marchand", "Marchand", tf_guarantee_boots|tf_guarantee_armor, scn_town_12_alley|entry(6), reserved, fac_neutral, [itm_nobleman_outfit,itm_woolen_hose,itm_dagger_medievale], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000 ],
["rouen_mercenaire", "Garde du marchand", "Garde du marchant", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_12_alley|entry(7), reserved, fac_commoners, [itm_bastard_sword_a,itm_tab_shield_heater_c,itm_haubergeon,itm_hide_boots,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_1 ],

#acteurs foret de roen
["rouenf_traire1", "Garde du marchand", "Garde du marchant", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_rouen_forest|entry(40), reserved, fac_commoners, [itm_bastard_sword_a,itm_haubergeon,itm_hide_boots,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_1 ],
["rouenf_traire2", "Garde du marchand", "Garde du marchant", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_rouen_forest|entry(41), reserved, fac_commoners, [itm_bastard_sword_a,itm_haubergeon,itm_hide_boots,itm_mail_coif], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_2, mercenary_face_2 ],
["rouenf_traire3", "Garde du marchand", "Garde du marchant", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_rouen_forest|entry(42), reserved, fac_commoners, [itm_bastard_sword_a,itm_tab_shield_heater_c,itm_mail_hauberk,itm_hide_boots,itm_mail_coif,itm_mail_gauntlets], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, 0x000000003f0040c006db6e375b61b6db00000000001db6eb0000000000000000, 0x000000003f0040c006db6e375b61b6db00000000001db6eb0000000000000000 ],
["rouenf_fill", "Fille du marchand", "Fille du marchand", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_rouen_forest|entry(2), reserved, fac_commoners, [itm_lady_dress_ruby,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_ironflesh_8, 0x000000094400500724da81a6dd6ca6d200000000001dc7130000000000000000, 0x000000094400500724da81a6dd6ca6d200000000001dc7130000000000000000 ],

#demi compagnon paris
["comp_catas", "Chevalier solitaire", "Chevalier solitaire", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_mail_hauberk,itm_mail_chausses_f1,itm_pigface_klappvisor_open,itm_warhorse_f1,itm_hourglass_gauntlets,itm_lance_white,itm_knight,itm_4hammer,itm_heraldric_shieldblueerminestripes], def_attrib|level(23), wp(160), knows_common|knows_riding_5|knows_shield_3|knows_ironflesh_3|knows_power_strike_3, 0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690000003adbadb6db6db6db00000000001db6db0000000000000000 ],
["dame_jardin", "Madeleine", "Madeleine", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_town_7_alley|entry(6), reserved, fac_commoners, [itm_lady_dress_green,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10, 0x0000000d4400400124da81a6dd6ca6d200000000001dc7130000000000000000, 0x0000000d4400400124da81a6dd6ca6d200000000001dc7130000000000000000 ],

#demi compagnon orleans
["comp_orleans", "Champion Arbaletier", "Champion Arbaletier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_surcoat_over_mail_f2,itm_mail_chausses_f1,itm_leather_gloves,itm_sniper_crossbow,itm_bolts,itm_templar,itm_tab_shield_pavise_c], def_attrib|level(26), wp(160), knows_common|knows_ironflesh_3|knows_power_draw_9|knows_athletics_8, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000 ],

#messager de marseille
["comp_marseille", "Messager", "Messager", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_sword_medieval_a,itm_wooden_shield,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts], def_attrib|agi_21|level(25), wp(130), knows_common|knows_riding_7|knows_horse_archery_5, 0x000000086900b5ca3adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900b5ca3adbadb6db6db6db00000000001db6db0000000000000000 ],

####compagnon bourges sl scene messagers
["comps_bourges", "Mercenaire du SansLys", "Mercenaire du SansLys", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_hourglass_gauntlets_ornate,itm_brigandine_sl,itm_steel_greaves,itm_pigface_klappvisor_open,itm_klappvisier,itm_battle_shieldcharlesv,itm_templar], def_attrib|level(22)|str_16|agi_10, wp(140), knows_common|knows_shield_3|knows_power_strike_2|knows_ironflesh_2, mercenary_face_1, mercenary_face_1 ],

#compagnon dijon hospices docteur
["comps_dijon", "Pere Daniel", "Pere Daniel", tf_guarantee_boots|tf_guarantee_armor, scn_town_6_fleuve|entry(9), reserved, fac_commoners, [itm_robecross,itm_leather_boots,itm_templar], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10|knows_wound_treatment_9, 0x00000008690014443adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690014443adbadb6db6db6db00000000001db6db0000000000000000 ],

#compagnon aventurier calais
["comps_calais", "Aventurier", "Aventurier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_bastard_sword_a,itm_tab_shield_heater_c,itm_mail_hauberk,itm_hide_boots,itm_mail_coif], def_attrib|level(20), wp(130), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, mercenary_face_1, mercenary_face_1 ],

#compagnon arquebusier limoge
["comps_limoge", "Ingenieur Arquebusier", "Ingenieur Arquebusier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_neutral, [itm_matchlock_2,itm_cartridges,itm_shirt,itm_sword_medieval_b_small,itm_woolen_hose], def_attrib|level(22), wp(110), knows_common|knows_ironflesh_2|knows_power_draw_4|knows_athletics_3, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690044c53adbadb6db6db6db00000000001db6db0000000000000000 ],

#pnj 1429E new tavern
["alcolo_1", "Pilier de Taverne", "Pilier de Taverne", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [itm_shirt,itm_mail_shirt,itm_woolen_hose,itm_leather_apron], def_attrib|level(22), wp_melee(105), knows_common|knows_ironflesh_2, swadian_face_middle_1, swadian_face_old_2 ],
["courtisane_taverne", "Ribaude", "Ribaude", tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, [itm_ribaude_dress6bluues,itm_ribaude_dresss,itm_woolen_hose], def_attrib|level(6), wp(20), knows_inventory_management_10, 0x0000000014002004391aca36dc12249300000000001da6db0000000000000000, 0x0000000014002004391aca36dc12249300000000001da6db0000000000000000 ],
["organisateur", "Organisateur de combats", "Organisateur de combats", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners, [itm_nobleman_outfit,itm_leather_apron,itm_leather_apron,itm_nobleman_outfit,itm_woolen_hose,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f0040c006db6e375b61b6db00000000001db6eb0000000000000000, swadian_face_old_2 ],
#
["parieur_1", "Parieur", "Parieur", tf_hero, scn_pugilat_4|entry(2), reserved, fac_commoners, [itm_shirt,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f0080c736db6db6db61b6db00000000001db6eb0000000000000000, swadian_face_old_2 ],
#spectacteurs

["spectapugilat_1", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_4|entry(3), reserved, fac_commoners, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000000290050043adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_2", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_4|entry(4), reserved, fac_commoners, [itm_leather_apron,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f0000043adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_3", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_4|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000002900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],

["combatant_pugilat", "Combatant", "Combatant", tf_hero|tf_is_merchant, scn_pugilat_4|entry(6), reserved, fac_commoners, [itm_dagger_medievale], def_attrib|level(42)|str_30|agi_30, wp(120), knows_athletics_6|knows_power_draw_5|knows_shield_10|knows_ironflesh_10, bandit_face1, bandit_face2 ],

#
["parieur_12", "Parieur", "Parieur", tf_hero, scn_pugilat_1|entry(2), reserved, fac_commoners, [itm_thick_coat,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000008690110003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690110003adbadb6db6db6db00000000001db6db0000000000000000 ],
#spectacteurs

["spectapugilat_12", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_1|entry(3), reserved, fac_commoners, [itm_shirt,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000008690124033adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690124033adbadb6db6db6db00000000001db6db0000000000000000 ],
["spectapugilat_22", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_1|entry(4), reserved, fac_commoners, [itm_thick_coat,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000002900c3823adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_32", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_1|entry(5), reserved, fac_commoners, [itm_shirt,itm_leather_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000008690113c33adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690113c33adbadb6db6db6db00000000001db6db0000000000000000 ],

["combatant_pugilat2", "Combatant", "Combatant", tf_hero|tf_is_merchant, scn_pugilat_1|entry(6), reserved, fac_commoners, [itm_dagger_medievale], def_attrib|level(42)|str_30|agi_30, wp(120), knows_athletics_6|knows_power_draw_5|knows_ironflesh_10|knows_shield_10, 0x000000003f0060c706db6e375b61b6db00000000001db6eb0000000000000000, bandit_face2 ],

#
["parieur_13", "Parieur", "Parieur", tf_hero, scn_pugilat_2|entry(2), reserved, fac_commoners, [itm_leather_boots,itm_leather_apron], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f0080c706db6e375b61b6db00000000001db6eb0000000000000000, swadian_face_old_2 ],
#spectacteurs

["spectapugilat_13", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_2|entry(3), reserved, fac_commoners, [itm_leather_jerkin,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000000000084043adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_23", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_2|entry(4), reserved, fac_commoners, [itm_leather_apron,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f0040443adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_33", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_2|entry(5), reserved, fac_commoners, [itm_shirt,itm_woolen_hose], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000000290060053adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290060053adbadb6db6db6db00000000001db6db0000000000000000 ],

["combatant_pugilat3", "Combatant", "Combatant", tf_hero|tf_is_merchant, scn_pugilat_2|entry(6), reserved, fac_commoners, [itm_dagger_medievale], def_attrib|level(42)|str_30|agi_30, wp(120), knows_athletics_6|knows_power_draw_5|knows_ironflesh_10|knows_shield_10, bandit_face1, bandit_face2 ],

#
["parieur_14", "Parieur", "Parieur", tf_hero, scn_pugilat_3|entry(2), reserved, fac_commoners, [itm_leather_jerkin,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, swadian_face_middle_1, swadian_face_old_2 ],
#spectacteurs

["spectapugilat_14", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_3|entry(3), reserved, fac_commoners, [itm_leather_boots,itm_tabard], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x00000000290090053adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_24", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_3|entry(4), reserved, fac_commoners, [itm_woolen_hose,itm_nobleman_outfit], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000002900a0003adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],
["spectapugilat_34", "Spectacteur", "Spectacteur", tf_hero, scn_pugilat_3|entry(5), reserved, fac_commoners, [itm_shirt,itm_nomad_boots], def_attrib|level(2), wp(20), knows_inventory_management_10|knows_trade_5, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000 ],

["combatant_pugilat4", "Combatant", "Combatant", tf_hero|tf_is_merchant, scn_pugilat_3|entry(6), reserved, fac_commoners, [itm_dagger_medievale], def_attrib|level(42)|str_30|agi_30, wp(120), knows_athletics_6|knows_power_draw_5|knows_ironflesh_10|knows_shield_10, 0x000000003f00310006db6e375b61b6db00000000001db6eb0000000000000000, bandit_face2 ],

#

######## maitre guild messagers! #####################
["messenger_master", "Maitre de Guilde des Messagers de Calais", "Maitre de Guilde des Messagers de Calais", tf_guarantee_boots|tf_guarantee_armor, scn_town_9_messagers|entry(2), reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_bb_noble_hat_simple], def_attrib|level(2), wp(20), knows_common, 0x00000000290010403adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290010403adbadb6db6db6db00000000001db6db0000000000000000 ],
["messenger_master_bourges", "Maitre de Guilde des Messagers de Bourges", "Maitre de Guilde des Messagers de Bourges", tf_guarantee_boots|tf_guarantee_armor, scn_town_bourges_messagers|entry(2), reserved, fac_neutral, [itm_woolen_hose,itm_leather_apron,itm_bb_noble_hat], def_attrib|level(2), wp(20), knows_common, 0x00000000290040413adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290040413adbadb6db6db6db00000000001db6db0000000000000000 ],
["messenger_master_bordeau", "Maitre de Guilde des Messagers de Bordeau", "Maitre de Guilde des Messagers de Bordeau", tf_guarantee_boots|tf_guarantee_armor, scn_town_14_alley|entry(6), reserved, fac_neutral, [itm_woolen_hose,itm_shirt], def_attrib|level(2), wp(20), knows_common, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290052c13adbadb6db6db6db00000000001db6db0000000000000000 ],
["messenger_master_calais", "Maitre de Guilde des Messagers de Marseille", "Maitre de Guilde des Messagers de Marseille", tf_guarantee_boots|tf_guarantee_armor, scn_town_marss_messagers|entry(2), reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_leather_apron,itm_dagger_medievale], def_attrib|level(2), wp(20), knows_common, 0x00000000290063013adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290063013adbadb6db6db6db00000000001db6db0000000000000000 ],
# ["messenger_master_end", "Maitre de Guilde des Messagers de Marseille", "Maitre de Guilde des Messagers de Marseille", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_leather_apron,itm_dagger_medievale], def_attrib|level(2), wp(20), knows_common, 0x000000036900d1c936db6db6db65b6db00000000001db6db0000000000000000, 0x000000036900d1c936db6db6db65b6db00000000001db6db0000000000000000 ],

#eveques paris
["paris_evec_troop1", "Cardinal de Paris", "évêque de Paris", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_1cat_alley|entry(2), reserved, fac_commoners, [itm_robepurple,itm_woolen_hose,itm_sword_medieval_a], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000, 0x00000000290093423adbadb6db6db6db00000000001db6db0000000000000000 ],
["paris_moine_segond", "Pretre de Paris", "Pretre de Paris", tf_hero, scn_town_1cat_alley|entry(4), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008690120003adbadb6db6db6db00000000001db6db0000000000000000 ],

#eveques bourges
["bourges_evec_troop1", "Cardinal de Bourges", "Cardinal de Bourges", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, scn_town_bourgcat_alley|entry(2), reserved, fac_commoners, [itm_robepurple,itm_woolen_hose,itm_sword_medieval_a], def_attrib|level(20), wp(100), knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_power_strike_2, 0x000000002900b3823adbadb6db6db6db00000000001db6db0000000000000000, 0x000000002900b3823adbadb6db6db6db00000000001db6db0000000000000000 ],
["bourges_moine_segond", "Pretre de Bourges", "Pretre de Bourges", tf_hero, scn_town_bourgcat_alley|entry(4), reserved, fac_commoners, [itm_robecross,itm_leather_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000002900e3c23adbadb6db6db6db00000000001db6db0000000000000000 ],

#banquiers
["Bourges_banquier", "Banquier de Bourges", "Banquier de Bourges", tf_hero, scn_town_bourgesbanque|entry(2), reserved, fac_commoners, [itm_nobleman_outfit,itm_bb_noble_hat,itm_woolen_hose], def_attrib|level(2)|str_16, wp(20), knows_common, 0x000000086900f3c23adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900f3c23adbadb6db6db6db00000000001db6db0000000000000000 ],
["paris_banquier", "Banquier de Paris", "Banquier de Bourges", tf_hero, scn_town_parisbanque|entry(2), reserved, fac_commoners, [itm_bb_noble_hat,itm_nobleman_outfit,itm_woolen_hose], def_attrib|level(2)|str_16, wp(20), knows_common, 0x00000008690103c23adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690103c23adbadb6db6db6db00000000001db6db0000000000000000 ],
["marseille_banquier", "Banquier de Marseille", "Banquier de Marseille", tf_hero, scn_town_marseillebanque|entry(2), reserved, fac_commoners, [itm_nobleman_outfit,itm_woolen_hose], def_attrib|level(2)|str_16, wp(20), knows_common, 0x00000008690004043adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690004043adbadb6db6db6db00000000001db6db0000000000000000 ],

["mercenary_bourges", "Garde du banquier", "Garde du banquier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_town_bourgesbanque|entry(3), reserved, fac_commoners, [itm_leather_gloves,itm_mail_boots,itm_iron_greaves,itm_gothic_armour,itm_early_transitional_boar,itm_early_transitional_hre,itm_early_transitional_horse,itm_guard_helmet,itm_black_helmetgrey,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_senlac,itm_knight,itm_count,itm_castellan,itm_sempach,itm_battle_shieldbluelysstripes,itm_battle_shieldbluelysstripes,itm_battle_shieldcharlesv], def_attrib|level(23), wp(110), knows_common|knows_trainer_7|knows_spotting_7|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_4, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["mercenary_paris", "Garde du banquier", "Garde du banquier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_town_parisbanque|entry(3), reserved, fac_commoners, [itm_leather_gloves,itm_mail_boots,itm_iron_greaves,itm_gothic_armour,itm_early_transitional_boar,itm_early_transitional_teu,itm_early_transitional_horse,itm_guard_helmet,itm_black_helmetgrey,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_senlac,itm_knight,itm_count,itm_castellan,itm_sempach,itm_battle_shieldbluelysstripes,itm_battle_shieldbluelysstripes,itm_battle_shieldcharlesv], def_attrib|level(23), wp(110), knows_common|knows_trainer_7|knows_spotting_7|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_4, swadian_face_young_1, swadian_face_old_2 ],
["mercenary_marseille", "Garde du banquier", "Garde du banquier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield, scn_town_marseillebanque|entry(3), reserved, fac_commoners, [itm_leather_gloves,itm_mail_boots,itm_iron_greaves,itm_gothic_armour,itm_early_transitional_boar,itm_early_transitional_blue,itm_early_transitional_horse,itm_guard_helmet,itm_black_helmetgrey,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_visored_sallet_coif,itm_senlac,itm_knight,itm_count,itm_castellan,itm_sempach,itm_battle_shieldcharlesv,itm_battle_shieldcharlesv,itm_battle_shieldbluecross], def_attrib|level(23), wp(110), knows_common|knows_trainer_7|knows_spotting_7|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_4, 0x00000008690020003adbadb6db6db6db00000000001db6db0000000000000000, swadian_face_old_2 ],

#caserne lyon
["lyon_caserne_1", "Garde frontière Lyonnais", "Soldat en garnison", tf_hero, scn_town_casern_lyon|entry(5), reserved, fac_commoners, [itm_templar,itm_bastard_sword_a,itm_tab_shield_kite_a,itm_mail_mittens,itm_nasal_helmet,itm_mail_boots,itm_heraldic_mail_with_surcoat], def_attrib|level(2)|str_16|agi_10, wp(140), knows_common|knows_shield_6, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["lyon_caserne_2", "Garde frontière Lyonnais", "Garde frontière Lyonnais", tf_hero, scn_town_casern_lyon|entry(6), reserved, fac_commoners, [itm_templar,itm_bastard_sword_a,itm_tab_shield_kite_b,itm_mail_mittens,itm_nasal_helmet,itm_mail_boots,itm_heraldic_mail_with_surcoat], def_attrib|level(2)|str_16|agi_10, wp(140), knows_common|knows_shield_6, 0x00000008690050003adbadb6db6db6db00000000001db6db0000000000000000 ],
["lyon_caserne_3", "Garde frontière Lyonnais", "Soldat en garnison", tf_hero, scn_town_casern_lyon|entry(7), reserved, fac_commoners, [itm_templar,itm_bastard_sword_b,itm_tab_shield_kite_b,itm_mail_mittens,itm_mail_boots,itm_heraldic_mail_with_surcoat], def_attrib|level(2)|str_16|agi_12, wp(140), knows_common|knows_shield_6, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000 ],
["lyon_caserne_4", "Instructeur", "Instructeur", tf_hero, scn_town_casern_lyon|entry(2), reserved, fac_commoners, [itm_bastard_sword_b,itm_tab_shield_kite_a,itm_heraldic_mail_with_surcoat,itm_mail_boots], def_attrib|level(22)|str_16|agi_20, wp(220), knows_common|knows_ironflesh_8|knows_shield_10, 0x000000000000734406db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000734406db6e375b61b6db00000000001db6eb0000000000000000 ],
["lyon_caserne_5", "Garde frontière Lyonnais", "Soldat en garnison", tf_hero, scn_town_casern_lyon|entry(40), reserved, fac_commoners, [itm_templar,itm_bastard_sword_b,itm_tab_shield_kite_b,itm_mail_mittens,itm_mail_boots,itm_heraldic_mail_with_surcoat], def_attrib|level(2)|str_16|agi_12, wp(140), knows_common|knows_shield_6, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000 ],
["lyon_caserne_6", "Garde frontière Lyonnais", "aaSoldat en garnison", tf_hero, scn_town_casern_lyon|entry(41), reserved, fac_commoners, [itm_templar,itm_bastard_sword_b,itm_tab_shield_kite_a,itm_tab_shield_kite_c,itm_mail_mittens,itm_mail_boots,itm_heraldic_mail_with_surcoat], def_attrib|level(2)|str_16|agi_12, wp(140), knows_common|knows_shield_6, 0x000000003f00e0043adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f00e0043adbadb6db6db6db00000000001db6db0000000000000000 ],


["braconnier_1", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_nomad_boots,itm_leather_armor,itm_leather_vestgreen,itm_coif_new_e1,itm_skullcap,itm_wooden_stick,itm_short_bow,itm_arrows,itm_arrows], def_attrib|level(12), wp(75), knows_common|knows_spotting_1|knows_athletics_5|knows_power_draw_3, 0x000000000000520306db6e375b61b6db00000000001db6eb0000000000000000, 0x000000003f00e08a36db6db6db61b6db00000000001db6eb0000000000000000 ],
["braconnier_2", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_nomad_boots,itm_leather_armor,itm_leather_vestgreen,itm_coif_new_e1,itm_skullcap,itm_short_bow,itm_short_bow,itm_arrows,itm_arrows], def_attrib|level(12), wp(75), knows_common|knows_spotting_1|knows_athletics_5|knows_power_draw_3, 0x000000000000624406db6e375b61b6db00000000001db6eb0000000000000000, 0x000000003f0090c736db6db6db61b6db00000000001db6eb0000000000000000 ],
["braconnier_3", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_nomad_boots,itm_leather_armor,itm_leather_vestgreen,itm_coif_new_e1,itm_skullcap,itm_wooden_stick,itm_short_bow,itm_arrows,itm_arrows], def_attrib|level(10), wp(75), knows_common|knows_spotting_1|knows_athletics_3|knows_power_draw_3, swadian_face_young_1, swadian_face_old_2 ],
# ["braconnier_4", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_nomad_boots,itm_leather_armor,itm_leather_vestgreen,itm_coif_new_e1,itm_skullcap,itm_1club,itm_hunting_bow,itm_short_bow,itm_arrows,itm_barbed_arrows], def_attrib|level(10), wp(75), knows_common|knows_spotting_1|knows_athletics_5|knows_power_draw_3, 0x00000000000073c43adbadb6db6db6db00000000001db6db0000000000000000, 0x000000003f00c0043adbadb6db6db6db00000000001db6db0000000000000000 ],

#concurent course
# ["concurent_1", "Concurent", "Concurent", tf_mounted|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_hide_boots,itm_leather_vestgreen,itm_skullcap,itm_courserf01], def_attrib|level(12), wp(75), knows_common|knows_athletics_5|knows_riding_8, 0x000000000000520306db6e375b61b6db00000000001db6eb0000000000000000, 0x000000003f00e08a36db6db6db61b6db00000000001db6eb0000000000000000 ],

# Vieil aventurier
["v_aventurier", "Vieil Aventurier", "Vieil Aventurier", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_haubergeon,itm_woolen_hose,itm_leather_cap,itm_bastard_sword_b], def_attrib|level(12), wp(75), knows_common|knows_athletics_5, 0x000000003f0050c436db6db6db6db6db00000000001db6db0000000000000000, 0x000000003f0050c436db6db6db6db6db00000000001db6db0000000000000000 ],

# moines quete tresort templiers
["moin_orleans", "Frere Patrique", "Frere Patrique", tf_hero, scn_monastere_orleans|entry(2), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000086900b0003adbadb6db6db6db00000000001db6db0000000000000000 ],
["moin_orleans2", "Moine", "Moine", tf_hero, scn_monastere_orleans|entry(3), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x00000008690010003adbadb6db6db6db00000000001db6db0000000000000000 ],

# moines quete tresort templiers interieur bibliotheque
["moin_orleans_interieur", "Moine Scribe", "Moine Scribe", tf_hero, scn_monastere_orleans_int|entry(2), reserved, fac_commoners, [itm_robecross,itm_wrapping_boots], def_attrib|level(2)|str_16, wp(20), knows_inventory_management_10, 0x000000086900a5883adbadb6db6db6db00000000001db6db0000000000000000 ],

#Disciple franc macon
["f_macon_bouclier", "Disciple Franc Macon", "Disciple Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_coif], def_attrib|level(15)|str_17, wp(95), knows_common|knows_athletics_5|knows_shield_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["f_macon_hache_bouclier", "Disciple Franc Macon", "Disciple Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_chausses,itm_mail_boots,itm_mail_coif], def_attrib|level(15)|str_16, wp(95), knows_common|knows_athletics_5|knows_shield_5, 0x000000000000114106db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000114106db6e375b61b6db00000000001db6eb0000000000000000 ],
["f_macon_hache2m", "Maistre Franc Macon", "Maistre Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_coif,itm_great_bardiche], def_attrib|level(19)|str_17, wp(115), knows_common|knows_athletics_5, 0x00000008690060003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690050003adbadb6db6db6db00000000001db6db0000000000000000 ],

["mendiant_rc", "mendiant", "mendiant", 0, no_scene, reserved, fac_commoners, [itm_wooden_stick], def_attrib|level(19)|str_11, wp(85), knows_common|knows_athletics_5, 0x000000000000218206db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000218206db6e375b61b6db00000000001db6eb0000000000000000 ],



["f_macon_bouclier1", "Maistre Franc Macon", "Disciple Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_coif], def_attrib|level(15)|str_17, wp(95), knows_common|knows_athletics_5|knows_shield_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["f_macon_hache_bouclier2", "Disciple Franc Macon", "Disciple Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_chausses,itm_mail_boots,itm_mail_coif], def_attrib|level(15)|str_16, wp(95), knows_common|knows_athletics_5|knows_shield_5, 0x000000000000114106db6e375b61b6db00000000001db6eb0000000000000000, 0x000000000000114106db6e375b61b6db00000000001db6eb0000000000000000 ],
["f_macon_hache2m3", "Maistre Franc Macon", "Maistre Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_coif,itm_great_bardiche], def_attrib|level(19)|str_17, wp(115), knows_common|knows_athletics_5, 0x00000008690060003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690050003adbadb6db6db6db00000000001db6db0000000000000000 ],
# ["f_macon_bouclier4", "Disciple Franc Macon", "Disciple Franc Macon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_maconique_armor,itm_maconique_armor,itm_maconique_armor,itm_templar_q_sword,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_coif], def_attrib|level(15)|str_17, wp(95), knows_common|knows_athletics_5|knows_shield_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],

["jouteur_training", "Jouteur", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_leather_boots,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_17, wp(115), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],

## Tourney Troops - EXCEL Templates here too - Kham
#jouteurs de tournois

["jouteur_tournament_1", "Jouteur débutant", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_new_shynbaulds,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(11)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_2", "Jeune Jouteur", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_new_shynbaulds,itm_mail_hauberk,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(11)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_3", "Jouteur confirmé", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_new_shynbaulds,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_4", "Jouteur expert", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_new_shynbaulds,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_5", "Jouteur vétéran", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_new_shynbaulds,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(16)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_6", "Jouteur vétéran", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(16)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_7", "Jouteur vétéran ", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_chausses,itm_new_shynbaulds,itm_new_shynbaulds,itm_mail_hauberk,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(16)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_8", "Jouteur vétéran", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_new_shynbaulds,itm_mail_hauberk,itm_mail_coif,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(16)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_9", "Jouteur maladroit", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(14)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_10", "Jouteur nerveux", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(14)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_11", "Jouteur anonyme", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(14)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_12", "Jouteur experimenté", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_13", "Jouteur inconnu", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_14", "Jouteur maladroit", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(14)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_15", "Jouteur occasionnel", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_16", "Jouteur ", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["jouteur_tournament_17", "Jouteur", "Jouteur", tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_training_joute_saddle_horse_enemi,itm_mail_mittens,itm_mail_boots,itm_mail_chausses,itm_mail_hauberk,itm_mail_coif,itm_new_shynbaulds,itm_leather_jacket,itm_greathelm1,itm_full_helm,itm_newlance_joutes_training_enemi,itm_newlance_joutes_training_enemi], def_attrib|level(15)|str_20, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],

["auberge_troop_1", "Vendeur de chevaux", "Vendeur de chevaux", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_1|entry(2), reserved, fac_commoners, [itm_saddle_horse,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse,itm_steppe_horse,itm_horse1,itm_horse6,itm_horse6,itm_horse1f01,itm_horse7f01,itm_hunting_horsef01,itm_hunting_horsef01,itm_g_tw_shirt,itm_woolen_hose], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000003d01005244dc8dbb2361b6db00000000001d571b0000000000000000, 0x000000003d01005244dc8dbb2361b6db00000000001d571b0000000000000000 ],
["auberge_troop_2", "Garde de l'Auberge", "Jouteur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_auberge_ext_1|entry(3), reserved, fac_commoners, [itm_mail_hauberk,itm_mail_mittens,itm_mail_boots,itm_mail_coif,itm_templar], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000003f00800b48db71b6eaaa452300000000001d26d30000000000000000, 0x000000003f00800b48db71b6eaaa452300000000001d26d30000000000000000 ],
["auberge_troop_3", "Vendeur de chevaux", "Vendeur de chevaux", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_2|entry(2), reserved, fac_commoners, [itm_sumpter_horse,itm_sumpter_horse,itm_sumpter_horse,itm_saddle_horse,itm_saddle_horse,itm_steppe_horse,itm_arabian_horse_a,itm_horse1,itm_horse7,itm_horse7,itm_horse8,itm_woolen_hose,itm_tunic_with_green_cape], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000009ff00f0c9251b89c6dca6491a00000000001e36db0000000000000000, 0x00000009ff00f0c9251b89c6dca6491a00000000001e36db0000000000000000 ],
["auberge_troop_4", "Garde de l'Auberge", "Garde de l'Auberge", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_auberge_ext_2|entry(3), reserved, fac_commoners, [itm_light_mail_and_plate,itm_mail_mittens,itm_mail_chausses,itm_bayeux,itm_chapel_de_fer], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000003f00e585251b89c6dca6491a00000000001e36db0000000000000000, 0x000000003f00e585251b89c6dca6491a00000000001e36db0000000000000000 ],
["auberge_troop_5", "Vendeur de chevaux", "Vendeur de chevaux", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_3|entry(2), reserved, fac_commoners, [itm_horse8,itm_horse8,itm_horse8,itm_horse1,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_sumpter_horse,itm_sumpter_horse,itm_sumpter_horse,itm_sumpter_horse,itm_woolen_hose,itm_shirt], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000003f00c544251b89c6dca6491a00000000001e36db0000000000000000, 0x000000003f00c544251b89c6dca6491a00000000001e36db0000000000000000 ],
["auberge_troop_6", "Garde de l'Auberge", "Garde de l'Auberge", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_auberge_ext_3|entry(3), reserved, fac_commoners, [itm_footman_helmet,itm_light_mail_and_plate,itm_mail_boots,itm_gaddhjalt], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000003d01109244dc8dbb2361b6db00000000001d571b0000000000000000, 0x000000003d01109244dc8dbb2361b6db00000000001d571b0000000000000000 ],
["auberge_troop_7", "Vendeur de chevaux", "Vendeur de chevaux", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_4|entry(2), reserved, fac_commoners, [itm_sumpter_horse,itm_sumpter_horse,itm_sumpter_horse,itm_sumpter_horse,itm_steppe_horse,itm_steppe_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,itm_horse6,itm_horse6,itm_woolen_hose,itm_shirt], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["auberge_troop_8", "Garde de l'Auberge", "Garde de l'Auberge", 0|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet, scn_auberge_ext_4|entry(3), reserved, fac_commoners, [itm_dark_light_mail_and_plate,itm_plate_mittens,itm_nasal_helmet,itm_mail_boots,itm_knight], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x000000000000b24f36db6db6db6db6db00000000001db6db0000000000000000, 0x000000000000b24f36db6db6db6db6db00000000001db6db0000000000000000 ],

#auberges interrieur
["auberge_troop_9", "Aubergiste", "Aubergiste", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_inter_1|entry(2), reserved, fac_commoners, [itm_leather_apron,itm_woolen_hose,itm_pate1,itm_pate1,itm_pate1,itm_pate2,itm_pate2,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausages,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_rhumm,itm_rhumm,itm_rhumm,itm_rhumm,itm_champi,itm_champi,itm_champi,itm_champi,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_apples,itm_apples,itm_apples,itm_apples,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_chicken,itm_poiss_soup,itm_poiss_soup,itm_soup,itm_potee], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["auberge_troop_10", "Aubergiste", "Aubergiste", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_inter_2|entry(2), reserved, fac_commoners, [itm_tavern_shirt,itm_woolen_hose,itm_pate3,itm_pate3,itm_pate2,itm_pate2,itm_pate2,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_sausages,itm_sausages,itm_sausages,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_bier,itm_bier,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_fesan,itm_potee,itm_potee,itm_potee,itm_potee,itm_potee,itm_soup,itm_soup], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["auberge_troop_11", "Aubergiste", "Aubergiste", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_inter_3|entry(2), reserved, fac_commoners, [itm_leather_apron,itm_woolen_hose,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate2,itm_pate2,itm_pate2,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_pate3,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausages,itm_sausages,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_rhumm,itm_rhumm,itm_champi,itm_champi,itm_champi,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_raw_grapes,itm_chicken,itm_chicken,itm_chicken,itm_chicken,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["auberge_troop_12", "Aubergiste", "Aubergiste", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_inter_4|entry(2), reserved, fac_commoners, [itm_tavern_shirt,itm_woolen_hose,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate2,itm_pate1,itm_pate1,itm_pate1,itm_pate1,itm_pate3,itm_pate3,itm_pate3,itm_bread,itm_bread,itm_bread,itm_bread,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausages,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_sausc,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_bier,itm_apples,itm_apples,itm_apples,itm_apples,itm_apples,itm_apples,itm_apples,itm_chicken,itm_chicken,itm_chicken,itm_oeufss,itm_oeufss,itm_soup,itm_soup,itm_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_poiss_soup,itm_fesan,itm_torch], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],


["manoir_troop_1", "Refugié", "Refugié", tf_guarantee_boots|tf_guarantee_armor, scn_maison_auberge_quete1|entry(2), reserved, fac_commoners, [itm_woolen_hose,itm_shirt], def_attrib|level(15)|str_17, wp(135), knows_common|knows_athletics_5|knows_shield_5|knows_riding_5, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000, 0x00000008690030003adbadb6db6db6db00000000001db6db0000000000000000 ],
["manoir_troop_2", "Refugiée", "Refugiée", tf_female|tf_guarantee_boots|tf_guarantee_armor, scn_maison_auberge_quete1|entry(3), reserved, fac_commoners, [itm_dress,itm_leather_boots], def_attrib|level(2), wp(50), knows_common|knows_riding_2, woman_face_1, woman_face_2 ],

# auberge pnj
["auberge_client_1", "Hobelar", "Hobelars", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_hunter,itm_hunter_f,itm_1mace,itm_tunic_with_green_cape,itm_white_gambeson_f1,itm_mail_mittens,itm_mail_gauntlets,itm_mail_chausses,itm_mail_boots,itm_mail_coif,itm_mail_coif_full,itm_tab_shield_kite_c,itm_tab_shield_kite_cav_a,itm_voulge_long_blunt,itm_voulge_long_blunt], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2|knows_riding_5, swadian_face_young_1, swadian_face_old_2 ],
["auberge_client_2", "Hacheur", "Hacheurs", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_mail_chausses,itm_mail_boots,itm_mail_hauberk,itm_cuir_bouilli,itm_mail_mittens,itm_mail_gauntlets,itm_mail_coif,itm_mail_coif_full,itm_chapel_de_fer,itm_tab_shield_heater_a,itm_tab_shield_round_d,itm_lui_knightaxeonehb,itm_lui_knightaxeonehb], def_attrib|level(9)|str_12, wp(85), knows_common|knows_spotting_1|knows_athletics_3|knows_shield_5, mercenary_face_1, mercenary_face_2 ],
["auberge_client_3", "Messager", "Messagers", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_common_hoodblack,itm_tabard,itm_dagger_medievale], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000000c01200c509d8db76962276b00000000001dbe0c0000000000000000, 0x000000000c01200c509d8db76962276b00000000001dbe0c0000000000000000 ],
["auberge_client_4", "Pilier d'Auberge", "Pilier d'Auberge", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_shirt,itm_woolen_hose,itm_short_tunic,itm_red_gambeson], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, swadian_face_young_1, swadian_face_old_2 ],
["auberge_client_5", "Jouteur", "Jouteurs", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_leather_jacket,itm_courtly_outfit,itm_bb_noble_hat], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, swadian_face_young_1, swadian_face_old_2 ],
["auberge_client_6", "Paysans joyeux", "Paysans joyeux", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_shirt,itm_woolen_hose,itm_arming_cap,itm_coarse_tunic], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000001b0002cd34e975b2b476b922000000000005bcdb0000000000000000, 0x00000001b10c8285459a919514d9bb1400000000001d38640000000000000000 ],
["auberge_client_7", "Homme ivre", "Hommes ivres", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_leather_cap,itm_nomad_vest], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000001e10b3d2588db9e3158f499200000000001d94930000000000000000, 0x000000001e10b3d2588db9e3158f499200000000001d94930000000000000000 ],
["auberge_client_8", "Medecin", "Medecin", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_leather_jacket,itm_courtly_outfit,itm_red_gambeson], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000003a0861d45d3471d4aa69c92200000000000534720000000000000000, 0x000000018e1023cf24ac8659ac91969b00000000001da8cd0000000000000000 ],

# auberge pnj
["camelot_1", "Camelot", "Camelot", tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_1|entry(6), reserved, fac_commoners, [itm_shirt,itm_woolen_hose,itm_book_tactics,itm_book_persuasion,itm_book_training_reference,itm_spice,itm_spice,itm_salt,itm_salt,itm_oil,itm_oil,itm_pottery,itm_pottery,itm_pottery,itm_wool,itm_wool,itm_wool_cloth,itm_velvet,itm_velvet,itm_velvet,itm_iron,itm_iron,itm_furs,itm_furs,itm_furs,itm_wine,itm_wine,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_smoked_fish,itm_honey,itm_honey,itm_apples,itm_apples,itm_grain,itm_grain,itm_grain,itm_grain,itm_bier,itm_bier,itm_sausc,itm_sausc,itm_arrows,itm_arrows,itm_bolts,itm_bolts,itm_bolts,itm_blue_hose,itm_blue_hose,itm_hide_boots,itm_mail_chausses,itm_mail_chausses,itm_mail_boots,itm_plan_1,itm_plan_1,itm_plan_2,itm_plan_4,itm_plume,itm_plume,itm_plume,itm_pier], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000000000b24f36db6db6db6db6db00000000001db6db0000000000000000, 0x000000000000b24f36db6db6db6db6db00000000001db6db0000000000000000 ],
["camelot_2", "Camelot", "Camelot", tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_2|entry(6), reserved, fac_commoners, [itm_orl_leather_apron,itm_woolen_hose,itm_shirt,itm_gambeson,itm_gambeson,itm_leather_vest_f2,itm_fur_hat,itm_fur_hat,itm_felt_hat,itm_falchion,itm_arena_sword,itm_book_weapon_mastery,itm_book_engineering,itm_book_wound_treatment_reference,itm_spice,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_salt,itm_oil,itm_oil,itm_linen,itm_wool,itm_wool,itm_wool,itm_tools,itm_tools,itm_tools,itm_iron,itm_furs,itm_furs,itm_furs,itm_furs,itm_wine,itm_wine,itm_smoked_fish,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_cheese,itm_honey,itm_honey,itm_rhumm,itm_rhumm,itm_oeufss,itm_oeufss,itm_oeufss,itm_plan_8,itm_plan_11,itm_plan_12,itm_plan_10,itm_plan_6,itm_enclume,itm_ustensil,itm_ustensil,itm_pier,itm_pier,itm_pier,itm_bois,itm_plume,itm_plume], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000003d01109244dc8dbb2361b6db00000000001d571b0000000000000000, 0x000000003d01109244dc8dbb2361b6db00000000001d571b0000000000000000 ],
["camelot_3", "Camelot", "Camelot", tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_3|entry(6), reserved, fac_commoners, [itm_woolen_hose,itm_tavern_shirt,itm_oeufss,itm_oeufss,itm_oeufss,itm_pate1,itm_pate1,itm_pate2,itm_champi,itm_champi,itm_champi,itm_champi,itm_legum,itm_legum,itm_tutorial_sword,itm_book_persuasion,itm_book_persuasion,itm_book_leadership,itm_book_training_reference,itm_spice,itm_salt,itm_salt,itm_salt,itm_salt,itm_oil,itm_oil,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_wool,itm_wool,itm_wool,itm_tools,itm_tools,itm_iron,itm_iron,itm_iron,itm_iron,itm_iron,itm_furs,itm_furs,itm_furs,itm_smoked_fish,itm_smoked_fish,itm_grain,itm_grain,itm_grain,itm_grain,itm_grain,itm_grain,itm_grain,itm_grain,itm_rhumm,itm_rhumm,itm_legum,itm_legum,itm_legum,itm_ustensil,itm_ustensil,itm_plan_1,itm_plan_1,itm_enclume,itm_enclume], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x00000009ff01010a251b89c6dca6491a00000000001e36db0000000000000000, 0x00000009ff01010a251b89c6dca6491a00000000001e36db0000000000000000 ],
["camelot_4", "Camelot", "Camelot", tf_hero|tf_guarantee_boots|tf_guarantee_armor, scn_auberge_ext_4|entry(6), reserved, fac_commoners, [itm_shirt,itm_woolen_hose,itm_nobleman_outfit,itm_nobleman_outfit_anglais,itm_nobleman_out,itm_tavern_shirt,itm_tavern_shirt,itm_fur_hat,itm_fur_hat,itm_crecy,itm_maul,itm_book_intelligence,itm_book_leadership,itm_book_leadership,itm_spice,itm_spice,itm_spice,itm_salt,itm_salt,itm_oil,itm_oil,itm_oil,itm_oil,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_pottery,itm_wool,itm_wool,itm_velvet,itm_velvet,itm_velvet,itm_iron,itm_iron,itm_tools,itm_tools,itm_tools,itm_tools,itm_tools,itm_tools,itm_tools,itm_tools,itm_furs,itm_furs,itm_plan_2,itm_plan_5,itm_plan_6,itm_plan_7,itm_plan_9,itm_plan_11,itm_plan_12,itm_plan_12,itm_torch,itm_torch,itm_torch,itm_enclume,itm_enclume,itm_cuir,itm_cuir,itm_corde,itm_corde,itm_champiv,itm_pier], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, 0x000000003f00c544251b89c6dca6491a00000000001e36db0000000000000000, 0x000000003f00c544251b89c6dca6491a00000000001e36db0000000000000000 ],

# pnj a quete a faire
#["auberge_client_9", "Paysan inquiet", "Paysan inquiet", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_shirt,itm_woolen_hose], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2, swadian_face_young_1, swadian_face_old_2 ],

["cvalier_invisible_quete_prairie", "Cheval exceptionnel", "Cheval exceptionnel", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_cheval_praire,itm_cavalier_invisible_casque,itm_cavalier_invisible_armor,itm_cavalier_invisible_bottes,itm_cavalier_invisible_gants], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2|knows_riding_5, swadian_face_young_1, swadian_face_old_2 ],
#["cvalier_invisible_quete_prairie_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],


["cvalier_invisible_quete_prairie_barder", "Cheval exceptionnel bardé", "Cheval exceptionnel bardé", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_horse, no_scene, reserved, fac_commoners, [itm_cheval_praire_barder,itm_cavalier_invisible_casque,itm_cavalier_invisible_armor,itm_cavalier_invisible_bottes,itm_cavalier_invisible_gants], def_attrib|level(9), wp(75), knows_common|knows_spotting_1|knows_athletics_2|knows_riding_5, swadian_face_young_1, swadian_face_old_2 ],
#["cvalier_invisible_quete_prairie_barder_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],


["auberge_barde", "Barde", "Barde", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_lutnia,itm_common_hoodblack,itm_common_hood,itm_g_tw_shirt,itm_gambeson,itm_woolen_hose,itm_woolen_hose], def_attrib|level(4), wp(60), knows_common, 0x000000002209251216dc30b6596dbc6c00000000000dca6d0000000000000000, 0x0000000180044553554d8cb5d27e515100000000001e47690000000000000000 ],
["auberge_barde_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

["auberge_walker", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_kufel,itm_short_tunic,itm_g_tw_shirt,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, 0x000000003f04018556db6d35244636db00000000001db69b0000000000000000, man_face_old_2 ],
["auberge_walker2", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_kufel,itm_short_tunic,itm_g_tw_shirt,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, 0x000000003f04018556db6d35244636db00000000001db69b0000000000000000, man_face_old_2 ],
["auberge_walker3", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_kufel,itm_short_tunic,itm_g_tw_shirt,itm_leather_vest,itm_leather_apron,itm_shirt,itm_woolen_hose,itm_blue_hose,itm_hide_boots,itm_ankle_boots,itm_leather_boots,itm_fur_hat,itm_leather_cap,itm_straw_hat,itm_felt_hat], def_attrib|level(4), wp(60), knows_common, 0x000000003f04018556db6d35244636db00000000001db69b0000000000000000, man_face_old_2 ],
["auberge_walker4", "Villageois", "Villageois", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_kufel,itm_blue_dress,itm_blue_dress_tw,itm_blue_dress_tw2,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
["auberge_walker5", "Villageois", "Villageois", tf_female|tf_guarantee_boots|tf_guarantee_armor, no_scene, reserved, fac_commoners, [itm_dedal_kufel,itm_blue_dress,itm_blue_dress_tw,itm_blue_dress_tw2,itm_peasant_dress,itm_woolen_hose,itm_blue_hose,itm_wimple_a,itm_wimple_with_veil,itm_female_hood], def_attrib|level(2), wp(40), knows_common, woman_face_1, woman_face_2 ],
["auberge_walker_end","_","_",tf_inactive,0,0,0,[],0,0,0,0],

#volontaire auberge broceliand
#villageois courrageux fantassin
["volontaire_grotte1", "Villageois", "Villageois", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_arming_cap,itm_coarse_tunic,itm_woolen_hose,itm_bayeux,itm_torch,itm_torch], def_attrib|level(9)|str_9, wp(90), knows_common|knows_spotting_1|knows_athletics_5|knows_shield_5|knows_ironflesh_6, 0x000000001e10b3d2588db9e3158f499200000000001d94930000000000000000, 0x000000001e10b3d2588db9e3158f499200000000001d94930000000000000000 ],
#ancien mercenaire solitaire et bougon fantassin
["volontaire_grotte2", "Brandon", "Brandon", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_3hammer,itm_breton_peasant_man,itm_woolen_hose,itm_common_hood,itm_leather_gloves,itm_torch,itm_torch], def_attrib|level(12)|str_8|agi_9, wp(120), knows_common|knows_spotting_1|knows_athletics_2, 0x000000000a011001375c4ebb2b55ba1100000000000dd3590000000000000000, 0x000000000a011001375c4ebb2b55ba1100000000000dd3590000000000000000 ],
# bandit qui est malg? tout "embarqu?dans le meme bateau" archer
["volontaire_grotte3", "Coupe gorge", "Coupe gorge", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged, no_scene, reserved, fac_commoners, [itm_hunting_bow,itm_khergit_arrows,itm_common_hoodblack,itm_dagger_medievale,itm_leather_cap,itm_leather_gloves,itm_leather_boots,itm_leather_coat,itm_woolen_cap], def_attrib|level(10)|str_8, wp(100), knows_common|knows_spotting_1|knows_athletics_2|knows_power_draw_5|knows_power_strike_4, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000 ],
#soldat a la retraite au service du duc de bretagne cavalier
["volontaire_grotte4", "Artus", "Artus", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_knight,itm_red_gambeson,itm_leather_boots,itm_torch,itm_torch], def_attrib|level(13)|str_7|agi_12, wp(140), knows_common|knows_spotting_1|knows_athletics_2|knows_riding_5, 0x00000000250c6411388b95cce3764b5400000000000eb72c0000000000000000, 0x00000000250c6411388b95cce3764b5400000000000eb72c0000000000000000 ],

#troupes de Penthi?re batailles
["penthiv_troop1", "Fantassin lourd de Penthièvre", "Fantassin lourd de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_full_helm,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_shynbaulds,itm_leather_boots], def_attrib|level(9)|agi_12, wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop2", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_woodenbuckler,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop3", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_mail_coif,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop4", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_leather_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop5", "Lancier de Penthièvre", "Lancier de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_shynbaulds,itm_bill,itm_2glaive,itm_voulge_1,itm_leather_boots], def_attrib|level(9)|agi_10, wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop6", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop7", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop8", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop9", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop10", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["Penthiv_troop11", "Epeiste de Penthièvre", "Epeiste de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_flamberge,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_shynbaulds,itm_leather_boots], def_attrib|level(9)|agi_10|str_11, wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],

#troupes de Penthi?re dialogues
#guardes entree auberge avant liberation maire
["dial_Penthiv_troop1", "Fantassin lourd de Penthièvre", "Fantassin lourd de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_full_helm,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_shynbaulds,itm_leather_boots], def_attrib|level(9)|agi_12, wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face1 ],
["dial_Penthiv_troop2", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_mail_coif,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
#gardes porte lac
["penthiv_troopporte_lac1", "Fantassin lourd de Penthièvre", "Fantassin lourd de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_full_helm,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_shynbaulds,itm_leather_boots], def_attrib|level(9)|agi_12, wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["penthiv_troopporte_lac2", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_woodenbuckler,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["penthiv_troopporte_lac3", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_heraldric_shieldblue3lys,itm_mail_coif,itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],



#gardes interrieur auberge
["dial_Penthiv_aubtrp1", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000 ],
["dial_Penthiv_aubtrp2", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["dial_Penthiv_aubtrp3", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["dial_Penthiv_aubtrp4", "Troupe de Penthièvre", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],


#soldat duc bretagne cordon
["cordon_breton_guard1", "Fantassin lourd Breton", "Fantassins lourds Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["cordon_breton_guard2", "Fantassin lourd Breton", "Fantassins lourds Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["cordon_breton_guard3", "Fantassin lourd Breton", "Fantassins lourds Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["cordon_breton_guard4", "Fantassin lourd Breton", "Fantassins lourds Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

#maire auberge broiceliand
["maire_auberge_broceliand", "Echanson", "Echanson", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_bb_noble_hat,itm_courtly_outfit], def_attrib|level(9)|str_9, wp(90), knows_common|knows_spotting_1|knows_athletics_5|knows_shield_5|knows_ironflesh_6, 0x000000000510a2c712ea92b92c9248ca000000000012c4b30000000000000000, 0x000000000510a2c712ea92b92c9248ca000000000012c4b30000000000000000 ],

#aubergiste et otage
["aubergiste_auberge_broceliand", "Aubergiste", "Aubergiste", tf_hero|tf_is_merchant|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield, no_scene, reserved, fac_commoners, [itm_woolen_hose,itm_tavern_shirt,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_choppe_bier,itm_bier,itm_bier,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_bread,itm_cheese,itm_cheese,itm_sausc,itm_sausc,itm_sausc], def_attrib|level(9)|str_9, wp(90), knows_common|knows_spotting_1|knows_athletics_5|knows_shield_5|knows_ironflesh_6, 0x000000002209251216dc30b6596dbc6c00000000000dca6d0000000000000000, 0x000000002209251216dc30b6596dbc6c00000000000dca6d0000000000000000 ],
#mercenaire a tuer dans la foret
["mercenair_aventurier", "Aventurier", "Aventurier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_common_hood,itm_haubergeon,itm_leather_boots,itm_agincourt,itm_woodenbuckler], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000020c85881333b5c55a734a890000000000111b1d0000000000000000, 0x00000000020c85881333b5c55a734a890000000000111b1d0000000000000000 ],


["otage_mineur1", "Chef mineur", "Mineur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_coarse_tunic,itm_torch], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000130c21cf14b24db2de6e34ab000000000015491a0000000000000000, 0x00000000130c21cf14b24db2de6e34ab000000000015491a0000000000000000 ],
["otage_mineur2", "Mineur", "Mineur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_torch], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000002508a1c6165a2546ad6e181c00000000000d28a30000000000000000, 0x000000002508a1c6165a2546ad6e181c00000000000d28a30000000000000000 ],
["otage_mineur3", "Mineur", "Mineur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_coarse_tunic,itm_torch], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000100443cd36dcb646e1697ad400000000000dbb130000000000000000, 0x00000000100443cd36dcb646e1697ad400000000000dbb130000000000000000 ],
["otage_mineur4", "Mineur", "Mineur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_torch], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000230411926aa34644da5a66f200000000001d4aac0000000000000000, 0x00000000230411926aa34644da5a66f200000000001d4aac0000000000000000 ],

#guide auberge broceliand
["guide_auberge", "Guide forestier", "Guide forestier", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_common_hood,itm_nomad_vest], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000160501cf66ec7ab4d431c5e200000000000ec8ed0000000000000000, 0x00000000160501cf66ec7ab4d431c5e200000000000ec8ed0000000000000000 ],

["chasseur_auberge", "Chasseur", "Chasseur", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_leather_cap,itm_rawhide_coat,itm_woolen_hose], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000000e04310265638f28e2b2494200000000001c972c0000000000000000, 0x000000000e04310265638f28e2b2494200000000001c972c0000000000000000 ],

#pnj mort de froid auberge eneigee
["pnj_mort_df", "Client de l'auberge perdu", "Client de l'auberge perdu", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, no_scene, reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_arming_cap], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000001b0002cd34e975b2b476b922000000000005bcdb0000000000000000, 0x000000001b0002cd34e975b2b476b922000000000005bcdb0000000000000000 ],

############ cranes de fer ####################
# troupes camp crane de fer
["crane_de_fercamp_troop1", "Capitaine des Cranes de Fer", "Capitaine des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves, scn_camp_crane_defer|entry(2), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_shynbaulds,itm_steel_greaves,itm_agincourt], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000001b0002cd34e975b2b476b922000000000005bcdb0000000000000000, 0x000000001b0002cd34e975b2b476b922000000000005bcdb0000000000000000 ],
["crane_de_fercamp_troop2", "Garde des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["crane_de_fercamp_troop3", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(4), reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000001be0c00cb07156d6ad9ad281e00000000001eb8d50000000000000000, 0x00000001be0c00cb07156d6ad9ad281e00000000001eb8d50000000000000000 ],
["crane_de_fercamp_troop4", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(5), reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000002f109054386d69511172255300000000000e31630000000000000000, 0x000000002f109054386d69511172255300000000000e31630000000000000000 ],
["crane_de_fercamp_troop5", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(6), reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000251055cc46f44fd6e48e268500000000000e3d650000000000000000, 0x00000000251055cc46f44fd6e48e268500000000000e3d650000000000000000 ],
["crane_de_fercamp_troop6", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(7), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000002200909226ab4944a36e36f100000000000ed2940000000000000000, 0x000000002200909226ab4944a36e36f100000000000ed2940000000000000000 ],
["crane_de_fercamp_troop7", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["crane_de_fercamp_troop8", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000211055011772a9a6d3a936b6000000000012c8530000000000000000, 0x00000000211055011772a9a6d3a936b6000000000012c8530000000000000000 ],
["crane_de_fercamp_troop9", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["crane_de_fercamp_troop10", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["crane_de_fercamp_troop11", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000100905823a9b4ebd62b13cd300000000000de79c0000000000000000, 0x00000000100905823a9b4ebd62b13cd300000000000de79c0000000000000000 ],
["crane_de_fercamp_troop12", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000091105522893499b59da255b00000000001634e30000000000000000, 0x00000000091105522893499b59da255b00000000001634e30000000000000000 ],
["crane_de_fercamp_troop13", "Fantassin des Cranes de Fer", "Fantassin des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

#crane de fer mercenaire
["crane_de_fer_mercenaire", "Mercenaire de la compagnie des Cranes de Fer", "Mercenaires de la compagnie des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

["crane_de_fer_mercenaire_up1", "Epeiste de la compagnie des Cranes de Fer", "Epeiste de la compagnie des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_bayeux,itm_gaddhjalt,itm_caithness], def_attrib|level(23)|str_15|agi_16, wp(130), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["crane_de_fer_mercenaire_up2", "Maistre d'arme de la compagnie des Cranes de Fer", "Maistre d'arme de la compagnie des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_pigface_klappvisor,itm_klappvisier,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_duke,itm_baron,itm_count], def_attrib|level(23)|str_17|agi_17, wp(140), knows_common|knows_shield_1|knows_ironflesh_4|knows_power_strike_4|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

#bandits tueurs de caravanier rennes


["tueur_caravane_chef","Tueur de caravaniers","Tueur de caravaniers",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_convoi_weapons,[itm_klappvisier,itm_greathelm1,itm_mail_coif,itm_banded_armor,itm_coat_of_plates,itm_early_transitional_teu,itm_haubergeon,itm_cuir_bouilli,itm_plate_mittens,itm_mail_gauntlets,itm_mail_chausses,itm_splinted_greaves_nospurs,itm_mace_4,itm_bastard_sword_c,itm_sword_medieval_c_long,itm_heraldric_shieldredblack,itm_tab_shield_kite_c,itm_war_shieldeagle,],def_attrib2_b,wp(90),knows_warrior_basic2,0x000000002508a1c6165a2546ad6e181c00000000000d28a30000000000000000,0x000000002508a1c6165a2546ad6e181c00000000000d28a30000000000000000],

["tueur_caravane_1","écorcheur Archer","écorcheurs Archers",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_bandit,0,0,fac_convoi_weapons,[itm_mail_coif,itm_cuir_bouilli,itm_haubergeon,itm_leather_armor,itm_leather_gloves,itm_wrapping_boots,itm_woolen_hose,itm_short_bow,itm_hunting_bow,itm_arrows,itm_khergit_arrows,itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_sword_medieval_c_small,],def_attrib2_b,wp(90),knows_archer_basic,0x000000003f00614626db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f00814926db6db6db6db6db00000000001db6eb0000000000000000],

["tueur_caravane_2","écorcheur Vougier","écorcheur Vougiers",tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_convoi_weapons,[itm_mail_coif,itm_nasal_helmet,itm_mail_hauberk,itm_studded_leather_coat,itm_leather_jerkin,itm_plate_mittens,itm_mail_mittens,itm_mail_chausses,itm_mail_boots,itm_leather_boots,itm_voulge_long,itm_voulge_long,itm_jam_scorpion,itm_spetum_3,itm_voulge_long,],def_attrib2,wp(90),knows_warrior_basic,0x000000003f00900b26db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f01100b22db6db6db6db6db00000000001db6f30000000000000000],

["tueur_caravane_end","écorcheur","écorcheurs",tf_hero|tf_guarantee_boots|tf_guarantee_armor|tf_bandit,0,0,fac_convoi_weapons,[itm_klappvisier,itm_greathelm1,itm_mail_coif,itm_banded_armor,itm_coat_of_plates,itm_early_transitional_teu,itm_haubergeon,itm_cuir_bouilli,itm_plate_mittens,itm_mail_gauntlets,itm_mail_chausses,itm_splinted_greaves_nospurs,itm_mace_4,itm_bastard_sword_c,itm_sword_medieval_c_long,itm_heraldric_shieldredblack,itm_tab_shield_kite_c,itm_war_shieldeagle,],def_attrib2_b,wp(90),knows_warrior_basic2,0x000000000000000026db6db6db6db6db00000000001db6eb0000000000000000,0x000000003f00100626db6db6db6db6db00000000001db6eb0000000000000000],



#comte rue des dame
["rue_dame_comte", "Comte de Rennes", "Comte de Rennes", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(2), reserved, fac_neutral, [itm_woolen_hose,itm_nobleman_outfit_anglais,itm_bb_noble_hat], def_attrib|level(13), wp(90), knows_common|knows_ironflesh_2|knows_athletics_2, 0x000000002209251216dc30b6596dbc6c00000000000dca6d0000000000000000, 0x000000002209251216dc30b6596dbc6c00000000000dca6d0000000000000000 ],
["rue_dame_interlocuteur", "Invité du Comte", "Invité du Comte", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(3), reserved, fac_neutral, [itm_woolen_hose,itm_courtly_outfit], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000130c21cf14b24db2de6e34ab000000000015491a0000000000000000, 0x00000000130c21cf14b24db2de6e34ab000000000015491a0000000000000000 ],

#assassins potentiels  rue des dame
["rue_dame_assassin1", "Habitant du Bourg", "Habitant du Bourg", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(4), reserved, fac_neutral, [itm_woolen_hose,itm_coarse_tunic,itm_sword_medieval_a], def_attrib|level(23), wp(90), knows_common|knows_athletics_2, 0x00000000110cb30d475d9096f4a944f200000000000db8140000000000000000, 0x00000000110cb30d475d9096f4a944f200000000000db8140000000000000000 ],
["rue_dame_assassin2", "Habitant du Bourg", "Habitant du Bourg", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(5), reserved, fac_neutral, [itm_woolen_hose,itm_felt_hat,itm_fur_coat,itm_dagger_medievale], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000110cc24642abea94f391b92200000000000d226b0000000000000000, 0x00000000110cc24642abea94f391b92200000000000d226b0000000000000000 ],
["rue_dame_assassin3", "Habitant du Bourg", "Habitant du Bourg", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(6), reserved, fac_neutral, [itm_woolen_hose,itm_g_tw_shirt,itm_knife,itm_butchering_knife], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000000510a2c712ea92b92c9248ca000000000012c4b30000000000000000, 0x000000000510a2c712ea92b92c9248ca000000000012c4b30000000000000000 ],
["rue_dame_assassin4", "Habitant du Bourg", "Habitant du Bourg", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(7), reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_butchering_knife], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000001c0041d0456e6cc254ad469d00000000000e691b0000000000000000, 0x000000001c0041d0456e6cc254ad469d00000000000e691b0000000000000000 ],
["rue_dame_assassin5", "Habitant du Bourg", "Habitant du Bourg", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_rue_des_dames_rennes|entry(8), reserved, fac_neutral, [itm_woolen_hose,itm_shirt,itm_arming_cap,itm_knife], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000001b10c8285459a919514d9bb1400000000001d38640000000000000000, 0x00000001b10c8285459a919514d9bb1400000000001d38640000000000000000 ],


####
#troupes  gardes passage secret
["penthiv_garde_pass1", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],
["penthiv_garde_pass2", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],



#panthievre
["penthievre", "Etienne de Penthièvre", "Etienne de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_courtly_outfit,itm_woolen_hose,itm_dagger_medievale], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000003a0861d45d3471d4aa69c92200000000000534720000000000000000, 0x000000003a0861d45d3471d4aa69c92200000000000534720000000000000000 ],
["cour_pant_garde1", "Chevalier Breton a pied", "Chevaliers_Bretons_a_pied", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_complet_plates,itm_breton_complet_plates,itm_bb_armet2,itm_bb_greathelm_bp,itm_hourglass_gauntlets_ornate,itm_wisby_gauntlets_black,itm_wisby_gauntlets_black,itm_shynbaulds,itm_shynbaulds,itm_steel_greaves,itm_bardiche_5,itm_bardiche_5,itm_bardiche_3,itm_count,itm_duke,itm_duke,itm_duke], def_attrib|level(25), wp(120), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

#gardes cour chateau panthievre
["cour_pant_garde2", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],
["cour_pant_garde3", "Coutillier de Penthièvre", "Coutilliers Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_steel_greaves,itm_mail_boots,itm_klappvisier,itm_nasal_helmet,itm_chapel_de_fer,itm_klappvisier,itm_mail_gauntlets,itm_voulge_long,itm_2glaive,itm_3glaive,itm_6halberd], def_attrib|level(23), wp(150), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_4, 0x000000000010849036db6db6db6db6db00000000001db6db0000000000000000, vaegir_face_older_2 ],
["cour_pant_garde4", "Coutillier de Penthièvre", "Coutilliers Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_steel_greaves,itm_mail_boots,itm_klappvisier,itm_nasal_helmet,itm_chapel_de_fer,itm_klappvisier,itm_mail_gauntlets,itm_voulge_long,itm_2glaive,itm_3glaive,itm_6halberd], def_attrib|level(23), wp(150), knows_common|knows_ironflesh_2|knows_shield_1|knows_athletics_4, 0x00000001b700054c3715b719533d992100000000001db54f0000000000000000, vaegir_face_older_2 ],
["cour_pant_garde5", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],
["cour_pant_garde6", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],
["cour_pant_garde7", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_klappvisier,itm_klappvisier,itm_chapel_de_fer,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, vaegir_face_young_1, vaegir_face_older_2 ],

["cour_pant_garde8", "Garde de Penthièvre", "Gardes Bretons", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield, no_scene, reserved, fac_neutral, [itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_gauntlets,itm_splinted_greaves_nospurs,itm_splinted_greaves_nospurs,itm_heraldric_shieldblue3lys,itm_tab_shield_kite_c,itm_gaddhjalt,itm_knight], def_attrib|level(24), wp(130), knows_athletics_1|knows_shield_2|knows_ironflesh_1, 0x000000002f0cd18f449a724333ae176b000000000005968b0000000000000000, 0x000000002f0cd18f449a724333ae176b000000000005968b0000000000000000 ],
["cour_pant_garde9", "Irégulier", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_gaddhjalt,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000, 0x000000003e0c73cf367792569e85b59b00000000001da5610000000000000000 ],
["cour_pant_garde10", "Irégulier", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],
["cour_pant_garde11", "Irégulier", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_plate_mittens,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, 0x000000019e08728f2525b59723cda2e400000000001e23610000000000000000, 0x000000019e08728f2525b59723cda2e400000000001e23610000000000000000 ],
["cour_pant_garde12", "Irégulier", "Troupe de Penthièvre", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_bandit, no_scene, reserved, fac_commoners, [itm_mail_coif,itm_agincourt,itm_lui_knightaxeonehb,itm_mail_hauberk,itm_mail_gauntlets,itm_mail_boots,itm_leather_boots], def_attrib|level(9), wp(90), knows_common|knows_spotting_1|knows_athletics_2, bandit_face1, bandit_face2 ],


#cdf du camp de siege
["siege_crane_de_fercamp_troop1", "Sergent des Cranes de Fer", "Sergent des Cranes de Fer", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000100443cd36dcb646e1697ad400000000000dbb130000000000000000, 0x00000000100443cd36dcb646e1697ad400000000000dbb130000000000000000 ],
["siege_crane_de_fercamp_troop2", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["siege_crane_de_fercamp_troop3", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000000080804d018ebb2bc8c9ac9b500000000001e14cc0000000000000000, 0x00000000080804d018ebb2bc8c9ac9b500000000001e14cc0000000000000000 ],
["siege_crane_de_fercamp_troop4", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x000000003f10e2cc125b92cadcb6cc4400000000001d1d9b0000000000000000, 0x000000003f10e2cc125b92cadcb6cc4400000000001d1d9b0000000000000000 ],
["siege_crane_de_fercamp_troop5", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["siege_crane_de_fercamp_troop6", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, 0x00000001b410e5d45aa2c94964863ae100000000001d9ee40000000000000000, 0x00000001b410e5d45aa2c94964863ae100000000001d9ee40000000000000000 ],
["siege_crane_de_fercamp_troop7", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["siege_crane_de_fercamp_troop8", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],
["siege_crane_de_fercamp_troop9", "Soldat", "Soldat", tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield, scn_camp_crane_defer|entry(3), reserved, fac_neutral, [itm_corrazina_breton,itm_corrazina_breton,itm_klappvisier,itm_klappvisier,itm_tab_shield_heater_a,itm_tab_shield_heater_a,itm_shynbaulds,itm_splinted_greaves_nospurs,itm_steel_greaves,itm_wisby_gauntlets_black,itm_plate_mittens,itm_wisby_gauntlets_black,itm_hourglass_gauntlets,itm_agincourt,itm_1mace,itm_2hammer,itm_bastard_sword_a,itm_one_handed_war_axe_a,itm_bayeux,itm_knight], def_attrib|level(23)|str_14|agi_15, wp(120), knows_common|knows_shield_1|knows_ironflesh_2|knows_power_strike_3|knows_athletics_2, vaegir_face_young_1, vaegir_face_older_2 ],

#Unhappy Troops - Kham
["unhappy_french_troop","Dissatisfied Soldier","Infanteries lourdes Francaise",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_neutral,[itm_full_helm,itm_kettlehat2,itm_open_sallet,itm_coat_of_plates_f2,itm_coat_of_plates_f1,itm_shynbaulds,itm_steel_greaves,itm_shynbaulds,itm_steel_greaves,itm_bayeux,itm_one_handed_war_axe_a,itm_bastard_sword_a,itm_bastard_sword_b,],def_attrib2_b,wp_melee(105),knows_warrior_normal,swadian_face_middle_1,swadian_face_old_2],
["unhappy_english_troop","Dissatisfied Soldier","Infanteries lourdes Anglaise",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield|tf_english,0,0,fac_neutral,[itm_kettlehat1,itm_visored_sallet,itm_mail_coif,itm_open_sallet,itm_coat_of_plates_e1,itm_coat_of_plates_e2,itm_hourglass_gauntlets,itm_hourglass_gauntlets,itm_mail_chausses_e1,itm_splinted_greaves_e1,itm_one_handed_war_axe_a,itm_bastard_sword_a,itm_1mace,itm_one_handed_battle_axe_c,itm_tab_shield_small_round_c,itm_tab_shield_small_round_c,],def_attrib2_b,wp_melee(105),knows_warrior_normal,vaegir_face_young_1,0x000000000600004114db6d46db6db6db00000000001db6ec0000000000000000],
["unhappy_burgandy_troop","Dissatisfied Soldier","Piquiers long Bourguignons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield|tf_bourgignon,0,0,fac_neutral,[itm_nasal_helmet,itm_heraldic_churburg_13_tabard,itm_heraldic_churburg_13_tabard,itm_mail_gauntlets,itm_steel_greaves,itm_mail_boots,itm_voulge_long,itm_voulge_long,itm_voulge_long,],def_attrib2_b,wp(150),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_old_2],
["unhappy_breton_troop","Dissatisfied Soldier","Coutilliers Bretons",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_neutral,[itm_klappvisier,itm_nasal_helmet,itm_chapel_de_fer,itm_klappvisier,itm_breton_surcoat_over_mail,itm_breton_surcoat_over_mail,itm_mail_gauntlets,itm_steel_greaves,itm_mail_boots,itm_voulge_long,itm_2glaive,itm_3glaive,itm_6halberd,],def_attrib2_b,wp(150),knows_warrior_normal,vaegir_face_middle_2,vaegir_face_old_2],
######################## FIN ############################

#Lumos List Troop
["upgrades", "{!}Upgrade list", "{!}List of available upgrades", tf_hero, no_scene, reserved, fac_neutral,[],level(60),wp(800),knows_lord_1,merchant_face_1, merchant_face_2],  

]

###

#Troop upgrade declarations

# upgrade(troops,"farmer", "watchman")
# upgrade(troops,"townsman","watchman")
upgrade(troops,"watchman","caravan_guard")
upgrade2(troops,"caravan_guard","caravan_master","mercenary_horseman")
upgrade(troops,"city_guard","hired_blade")
# upgrade(troops,"mercenary_horseman","mercenary_cavalry")

upgrade2  (troops,"farmer","townsman","monk")
upgrade2  (troops,"townsman","lumberman","watchman")
upgrade2  (troops,"watchman","sentry","rider")
upgrade  (troops,"rider","master_rider")
#upgrade (troops,"mercenary","hired_blade")
upgrade2(troops,"caravan_guard","rider","master_rider")

upgrade(troops,"lumberman","executioner")

upgrade(troops,"priest","chaplain")
upgrade(troops,"monk","priest")
upgrade(troops,"executioner","torturer")
upgrade(troops,"sentry","city_guard")

upgrade(troops,"chaplain","bishop")
#upgrade(troops,"swiss_halberdier","swiss_veteran_halberdier")

upgrade(troops,"caravan_guard","caravan_master")


upgrade2(troops,"swadian_recruit","swadian_militia","french_javelinier")

upgrade2(troops,"french_javelinier","french_bowmen","swadian_crossbowman")

upgrade2(troops,"swadian_militia","swadian_footman","french_spearmen")

upgrade2(troops,"french_spearmen","french_hallebardier","french_pikemen")

upgrade2(troops,"swadian_footman","swadian_infantry","swadian_sergeant")
#OLD#upgrade2(troops,"swadian_footman","swadian_infantry","swadian_sergeant")
upgrade(troops,"swadian_skirmisher","swadian_crossbowman")

upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")

#new troops fr
upgrade(troops,"swadian_infantry","swadian_sergent")



upgrade2(troops,"swadian_man_at_arms","french_chevalier_bachelier_a_pied","swadian_knight")

upgrade2(troops,"swadian_man_at_arms","french_chevalier_bachelier_a_pied","swadian_knight")
upgrade(troops,"french_chevalier_bachelier_a_pied","french_chevalier_banneret_a_pied")
upgrade(troops,"french_chevalier_banneret_a_pied","french_chevalier_lancier_a_pied")
upgrade(troops,"swadian_knight","french_chevalier_banneret")
upgrade(troops,"french_chevalier_banneret","french_chevalier_lancier")

upgrade2(troops,"vaegir_recruit","vaegir_footman","vaegir_skirmisher")
upgrade2(troops,"vaegir_footman","vaegir_veteran","english_spearman")

upgrade2(troops,"vaegir_skirmisher","vaegir_archer","english_peasant_crossbowman")
###########
#upgrade(troops,"vaegir_recruit","english_dismounted_knight")
##########
#upgrade(troops,"english_arbalester","english_crossbowman")
upgrade2(troops,"english_spearman","english_pikeman","english_halberdier")

upgrade(troops,"vaegir_archer","vaegir_marksman")

upgrade2(troops,"vaegir_veteran","vaegir_guard","vaegir_infantry")

#OLD# upgrade2(troops,"vaegir_veteran","vaegir_guard","vaegir_infantry")
upgrade(troops,"english_pikeman","english_halberdier")
#upgrade(troops,"english_crossbowman","english_sharpshooter")

upgrade(troops,"vaegir_infantry","vaegir_sergent")

#new troops eng##################################################################################################



#English Noble Line
upgrade2(troops, "vaegir_horseman", "english_captain", "vaegir_knight"),
upgrade(troops, "vaegir_knight","english_heavy_knight",),
upgrade2(troops, "english_captain", "three_lions_guard", "english_longbowman_captain"),
upgrade(troops, "english_heavy_knight", "saint_georges_knight"),

#bourgignons
upgrade2(troops,"bourg_recruit","bourg_footman","bourg_skirmisher")
upgrade2(troops,"bourg_footman","bourg_veteran","bourg_spearman")

upgrade2(troops,"bourg_skirmisher","bourg_archer","bourg_peasant_crossbowman")

upgrade2(troops,"bourg_spearman","bourg_pikeman","bourg_halberdier")

upgrade(troops,"bourg_archer","bourg_marksman")

upgrade2(troops,"bourg_veteran","bourg_guard","bourg_infantry")



#new troops bourg##################################################################################################
upgrade(troops,"bourg_infantry","bourg_sergent")


#Burgandy Noble Line
upgrade2(troops, "bourg_horseman", "burgandy_captain", "bourg_knight"),
upgrade(troops, "bourg_knight","burgandy_heavy_knight",),
upgrade2(troops, "burgandy_captain", "burgandy_elite_guard", "burgandy_mounted_crossbowman_captain"),
upgrade(troops, "burgandy_heavy_knight", "burgandy_iron_knight"),


upgrade2(troops,"looter","mountain_bandit","forest_bandit")

#new tree connections
#upgrade(troops,"mountain_bandit","rhodok_tribesman")
upgrade(troops,"forest_bandit","mercenary_crossbowman")

upgrade(troops,"taiga_bandit","vaegir_recruit")
#upgrade(troops,"sea_raider","nord_recruit")
#upgrade(troops,"desert_bandit","sarranid_recruit")
#new tree connections ended

#upgrade2(troops,"bandit","brigand","mercenary_swordsman")
upgrade(troops,"manhunter","slave_driver")

#upgrade(troops,"forest_bandit","mercenary_crossbowman")

upgrade(troops,"slave_driver","slave_hunter")
upgrade(troops,"slave_hunter","slave_crusher")
upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman") #
upgrade(troops,"peasant_woman","follower_woman") #









#Bretagne


upgrade2(troops,"breton_recruit","breton_footman","breton_skirmisher")
upgrade2(troops,"breton_footman","breton_veteran","breton_spearman")

upgrade2(troops,"breton_skirmisher","breton_archer","breton_peasant_crossbowman")

upgrade2(troops,"breton_spearman","breton_pikeman","breton_halberdier")

upgrade(troops,"breton_archer","breton_marksman")

upgrade2(troops,"breton_veteran","breton_guard","breton_infantry")



#new troops bourg##################################################################################################
upgrade(troops,"breton_infantry","breton_sergent")



#Breton Noble Line
upgrade2(troops, "breton_horseman", "breton_noble", "breton_knight"),
upgrade(troops, "breton_knight","breton_heavy_knight",),
upgrade2(troops, "breton_noble", "breton_honour_guard", "breton_noble_swordsman"),
upgrade(troops, "breton_heavy_knight", "breton_hermine_knight"),



#upgrade cranes de fer
upgrade(troops,"crane_de_fer_mercenaire","crane_de_fer_mercenaire_up1")
upgrade(troops,"crane_de_fer_mercenaire_up1","crane_de_fer_mercenaire_up2")

























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































