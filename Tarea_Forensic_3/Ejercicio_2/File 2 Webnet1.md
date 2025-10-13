# 2 - WebNet1

## Descripcion:
* We found this packet capture and key. Recover the flag.
* Try using a tool like Wireshark.
* How can you decrypt the TLS stream?

## Solucion:
* ls -la capture.pcap picopico.key
* tshark -r capture.pcap -o ssl.keys_list:0.0.0.0,443,http,picopico.key -q -z follow,ssl,ascii,0
* picoCTF{honey.roasted.peanuts}

## Notas:

## Referencias:
