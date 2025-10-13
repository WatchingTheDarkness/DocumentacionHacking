# 5 - MacroHard WeskEdge.md

## Descripcion:
* I've hidden a flag in this file. Can you find it? Forensics is fun.pptm

## Solucion:
* wget https://mercury.picoctf.net/static/2e739f9e0dc9f4c1556ea6b033c3ec8e/Forensics%20is%20fun.pptm
* curl https://mercury.picoctf.net/static/2e739f9e0dc9f4c1556ea6b033c3ec8e/Forensics%20is%20fun.pptm >> funt.pptm
* unzip funt.pptm
* cd ppt/slideMasters/
* strings hidden
* Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
* MacroHard.py
* picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## Notas:

## Referencias:
