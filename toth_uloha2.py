import argparse
import sys


def main():
    moj_parser = argparse.ArgumentParser(description = "Program, ktorý ráta znaky, slová a riadky v textových súboroch.")
    moj_parser.add_argument("subor", help = "názov vstupného súboru")
    moj_parser.add_argument("--znaky", help = "spočíta znaky", action = "store_true")
    moj_parser.add_argument("--slova", help = "spočíta slová", action = "store_true")
    moj_parser.add_argument("--riadky", help = "spočíta riadky", action = "store_true")
    argumenty = moj_parser.parse_args()

    try:
        subor = open(argumenty.subor, "r")
        obsah = subor.read()
        subor.close()
        cek = False
        
        if argumenty.znaky:
            pocet_znakov = char_counter(obsah)
            print(f"Počet znakov: {pocet_znakov}")
            cek = True
        
        if argumenty.slova:
            pocet_slov = word_counter(obsah)
            print(f"Počet slov: {pocet_slov}")
            cek = True

        if argumenty.riadky:
            pocet_riadkov = line_counter(obsah)
            print(f"Počet riadkov: {pocet_riadkov}")
            cek = True 
            
        if cek == False:
            pocet_znakov = char_counter(obsah) 
            pocet_slov = word_counter(obsah)
            pocet_riadkov = line_counter(obsah)
            print(f"Počet znakov: {pocet_znakov}\nPočet slov: {pocet_slov}\nPočet riadkov: {pocet_riadkov}")

    except:
        print("chyba")
        sys.exit(1)
        

def char_counter(subor):
    pocet_znakov = len(subor)
    return pocet_znakov  
    
def word_counter(subor):
    pocet_slov = subor.count(" ") + len(subor.split("\n"))
    return pocet_slov 
    
def line_counter(subor):
    pocet_riadkov = len(subor.split("\n"))
    return pocet_riadkov   


main()    
            