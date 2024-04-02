
50
52
def uvod():
    print("Vítejte v programu kalkulačka...")
    print("Tato kalkulačka umožňuje provádět základní vypocty")
    print("Začněte zadáním prvního čísla.")

def vypocet():
    while True:
        cislo1 = float(input("Zadejte první číslo: "))
        operator = input("Zadejte operátor (+, -, *, /, ** pro mocninu, sqrt pro odmocninu): ")
        
        if operator == 'sqrt':
            print("Odmocnina z", cislo1, "je", math.sqrt(cislo1))
        else:
            cislo2 = float(input("Zadejte druhé číslo: "))
            if operator == '+':
                print("Výsledek:", cislo1 + cislo2)
            elif operator == '-':
                print("Výsledek:", cislo1 - cislo2)
            elif operator == '*':
                print("Výsledek:", cislo1 * cislo2)
            elif operator == '/':
                if cislo2 == 0:
                    print("Chyba: Nelze dělit nulou.")
                else:
                    print("Výsledek:", cislo1 / cislo2)
            elif operator == '**':
                print("Výsledek:", cislo1 ** cislo2)
            else:
                print("Chyba: Neplatný operátor.")

        pokracovat = input("Chcete provést další výpočet? (ano/ne): ")
        if pokracovat.lower() != 'ano':
            break

def zaver():
    print("Děkujeme, že jste použili kalkulačku. Hezký den!")

def kalkulacka():
    uvod()
    vypocet()
    zaver()

if __name__ == "__main__":
    kalkulacka()