def string_corr (filename):
  print "Correcting string line breaks in " + filename
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")
  
  line_break = 0
  last_line = "last line"
  for line in lines:
    is_comment = line.strip().find("#")

    if is_comment != 0:
        
      if line_break > 0:
        line = last_line + line
      
      line_break = line.find("\\\n")
      
      if line_break > 0:
        last_line = line.replace("\\\n", " \" + \"")
        line_break = 1
      
      for x in range(0, 20):
        line = line.replace("  \" + \"", " \" + \"")
        line = line.replace("\" + \" ", "\" + \"")
      
      line = line.replace("^ \" + \"", "^\" + \"")
      line = line.replace("\" + \"", "\" + \n\"")

    if line_break < 1:
      line = line.strip()
      file.write("%s\n"%line)  
  file.close()


def line_corr(filename):
  print "Correcting lines in " + filename
  #string_corr (filename)
  file = open(filename,"r")
  lines = file.readlines()
  file.close()

  file = open(filename,"w")

  level = 0
  for line in lines:
    line = line.strip()
    acceptableindex = line.find("#")
    if (acceptableindex == -1):
        acceptableindex = len(line)
    level -= line.count("try_end", 0, acceptableindex)
    level -= line.count("end_try", 0, acceptableindex)
    level -= line.count("else_try", 0, acceptableindex)
    newlevel = level
    level_positive_change = 0
    newlevel += line.count("else_try", 0, acceptableindex)
    newlevel += line.count("(", 0, acceptableindex)
    newlevel += line.count("[", 0, acceptableindex)
    newlevel += line.count("try_begin", 0, acceptableindex)
    newlevel += line.count("(try_for", 0, acceptableindex)
    level_positive_change = newlevel - level
    newlevel -= line.count(")", 0, acceptableindex)
    newlevel -= line.count("]", 0, acceptableindex)
    if (level_positive_change == 0):
      level = newlevel
    for i in xrange(level):
      file.write("  ")
    level = newlevel
    file.write("%s\n"%line)
  file.close()
    
    


line_corr("module_scripts.py")
line_corr("module_game_menus.py")
line_corr("module_mission_templates.py")
line_corr("module_presentations.py")
line_corr("module_simple_triggers.py")
line_corr("module_triggers.py")
line_corr("module_dialogs.py")
line_corr("multi_missions.py")
#line_corr("multi_scripts.py")