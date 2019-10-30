#!/usr/bin/env python
#  from whatever import list

list1 = list()   # calls list.__init__()
list2 = list("wombat")
print(list2)

class Foom:
    def blarf(self):
        print("BLARF BLARF")

foom1 = Foom()  # calls Foom.__init__()
foom2 = Foom()

print(foom1, foom2)

foom1.blarf()  #  Foom.blarf(foom1)
foom2.blarf()  #  Foom.blarf(foom2)

# properties
print(foom1.thing)     #  Foom.thing(foom1)
print(foom1.name)      #  Foom.name(foom1)
foom1.other_name = 5   #  Foom.other_name(foom1, 5)

# getters/setters
print(foom1.get_thing())
print(foom1.get_name())
foom1.set_other_name(5)
