from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *
from compiler import *
###################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

scenes = [
  ("random_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[]),
  
  ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
#######
 
  ("water1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563c00691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain5"),
  ("water2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230068563c00691a400003efe000061bb0000741e",
    [],[], "outer_terrain_plain7"),
  ("water3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000023003c863c00691a400003efe0000120100001af3",
    [],[], "outer_terrain_plain5"),
  ("water4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230000b63c00691a400003efe00003ab7000073d6",
    [],[], "outer_terrain_plain5"),
  ("water5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230010563c00691a400003efe00001e460000122c",
    [],[], "outer_terrain_plain9"),
  ("water6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230010563c00691a400003efe000016c10000450f",
    [],[], "outer_terrain_plain5"),  
#######
##The Bowman's Improved Battle Scenes Begin:
  ("random_scene_steppe_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000002c600563000d234800006fb100000c280000193e",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000002c600563000d23480000163d00000c2800000d67",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000020800563000d23480000163d00000c2800000a91",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000020800563000d234800006b1f00000c2800004a0a",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000022e00563000d234800006b1f00000c2800006b90",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000022e00be3000d234800007d4c00000c28000031f4",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000022e00be3000d23480000012800000c2800000dc4",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000002c6008e3000d234800002ada00000c2800000eb7",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000002c6008e3000d234800003c6e00000c2800006676",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000027c008e3000d234800003c6e00000c2800006ba7",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe_custom_11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000212008e3800d2348000011ba000067d500000c9c",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034400925000d23480000659c00004d18000006c9",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000033a01221000d23480000511700001f5300004fd2",
    [],[], "outer_terrain_plain2"),
  ("random_scene_plain_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000035e00f21000d23480000511700001f530000785e",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000035e00f21000d23480000413900001f530000785e",
    [],[], "outer_terrain_plain4"),
  ("random_scene_plain_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000035e00715000d23480000662800001f5300007ea6",
    [],[], "outer_terrain_plain5"),
  ("random_scene_plain_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000035e00715000d234800004b0600001f5300001905",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c600715000d23480000567b00001f5300001905",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6009a7000d2348000068ab00001f530000639d",
    [],[], "outer_terrain_plain8"),
  ("random_scene_plain_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6009a7000d23480000076d00001f5300001ac2",
    [],[], "outer_terrain_plain9"),
  ("random_scene_plain_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000368009a7000d23480000585500001f5300005855",
    [],[], "outer_terrain_plain10"),
  ("random_scene_plain_custom_11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000030e009a7000d234800001f5800001f5300001b9f",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain_custom_12",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000346009a7000d234800006c9200001f5300006421",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_13",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000346009a7000d2348000064d200001f5300005603",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_14",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034600ca0000d2348000066cf00001f530000638a",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_15",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034600ca0000d234800001bf700001f530000217f",
    [],[], "outer_terrain_plain2"),
  ("random_scene_plain_custom_16",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034600ca0000d2348000052f100001f530000626d",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_custom_17",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034600ca0000d23480000148400001f53000064ca",
    [],[], "outer_terrain_plain4"),
  ("random_scene_plain_custom_18",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000038800ca0000d2348000079b800001f5300004656",
    [],[], "outer_terrain_plain5"),
  ("random_scene_plain_custom_19",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000036e00820000d2348000079b800001f53000021e8",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_custom_20",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000034e00820000d2348000079b800001f5300000f0c",
    [],[], "outer_terrain_plain7"),
  ("random_scene_snow_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000468005e3000d234800004470000067d500004470",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000041c005e3000d234800004470000067d500002885",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000426005e3000d234800004470000067d5000055c9",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000426005e3000d23480000057f000067d500007ecc",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000043e005e3000d23480000057f000067d50000660b",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000004c6005e3800d23480000057f0000403d00004af3",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000044e005e3800d23480000057f000000db00005e1b",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000044e005e3000d23480000590a000000db0000455e",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000482005e3000d23480000590a000000db0000229b",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000004c600563000d23480000590a000000db00006bd5",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_custom_11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000004c600ae3000d23480000590a000000db00006e4b",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c601063000d2348000052d4000067d500007b2d",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c6009e3000d2348000052d4000067d500006373",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600563000d2348000052d4000067d5000029c1",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600563000d2348000052d4000067d5000070e2",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600563000d2348000052d4000067d500004f42",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600963000d2348000052d4000067d500007cc4",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600963000d2348000052d4000067d5000070e2",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600963000d2348000052d4000067d50000474c",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600963000d2348000052d4000067d5000031b4",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000005c600963000d2348000052d4000067d500005ec1",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ac600563000d234800000692000000db00002d7c",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ac600863000d234800000692000000db000011cf",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ac600563000d234800000572000000db0000773a",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ac600563000d2348000060bd000000db00006d4c",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ac600563800d2348000060bd00005053000043dc",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c600715000d23480000499200001f530000639d",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_forest_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ba018a63000d23480000163100005cd6000004ad",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain_forest_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000ba018a63000d234800004a3e00005cd600001fcc",
    [],[], "outer_terrain_plain9"),
  ("random_scene_plain_forest_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc618a63000d234800004a3e00005cd600005be9",
    [],[], "copy_outer_terrain_plain5"),
  ("random_scene_plain_forest_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc618a63000d234800004a3e00005cd6000045cc",
    [],[], "forest_wall"),
  ("random_scene_plain_forest_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600e63000d234800004a3e00005cd600003541",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_forest_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600e63000d2348000023f400005cd600006475",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain_forest_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600e63000d2348000023f400005cd600001e1d",
    [],[], "outer_terrain_plain9"),
  ("random_scene_plain_forest_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600963000d2348000054f800005cd6000000d6",
    [],[], "copy_outer_terrain_plain3"),
  ("random_scene_plain_forest_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600563000d234800000d1400000c2800006616",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_forest_custom_11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000bc600563800d23480000769000000c280000193e",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain_mountain_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6013e3000d234800004d6a00007a9000000f49",
    [],[], "outer_terrain_plain9"),
  ("random_scene_plain_mountain_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000344013e3000d2348000054c300007a9000000c96",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000344013e3000d234800005d5900007a90000064f6",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000390251e3000d23480000197500007a90000064f6",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000390013e3000d23480000197500007a900000075b",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6013e3000d23480000197500007a9000006f62",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000372013e3000d23480000731200007a9000003311",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003a4013e3000d23480000731200007a90000030e6",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6a4fe3000d23480000731200007a90000013df",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_mountain_custom_10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000003c6d4763000d23480000731200007a9000001d00",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_river_custom_1",sf_generate|sf_auto_entry_points|sf_muddy_water,"none", "none", (0,0),(240,240),-0.5,"0x0000000034e00557800d23480000127b00001f5300006aee",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_river_custom_2",sf_generate|sf_auto_entry_points|sf_muddy_water,"none", "none", (0,0),(240,240),-0.5,"0x0000000034e005bf800d23480000048e00004ae900005db3",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_river_custom_3",sf_generate|sf_auto_entry_points|sf_muddy_water,"none", "none", (0,0),(240,240),-0.5,"0x0000000034e00633800d234800004d7800007a9000005db3",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_river_custom_4",sf_generate|sf_auto_entry_points|sf_muddy_water,"none", "none", (0,0),(240,240),-0.5,"0x0000000034e00633800d234800007d9100007a9000001a3b",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_river_custom_5",sf_generate|sf_auto_entry_points|sf_muddy_water,"none", "none", (0,0),(240,240),-0.5,"0x000000003c600663800d234800004d6a00007a9000007359",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000cc600ae3000d23480000590a000000db00006e4b",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000cc600563000d2348000037cc000000db000045f6",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000cc600563000d234800001ea3000000db000027bb",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000cc600563000d234800005cfa000000db000017fb",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow_forest_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000cc600563000d234800007432000000db00002d7c",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest_custom_1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000d12008e3000d2348000011ba000067d500000c9c",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_forest_custom_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000dc600663000d234800000fdb000067d500007142",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_forest_custom_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000dc600663000d234800004132000067d500003697",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_forest_custom_4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000dc600663000d234800002da0000067d500000fe5",
    [],[], "outer_terrain_plain"),
  ("random_scene_desert_forest_custom_5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000dc600a63000d2348000052d4000067d500007b2d",
    [],[], "outer_terrain_plain"),
####The Bowman's Improved Battle scenes END
#######
  ("random_scene_steppe1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000022004c563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain10"),
  ("random_scene_steppe2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000022008c563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),
  ("random_scene_steppe3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220018600400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain10"),
  ("random_scene_steppe4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220018600400691a400003efe00004b34000017e5",
    [],[], "outer_terrain_steppe"),
  ("random_scene_steppe5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220028600400691a400003efe00004b34000017e5",
    [],[], "outer_terrain_plain3"),
  ("random_scene_steppe6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000220028500400691a400003efe00004b3400004543",
    [],[], "outer_terrain_steppe"),
# # #
  ("random_scene_steppe7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain11"),  

  ("random_scene_steppe8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000022008c563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),  
#######
  ("random_scene_plain1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300006e3400691a40000437e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b3400001e5c",
    [],[], "outer_terrain_plain2"),
  ("random_scene_plain5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a40000612600004b3400000585",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563c00691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain8"),
  ("random_scene_plain8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a40000612600004b3400000585",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230068563c00691a400003efe000061bb0000741e",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300006e3400691a40000437e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b34000059be",
    [],[], "outer_terrain_plain"),
#
  ("random_scene_plain12",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563c00691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain8"),
  ("random_scene_plain13",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a40000612600004b3400000585",
    [],[], "outer_terrain_plain"),

# # #

  ("random_scene_plain16",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300006e3400691a40000437e00004b34000059be",
    [],[], "outer_terrain_plain"),

  ("random_scene_plain17",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain"),

  ("random_scene_plain18",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain11"),

  ("random_scene_plain20",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain"),

    ("random_scene_plain19",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain11"),

  ("random_scene_plain21",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain"),


  ("random_scene_plain22",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain3"),


  ("random_scene_plain23",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain5"),

  ("random_scene_plain24",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002300485e3400691a40000461c00004b3400006d3b",
    [],[], "outer_terrain_plain5"),
  
#######
  ("random_scene_snow1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002400586e3400691a400003efe00004b34000059be",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002400586e3400691a400003efe00004b340000458e",
    [],[], "outer_terrain_snow"),
  ("random_scene_snow3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002400586e3400691a400003efe00004b34000038e2",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000002400c06e3400691a400003efe00004b3400003eb1",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000024011c563400691a400003efe00004b34000051ab",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000240034563400691a400003efe00004b34000020c2",
    [],[], "outer_terrain_snow"),

# # #
  
  ("random_scene_snow7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000240034563400691a400003efe00004b34000020c2",
    [],[], "outer_terrain_snow"),  
    
#######
  ("random_scene_desert",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
#######
  ("random_scene_steppe_forest1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000078f00000356b00002c27",
    [],[], "paris_outer_terrain_plain9"),  
  ("random_scene_steppe_forest2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain3"), 
  ("random_scene_steppe_forest3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),  
  ("random_scene_steppe_forest4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain3"),
  ("random_scene_steppe_forest5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000078f00000356b00002c27",
    [],[], "outer_terrain_plain9"),  
  ("random_scene_steppe_forest6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000078f00000356b00002c27",
    [],[], "copy_outer_terrain_plain3"),

  ("random_scene_steppe_forest7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000a0034a0740025896000078f00000356b00002c27",
    [],[], "outer_terrain_plain9"),
#######
  ("random_scene_plain_forest1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),
  ("random_scene_plain_forest2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),
  ("random_scene_plain_forest3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain_forest4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "copy_outer_terrain_plain5"),
  ("random_scene_plain_forest5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain_forest6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),

  ("random_scene_plain_forest8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "copy_outer_terrain_plain5"),
  ("random_scene_plain_forest9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain11"),
  ("random_scene_plain_forest10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),



# # #
  
  ("random_scene_plain_forest7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),
  
#######                      
  ("random_scene_snow_forest1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow_forest2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow_forest3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow_forest4",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_desert_forest",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000400446e34003e8fa0000034e00004b34000071b8",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"),
  ("random_scene_snow_forest6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow_mix"), 
####### not used
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),
  ("random_scene_steppe",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000229602800000691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain3"),
  ("random_scene_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain5"),
  ("random_scene_snow_forest",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x400211130001e07800002ad400001172000035c4",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
     #                      
  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
  ("quick_battle_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30401ee300059966000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x4c6024e3000691a400001b7c0000591500007b52", 
    [],[], "outer_terrain_snow"),
  ("quick_battle_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00001d63c005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a078bb2000589630000667200002fb90000179c", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_6",sf_generate,"none", "none", (0,0),(120,120),-100,"0xa0425ccf0004a92a000063d600005a8a00003d9a", 
    [],[], "outer_terrain_steppe"),
  ("quick_battle_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain"),
  ("salt_mine",sf_generate,"none", "none", (-200,-200),(200,200),-100,"0x2a07b23200025896000023ee00007f9c000022a8",  
    [],[], "outer_terrain_steppe"),
  ("novice_ground",sf_indoors,"training_house_a", "bo_training_house_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("zendar_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[], "outer_terrain_plain"),
  ("dhorak_keep",sf_generate,"none", "none", (0,0),(120,120),-100,"0x33a7946000028ca300007f4a0000479400161992",
    ["exit"],[]),
  ("reserved4",sf_generate,"none", "none", (0,0),(120,120),-100,"28791",
    [],[]),
  ("reserved5",sf_generate,"none", "none", (0,0),(120,120),-100,"117828",
    [],[]),
  ("reserved6",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved7",sf_generate,"none", "none", (0,0),(100,100),-100,"6849",
    [],[]),
  ("reserved8",sf_generate,"none", "none", (0,0),(100,100),-100,"13278",
    [],[]),
  ("reserved9",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved10",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved11",0,"none", "none", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("reserved12",sf_indoors,"thirsty_lion", "bo_thirsty_lion", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],["tutorial_chest_1", "tutorial_chest_2"], "outer_terrain_plain"),
  ("tutorial_1",sf_indoors,"tutorial_1_scene", "bo_tutorial_1_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
##  ("tutorial_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003a04ce140005e17a000030030000780e00006979",
##    [],[], "outer_terrain_plain"),
  ("tutorial_2",sf_indoors,"tutorial_2_scene", "bo_tutorial_2_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_3",sf_indoors,"tutorial_3_scene", "bo_tutorial_3_scene", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("tutorial_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x30000500400360d80000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
  ("tutorial_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x3a06dca80005715c0000537400001377000011fe",
    [],[], "outer_terrain_plain"),


  ("training_ground_horse_track_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000337553240004d53700000c0500002a0f80006267",
    [],[], "outer_terrain_plain2"),
  ("training_ground_horse_track_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000301553240004d5370000466000002a0f800073f1",
    [],[], "outer_terrain_plain2"),
  #Kar
  ("training_ground_horse_track_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000400c12b2000515470000216b0000485e00006928",
    [],[], "outer_terrain_snow_2"),
  #Steppe
  ("training_ground_horse_track_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x00000000200b60320004a5290000180d0000452f00000e90",
    [],[], "outer_terrain_plain3"),
  #Plain
  ("training_ground_horse_track_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003008208e0006419000000f730000440f00003c86",
    [],[], "outer_terrain_plain"),

  ("training_ground_ranged_melee_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000013004451b4005194a000041cb00005ae800000ff5",
    [],[], "outer_terrain_plain2"),
  ("training_ground_ranged_melee_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000053008c52e4005194a000041cb00005ae800001bdd",
    [],[], "outer_terrain_plain2"),
  #Kar
  ("training_ground_ranged_melee_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000054327dcba0005194a00001b1d00005ae800004d63",
    [],[], "outer_terrain_snow_2"),
  #Steppe
  ("training_ground_ranged_melee_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000120058b484005194a000041ef00005ae8000050af",
    [],[], "outer_terrain_plain3"),
  #Plain
  ("training_ground_ranged_melee_5",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000013005cee34005194a000041ef00005ae800003c55",
    [],[], "outer_terrain_plain"),

  ("zendar_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    ["the_happy_boar","","zendar_merchant"],[], "outer_terrain_plain"),
#  ("zendar_center",0,"sargoth_square", "bo_sargoth_square", (-24,-22),(21,13),-100,"0",
#    ["the_happy_boar","","zendar_merchant"],[]),
  ("the_happy_boar",sf_indoors,"interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["zendar_center"],["zendar_chest"]),
  ("zendar_merchant",sf_indoors,"interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#  tavern quest sl 1429
    ("tavern_3lys",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

# Tvern names:
  #the shy monkey
  #the singing pumpkin
  #three swords
  #red stag
  #the bard's corner


#interior_tavern_a
#  town_1   Sargoth     #plain
#  town_2   Tihr        #plain
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain  
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
  ("town_1_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"paris_outer_terrain_plain9"),
  ("town_2_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],["bonus_chest_3"],"outer_terrain_town_thir_1"),
  ("town_3_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_4_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_5_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300214100003ecfb00002b930000051900002c29",
    [],["bonus_chest_2"],"outer_terrain_plain"),
  ("town_6_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
    [],[],"outer_terrain_plain"),
  ("town_7_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300785320004c93200002bc700005e48000008d2",
    [],[],"outer_terrain_plain"),
  ("town_8_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"copy_sea_outer_terrain_1"),
  ("town_9_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_snow_mix"),
  ("town_10_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"outer_terrain_plain5"),
  ("town_11_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach_snowny"),
  ("town_12_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_snow"),
  ("town_13_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x300416a600035cd600007ee80000012100003fbc",
    [],["bonus_chest_1"],"outer_terrain_plain3"),
  ("town_14_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"outer_terrain_plain3"),
  ("town_15_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_16_center",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain5"),
  ("town_17_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000020045abc000308c4000029d9000033bd000009b9",
    [],[],"outer_terrain_plain3"),
  ("town_18_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x0000000020049cbd00025896000048e90000164400002b3f",
    [],[],"outer_terrain_steppe"),
  ("town_19_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach_snowny"),
  ("town_20_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x300416a600035cd600007ee80000012100003fbc",
    [],[],"outer_terrain_plain5"),
  ("town_21_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"outer_terrain_plain3"),
  ("town_22_center",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000300214100003ecfb00002b930000051900002c29",
    [],[],"outer_terrain_plain"),
  
 
  ("town_1_castle",sf_indoors,"co_interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_1_seneschal"]),
  ("town_2_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_2_seneschal"]),
  ("town_3_castle",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_3_seneschal"]),
  ("town_4_castle",sf_indoors, "interior_castle_q", "bo_interior_castle_q", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_4_seneschal"]),
  ("town_5_castle",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_5_seneschal"]),
  ("town_6_castle",sf_indoors, "interior_castle_z", "bo_interior_castle_z", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_6_seneschal"]),
  ("town_7_castle",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_7_seneschal"]),
  ("town_8_castle",sf_indoors, "interior_castle_w", "bo_interior_castle_w", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_8_seneschal"]),
  ("town_9_castle",sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_9_seneschal"]),
  ("town_10_castle",sf_generate, "none", "none", (-100,-100),(100,100),-100,"0x00000007300005000002308c00004a840000624700004fda",
    ["exit"],["town_10_seneschal"]),
  ("town_11_castle",sf_indoors, "interior_castle_i", "bo_interior_castle_i", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_11_seneschal"]),
  ("town_12_castle",sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_12_seneschal"]),
  ("town_13_castle",sf_indoors, "interior_castle_b", "bo_interior_castle_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_13_seneschal"]),
  ("town_14_castle",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_14_seneschal"]),
  ("town_15_castle",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_15_seneschal"]),
  ("town_16_castle",sf_indoors, "interior_square_keep_b", "bo_interior_square_keep_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_16_seneschal"]),
  ("town_17_castle",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_17_seneschal"]),
  ("town_18_castle",sf_generate, "none", "none", (-100,-100),(100,100),-100,"0x00000007300005000002308c00004a840000624700004fda",
    ["exit"],["town_18_seneschal"]),
  ("town_19_castle",sf_indoors, "interior_castle_i", "bo_interior_castle_i", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_19_seneschal"]),
  ("town_20_castle",sf_indoors, "interior_castle_g", "bo_interior_castle_g", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_20_seneschal"]),
  ("town_21_castle",sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_21_seneschal"]),
  ("town_22_castle",sf_indoors,"castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["town_22_seneschal"]),
  
  ("town_1_tavern",sf_indoors,"copy_viking_interior_keep_a", "bo_copy_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_2_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[],"outer_terrain_town_thir_1"),
  ("town_3_tavern",sf_indoors, "interior_town_house_aa", "bo_interior_town_house_aa", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_4_tavern",sf_indoors, "interior_tavern_f", "bo_interior_tavern_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_5_tavern",sf_indoors, "interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_tavern",sf_indoors, "interior_town_house_f", "bo_interior_town_house_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_tavern",sf_indoors, "interior_tavern_h", "bo_interior_tavern_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_tavern",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_tavern",sf_indoors, "interior_tavern_c", "bo_interior_tavern_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_13_tavern",sf_indoors, "interior_tavern_g", "bo_interior_tavern_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_tavern",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_tavern",sf_indoors, "interior_rhodok_houses_d2", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_tavern",sf_indoors, "interior_tavern_b", "bo_interior_tavern_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_17_tavern",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_tavern",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_tavern",sf_indoors, "interior_tavern_c", "bo_interior_tavern_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_tavern",sf_indoors, "small_tavern", "bo_small_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_tavern",sf_indoors, "small_tavern", "bo_small_tavern", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_tavern",sf_indoors,"interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_1_store",sf_indoors,"interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_2_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_3_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_4_store",sf_indoors, "interior_town_house_a", "bo_interior_town_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_5_store",sf_indoors, "interior_rhodok_houses_b", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_store",sf_indoors, "interior_house_a", "bo_interior_house_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_store",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_store",sf_indoors, "interior_tavern_a", "bo_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_store",sf_indoors, "interior_tavern_a", "bo_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_13_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_store",sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_store",sf_indoors, "interior_rhodok_houses_b2", "bo_interior_rhodok_houses_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_store",sf_indoors, "interior_town_house_i", "bo_interior_town_house_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_17_store",sf_indoors, "interior_town_house_steppe_g", "bo_interior_town_house_steppe_g", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_store",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_store",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_store",sf_indoors, "interior_house_extension_h", "bo_interior_house_extension_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_store",sf_indoors,"interior_rhodok_houses_d", "bo_interior_rhodok_houses_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  
  ("town_1_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"paris_outer_terrain_plain9"),
  ("town_2_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_town_thir_1"),
  ("town_3_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_4_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_5_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_6_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_7_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_8_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"copy_sea_outer_terrain_1"),
  ("town_9_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x40001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_snow"),
  ("town_10_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain5"),
  ("town_11_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x40001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_snow"),
  ("town_12_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x40001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_snow"),
  ("town_13_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain3"),
  ("town_14_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain3"),
  ("town_15_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  ("town_16_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain5"),
  ("town_17_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain3"),
  ("town_18_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_steppe"),
  ("town_19_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0x40001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_snow"),
  ("town_20_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[]),
  ("town_21_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain3"),
  ("town_22_arena",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
  
  ("town_1_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_2_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_3_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_4_prison",sf_indoors,"interior_prison_g", "bo_interior_prison_g", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_7_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_prison",sf_indoors,"dungeon_cell_b", "bo_dungeon_cell_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_9_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_11_prison",sf_indoors,"dungeon_a", "bo_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_12_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_13_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_14_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_15_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_16_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_17_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_18_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_prison",sf_indoors,"dungeon_a", "bo_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_20_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_21_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_22_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),
  
  ("town_1_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_2_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_3_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
   ("town_4_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0",
    [],[],"outer_terrain_plain"),
  ("town_5_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_6_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_7_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002491600055157000000d20000152a0000611a",
    [],[],"outer_terrain_plain"),
  ("town_8_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300015e300063d8800002757000055df00001b08",
    [],[],"sea_outer_terrain_1"),
  ("town_9_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_snow"),
  ("town_10_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_plain3"),
  ("town_11_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_snow"),
  ("town_12_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_snow"),
  ("town_13_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130028e320005e17b00004a14000006d70000019d",
    [],[],"outer_terrain_plain"),
  ("town_14_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_plain3"),
  ("town_15_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030024e108003fd0100007bd300006c31000061aa",
    [],[],"outer_terrain_plain"),
  ("town_16_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98d0005b56d000072a70000240a00001e09",
    [],[],"outer_terrain_plain2"),
  ("town_17_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_plain3"),
  ("town_18_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_steppe"),
  ("town_19_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140015033000651900000159f0000619800006af6",
    [],[],"outer_terrain_snow"),
  ("town_20_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130028e320005e17b00004a14000006d70000019d",
    [],[],"outer_terrain_plain5"),
  ("town_21_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200011af00065192000067110000688300003435",
    [],[],"outer_terrain_plain3"),
  ("town_22_walls",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300214100003ecfb00002b930000051900002c29",
    [],[],"outer_terrain_plain"),
  
  ("town_1_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"0"),
  ("town_2_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),
  ("town_3_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_4_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_5_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_6_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
    [],[],"outer_terrain_plain2"),
  ("town_7_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x20008a110002589600006af30000356b00002c27",
    [],[],"outer_terrain_plain"),
  ("town_8_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_9_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
  ("town_10_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_plain3"),
  ("town_11_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
  ("town_12_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
  ("town_13_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_14_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_steppe"),
  ("town_15_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),
  ("town_16_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain2"),
  ("town_17_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_plain3"),
#  jardins de poitier vides
  ("town_17_vide_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"outer_terrain_plain3"),
#  
  ("town_18_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"sea_outer_terrain_2"),
  ("town_19_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[]),
  ("town_20_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[]),
  ("town_21_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_22_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
  ("town_paris6_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"0"),

  ("town_6_fleuve",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),  
  ("town_9bis_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),
 ("town_6_pirates",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300491830004a529000036230000312a00003653",
    [],[],"outer_terrain_plain2"),
#camps joueur seul
  ("town_19x_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],["tutorial_chest_4",],"outer_terrain_snow_2"),
  ("town_22x_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],["tutorial_chest_4",],"outer_terrain_steppe"),
  ("town_20x_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],["tutorial_chest_4",],"outer_terrain_steppe"),
  ("town_21x_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],["tutorial_chest_4",],"outer_terrain_plain"),  
#entrepots bourges
  ("town_4_etpalley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
#benezet sans camp de siege
 ("town_18_benezet_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],[],"sea_outer_terrain_2"),
  ("town_4_battle_v",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),
  ("town_5_batetp",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_plain"),  
#catacombes paris
  ("catacomb_entry",sf_indoors,"catacombe_entry", "bo_catacombe_entry", (-100,-100),(100,100),-100,"0",
    ["exit"],[]), 
#crypte
  ("catacomb_crypte",sf_indoors,"crypte_paris", "bo_crypte_paris", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#maison des 3 sirenes
  ("t_sirenes",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    ["exit"],[]),
#vieux chateau de tours
  ("town_16_vchateau",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],["tutorial_chest_5",],"outer_terrain_plain2"),
#manoire assasinat
  ("assa_manoire",sf_indoors,"interior_tavern_e", "bo_interior_tavern_e", (-40,-40),(40,40),-100,"0",
    ["exit"],[]),






#entree catas paris
  ("town_paris_cataentry",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[]),
#catacombes cote ville/rebels
  ("catacomb_entville",sf_indoors,"co_dungeon_a", "bo_co_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#####  DANS LES CATACOMBES begin ######  
#reservoir
  ("catacomb_reservoir",sf_indoors,"interior_square_keep_a", "bo_interior_square_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#crypte ronde vide
  ("catacomb_roundcrypt",sf_indoors,"interior_round_keep_a", "bo_interior_round_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#crypte ronde item
  ("catacomb_itemcrypt",sf_indoors,"interior_round_keep_a", "bo_interior_round_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_6",]),   
#crypte repert anglais
  ("catacomb_reperteng",sf_indoors,"crypte_2", "bo_crypte_2", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#####  DANS LES CATACOMBES end  ######
#  tourelles orleans script neutre
#  ("castle_tourellesorl",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
  #  [],[],"outer_terrain_plain"),
#  tourelles orleans script ATTAQUE
 # ("castle_tourellesorlatack",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
  #  [],[],"outer_terrain_plain"),  
#  tourelles orleans script BOMB
  #("castle_tourellesbomb",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
   # [],[],"outer_terrain_plain"),  
#  tourelles orleans assaut final
  #("castle_tourellesfinal",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
  #  [],[],"outer_terrain_plain"),  
#calais guild messagers
  ("town_9_messagers",sf_generate,"none", "none",(0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach_snowny"),
#marsseille guild messagers
  ("town_marss_messagers",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"0"),
#bourges guild messagers
  ("town_bourges_messagers",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"0"),
#cathedrale paris
  ("town_1cat_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),  
#cathedrale bourges
  ("town_bourgcat_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30001d9300031ccb0000156f000048ba0000361c",
    [],[],"outer_terrain_plain"),
#banque bourges
  ("town_bourgesbanque",sf_indoors,"interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#banque paris
  ("town_parisbanque",sf_indoors,"interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#banque marseille
  ("town_marseillebanque",sf_indoors,"interior_castle_h", "bo_interior_castle_h", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#caserne lyon
  ("town_casern_lyon",sf_generate,"none", "none",(0,0),(100,100),-100,"0x300416a600035cd600007ee80000012100003fbc",
    [],[],"outer_terrain_plain5"),

#taverne pugilat
  ("pugilat_1",sf_indoors,"salle_pugilat_1", "bo_salle_pugilat_1", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),#type 1

  ("pugilat_2",sf_indoors,"salle_pugilat_2", "bo_salle_pugilat_1", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),#type 2

  ("pugilat_3",sf_indoors,"salle_pugilat_1", "bo_salle_pugilat_1", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),#type 1

  ("pugilat_4",sf_indoors,"pugilat_5", "bo_pugilat_5", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),#type work shoprennes

#
  ("grotte_1",sf_indoors,"chasm", "bo_chasm", (-100,-100),(100,100),-100,"0",
    ["exit"],["chest_6rennes"]),

#valle pendus



#monastere orleans
  ("monastere_orleans",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),

#monastere orleans interieur
  ("monastere_orleans_int",sf_indoors, "monastere_q", "bo_monastere_q", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
#monastere orleans interieur COPIE SCRIPTEE
  ("monastere_orl_int2",sf_indoors,"monastere_q", "bo_monastere_q", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  
#monastere orleans interieur LOGE SECRETE
    ("monastere_orl_intloge_secry",sf_indoors,"catacombe_entry", "bo_catacombe_entry", (-100,-100),(100,100),-100,"0",
    ["exit"],["chest_9_logesecrete"]),


  ("town_14_port",sf_generate,"none", "none",(0,0),(100,100),-100,"0x00000000200016da000364d9000060f500007591000064e7",
    [],[],"outer_terrain_plain3"),  
#0x30054d228004050000005a768000688400002e3b
#0x30054da28004050000005a76800022aa00002e3b
#Castles:

#       1 Steppe #Was castle 39
   ("castle_1_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007a0320005695f0000601c00007a8800001a17",
     [],[],"outer_terrain_snow"),
   ("castle_1_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
     ["exit"],["castle_1_seneschal"]),
   ("castle_1_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
     [],[]),  

#       2 Plain #Switched with castle 18
  ("castle_2_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240079f9e0005695a0000035f00003ef400004aa8",
    [],[],"outer_terrain_snow"),
  ("castle_2_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_2_seneschal"]),
  ("castle_2_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       3 Plain
  ("castle_3_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain9"),
  ("castle_3_interior",sf_indoors, "interior_castle_m", "bo_interior_castle_m", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_3_seneschal"]),
  ("castle_3_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       4 Plain
  ("castle_4_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"copy_outer_terrain_plain3"),
  ("castle_4_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_4_seneschal"]),
  ("castle_4_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       5 Plain
  ("castle_5_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x3189dc1a000429090000619700007cbd00005ab7",
    [],[],"outer_terrain_plain5"),
  ("castle_5_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_5_seneschal"]),
  ("castle_5_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       6 Plain
  ("castle_6_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b009723200059d6800005f4f0000757f000069cd",
    [],[],"outer_terrain_plain"),
  ("castle_6_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_6_seneschal"]),
  ("castle_6_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       7 Snow #Was castle 1
   ("castle_7_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
     [],[],"copy_outer_terrain_plain3"),
   ("castle_7_interior",sf_indoors, "dungeon_entry_a", "bo_dungeon_entry_a", (-100,-100),(100,100),-100,"0",
     ["exit"],["castle_7_seneschal"]),
   ("castle_7_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
     [],[]),
	

	
#       8 Plain
  ("castle_8_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x314d060900036cd70000295300002ec9000025f3",
    [],[],"outer_terrain_plain7"),
  ("castle_8_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_8_seneschal"]),
  ("castle_8_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       9 Steppe
  ("castle_9_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa0048e000004d93700004f91000065980000229b",
    [],[],"outer_terrain_steppe"),
  ("castle_9_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_9_seneschal"]),
  ("castle_9_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),
#       10 Steppe  
  ("castle_10_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b23200049d2a00003c37000040ef000037cd",
    [],[],"outer_terrain_castle_9"),
  ("castle_10_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_10_seneschal"]),
  ("castle_10_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#       11 Plain
  ("castle_11_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain2"),
  ("castle_11_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_11_seneschal"]),
  ("castle_11_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_12_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_castle_9"),
  ("castle_12_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_12_seneschal"]),
  ("castle_12_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_13_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230054f630005fd820000222a00003de000005f00",
    [],[],"outer_terrain_plain10"),
  ("castle_13_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_13_seneschal"]),
  ("castle_13_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_14_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"outer_terrain_plain"),
  ("castle_14_interior",sf_indoors, "interior_castle_j", "bo_interior_castle_j" , (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_14_seneschal"]),
  ("castle_14_prison",sf_indoors,"interior_prison_m", "bo_interior_prison_m", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_15_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007941f0005415000007e650000225f00003b3e",
    [],[],"outer_terrain_plain"),
  ("castle_15_interior",sf_indoors, "interior_castle_p", "bo_interior_castle_p", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_15_seneschal"]),
  ("castle_15_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain
  ("castle_16_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"outer_terrain_plain9"),
  ("castle_16_interior",sf_indoors, "interior_castle_e", "bo_interior_castle_e", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_16_seneschal"]),
  ("castle_16_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Steppe
  ("castle_17_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220045d9b0005d9760000034a00002a3e00006fbd",
    [],[],"outer_terrain_steppe"),
  ("castle_17_interior",sf_indoors, "interior_castle_l", "bo_interior_castle_l", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_17_seneschal"]),
  ("castle_17_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#      Snow

  ("castle_18_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0xa00363638005c16d00003c82000037e000002303",
    [],[],"outer_terrain_plain4"),
  ("castle_18_interior",sf_indoors, "interior_castle_u", "bo_interior_castle_u", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_18_seneschal"]),
  ("castle_18_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",#### B bkullanilmayacak
    [],[]),

#       Snow
  ("castle_19_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014004d81100057963000062ce0000255800004c09",
    [],[],"outer_terrain_snow"),
  ("castle_19_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_19_seneschal"]),
  ("castle_19_prison",sf_indoors,"interior_prison_e", "bo_interior_prison_e", (-100,-100),(100,100),-100,"0",
    [],[]),
#       Plain #was 39
#  ("castle_39_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
#     [],[],"outer_terrain_snow"),
#  ("castle_39_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
#    ["exit"],["castle_39_seneschal"]),
#  ("castle_39_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
#    [],[]),
   ("castle_20_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013006199a0004e5370000494f000028fc00006cf6",
     [],[],"outer_terrain_plain"),
   ("castle_20_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
     ["exit"],["castle_20_seneschal"]),
   ("castle_20_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
     [],[]),

  ("castle_21_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230011ab20005d57800003a2600004b7a000071ef",
    [],[],"outer_terrain_plain11"),
  ("castle_21_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_21_seneschal"]),
  ("castle_21_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_22_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000ad340004d537000024650000253c00000461",
    [],[],"outer_terrain_plain"),
  ("castle_22_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_22_seneschal"]),
  ("castle_22_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
  
  ("castle_23_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300658bc0007bded000025520000093800006114",
    [],[], "outer_terrain_plain"),
  ("castle_23_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_23_seneschal"]),
  ("castle_23_prison",sf_indoors,"interior_prison_b", "bo_interior_prison_b", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_24_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130021f63000721ca000055be000079d90000156d",
    [],[],"outer_terrain_plain"),
  ("castle_24_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_24_seneschal"]),
  ("castle_24_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_25_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004e0a600061989000053d50000749800005f64",
    [],[],"outer_terrain_plain"),
  ("castle_25_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_25_seneschal"]),
  ("castle_25_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),


  ("castle_26_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_plain5"),



  
  ("castle_26_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_26_seneschal"]),
  ("castle_26_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_27_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b23200070dbc000041de00000c4900003cfc",
    [],[],"outer_terrain_plain5"),
  ("castle_27_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_27_seneschal"]),
  ("castle_27_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
#ex monterean
#  ("castle_28_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b232000715c50000084c00001b5b000018ec",
 #   [],[],"outer_terrain_plain"),


    ("castle_28_exterior",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain"),


  
  ("castle_28_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_28_seneschal"]),
  ("castle_28_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_29_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006400796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_snow"),
  ("castle_29_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_29_seneschal"]),
  ("castle_29_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_30_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220035e32000611840000147f00003dac00000660",
    [],[],"outer_terrain_plain"),
  ("castle_30_interior",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_30_seneschal"]),
  ("castle_30_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_31_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025b8d0006459400006a3700002adb00007091",
    [],[],"outer_terrain_plain5"),
  ("castle_31_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_31_seneschal"]),
  ("castle_31_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_32_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230041fb20005fd7d00002692000029b700007d12",
    [],[],"outer_terrain_plain"),
  ("castle_32_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_32_seneschal"]),
  ("castle_32_prison",sf_indoors,"interior_prison_j", "bo_interior_prison_j", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_33_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029cb2000709c200003c9500004b9b00002f4d",
    [],[],"outer_terrain_plain"),
  ("castle_33_interior",sf_indoors, "interior_castle_v", "bo_interior_castle_v", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_33_seneschal"]),
  ("castle_33_prison",sf_indoors,"interior_prison_d", "bo_interior_prison_d", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_34_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b007b232000715c50000084c00001b5b00006580",
    [],[],"outer_terrain_plain"),
  ("castle_34_interior",sf_indoors, "interior_castle_c", "bo_interior_castle_c", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_34_seneschal"]),
  ("castle_34_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_35_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130031be30006f9bc00000aae00000fb80000243f",
    [],[],"outer_terrain_plain"),
  ("castle_35_interior",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_35_seneschal"]),
  ("castle_35_prison",sf_indoors,"interior_prison_f", "bo_interior_prison_f", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_36_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007b2630005695c00001ebe0000028e00007e37",
    [],[],"outer_terrain_plain"),
  ("castle_36_interior",sf_indoors, "castle_h_interior_b", "bo_castle_h_interior_b", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_36_seneschal"]),
  ("castle_36_prison",sf_indoors,"interior_prison_h", "bo_interior_prison_h", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_37_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9",
    [],[],"outer_terrain_plain"),
  ("castle_37_interior",sf_indoors, "interior_castle_k", "bo_interior_castle_k", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_37_seneschal"]),
  ("castle_37_prison",sf_indoors,"interior_prison_l", "bo_interior_prison_l", (-100,-100),(100,100),-100,"0",
    [],[]),
#was 7
   ("castle_38_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000c007a56300047d1e00006c9100002859000028bc",
     [],[],"outer_terrain_snow"),
   ("castle_38_interior",sf_indoors, "interior_castle_o", "bo_interior_castle_o", (-100,-100),(100,100),-100,"0",
     ["exit"],["castle_38_seneschal"]),
   ("castle_38_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
     [],[]),
#not used	 
  # ("castle_38_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    # [],[],"outer_terrain_steppe"),
  # ("castle_38_interior",sf_generate, "none", "none", (-100,-100),(100,100),-100,"0x00000007300005000002308c00004a840000624700004fda",
    # ["exit"],["castle_38_seneschal"]),
  # ("castle_38_prison",sf_indoors,"interior_prison_o", "bo_interior_prison_o", (-100,-100),(100,100),-100,"0",
    # [],[]),


  ("castle_39_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030044e900003dd02000077b20000400100005697",
    [],[],"outer_terrain_plain"),
  ("castle_39_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_11_seneschal"]),
  ("castle_39_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    [],[]),	
	#moved to 20 replacing it
  # ("castle_39_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007a0320005695f0000601c00007a8800001a17",
    # [],[],"outer_terrain_snow"),
  # ("castle_39_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    # ["exit"],["castle_39_seneschal"]),
  # ("castle_39_prison",sf_indoors,"interior_prison_k", "bo_interior_prison_k", (-100,-100),(100,100),-100,"0",
    # [],[]),
#is copy of 29!
  ("castle_40_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006400796b20005053e000042ed0000199b000037cd",
    [],[],"outer_terrain_snow"),
  ("castle_40_interior",sf_indoors, "interior_castle_n", "bo_interior_castle_n", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_40_seneschal"]),
  ("castle_40_prison",sf_indoors,"interior_prison_a", "bo_interior_prison_a", (-100,-100),(100,100),-100,"0",
    [],[]),
#not used	
  # ("castle_40_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    # [],[],"outer_terrain_steppe"),
  # ("castle_40_interior",sf_indoors, "interior_castle_g_square_keep", "bo_interior_castle_g_square_keep", (-100,-100),(100,100),-100,"0",
    # ["exit"],["castle_40_seneschal"]),
  # ("castle_40_prison",sf_indoors,"interior_prison_n", "bo_interior_prison_n", (-100,-100),(100,100),-100,"0",
    # [],[]),


  ("castle_41_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005a0932320004cd3000004e7d00007d6e00006c58",
    [],[],"outer_terrain_plain"),
  ("castle_41_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_31_seneschal"]),
  ("castle_41_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_42_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_42_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_16_seneschal"]),
  ("castle_42_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_43_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_43_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_33_seneschal"]),
  ("castle_43_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_44_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_44_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_34_seneschal"]),
  ("castle_44_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_45_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_45_interior",sf_indoors, "interior_castle_t", "bo_interior_castle_t", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_35_seneschal"]),
  ("castle_45_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_46_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_46_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_34_seneschal"]),
  ("castle_46_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

  ("castle_47_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc",
    [],[],"sea_outer_terrain_2"),
  ("castle_47_interior",sf_indoors, "interior_castle_y", "bo_interior_castle_y", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_37_seneschal"]),
  ("castle_47_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),

#  ("castle_48_exterior",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003000ad340004d537000024650000253c00000461",
 #   [],[],"outer_terrain_plain"),

  ("castle_48_exterior",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000002300006e3400691a40000437e00004b34000059be",
    [],[], "outer_terrain_plain"),
  
  ("castle_48_interior",sf_indoors, "interior_castle_a", "bo_interior_castle_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["castle_22_seneschal"]),
  ("castle_48_prison",sf_indoors,"interior_prison_i", "bo_interior_prison_i", (-100,-100),(100,100),-100,"0",
    [],[]),
	
#!!Villages !!#
  ("village_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240031a0f0006b9ae00006e1b00006e9000007281",
    [],[],"outer_terrain_snow"),
  ("village_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002c003131700066da00000484c000008630000613d",
    [],[],),
  ("village_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003991e0006f1bc000055cc0000085600001563",
    [],[],"outer_terrain_snow_mix"),
  ("village_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_snow"),
  ("village_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003001ce100006097d0000134c000016d8000042a2",
    [],[],"outer_terrain_plain"),
  ("village_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230035598000761df000058ea000006f3000005e7",
    [],[],"outer_terrain_plain2"),
  ("village_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain4"),
  ("village_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300798320006499200002acc000040d70000421d",
    [],[],"outer_terrain_plain2"),
  ("village_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain4"),
  ("village_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005dad40005f57b0000543e0000279d000052b4",
    [],[],"outer_terrain_plain4"),
  ("village_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220029c4400077de100002dcc00002edf00003925",
    [],[],"outer_terrain_steppe"),
  ("village_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e",
    [],[],"outer_terrain_steppe"),
  ("village_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300265e3400691a400005e4d80006dfa00003bc8",
    [],[], "outer_terrain_plain"),
  ("village_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230029ce30004912400002acc000040d7000077db",
    [],[], "outer_terrain_plain"),
  ("village_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300029d4000691a4000015148000335800004190",
    [],[],"outer_terrain_plain"),
  ("village_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240031a0f0006b9ae00006e1b00006e9000007281",
    [],[],"outer_terrain_snow"),
  ("village_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002c003131700066da00000484c000008630000613d",
    [],[],),
  ("village_18",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003561a00070dbe000016f8000010ca000069f8",
    [],[],"outer_terrain_snow"),
  ("village_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003991e0006f1bc000055cc0000085600001563",
    [],[],"outer_terrain_snow"),
  ("village_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_snow"),
  ("village_21",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240024d3800074dcc0000488b0000016100002047",
    [],[],"outer_terrain_snow"),
#switched with 87
  ("village_22",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001c98a0004dd3000001a5e00005c6200001ec9",
    [],[],"outer_terrain_plain"),	

  ("village_23",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300415380007b5e600005f7b00000a9200001615",
    [],[],),
  ("village_24",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002e1ad00048924000031e70000677500002a0c",
    [],[],"outer_terrain_plain2"),
  ("village_25",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002d0021ede000775dd000032670000173700007c40",
    [],[],"outer_terrain_plain3"),
  ("village_26",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230020a008005294c000063fc0000771c0000216f",
    [],[],"outer_terrain_plain5"),
  ("village_27",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b2320004a52900004d390000518c00001ab1",
    [],[],"outer_terrain_plain"),
  ("village_28",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022002de4c00077ddd00007e1300000af400006de1",
    [],[],"outer_terrain_steppe"),
  ("village_29",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007b2320004f93c000023ed000053e500002949",
    [],[],"outer_terrain_plain5"),
  ("village_30",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025e0a0004dd3700004822000032ea0000011b",
    [],[],"outer_terrain_plain"),
  ("village_31",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e38003a8ec00004c8380005c6600001cb5", ##0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain"),
  ("village_32",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300619e30003a8ec00004c8380007de100001cb5",
    [],[],"outer_terrain_plain2"),
  ("village_33",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001700000649920000423900007768000062c3",
    [],[],"outer_terrain_plain"),
  ("village_34",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300323e3000611860000392d00005c05000067e1",
    [],[],"outer_terrain_plain2"),
  ("village_35",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079cb20005394e00001ef90000753000000731",
    [],[],"outer_terrain_castle_9"),
  ("village_36",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003a1560006118d00003ce300004123000043b2",
    [],[],"outer_terrain_plain"),
  ("village_37",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022004d36300077dd600002e08000036ab00004651",
    [],[],"outer_terrain_steppe"),
  ("village_38",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e21e0005fd7f000028920000650500005c53",
    [],[],"outer_terrain_plain"),
  ("village_39",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003e5990005fd78000069670000446c00007476",
    [],[],"outer_terrain_plain2"),
  ("village_40",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220031f6300076dda000056f100004f6d000070b3",
    [],[],"outer_terrain_steppe"),

  ("village_41",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000a3e300062d8d0000444e0000276e00006eb1",
    [],[],"outer_terrain_steppe"),
  ("village_42",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022007b23200062d8d000060b900003b8b00006c93",
    [],[],"outer_terrain_steppe"),
  ("village_43",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000320e0005856300001d770000792700002aa1",
    [],[],"outer_terrain_plain3"),
  ("village_44",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200020200005c574000075480000002d00004be7",
    [],[],"outer_terrain_steppe"),
  ("village_45",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007a3df0004e52b0000167700005180000051ea",
    [],[],"outer_terrain_steppe"),
  ("village_46",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a03200061184000058d20000717a00001af0",
    [],[],"outer_terrain_plain2"),
  ("village_47",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000300621b100051d47000034e300007926000048d3",
    [],[],"outer_terrain_plain4"),
  ("village_48",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_snow"),
  ("village_49",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_snow"),
  ("village_50",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000140029bbc0006799b000009cb0000720000006555",
    [],[],"outer_terrain_snow_mix"),
  ("village_51",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002b0e30006a5a90000722700002f5200005e2b",
    [],[],"outer_terrain_plain3"),
  ("village_52",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000220011de30005655900002c2300003b2400000d47",
    [],[],"outer_terrain_plain3"),
  ("village_53",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_54",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300032300005c5740000243e000056aa00003a7a",
    [],[],"outer_terrain_plain"),
  ("village_55",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
  ("village_56",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_57",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300027b200065d9700004dcf0000212800001bf0",
    [],[],"outer_terrain_plain"),
#  ("village_58",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240024d3800074dcc0000488b0000016100002047",
#    [],[],"outer_terrain_snow"),
  ("village_41b",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000a3e300062d8d0000444e0000276e00006eb1",
    [],[],"outer_terrain_steppe"),
  ("village_59",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain2"),
  ("village_60",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079c3200060d860000428100007e01000071b4",
    [],[],"outer_terrain_plain"),
  ("village_61",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300325350006659e0000603500006b0200005676",
    [],[],"outer_terrain_plain"),
  ("village_62",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000143c08f060004e53a00000a500000187700007c9b",
    [],[],"outer_terrain_snow"),
  ("village_63",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013007a6b20006258b00006bb8000074df00002f18",
    [],[],"outer_terrain_plain"),
  ("village_64",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
  ("village_65",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013004d8320006358b00006d2b000005d5000023e5",
    [],[],"outer_terrain_plain"),
  ("village_66",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240024d3800074dcc0000488b0000016100002047",
    [],[],"outer_terrain_snow"),
  ("village_67",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_snow"),
  ("village_68",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000240031a0f0006b9ae00006e1b00006e9000007281",
    [],[],"outer_terrain_snow"),
  ("village_69",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_plain2"),
  ("village_70",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003991e0006f1bc000055cc0000085600001563",
    [],[],"outer_terrain_snow"),
  ("village_71",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000630079ab20005fd7f0000687300007190000006df",
    [],[],"outer_terrain_plain"),
  ("village_72",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000006300654ac00062d910000635800007c9600005d35",
    [],[],"outer_terrain_plain"),
  ("village_73",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230079db200050d4500001b4b00007cf400001973",
    [],[],"outer_terrain_plain"),
  ("village_74",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003561a00070dbe000016f8000010ca000069f8",
    [],[],"outer_terrain_snow"),
  ("village_75",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain"),
  ("village_76",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002c003131700066da00000484c000008630000613d",
    [],[],),
  ("village_77",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000004300005008005b57000004e31800017d80000754b",
    [],[],"outer_terrain_plain"),
  ("village_78",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023004561e00069da700000f490000256b000058b5",
    [],[],"outer_terrain_plain2"),
  ("village_79",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002400798b20005ed7b000019160000650f000072d2",
    [],[],"outer_terrain_snow_mix"),
 # ("village_80",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
#    [],[],"outer_terrain_plain"),
#rennes le chateau 
  ("village_80",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300005634005053f000060250000146300006e84",
    [],[],"outer_terrain_plain3"),  
  #################### Yeni koyler ######################
  ("village_81",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300296320006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_town_thir_1"),
  ("village_82",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000031059a0d0004792000005c3a00004df500000dbc",
    [],[],"outer_terrain_plain"),
  ("village_83",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023004561e00069da700000f490000256b000058b5",
    [],[],"outer_terrain_plain2"),
  ("village_84",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000320e0005856300001d770000792700002aa1",
    [],[],"outer_terrain_plain"),
  ("village_85",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
    [],[],"outer_terrain_snow"),
 # ("village_86",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000014007b26300059563000051e000001aa4000034ee",
 #   [],[],"outer_terrain_snow"),0x00000000b00185134005615800005564000023590000579e
  ("village_86b",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e",
    [],[],"outer_terrain_plain"),
#switched with 22	
  ("village_87",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000024003d7d20007d1f40000374100001e120000097b",
    [],[],"outer_terrain_snow"),	
	
  ("village_88",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002dd19000691a40000566a000012a000001037",
    [],[],"outer_terrain_plain"),
  ("village_89",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300022a60005314c0000428100007e0100002e97",
    [],[],"outer_terrain_steppe"),
  ("village_90",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002cd900005314c00001f6d00006d7700003493",
    [],[],"outer_terrain_steppe"),
	
  ("village_91",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000022000a3e300062d8d0000444e0000276e00006eb1",
    [],[],"outer_terrain_plain"),
	
  ("village_92",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300019500006c1b4000065c700002bea0000154e",
    [],[],"outer_terrain_plain"),
	
  ("village_93",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230025e0a0004dd3700004822000032ea0000011b",
    [],[],"outer_terrain_plain5"),
	
  ("village_94",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200213e300077ddf000019d3000034520000626e",
    [],[],"outer_terrain_plain5"),
	
	("village_95",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_96",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_97",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_98",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_99",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_100",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_101",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_102",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_103",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_104",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_105",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_106",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_107",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_108",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_109",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	("village_110",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001500410320005a96800006b5300004edc00000d11",
    [],[],"outer_terrain_plain"),
	
	
	
  ("field_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a059a5a0009525600002005000060e300001175",
    [],[],"outer_terrain_plain"),
  ("field_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000033a079a3f000a3a8000006dfd000030a100006522",
    [],[],"outer_terrain_steppe"),
  ("field_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
  ("field_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x30054da28004050000005a76800022aa00002e3b",
    [],[],"outer_terrain_steppe"),
#1429 Scenes sur world map
#  camp anglais
  ("camp_brit_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_castle_9"),

#village toul
  ("villag_toul",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300323e3000611860000392d00005c05000067e1",
    [],["chest_4toul",],"outer_terrain_plain2"),

# camp de verzy rebels
  ("verzy_camp",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_town_thir_1"),

#PLACE FORTE
  ("p_forte",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_castle_9"),

#PLACE FORTE aux rebels
  ("p_fneutral",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_castle_9"),
  
# toour des pins
  ("tour_pins",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_plain10"),
    
#ferme mathieu
  ("ferm_mat",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b",
    [],[],"outer_terrain_plain2"),

#camp de chasse
  ("camp_chasseur",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain2"),
  
#chapelle fierbois
  ("fierbois_cha",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130001887000334d0000073ed00004f1a00007a35",
    [],[],"outer_terrain_plain5"),        

#chapelle interieure
  ("chapelle_indoor",sf_indoors,"fierbois", "bo_crypte_paris", (-100,-100),(100,100),-100,"0",
    ["exit"],["chest_5cat",]),  

#foret de rouen
  ("rouen_forest",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400790b20002c8b0000050d500006f8c00006dbd",
    [],[],"outer_terrain_snow_mix"),

#scenes quete de reserve
#  moyene
 # ("test_moyen",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
  #  [],[], "outer_terrain_plain9"),

  ("test_foret",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001b003cd634005053f00006cd70000146300006e84",
    [],[],"outer_terrain_plain7"), 
#grande (foret)
  #("test_foret",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001b003cc634005053f00007dea0000146300006e84",
    #[],[],"outer_terrain_plain7"),  
#################
  ("test2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b005c5634003fd00000047140000288c0000286f",
    [],[],"outer_terrain_steppe"),

    ("test3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00511d98004b12e0000039f00004e6300005c7d",
    [],[],"outer_terrain_plain"),




  ("bracon_forest1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b00285324006b5aa00006f3200003a5000004fed",
    [],[],"outer_terrain_plain5"),
  ("bracon_forest2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain7"),
  ("bracon_forest3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain11"),

  ("bracon_forest4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain5"),
  ("bracon_forest5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain5"),
  ("bracon_forest6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"copy_outer_terrain_plain5"),
  ("bracon_forest7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"copy_outer_terrain_plain5"),
  ("bracon_forest8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain5"),
  ("bracon_forest9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_plain7"),
  ("bracon_forest10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_snow"),
  ("bracon_forest11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_snow"),
  ("bracon_forest12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002b000050a4004dd3700005db3000032ea0000011b",
    [],[],"outer_terrain_snow"),


#rennes le chateau cote chateau
  ("rennes_le_chateau",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300005634005053f000060250000146300006e84",
    [],[],"outer_terrain_plain3"),
#
  ("castle_rennes_chat_interior",sf_indoors, "interior_rennes_castle", "bo_interior_rennes_castle", (-100,-100),(100,100),-100,"0",
    ["exit"],["chest_8chateaux"]),

#vieux cimetiere rouen
  ("vieux_cimetier_rouen",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],[],"outer_terrain_snow"),

#loge rouen
  ("loge_de_rouen",sf_indoors,"co_dungeon_a", "bo_co_dungeon_a", (-100,-100),(100,100),-100,"0",
    ["exit"],["chest_10_logerouen"]),

  ("auberge_ext_1",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b3400001e5c",
    [],[], "outer_terrain_plain7"),

    ("auberge_ext_2",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b3400001e5c",
    [],[], "outer_terrain_plain2"),

  ("auberge_ext_3",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x0000000240034563400691a400003efe00004b34000020c2",
    [],[], "outer_terrain_snow"),  


    ("auberge_ext_4",sf_generate,"none", "none", (0,0),(240,240),-0.5,"0x00000002300285e3400691a4000043af00004b3400001e5c",
    [],[], "outer_terrain_plain3"),



  ("auberge_inter_1",sf_indoors, "viking_interior_keep_a", "bo_viking_interior_keep_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("auberge_inter_2",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("auberge_inter_3",sf_indoors, "interior_tavern_a", "bo_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("auberge_inter_4",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("maison_auberge_quete1",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_7"]),


 
  ("prairie_bourges",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    ["exit"],["tutorial_chest_8"], "outer_terrain_plain3"),




#camps
  ("camp_19_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x400211130001e07800002ad400001172000035c4",
    [],["tutorial_chest_4",],"outer_terrain_snow_2"),


  ("camp_20_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000420000500000334ce00001d1100003d0600000d27",
    [],["tutorial_chest_4",],"outer_terrain_steppe"),

  ("camp_21_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],["tutorial_chest_4",],"outer_terrain_plain"),


  ("camp_22_alley",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],["tutorial_chest_4",],"outer_terrain_steppe"),

##scenes rpg pretes !!!

  ("maison_pilotis",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),


  ("rpg_foret1",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),

  ("maison_pilotis2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),

  ("rpg_foret2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"forest_wall"),




  ("rpg_foret3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],["tutorial_chest_15",],"forest_wall"),


  ("rpg_foret4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"forest_wall"),
  


  ("rpg_foret5",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),

  ("rpg_foret6",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),  


  ("rpg_foret7",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain"),
  

  ("rpg_foret8",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),  



  ("rpg_foret9",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],["tutorial_chest_16",], "forest_wall"),


    ("rpg_foret10",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),



    ("rpg_foret11",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "forest_wall"),



    ("bois_descerfs",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],["tutorial_chest_17",], "forest_wall"),

#rpg broceliand interrieurs
#
#  ("grotte_1",sf_indoors,"chasm", "bo_chasm", (-100,-100),(100,100),-100,"0",
#    ["exit"],["chest_6rennes"]),
#####

  ("pilotis_int_lac_broceliand",sf_indoors,"pilotis_int", "bo_pilotis_int", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("pilotis_int_rainbow",sf_indoors,"pilotis_int", "bo_pilotis_int", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

#grottes begin
  ("mine_fer_broceliand_lvl_1",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_9",]),



  ("mine_fer_broceliand_lvl_2",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_10",]),   


  ("mine_fer_broceliand_lvl_3",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_11",]),   



  ("grotte_bandits_broceliand_lvl_1",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_12",]),   

  ("grotte_bandits_broceliand_lvl_2",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_13",]),



  ("grotte_bandits_sortie",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),
  
#grottes end

  ("broceliand_auberge_inter",sf_indoors, "interior_castle_j", "bo_interior_castle_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),


  ("cabane_broceliand_1",sf_indoors,"interior_town_house_e", "bo_interior_town_house_e", (-100,-100),(100,100),-100,"0",
    ["exit"],["tutorial_chest_14",]),
  



  ("village_brulle",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),




#foret quete auberge neige
    ("foret_neige_auberge",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_snow"),



#camp_crane_defer 
  ("camp_crane_defer",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],["tutorial_chest_18",], "outer_terrain_plain3"),
## rue des dames rennes

  ("rue_des_dames_rennes",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain"),
##chateau de panthievre

   ("chateau_panthievre",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),

  ##chateau de panthievre cote cour
   ("chateau_panthievre_cour",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),
  
## passage secret sous chateau pantievre
  ("passage_chat_panthievre",sf_indoors,"tunnel_sloped_supports", "bo_tunnel_sloped_supports", (-100,-100),(100,100),-100,"0",
    [],[]),  
  
#### test tailles scenes rpg ###########

  ("rpg_taille_1_foret",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b0018a0740025896000000f80000356b00002c27",
    [],[], "forest_wall"), 


  ("rpg_taille_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x300bc5430001e0780000448a0000049f00007932",
    [],[],"outer_terrain_steppe"),

  ("rpg_taille_2",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000000b002ca0740025896000000f80000356b00002c27",
    [],[], "outer_terrain_plain7"),


  ("rpg_taille_3",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000230028563400691a400003efe00004b34000059be",
    [],[], "outer_terrain_plain3"),


####################
 
# multiplayer
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
    [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",   
    [],[],"outer_terrain_snow"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_plain"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("wedding",sf_indoors, "castle_h_interior_a", "bo_castle_h_interior_a", (-100,-100),(100,100),-100,"0", [],[]),
  ("lair_steppe_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000002001cccf40043d0d0000556b0000768400003ea9",
    [],[],"outer_terrain_steppe"), #a box canyon with a spring? -tents...
  ("lair_taiga_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000004c079c3e000499280000420f0000495d000048d6",
    [],[],"outer_terrain_snow"),
  ("lair_desert_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000005024cd120005595400003882000037a90000673e",
    [],[],"outer_terrain_plain"), #an encampment in the woods
  ("lair_forest_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b0030be34003ecfb0000657e0000213500002461",
    [],[],"outer_terrain_plain"), #a cliffside ledge or cave overlooking a valley
  ("lair_mountain_bandits",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000200434070004450c000022bf00006ad6000060ed",
    [],[],"outer_terrain_steppe"),
  ("lair_sea_raiders",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000b00562e200040900000063f40000679f00006cda",
    [],[],"sea_outer_terrain_1"), #the longships beached on a hidden cove


  ("quick_battle_scene_1",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002dee300045d1d000001bf0000299a0000638f", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_2",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000250001d630005114300006228000053bf00004eb9", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_3",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000023002b76300046d2400000190000076300000692a", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_4",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000025a00f23700057d5f00006d6a000050ba000036df", 
    [],[], "outer_terrain_plain"),
  ("quick_battle_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012007985300055550000064d500005c060000759e",
    [],[],"outer_terrain_plain"),
  ("quick_battle_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),

  ("tutorial_training_ground",sf_generate,"none", "none", (0,0),(120,120),-100,"0x000000003000050000046d1b0000189f00002a8380006d91",
    [],[], "outer_terrain_plain"),
    
  ("town_1_room",sf_indoors,"viking_interior_tavern_a", "bo_viking_interior_tavern_a", (-100,-100),(100,100),-100,"0",
    [],[]),
  ("town_5_room",sf_indoors, "interior_town_house_d", "bo_interior_town_house_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_6_room",sf_indoors, "interior_town_house_j", "bo_interior_town_house_j", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_8_room",sf_indoors, "interior_house_b", "bo_interior_house_b", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_10_room",sf_indoors, "interior_town_house_steppe_c", "bo_interior_town_house_steppe_c", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),
  ("town_19_room",sf_indoors, "interior_town_house_steppe_d", "bo_interior_town_house_steppe_d", (-100,-100),(100,100),-100,"0",
    ["exit"],[]),

  ("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_snow_forest",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),


  ("enterprise_tannery",sf_generate,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0x000000012004480500040902000041cb00005ae800000ff5",
    [],[]),
  ("enterprise_winery",sf_indoors,"winery_interior", "bo_winery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_mill",sf_indoors,"mill_interior", "bo_mill_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_smithy",sf_indoors,"smithy_interior", "bo_smithy_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_dyeworks",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_linen_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_wool_weavery",sf_indoors,"weavery_interior", "bo_weavery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_brewery",sf_indoors,"brewery_interior", "bo_brewery_interior", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("enterprise_oil_press",sf_indoors,"oil_press_interior", "bo_oil_press_interior", (-40,-40),(40,40),-100,"0",
    [],[]),

#Freelancer Scenes
  ("duel_scene",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_plain"),

 # New Convo Scenes - Kham
  ("conversation_scene_tld_plain",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_plain"),
  ("conversation_scene_tld_snow",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"outer_terrain_snow"),
  ("conversation_scene_tld_forest",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x00000006300005000002308c00003005000018b300001d92",[],[],"forest_wall"),

]