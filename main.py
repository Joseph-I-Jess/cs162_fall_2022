# demo exceptions

import inheritance_basics.inheritance_basics as inh

cat_1 = inh.Cat(tail="short", whiskers="curly")
# we do not need to do this... most of the time
cat_1.__dict__["whiskers"] = "none" # interesting quirk about Python's design🙂!
cat_2 = inh.Cat("short straight", "short")

print(cat_1)
print(f"cat_1 vocalizes like this: \"{cat_1.vocalize()}\"")

print(cat_2)
print(f"cat_2 vocalizes like this: \"{cat_2.vocalize()}\"")

tiger_1 = inh.Tiger()
print(tiger_1)
print(f"tiger_1 vocalizes like this: \"{tiger_1.vocalize()}\"")

house_cat_1 = inh.House_cat()
print(house_cat_1)
print(f"house_cat_1 vocalizes like this: \"{house_cat_1.vocalize()}\"")
