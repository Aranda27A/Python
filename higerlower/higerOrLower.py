# Dataset para juego Higher or Lower - Personas más ricas del mundo
# Valores de fortuna en miles de millones de USD (aproximados)

personas_ricas = [
    {"nombre": "Elon Musk", "ocupacion": "CEO Tesla/SpaceX", "fortuna": 230, "pais": "Estados Unidos"},
    {"nombre": "Jeff Bezos", "ocupacion": "Fundador Amazon", "fortuna": 170, "pais": "Estados Unidos"},
    {"nombre": "Bernard Arnault", "ocupacion": "CEO LVMH", "fortuna": 211, "pais": "Francia"},
    {"nombre": "Bill Gates", "ocupacion": "Cofundador Microsoft", "fortuna": 129, "pais": "Estados Unidos"},
    {"nombre": "Warren Buffett", "ocupacion": "Inversor/Berkshire Hathaway", "fortuna": 120, "pais": "Estados Unidos"},
    {"nombre": "Larry Ellison", "ocupacion": "Cofundador Oracle", "fortuna": 141, "pais": "Estados Unidos"},
    {"nombre": "Mark Zuckerberg", "ocupacion": "CEO Meta/Facebook", "fortuna": 123, "pais": "Estados Unidos"},
    {"nombre": "Larry Page", "ocupacion": "Cofundador Google", "fortuna": 114, "pais": "Estados Unidos"},
    {"nombre": "Sergey Brin", "ocupacion": "Cofundador Google", "fortuna": 110, "pais": "Estados Unidos"},
    {"nombre": "Steve Ballmer", "ocupacion": "Ex-CEO Microsoft", "fortuna": 118, "pais": "Estados Unidos"},
    {"nombre": "Mukesh Ambani", "ocupacion": "Chairman Reliance Industries", "fortuna": 92, "pais": "India"},
    {"nombre": "Gautam Adani", "ocupacion": "Fundador Adani Group", "fortuna": 84, "pais": "India"},
    {"nombre": "Françoise Bettencourt Meyers", "ocupacion": "Heredera L'Oréal", "fortuna": 95, "pais": "Francia"},
    {"nombre": "Carlos Slim", "ocupacion": "Empresario/Telecom", "fortuna": 81, "pais": "México"},
    {"nombre": "Amancio Ortega", "ocupacion": "Fundador Zara/Inditex", "fortuna": 89, "pais": "España"},
    {"nombre": "Michael Bloomberg", "ocupacion": "Fundador Bloomberg LP", "fortuna": 96, "pais": "Estados Unidos"},
    {"nombre": "Jim Walton", "ocupacion": "Heredero Walmart", "fortuna": 68, "pais": "Estados Unidos"},
    {"nombre": "Rob Walton", "ocupacion": "Heredero Walmart", "fortuna": 67, "pais": "Estados Unidos"},
    {"nombre": "Alice Walton", "ocupacion": "Heredera Walmart", "fortuna": 66, "pais": "Estados Unidos"},
    {"nombre": "Zhong Shanshan", "ocupacion": "Fundador Nongfu Spring", "fortuna": 62, "pais": "China"},
    {"nombre": "Charles Koch", "ocupacion": "CEO Koch Industries", "fortuna": 64, "pais": "Estados Unidos"},
    {"nombre": "Julia Koch", "ocupacion": "Heredera Koch Industries", "fortuna": 64, "pais": "Estados Unidos"},
    {"nombre": "Francois Pinault", "ocupacion": "Fundador Kering", "fortuna": 42, "pais": "Francia"},
    {"nombre": "Michael Dell", "ocupacion": "Fundador Dell Technologies", "fortuna": 71, "pais": "Estados Unidos"},
    {"nombre": "Giovanni Ferrero", "ocupacion": "CEO Ferrero", "fortuna": 43, "pais": "Italia"},
    {"nombre": "Jacqueline Mars", "ocupacion": "Heredera Mars Inc", "fortuna": 38, "pais": "Estados Unidos"},
    {"nombre": "John Mars", "ocupacion": "Heredero Mars Inc", "fortuna": 38, "pais": "Estados Unidos"},
    {"nombre": "Phil Knight", "ocupacion": "Cofundador Nike", "fortuna": 45, "pais": "Estados Unidos"},
    {"nombre": "MacKenzie Scott", "ocupacion": "Filantropa/Ex Amazon", "fortuna": 38, "pais": "Estados Unidos"},
    {"nombre": "Len Blavatnik", "ocupacion": "Inversor/Access Industries", "fortuna": 32, "pais": "Reino Unido"},
    {"nombre": "Tadashi Yanai", "ocupacion": "Fundador Uniqlo/Fast Retailing", "fortuna": 37, "pais": "Japón"},
    {"nombre": "Jorge Paulo Lemann", "ocupacion": "Inversor/3G Capital", "fortuna": 15, "pais": "Brasil"},
    {"nombre": "Li Ka-shing", "ocupacion": "Inversor/CK Hutchison", "fortuna": 36, "pais": "Hong Kong"},
    {"nombre": "Colin Huang", "ocupacion": "Fundador Pinduoduo", "fortuna": 48, "pais": "China"},
    {"nombre": "Ma Huateng", "ocupacion": "Fundador Tencent", "fortuna": 44, "pais": "China"},
    {"nombre": "Zhang Yiming", "ocupacion": "Fundador ByteDance/TikTok", "fortuna": 49, "pais": "China"},
    {"nombre": "Dieter Schwarz", "ocupacion": "Fundador Lidl/Schwarz Gruppe", "fortuna": 47, "pais": "Alemania"},
    {"nombre": "Klaus-Michael Kühne", "ocupacion": "Chairman Kühne + Nagel", "fortuna": 35, "pais": "Alemania"},
    {"nombre": "Beate Heister", "ocupacion": "Heredera Aldi Süd", "fortuna": 34, "pais": "Alemania"},
    {"nombre": "Karl Albrecht Jr", "ocupacion": "Heredero Aldi Süd", "fortuna": 34, "pais": "Alemania"},
    {"nombre": "David Thomson", "ocupacion": "Chairman Thomson Reuters", "fortuna": 41, "pais": "Canadá"},
    {"nombre": "Gina Rinehart", "ocupacion": "Minería/Hancock Prospecting", "fortuna": 30, "pais": "Australia"},
    {"nombre": "Miriam Adelson", "ocupacion": "Heredera Las Vegas Sands", "fortuna": 32, "pais": "Estados Unidos"},
    {"nombre": "Susanne Klatten", "ocupacion": "Heredera BMW", "fortuna": 28, "pais": "Alemania"},
    {"nombre": "Stefan Quandt", "ocupacion": "Heredero BMW", "fortuna": 26, "pais": "Alemania"},
    {"nombre": "Jensen Huang", "ocupacion": "CEO Nvidia", "fortuna": 70, "pais": "Estados Unidos"},
    {"nombre": "Germán Larrea", "ocupacion": "CEO Grupo México", "fortuna": 27, "pais": "México"},
    {"nombre": "Lee Shau Kee", "ocupacion": "Fundador Henderson Land", "fortuna": 29, "pais": "Hong Kong"},
    {"nombre": "Abigail Johnson", "ocupacion": "CEO Fidelity Investments", "fortuna": 28, "pais": "Estados Unidos"},
    {"nombre": "John Menard Jr", "ocupacion": "Fundador Menards", "fortuna": 22, "pais": "Estados Unidos"},
    {"nombre": "Thomas Frist Jr", "ocupacion": "Fundador HCA Healthcare", "fortuna": 23, "pais": "Estados Unidos"},
    {"nombre": "Lukas Walton", "ocupacion": "Heredero Walmart", "fortuna": 26, "pais": "Estados Unidos"},
    {"nombre": "Iris Fontbona", "ocupacion": "Minería/Antofagasta PLC", "fortuna": 23, "pais": "Chile"},
    {"nombre": "He Xiangjian", "ocupacion": "Fundador Midea Group", "fortuna": 28, "pais": "China"},
    {"nombre": "Alain Wertheimer", "ocupacion": "Propietario Chanel", "fortuna": 40, "pais": "Francia"},
    {"nombre": "Gerard Wertheimer", "ocupacion": "Propietario Chanel", "fortuna": 40, "pais": "Francia"},
    {"nombre": "Rafaela Aponte-Diamant", "ocupacion": "Shipping/MSC", "fortuna": 32, "pais": "Suiza"},
    {"nombre": "Gianluigi Aponte", "ocupacion": "Fundador MSC", "fortuna": 32, "pais": "Suiza"},
    {"nombre": "Leonard Lauder", "ocupacion": "Heredero Estée Lauder", "fortuna": 27, "pais": "Estados Unidos"},
    {"nombre": "Wang Wei", "ocupacion": "Fundador SF Express", "fortuna": 24, "pais": "China"},
    {"nombre": "Li Xiting", "ocupacion": "Cofundador Mindray Medical", "fortuna": 22, "pais": "Singapur"},
    {"nombre": "Xu Hang", "ocupacion": "Cofundador Mindray Medical", "fortuna": 20, "pais": "China"},
    {"nombre": "Vladimir Potanin", "ocupacion": "CEO Nornickel", "fortuna": 31, "pais": "Rusia"},
    {"nombre": "Vagit Alekperov", "ocupacion": "Fundador Lukoil", "fortuna": 24, "pais": "Rusia"},
    {"nombre": "Leonid Mikhelson", "ocupacion": "Chairman Novatek", "fortuna": 27, "pais": "Rusia"},
    {"nombre": "Alexey Mordashov", "ocupacion": "Chairman Severstal", "fortuna": 26, "pais": "Rusia"},
    {"nombre": "Emmanuel Besnier", "ocupacion": "CEO Lactalis", "fortuna": 21, "pais": "Francia"},
    {"nombre": "Reinhold Würth", "ocupacion": "Chairman Würth Group", "fortuna": 19, "pais": "Alemania"},
    {"nombre": "Eric Schmidt", "ocupacion": "Ex-CEO Google", "fortuna": 25, "pais": "Estados Unidos"},
    {"nombre": "Shiv Nadar", "ocupacion": "Fundador HCL Technologies", "fortuna": 29, "pais": "India"},
    {"nombre": "Cyrus Poonawalla", "ocupacion": "Fundador Serum Institute", "fortuna": 21, "pais": "India"},
    {"nombre": "Radhakishan Damani", "ocupacion": "Fundador DMart", "fortuna": 20, "pais": "India"},
    {"nombre": "Savitri Jindal", "ocupacion": "Chairman OP Jindal Group", "fortuna": 18, "pais": "India"},
    {"nombre": "Azim Premji", "ocupacion": "Chairman Wipro", "fortuna": 22, "pais": "India"},
    {"nombre": "Uday Kotak", "ocupacion": "Fundador Kotak Mahindra Bank", "fortuna": 15, "pais": "India"},
    {"nombre": "Lakshmi Mittal", "ocupacion": "Chairman ArcelorMittal", "fortuna": 17, "pais": "Reino Unido"},
    {"nombre": "Andreas von Bechtolsheim", "ocupacion": "Cofundador Sun Microsystems", "fortuna": 16, "pais": "Estados Unidos"},
    {"nombre": "James Simons", "ocupacion": "Fundador Renaissance Technologies", "fortuna": 31, "pais": "Estados Unidos"},
    {"nombre": "Dustin Moskovitz", "ocupacion": "Cofundador Facebook/Asana", "fortuna": 17, "pais": "Estados Unidos"},
    {"nombre": "Eduardo Saverin", "ocupacion": "Cofundador Facebook", "fortuna": 18, "pais": "Singapur"},
    {"nombre": "Jan Koum", "ocupacion": "Cofundador WhatsApp", "fortuna": 15, "pais": "Estados Unidos"},
    {"nombre": "Brian Chesky", "ocupacion": "CEO Airbnb", "fortuna": 14, "pais": "Estados Unidos"},
    {"nombre": "Bobby Murphy", "ocupacion": "Cofundador Snapchat", "fortuna": 13, "pais": "Estados Unidos"},
    {"nombre": "Evan Spiegel", "ocupacion": "CEO Snapchat", "fortuna": 13, "pais": "Estados Unidos"},
    {"nombre": "Daniel Gilbert", "ocupacion": "Fundador Quicken Loans", "fortuna": 20, "pais": "Estados Unidos"},
    {"nombre": "Harold Hamm", "ocupacion": "CEO Continental Resources", "fortuna": 18, "pais": "Estados Unidos"},
    {"nombre": "Donald Bren", "ocupacion": "Chairman Irvine Company", "fortuna": 17, "pais": "Estados Unidos"},
    {"nombre": "Stephen Schwarzman", "ocupacion": "CEO Blackstone", "fortuna": 37, "pais": "Estados Unidos"},
    {"nombre": "Ken Griffin", "ocupacion": "CEO Citadel", "fortuna": 35, "pais": "Estados Unidos"},
    {"nombre": "Ray Dalio", "ocupacion": "Fundador Bridgewater Associates", "fortuna": 19, "pais": "Estados Unidos"},
    {"nombre": "Carl Icahn", "ocupacion": "Inversor activista", "fortuna": 24, "pais": "Estados Unidos"},
    {"nombre": "George Soros", "ocupacion": "Inversor/Filántropo", "fortuna": 8.6, "pais": "Estados Unidos"},
    {"nombre": "Rupert Murdoch", "ocupacion": "Fundador News Corp", "fortuna": 17, "pais": "Estados Unidos"},
    {"nombre": "Elon Musk's Mother", "ocupacion": "Modelo/Dietista", "fortuna": 0.45, "pais": "Canadá"},
    {"nombre": "Jack Ma", "ocupacion": "Cofundador Alibaba", "fortuna": 34, "pais": "China"},
    {"nombre": "Lei Jun", "ocupacion": "Fundador Xiaomi", "fortuna": 19, "pais": "China"},
    {"nombre": "Robin Zeng", "ocupacion": "Fundador CATL", "fortuna": 33, "pais": "China"},
    {"nombre": "William Ding", "ocupacion": "Fundador NetEase", "fortuna": 23, "pais": "China"},
]

# Ejemplo de uso para el juego Higher or Lower
#if __name__ == "__main__":
#    print(f"Total de personas en el dataset: {len(personas_ricas)}")
#    print(f"\nEjemplo de datos:")
#    for i in range(5):
#        persona = personas_ricas[i]
#        print(f"{i+1}. {persona['nombre']} - {persona['ocupacion']}")
#        print(f"   Fortuna: ${persona['fortuna']} mil millones - {persona['pais']}")
#        print()
#

import random

Points = 0


def startGame():
    comparacion = []
    for i in range(2):

     posicion1 = personas_ricas[random.randrange(0, len(personas_ricas))]
     comparacion.append(posicion1)

     
    return comparacion

def newRandom():
   
   newrandom = personas_ricas[random.randrange(0, len(personas_ricas))]
   return newrandom



gameSet = startGame()
is_game_over = False

first = gameSet[0]
second = gameSet[1]
    

while not is_game_over: 
   
    guess = input(f"Do you think that {first['nombre']} which has {first['fortuna']} billions has more network than {second['nombre']} ")
    if guess == 'y':
        if first['fortuna'] > second['fortuna']:
           print("correcto")
           print(second["fortuna"])
           Points += 1
           print(Points)

           second = newRandom()



        else:
           print("Incorrecto")
           print(second['fortuna'])
           is_game_over = True

    elif guess == "n":
           if second['fortuna'] > first['fortuna']:
             print("correcto")
             print(second["fortuna"])
             Points += 1
             print(Points)

             first = second
             second = newRandom()
           




           else:
            print("Incorrecto")
            print(second['fortuna'])
            is_game_over = True



    else:
       is_game_over = True

