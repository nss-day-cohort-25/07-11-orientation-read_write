
# permission oprions: r: read only, w: write only, a: appending, r+: read and write
with open("test.txt", 'w') as testfile:
  testfile.write("Hello, C25. Hope you're having a great day.")

with open("test.txt", 'a') as testfile:
  testfile.write("Hello, C25. Hope you're awake.")

nickset = {"The Mooch", "Knuckles", "Burninator", "Kneecap", "Ole Red", "Bubba",
           "OG", "KitKat", "Spanky", "Monkeybutt", "L`il Devil", "Bird Person", "Fancy Slacks"}

nameset = {"Bob Smith", "Charise Anderson", "Jissie David", "Henry Goldberg", "Greg Korte", "Steve Brownlee", "Kimmy Bird", "Joe Shepherd", "Emily Lemmon", "Brenda Long", "Harold Brown", "Megan Ducharme", "Darth Vader"}

with open("data/nicknames.txt", "w") as nicknames:
  for nick in nickset:
    nicknames.write(nick + '\n')

with open("data/names.txt", "w") as names:
  for name in nameset:
    names.write(name + '\n')

# later, back at the batcave...``
with open("data/names.txt", "r") as names:
  namelist = names.readlines()

with open("data/nicknames.txt", "r") as nicks:
  nicklist = nicks.readlines()

mob_names = [f"{name.strip().split(' ')[0]} \"{nicklist[i].strip()}\" {name.strip().split(' ')[1]}" for i, name in enumerate(namelist)]

print(mob_names)

