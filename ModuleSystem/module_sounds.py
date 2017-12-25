from header_sounds import *
from compiler import *
sounds = [
 ("click", sf_2d|sf_vol_1,["drum_3.ogg"]),
 ("tutorial_1", sf_2d|sf_vol_7,["tutorial_1.ogg"]),
 ("tutorial_2", sf_2d|sf_vol_7,["tutorial_2.ogg"]),
 ("gong", sf_2d|sf_priority_9|sf_vol_7, ["s_cymbals.ogg"]),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_7, ["quest_completed.ogg"]),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_7, ["quest_succeeded.ogg"]),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, ["quest_concluded.ogg"]),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, ["quest_failed.ogg"]),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, ["quest_cancelled.ogg"]),
 ("rain",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["rain_1.ogg"]),
 ("money_received",sf_2d|sf_priority_10|sf_vol_6, ["coins_dropped_1.ogg"]),
 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, ["coins_dropped_2.ogg"]),
 ("sword_clash_1", 0,["sword_clank_metal_09.wav","sword_clank_metal_09b.wav","sword_clank_metal_10.wav","sword_clank_metal_10b.wav","sword_clank_metal_12.wav","sword_clank_metal_12b.wav","sword_clank_metal_13.wav","sword_clank_metal_13b.wav"]),
 ("sword_clash_2", 0,["s_swordClash2.wav"]),
 ("sword_clash_3", 0,["s_swordClash3.wav"]),
 ("sword_swing", sf_vol_8|sf_priority_2,["s_swordSwing.wav"]),
 ("footstep_grass", sf_vol_4|sf_priority_1,["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),
 ("footstep_wood", sf_vol_6|sf_priority_1,["footstep_wood_1.ogg","footstep_wood_2.ogg","footstep_wood_4.ogg"]),
# ("footstep_wood", sf_vol_3|sf_priority_1,["footstep_stone_1.ogg","footstep_stone_3.ogg","footstep_stone_4.ogg"]),
 ("footstep_water", sf_vol_4|sf_priority_3,["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg"]),
 ("footstep_horse",sf_priority_3|sf_vol_15, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_3|sf_vol_15, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
# ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
 ("footstep_horse_2b",sf_priority_3|sf_vol_15, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f",sf_priority_3|sf_vol_15, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b",sf_priority_3|sf_vol_15, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f",sf_priority_3|sf_vol_15, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b",sf_priority_3|sf_vol_15, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f",sf_priority_3|sf_vol_15, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b",sf_priority_3|sf_vol_15, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f",sf_priority_3|sf_vol_15, ["s_footstep_horse_5f.wav"]),
 ("jump_begin", sf_vol_7|sf_priority_9,["jump_begin.ogg"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_end.ogg"]),
 ("jump_begin_water", sf_vol_4|sf_priority_9,["jump_begin_water.ogg"]),
 ("jump_end_water", sf_vol_4|sf_priority_9,["jump_end_water.ogg"]),
 ("horse_jump_begin", sf_vol_12|sf_priority_9,["horse_jump_begin.ogg"]),
 ("horse_jump_end", sf_vol_12|sf_priority_9,["horse_jump_end.ogg"]),
 ("horse_jump_begin_water", sf_vol_6|sf_priority_9,["jump_begin_water.ogg"]),
 ("horse_jump_end_water", sf_vol_6|sf_priority_9,["jump_end_water.ogg"]), 

 ("release_bow",sf_vol_5, ["bow_shoot_09.wav"]),
 ("release_crossbow",sf_vol_7, ["crossbow_shoot_04.wav"]),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_7, ["throw_axe_1.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_1.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.ogg"]),

 ("reload_crossbow",sf_vol_3, ["reload_crossbow_1.ogg"]),
 ("reload_crossbow_continue",sf_vol_6, ["put_back_dagger.ogg"]),
 ("pull_bow",sf_vol_4, ["pull_bow_1.ogg"]),
 ("pull_arrow",sf_vol_5, ["pull_arrow.ogg"]),

 ("arrow_pass_by",0, ["arrow_pass_by_1.wav","arrow_pass_by_2.wav","arrow_pass_by_3.wav","arrow_pass_by_4.wav"]),
 ("bolt_pass_by",0, ["bolt_pass_by_1.ogg"]),
 ("javelin_pass_by",0, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9, ["stone_pass_by_1.ogg"]),
 ("axe_pass_by",0, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",0, ["knife_pass_by_1.ogg"]),
 ("bullet_pass_by",0, ["bullet_pass_02.wav"]),
 
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.wav","arrow_hit_ground_3.wav","incoming_bullet_hit_ground_1.wav"]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_7, ["arrow_hit_ground_2.ogg","arrow_hit_ground_3.ogg","incoming_bullet_hit_ground_1.wav"]),
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.wav"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_7,  ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["outgoing_arrow_hit_ground.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["incoming_javelin_hit_ground_1.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["incoming_stone_hit_ground_1.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_7, ["incoming_bullet_hit_ground_1.wav"]),


 ("draw_sword",sf_priority_4, ["draw_sword_03.wav"]),
 ("put_back_sword",sf_priority_4, ["put_away_sword_01.wav"]),
 ("draw_greatsword",sf_priority_4, ["draw_greatsword.wav"]),
 ("put_back_greatsword",sf_priority_4, ["put_back_sword.ogg"]),
 ("draw_axe",sf_priority_4, ["draw_mace.ogg"]),
 ("put_back_axe",sf_priority_4, ["put_back_to_holster.ogg"]),
 ("draw_greataxe",sf_priority_4, ["draw_greataxe.ogg"]),
 ("put_back_greataxe",sf_priority_4, ["put_back_to_leather.ogg"]),
 ("draw_spear",sf_priority_4, ["draw_spear.ogg"]),
 ("put_back_spear",sf_priority_4, ["put_back_to_leather.ogg"]),
 ("draw_crossbow",sf_priority_4, ["draw_crossbow_01.wav"]),
 ("put_back_crossbow",sf_priority_4, ["put_away_crossbow_01.wav"]),
 ("draw_revolver",sf_priority_4, ["draw_from_holster.ogg"]),
 ("put_back_revolver",sf_priority_4, ["put_back_to_holster.ogg"]),
 ("draw_dagger",sf_priority_4, ["draw_dagger.ogg"]),
 ("put_back_dagger",sf_priority_4, ["put_back_dagger.ogg"]),
 ("draw_bow",sf_priority_4, ["draw_bow.ogg"]),
 ("put_back_bow",sf_priority_4, ["put_back_to_holster.ogg"]),
 ("draw_shield",sf_priority_4|sf_vol_7, ["draw_shield.ogg"]),
 ("put_back_shield",sf_priority_4|sf_vol_7, ["put_back_shield.ogg"]),
 ("draw_other",sf_priority_4, ["draw_other.ogg"]),
 ("put_back_other",sf_priority_4, ["draw_other2.ogg"]),

 ("body_fall_small",sf_priority_6|sf_vol_10, ["body_fall_small_1.ogg","body_fall_small_2.ogg"]),
 ("body_fall_big",sf_priority_6|sf_vol_10, ["body_fall_1.ogg","body_fall_2.ogg","body_fall_3.ogg"]),
# ("body_fall_very_big",sf_priority_9|sf_vol_10, ["body_fall_very_big_1.ogg"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_body_fall_begin_1.ogg"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_body_fall_end_1.ogg","body_fall_2.ogg","body_fall_very_big_1.ogg"]),
 
## ("clang_metal",sf_priority_9, ["clang_metal_1.ogg","clang_metal_2.ogg","s_swordClash1.wav","s_swordClash2.wav","s_swordClash3.wav"]),
 ("hit_wood_wood",sf_priority_7|sf_vol_10, ["hit_wood_wood_1.ogg","hit_wood_wood_2.ogg","hit_wood_wood_3.ogg","hit_wood_wood_4.ogg","hit_wood_metal_4.ogg","hit_wood_metal_5.ogg","hit_wood_metal_6.ogg"]),#dummy
 ("hit_metal_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_3.wav","hit_metal_metal_7.wav",
                                              "hit_metal_metal_8.wav","hit_metal_metal_10.wav",
                                              "hit_metal_metal_4v.wav","hit_metal_metal_5v.wav",                  
                                              "clang_metal_1.wav","clang_metal_2.wav"]),
 ("hit_wood_metal",sf_priority_7|sf_vol_10, ["hit_metal_metal_1.wav","hit_metal_metal_2.wav","hit_wood_metal_7.wav"]),
# ("clang_metal", sf_priority_9,["sword_clank_metal_09.ogg","sword_clank_metal_10.ogg","sword_clank_metal_12.ogg","sword_clank_metal_13.ogg"]),
## ("shield_hit_cut",sf_priority_5, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg"]),
 ("shield_hit_wood_wood",sf_priority_7|sf_vol_10, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_metal_metal_01.wav","shield_metal_metal_03.wav","shield_metal_metal_04.wav","shield_metal_metal_07.wav"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_broken.ogg"]),
 ("man_hit",sf_priority_7|sf_vol_10, ["man_hit_5.ogg","man_hit_6.ogg","man_hit_7.ogg","man_hit_8.ogg","man_hit_9.ogg","man_hit_10.ogg","man_hit_11.ogg","man_hit_12.ogg","man_hit_13.ogg","man_hit_14.ogg","man_hit_15.ogg",
                                      "man_hit_17.ogg","man_hit_18.ogg","man_hit_19.ogg","man_hit_22.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg","man_hit_59.ogg"]),
 ("man_die",sf_priority_10,  ["man_die_01.wav","man_die_02.wav","man_die_03.wav","man_die_04.wav","man_die_05.wav","man_die_06.wav","man_die_07.wav","man_die_08.wav","man_die_09.wav","man_die_10.wav","man_die_11.wav","man_die_12.wav","man_die_13.wav","man_die_14.wav"]),# ["man_fall_1.ogg","man_fall_2.ogg","man_fall_3.ogg","man_fall_4.ogg"]),
 ("woman_hit",sf_priority_7, ["woman_hit_2.ogg","woman_hit_3.ogg",
                              "woman_hit_b_2.ogg","woman_hit_b_4.ogg","woman_hit_b_6.ogg","woman_hit_b_7.ogg","woman_hit_b_8.ogg",
                              "woman_hit_b_11.ogg","woman_hit_b_14.ogg","woman_hit_b_16.ogg"]),
 ("woman_die",sf_priority_10, ["woman_fall_1.ogg","woman_hit_b_5.ogg"]),
 ("woman_yell",sf_priority_10|sf_vol_10, ["woman_yell_1.ogg","woman_yell_2.ogg"]),
 ("hide",0, ["s_hide.wav"]),
 ("unhide",0, ["s_unhide.wav"]),
 ("neigh",0, ["horse_exterior_whinny_01.ogg","horse_exterior_whinny_02.ogg","horse_exterior_whinny_03.ogg","horse_exterior_whinny_04.ogg","horse_exterior_whinny_05.ogg","horse_whinny.ogg"]),
 ("gallop",sf_vol_3, ["horse_gallop_3.ogg","horse_gallop_4.ogg","horse_gallop_5.ogg"]),
 ("battle",sf_vol_4, ["battle.ogg"]),
# ("bow_shoot_player",sf_priority_10|sf_vol_10, ["bow_shoot_4.ogg"]),
# ("bow_shoot",sf_priority_4, ["bow_shoot_4.ogg"]),
# ("crossbow_shoot",sf_priority_4, ["bow_shoot_2.ogg"]),
 ("arrow_hit_body",sf_priority_4, ["arrow_hit_body_1.ogg","arrow_hit_body_2.ogg","arrow_hit_body_3.ogg"]),
 ("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_lo_dmg_1.ogg","sword_hit_lo_armor_lo_dmg_2.ogg","sword_hit_lo_armor_lo_dmg_3.ogg"]),
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_lo_armor_hi_dmg_1.ogg","sword_hit_lo_armor_hi_dmg_2.ogg","sword_hit_lo_armor_hi_dmg_3.ogg"]),
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_hit_high_armor_low_damage.ogg","metal_hit_high_armor_low_damage_2.ogg","metal_hit_high_armor_low_damage_3.ogg"]),
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["sword_hit_hi_armor_hi_dmg_1.ogg","sword_hit_hi_armor_hi_dmg_2.ogg","sword_hit_hi_armor_hi_dmg_3.ogg"]),
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_hit_low_1.ogg","blunt_hit_low_2.ogg","blunt_hit_low_3.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["wooden_hit_high_armor_low_damage.ogg","wooden_hit_high_armor_low_damage_2.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_hit_high_1.ogg","blunt_hit_high_2.ogg","blunt_hit_high_3.ogg"]),
 ("mp_arrow_hit_target",sf_2d|sf_priority_10|sf_vol_9, ["mp_arrow_hit_target.ogg"]),
 ("blunt_hit",sf_priority_5|sf_vol_9, ["punch_1.ogg","punch_4.ogg","punch_4.ogg","punch_5.ogg"]),
 ("player_hit_by_arrow",sf_priority_10|sf_vol_10, ["player_hit_by_arrow.ogg"]),
 ("pistol_shot",sf_priority_10|sf_vol_15, ["fl_pistol.wav"]),
 ("man_grunt",sf_priority_6|sf_vol_4, ["man_excercise_1.ogg","man_excercise_2.ogg","man_excercise_4.ogg"]),
 ("man_breath_hard",sf_priority_3|sf_vol_8, ["man_ugh_1.ogg","man_ugh_2.ogg","man_ugh_4.ogg","man_ugh_7.ogg","man_ugh_12.ogg","man_ugh_13.ogg","man_ugh_17.ogg"]),
 ("man_stun",sf_priority_3|sf_vol_9, ["man_stun_1.ogg"]),
 ("man_grunt_long",sf_priority_5|sf_vol_8, ["man_grunt_1.ogg","man_grunt_2.ogg","man_grunt_3.ogg","man_grunt_5.ogg","man_grunt_13.ogg","man_grunt_14.ogg"]),
 ("man_yell",sf_priority_6|sf_vol_10, ["man_yell_4.ogg","man_yell_4_2.ogg","man_yell_7.ogg","man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","man_yell_15.ogg","man_yell_16.ogg","man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                        "man_yell_b_18.ogg","man_yell_22.ogg", "man_yell_c_20.ogg",  "man_yell_b_22.ogg", "man_yell_b_23.ogg"]),
## not adequate, removed: "man_yell_b_21.ogg","man_yell_b_22.ogg","man_yell_b_23.ogg"]),
#TODONOW:
 #anglais
 ("eng_man_yell",sf_priority_6|sf_vol_10, ["en_man_yell_4.ogg","man_yell_4_2.ogg","en_man_yell_7.ogg","en_man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","en_man_yell_15.ogg","man_yell_16.ogg","en_man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                     "man_yell_b_18.ogg","man_yell_22.ogg", "en_man_yell_c_20.ogg","en_man_warc.ogg","en_man_warc_2.ogg"]),
 ("eng_man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","en_man_victory_4.ogg","man_victory_5.ogg","en_man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","en_man_victory_54.ogg","en_man_victory_56.ogg","man_victory_57.ogg","man_victory_71.ogg","en_man_victory_x.ogg"]),
#bourgignons
 ("bourg_man_yell",sf_priority_6|sf_vol_10, ["brg_man_yell_4.ogg","man_yell_4_2.ogg","brg_man_yell_7.ogg","brg_man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","brg_man_yell_15.ogg","man_yell_16.ogg","brg_man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                        "man_yell_b_18.ogg","man_yell_22.ogg", "brg_man_yell_c_20.ogg"]),
 ("bourg_man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","brg_man_victory_4.ogg","man_victory_5.ogg","brg_man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_57.ogg","man_victory_71.ogg"]),
#bandits
 ("bandit_man_yell",sf_priority_6|sf_vol_10, ["band_man_yell_4.ogg","man_yell_4_2.ogg","band_man_yell_7.ogg","band_man_yell_9.ogg","man_yell_11.ogg","man_yell_13.ogg","band_man_yell_15.ogg","man_yell_16.ogg","band_man_yell_17.ogg","man_yell_20.ogg","man_shortyell_4.ogg","man_shortyell_5.ogg","man_shortyell_6.ogg","man_shortyell_9.ogg","man_shortyell_11.ogg","man_shortyell_11b.ogg",
                        "man_yell_b_18.ogg","man_yell_22.ogg", "band_man_yell_c_20.ogg"]),
 ("bandit_man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","band_man_victory_4.ogg","man_victory_5.ogg","band_man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","band_man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"]),

 ("man_warcry",sf_priority_6, ["man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("jeanne_yell",sf_priority_10|sf_vol_10, ["woman_yell_1.ogg","woman_yell_2.ogg","jeanne_cry.ogg","jeanne_cry_2.ogg","jeanne_cry_3.ogg","jeanne_cry_4.ogg"]),


 ("encounter_looters",sf_2d|sf_vol_8, ["encounter_river_pirates_5.ogg","encounter_river_pirates_6.ogg","encounter_river_pirates_9.ogg","encounter_river_pirates_10.ogg","encounter_river_pirates_4.ogg"]),

 ("encounter_bandits",sf_2d|sf_vol_8, ["encounter_bandit_2.ogg","encounter_bandit_9.ogg","encounter_bandit_12.ogg","encounter_bandit_13.ogg","encounter_bandit_15.ogg","encounter_bandit_16.ogg","encounter_bandit_10.ogg",]),
 ("encounter_farmers",sf_2d|sf_vol_8, ["encounter_farmer_2.ogg","encounter_farmer_5.ogg","encounter_farmer_7.ogg","encounter_farmer_9.ogg"]),
 ("encounter_sea_raiders",sf_2d|sf_vol_8, ["encounter_sea_raider_5.ogg","encounter_sea_raider_9.ogg","encounter_sea_raider_9b.ogg","encounter_sea_raider_10.ogg"]),
 ("encounter_steppe_bandits",sf_2d|sf_vol_8, ["encounter_steppe_bandit_3.ogg","encounter_steppe_bandit_3b.ogg","encounter_steppe_bandit_8.ogg","encounter_steppe_bandit_10.ogg","encounter_steppe_bandit_12.ogg"]),
 ("encounter_nobleman",sf_2d|sf_vol_8, ["encounter_nobleman_1.ogg"]),
 ("encounter_vaegirs_ally",sf_2d|sf_vol_8, ["encounter_vaegirs_ally.ogg","encounter_vaegirs_ally_2.ogg"]),
 ("encountmanbourg_man_yell_excercisman_victoryeng_man_victorye_1er_vaegirs_neutral",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("encounter_vaegirs_enemy",sf_2d|sf_vol_8, ["encounter_vaegirs_neutral.ogg","encounter_vaegirs_neutral_2.ogg","encounter_vaegirs_neutral_3.ogg","encounter_vaegirs_neutral_4.ogg"]),
 ("sneak_town_halt",sf_2d, ["sneak_halt_1.ogg","sneak_halt_2.ogg"]),
 ("horse_walk",sf_priority_3|sf_vol_12, ["horse_walk_1.ogg","horse_walk_2.ogg","horse_walk_3.ogg","horse_walk_4.ogg"]),
 ("horse_trot",sf_priority_3|sf_vol_13, ["horse_trot_1.ogg","horse_trot_2.ogg","horse_trot_3.ogg","horse_trot_4.ogg"]),
 ("horse_canter",sf_priority_3|sf_vol_14, ["horse_canter_1.ogg","horse_canter_2.ogg","horse_canter_3.ogg","horse_canter_4.ogg"]),
 ("horse_gallop",sf_priority_3|sf_vol_15, ["horse_gallop_6.ogg","horse_gallop_7.ogg","horse_gallop_8.ogg","horse_gallop_9.ogg"]),
 ("horse_breath",sf_priority_3|sf_priority_9|sf_vol_10, ["horse_breath_4.ogg","horse_breath_5.ogg","horse_breath_6.ogg","horse_breath_7.ogg"]),
 ("horse_snort",sf_priority_5|sf_vol_10, ["horse_snort_1.ogg","horse_snort_2.ogg","horse_snort_3.ogg","horse_snort_4.ogg","horse_snort_5.ogg"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.ogg","horse_whinny-2.ogg"]),
 ("block_fist",0, ["block_fist_3.ogg","block_fist_4.ogg"]),
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_weak",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_hit_cut_strong",sf_priority_5|sf_vol_10, ["man_hit_13.ogg","man_hit_29.ogg","man_hit_32.ogg","man_hit_47.ogg","man_hit_57.ogg"]),
 ("man_victory",sf_priority_5|sf_vol_10, ["man_victory_3.ogg","man_victory_4.ogg","man_victory_5.ogg","man_victory_8.ogg","man_victory_15.ogg","man_victory_49.ogg","man_victory_52.ogg","man_victory_54.ogg","man_victory_57.ogg","man_victory_71.ogg"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("dummy_hit",sf_priority_9, ["shield_hit_cut_3.ogg","shield_hit_cut_5.ogg"]),
 ("dummy_destroyed",sf_priority_9, ["shield_broken.ogg"]),
 ("gourd_destroyed",sf_priority_9, ["shield_broken.ogg"]),#TODO
 ("cow_moo", sf_2d|sf_priority_9|sf_vol_8, ["cow_moo_1.ogg"]),
 ("cow_slaughter", sf_2d|sf_priority_9|sf_vol_8, ["cow_slaughter.ogg"]),
 ("distant_dog_bark", sf_2d|sf_priority_8|sf_vol_8, ["d_dog1.ogg","d_dog2.ogg","d_dog3.ogg","d_dog7.ogg"]),
 ("distant_owl", sf_2d|sf_priority_8|sf_vol_9, ["d_owl2.ogg","d_owl3.ogg","d_owl4.ogg"]),
 ("distant_chicken", sf_2d|sf_priority_8|sf_vol_8, ["d_chicken1.ogg","d_chicken2.ogg"]),
 ("distant_carpenter", sf_2d|sf_priority_8|sf_vol_3, ["d_carpenter1.ogg","d_saw_short3.ogg"]),
 ("distant_blacksmith", sf_2d|sf_priority_8|sf_vol_4, ["d_blacksmith2.ogg"]),
 ("arena_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["arena_loop11.ogg"]),
 ("town_ambiance", sf_2d|sf_priority_8|sf_vol_3|sf_looping, ["town_loop_3.ogg"]),
  ("taverne_ambiance", sf_2d|sf_priority_8|sf_vol_10|sf_looping, ["taverne_loop.ogg"]),
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.ogg"]),
 ("your_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_taken.ogg"]),
 ("enemy_flag_taken", sf_2d|sf_priority_10|sf_vol_10, ["enemy_flag_taken.ogg"]),
 ("flag_returned", sf_2d|sf_priority_10|sf_vol_10, ["your_flag_returned.ogg"]),
 ("team_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["you_scored_a_point.ogg"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_10|sf_vol_10, ["enemy_scored_a_point.ogg"]),
 ("chant_1", sf_2d|sf_priority_9|sf_vol_8, ["chant_1_1.ogg"]),
 ("chant_2", sf_2d|sf_priority_9|sf_vol_8, ["chant_2_1.ogg"]),
 ("sex_1a", sf_2d|sf_priority_9|sf_vol_8, ["sex_1.ogg"]),
 ("sex_2a", sf_2d|sf_priority_9|sf_vol_8, ["sex_2.ogg"]),
 ("sex_3a", sf_2d|sf_priority_9|sf_vol_8, ["sex_3.ogg"]),
 ("nuit_1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["nuit_1_1.ogg"]),
 ("nuit_ville1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["nuit_ville1_1.ogg"]),
 ("ville_sons1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["ville_sons1_1.ogg"]),
 ("foret_1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["foret_1_1.ogg"]),
 ("vent1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["vent1_1.ogg"]),
 ("campagn1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["campagn1_1.ogg"]),
 ("plaines1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["plaines1_1.ogg"]),
 ("ecuries1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["ecuries1_1.ogg"]),
 ("abbaye1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["abbaye1_1.ogg"]),
 ("ville_sons2",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["ville_sons2_2.ogg"]),
 ("traing_equitation1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["traing_equitation1_1.ogg"]),
 ("riviere1",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["riviere1_1.ogg"]),
 ("benir1",sf_2d|sf_priority_10|sf_vol_4, ["benir1_1.ogg"]),
 ("soin1",sf_2d|sf_priority_10|sf_vol_4, ["soin1_1.ogg"]),
 ("soin2",sf_2d|sf_priority_10|sf_vol_4, ["soin2_2.ogg"]),
 ("training1",sf_2d|sf_priority_10|sf_vol_4, ["training1_1.ogg"]),
 ("page_generique",sf_2d|sf_priority_10|sf_vol_4, ["page_generique_1.ogg"]),
 ("music_fleuve",sf_2d|sf_priority_10|sf_vol_4, ["mount_and_blade_title.ogg"]), 
 ("pistol_shot_2",sf_priority_10|sf_vol_15, ["fl_pistol_arquebuse.wav", "feu.wav"]),
 ("adrenaline_generique1",sf_priority_10|sf_vol_10, ["adrenaline_generique1_1.wav"]),
 ("chrono_cry_pirates",sf_priority_10|sf_vol_10, ["chrono_cry1.ogg"]),
 ("chrono_cry_slwar1",sf_priority_10|sf_vol_10, ["chrono_cry2.ogg"]),
 ("chrono_cry_slwar2",sf_priority_10|sf_vol_10, ["chrono_cry3.ogg"]),
 ("chrono_cry_alerte",sf_priority_10|sf_vol_10, ["chrono_cry4.ogg"]),
 ("craft_camp",sf_priority_10|sf_vol_10, ["forge_craft_generique.wav"]),
 ("start_quest",sf_priority_10|sf_vol_10, ["quest_start.ogg"]),
 ("cor",sf_priority_10|sf_vol_10, ["cor_signal.wav"]), 
 ("cata",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["catacomb_1.ogg"]),
 ("death",sf_priority_10|sf_vol_10, ["death_end.ogg"]),
 ("cruch",sf_priority_10|sf_vol_10, ["cruche.ogg"]),
 ("orleans_loop",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["orleans_war.wav"]), 
 ("greet_jeanne",sf_priority_10|sf_vol_10, ["greeting_jeanne.ogg"]),
 ("start_orljeanne",sf_priority_10|sf_vol_10, ["speech_jhoan2.ogg"]), 
 ("boum_bombard",sf_priority_10|sf_vol_15, ["bombarde_orleans.ogg"]),
 ("jspeech_bridgeorl",sf_priority_10|sf_vol_10, ["jspeech_bridg.ogg"]),
 ("final_battl",sf_priority_10|sf_vol_10, ["batttend.ogg"]),
 ("food_camp",sf_priority_10|sf_vol_10, ["food_c.wav"]),
 ###### jeux des 
 ("dices",sf_priority_10|sf_vol_10, ["dices1.wav"]), 
 ("dices_2",sf_priority_10|sf_vol_10, ["dices2.wav"]),
 ("drunk_concourt",sf_priority_10|sf_vol_10, ["drunk_fight.wav"]),
 ("drunk_ko",sf_priority_10|sf_vol_10, ["vomi.wav"]),  


 ("tournament_play",sf_2d|sf_priority_10|sf_vol_4|sf_looping, ["tournament_play.wav"]), # ou ogg

 ("tournois_ambiance_fete",sf_priority_10|sf_vol_10, ["tournois_ambiance_fete.wav"]),  

 ("bravo",sf_priority_10|sf_vol_10, ["bravo.wav"]),  
 ("hues",sf_priority_10|sf_vol_10, ["hues.wav"]),
 
 ("mouettes",sf_2d|sf_priority_10|sf_vol_9|sf_looping, ["mouettes.wav"]),


 ("ligne",sf_priority_10|sf_vol_10, ["rangs.wav","bataille1.wav","bataille2.wav"]), 
 
#sound box 
 ("sb_camps_1",sf_priority_6|sf_vol_10, ["camps_1.wav","camps_2.wav","etern.wav","renif.wav"]),
 ("sb_camps_tent",sf_priority_6|sf_vol_10, ["sante.wav","morts.wav","etern.wav","merde.wav","quand.wav","angl.wav","des.wav","renif.wav"]),


#greetings
 
 ("capitaine",sf_priority_10|sf_vol_10, ["capitaine_1.wav","capitaine_2.wav","capitaine_3.wav","capitaine_6.wav","capitaine_7.wav","capitaine_8.wav"]), 

 ("lords_greetings_debut",sf_priority_10|sf_vol_10, ["lord_first_1.wav","lord_first_2.wav","lord_first_3.wav","messire_2.wav"]), 
 ("jeanne_greetings_debut",sf_priority_10|sf_vol_10, ["un_chevaliet.wav"]),
 ("charles_greetings_debut",sf_priority_10|sf_vol_10, ["greetings_charles7_debut.wav"]),
 ("henry_greetings_debut",sf_priority_10|sf_vol_10, ["greeting_henry.wav"]),
 ("duc_greetings_debut",sf_priority_10|sf_vol_10, ["un_bourguignon.wav"]),
 ("jeanne_gueroyer",sf_priority_10|sf_vol_10, ["gueroyer_jeanne.wav"]),
 ("jeanne_epee",sf_priority_10|sf_vol_10, ["messire_femme_1.wav"]),
 ("lords_greetings",sf_priority_10|sf_vol_10, ["lords_encounter_s.wav","messire_2.wav","encounter_lord1.ogg","encounter_lord2.ogg","encounter_lord3.ogg","encounter_lord4.ogg","encounter_lord5.ogg","encounter_lord6.ogg"]), 
 ("jeanne_greetings",sf_priority_10|sf_vol_10, ["messire_femme_1.wav"]),
 ("enemi_greetings",sf_priority_10|sf_vol_10, ["enemi.wav,","enemi_2.wav","enemi_3.wav","enemi_4.wav"]),
#ribaudes
 ("ribaudes",sf_priority_10|sf_vol_10, ["ribaude_1.wav","ribaude_2.wav","ribaude_3.wav"]),
 ("taverniers_h",sf_priority_10|sf_vol_10, ["tavernier_homme.wav","tavernier_homme_2.wav","tavernier_homme_3.wav"]),
 ("taverniers_f",sf_priority_10|sf_vol_10, ["tavernier_femme.wav","tavernier_femme2.wav","messire_femme_3.wav","tavernier_femme3.wav"]),
# maitres guild
 ("maitre_guild",sf_priority_10|sf_vol_10, ["maitre_guild.wav","maitre_guild_2.wav"]),

# rebels
 ("rebels_greetings",sf_priority_10|sf_vol_10, ["force2.wav","compagnon.wav","rebel.wav","rebel3.wav"]),
 ("alt",sf_priority_10|sf_vol_10, ["halte.wav"]), 
# sans lys
 ("sanslys_greetings",sf_priority_10|sf_vol_10, ["sanslys.wav","sanslys2.wav","gloire_sl_2.wav"]),
 ("sanslys_taverne",sf_priority_10|sf_vol_10, ["oui.wav","veux2.wav","veux.wav","quois2.wav"]),


 #continuer: rebels, licorne,grossiste,vendeur armes armures (hommes/femmes) 

 #marchands
# resources
 ("marchands_res_greetings",sf_priority_10|sf_vol_10, ["tavernier_homme.wav,"]), 
# ("windmill_turning",sf_2d|sf_priority_10|sf_vol_6|sf_looping, ["windmill_t.ogg"]),
 ("windwill",sf_2d|sf_priority_9|sf_vol_8|sf_looping, ["windmill.wav"]),
 ("mer",sf_2d|sf_priority_9|sf_vol_6|sf_looping, ["sea.wav"]),

 ("feu_camp",sf_2d|sf_priority_9|sf_vol_9|sf_looping, ["feu_camp.wav"]),

 ("monfrere",sf_priority_10|sf_vol_10, ["monfreres.wav"]),
 ("monfrere2",sf_priority_10|sf_vol_10, ["monfrere2s.wav"]),
 ("decouverte",sf_priority_10|sf_vol_10, ["decouvertes.wav"]),
 ("eternue",sf_priority_10|sf_vol_10, ["etern.wav"]),
 ("passage_secret",sf_priority_10|sf_vol_10, ["pass_secret.wav"]),
#
 #("musique_intro_tournois",sf_priority_10|sf_vol_10, ["ambiancejoute_loop.wav"]),
#
  ("public_loop",sf_2d|sf_priority_10|sf_vol_8|sf_looping, ["ambiancejoute_loop.wav"]),
 
# ("defaite_joute",sf_priority_10|sf_vol_10, ["defaite1.wav,defaite2.wav"]),
 ("mort_cheval_joute",sf_priority_10|sf_vol_10, ["hues1.wav","hues2.wav"]),
 ("trompette_tournois",sf_priority_10|sf_vol_10, ["trompette.wav"]),
 ("tournois_remporte",sf_priority_10|sf_vol_10, ["victoire_tournoisfin.wav"]),
# ("victoire_manche",sf_priority_10|sf_vol_10, ["victoire1.wav,victoire2.wav,victoire3.wav,victoire4.wav,victoire5.wav"]),
 ("victoire_manche",sf_priority_10|sf_vol_10, ["victoire_3.wav","victoire_5.wav","victoire4.wav","victoire2.wav"]),
 ("defaite_joute",sf_priority_10|sf_vol_10, ["defaite1.wav","defaite2.wav"]),
 ("porte",sf_priority_10|sf_vol_10, ["porte1.wav","porte2.wav"]),

 ("auberge",sf_priority_10|sf_vol_10, ["auberge_1.wav","auberge_2.wav","auberge_3.wav","auberge_4.wav","auberge_5.wav","auberge_6.wav","auberge_7.wav","auberge_8.wav","auberge_9.wav","auberge_10.wav","auberge_11.wav","auberge_12.wav","auberge_13.wav","auberge_14.wav","auberge_15.wav","auberge_16.wav","auberge_17.wav","auberge_18.wav","auberge_19.wav","auberge_20.wav","auberge_21.wav","auberge_22.wav","auberge_23.wav","auberge_24.wav","auberge_25.wav","auberge_26.wav","auberge_27.wav","auberge_28.wav","auberge_29.wav","auberge_30.wav"]),
  ("auberge_ambiance_sounds",sf_2d|sf_priority_10|sf_vol_8|sf_looping, ["auberge_loop.wav"]),
 ("porte_fermee",sf_priority_10|sf_vol_10, ["porte_fermee.wav"]),

  ("bruit_pas",sf_priority_10|sf_vol_10, ["bruit_pas.wav"]),
   ("ambiance_pnj",sf_priority_10|sf_vol_10, ["camps_1.wav","etern.wav","renif.wav","veux2.wav","quois2.wav","oui.wav"]),

  ("decouvertes",sf_priority_10|sf_vol_10, ["decouvertes.wav"]),

("dedal_tavern_lute",	sf_priority_6|sf_vol_5|sf_looping, ["dedal_tavern_lute_1.ogg","dedal_tavern_lute_2.ogg","dedal_tavern_lute_3.ogg"]),
 ("dedal_tavern_lyre",	sf_priority_6|sf_vol_6|sf_looping, ["dedal_tavern_lyre_1.ogg","dedal_tavern_lyre_2.ogg","dedal_tavern_lyre_3.ogg"]),
  ("henissement",sf_priority_10|sf_vol_10, ["henissement.wav"]),


 ("cascade",sf_2d|sf_priority_9|sf_vol_8|sf_looping, ["cascade.wav"]),
  ("intro_broceliand",sf_2d|sf_priority_10|sf_vol_8|sf_looping, ["intro_foret.wav"]),
  ("helm_down",sf_priority_8|sf_vol_10, ["helmet.wav"]),
  ("helmet_open",sf_priority_8|sf_vol_10, ["helmet_open.wav"]),
 

 ("ambiance_camp_cdf",sf_2d|sf_priority_9|sf_vol_8|sf_looping, ["ambiance_camp_cdf.wav"]),
  ("ambiance_ravin",sf_2d|sf_priority_9|sf_vol_8|sf_looping, ["ambiance_ravin.wav"]),
 
 ]
