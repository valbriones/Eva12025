OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

protocolo = input("Ingrese el nombre de un protocolo de enrutamiento (OSPF, RIP, EIGRP, BGP): ").upper()

if protocolo == "OSPF":
    print(f"La distancia administrativa de {protocolo} es {OSPF}.")
elif protocolo == "RIP":
    print(f"La distancia administrativa de {protocolo} es {RIP}.")
elif protocolo == "EIGRP":
    print(f"La distancia administrativa de {protocolo} es {EIGRP}.")
elif protocolo == "BGP":
    print(f"La distancia administrativa de {protocolo} es {BGP}.")
else:
    print("Protocolo no reconocido. Intente con OSPF, RIP, EIGRP o BGP.")