from breed import *
from shelter import *
from dog import *

pug = Breeds("Pug", 10.5, 0.55)
bullterrier = Breeds("Bullterrier", 12, 0.75)
boxer = Breeds("Boxer", 8, 0.8)

sh1 = Shelter("Moscow, Kuzminkri str., h.13", "2022-10-10", "Rogov Andrew")
sh2 = Shelter("Moscow, Kremlin str., h.1", "2019-09-11", "Sergey Savchenko")
sh3 = Shelter("Moscow, Okskay str., h.19", "2000-09-01", "Mazhorov Ilia")

d1 = Dogs(pug, "Nikitas", sh1)
d2 = Dogs(boxer, "Andrew", sh2)
print(d1==d2)
print(d1)
print(d1>d2)