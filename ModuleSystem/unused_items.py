from module_troops import troops

item_set = []
troop_items = []
unused_items = []

print ("Grabbing item names and values from ID_items.py")
item_IDs = open("ID_items.py", "r")

for i, line in enumerate(item_IDs):
  numberPos = line.find('=') + 2
  namePos = numberPos - 3
  name = line[4:namePos]
  number = line[numberPos:-1]
  item_set.append([name, int(number)])

print (str(len(item_set)) + " items found")

print ("Grabbing item values from module_troops.py")
for i, v in enumerate(troops):
  for j, b in enumerate(v[7]):
    if (troop_items.count(b) == 0):
      troop_items.append(b)
      
print (str(len(troop_items)) + " items used by troops")

item_used = False

for i, v in enumerate(item_set):
  item_used = False
  for j, b in enumerate(troop_items):
    if (b == v[1]):
      item_used = True
  
  if (not item_used):
    unused_items.append(v[0])
        
print (str(len(unused_items)) + " unused item names saved to unused_items.txt")

file = open("unused_items.txt", "w")

for i, v in enumerate(unused_items):
  file.write(unused_items[i] + '\n')

file.close()

print ("Finished")