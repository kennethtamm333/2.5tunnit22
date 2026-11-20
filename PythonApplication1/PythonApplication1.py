import random
from datetime import date
 
def ülesanne1():
    a = float(input("Sisesta a"))
    b = float(input("Sisesta b"))
    c = float(input("Sisesta c"))

    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a) 
        x2 = (-b - D ** 0.5) / (2 * a)
        print("Kaks lahendit:", x1, x2)
    else:
     if D == 0:
      x1= -b / (2 * a)
      print("Üks lahend:", x1)
     else: 
       print("Reaalarvulised lahendid puuduvad")

def ülesanne2():
     
    tunnid = float(input("Sisesta töötunnid nädalas => "))
    tunnitasu = float(input("Sisesta tunnitasu (€) => "))
     
    if tunnid < 0 and tunnid > 168:
         print("Vigane tundide arv")
    elif tunnid <= 40:
     palk = tunnid * tunnitasu
     print("Nädalapalk:", palk, "€")
    else:
     palk = 40 * tunnitasu + (tunnid - 40) * tunnitasu * 1,5
    print("Nädalapalk koos ületundidega:", palk, "€")
    print()
    
def ülesanne3():
    
   tunnid = int(input("Sisesta parkimise aeg tundides => "))
   if tunnid <= 0:
     print("Vigane aeg")
   elif tunnid <= 3:
         print("Hind: 5 €")
   elif tunnid >= 8:
         print("Hind: 10 € (päevapilet)")
   else:
        print("Hind: 2 €")

#Programmi tulemus:
 

#Ruutvõrrandi lahendamine
#Sisesta a => 2
#Sisesta b => -6
#Sisesta c => 4
#Kaks lahendit: 2.0 1.0

#Palga arvutamine
#Sisesta töötunnid nädalas => 45
#Sisesta tunnitasu (€) => 10
#Nädalapalk koos ületundidega: 475.0 €

#Parkimise hind
#Sisesta parkimise aeg tundides => 10
#Hind: 10 € (päevapilet)


while True:
    print("\n================================")
    print("       ülesanded")
    print("================================")
    print("1. RUUTVÕRRAND")
    print("2. PALGA ARVUTAMINE")
    print("3. PARKIMISE HIND")
    print("================================")

    valik = input("Vali ülesanne (0-14): ")

    if valik == "1":
        ülesanne1()
    elif valik == "2":
        ülesanne2()
    elif valik == "3":
        ülesanne3()