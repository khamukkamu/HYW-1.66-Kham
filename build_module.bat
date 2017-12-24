@echo off && title building HYW for [wait for it]--
set PATH="C:\Python24";"C:\Python26";C:\Python27;%PATH%
set PYTHONPATH=%cd%;%cd%\data;%cd%\header;%cd%\id;%cd%\process

:top
cls

python -B -OO process\process_all.py

:: python -B -OO process\process_init.py
:: python -B -OO process\process_global_variables.py
:: python -B -OO process\process_strings.py
:: python -B -OO process\process_skills.py
:: python -B -OO process\process_music.py
:: python -B -OO process\process_animations.py
:: python -B -OO process\process_meshes.py
:: python -B -OO process\process_sounds.py
:: python -B -OO process\process_skins.py
:: python -B -OO process\process_map_icons.py
:: python -B -OO process\process_factions.py
:: python -B -OO process\process_items.py
:: python -B -OO process\process_scenes.py
:: python -B -OO process\process_troops.py
:: python -B -OO process\process_particle_sys.py
:: python -B -OO process\process_scene_props.py
:: python -B -OO process\process_tableau_materials.py
:: python -B -OO process\process_presentations.py
:: python -B -OO process\process_party_tmps.py
:: python -B -OO process\process_parties.py
:: python -B -OO process\process_quests.py
:: python -B -OO process\process_info_pages.py
:: python -B -OO process\process_scripts.py
:: python -B -OO process\process_mission_tmps.py
:: python -B -OO process\process_game_menus.py
:: python -B -OO process\process_simple_triggers.py
:: python -B -OO process\process_dialogs.py
:: python -B -OO process\process_postfx.py
:: python -B -OO process\process_global_variables_unused.py


echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to restart. . .
pause>nul && goto :top
