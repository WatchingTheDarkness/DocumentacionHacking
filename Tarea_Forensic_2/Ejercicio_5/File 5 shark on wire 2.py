from scapy.all import *

# Usa la ruta completa al archivo capture.pcap
packets = rdpcap('C:/Users/watch/Downloads/NotasHacking/DocumentacionHacking/Tarea_Forensic_2/Ejercicio_5/capture.pcap')

flag=''

for p in packets:
    if UDP in p and p[UDP].dport == 22: # type: ignore
        if p[UDP].sport > 5000: # type: ignore
            flag+=chr(p[UDP].sport - 5000) # type: ignore

print(flag)