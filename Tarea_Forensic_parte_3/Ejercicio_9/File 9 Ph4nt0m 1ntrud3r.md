# 9 - Ph4nt0m intrud3r

## Descripcion:
* A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!Find the PCAP file here Network Traffic PCAP file and try to get the flag.

## Solucion:
* wget https://challenge-files.picoctf.net/c_verbal_sleep/3fe089c41615b9413666bedca922e07bf6ad8894a3dabd2737735143ad2396cf/myNetworkTraffic.pcap
* picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}

## Notas:
* descargamos el archivo, vemos el tipo de archivo q es ![[Pasted image 20251026003616.png]] vemos los paquetes q hay usando el comando tshark ![[Pasted image 20251026003838.png]] limpiamos la basura y nos da la bandera ![[Pasted image 20251026003723.png]]

## Referencias: