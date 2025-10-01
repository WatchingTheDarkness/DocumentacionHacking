# 3 - Python Wrangling

## Descripcion:
* Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?
* Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py
* $ man python

## Solucion:
* wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/ende.py
* ls
* wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/pw.txt
* ls
* wget https://mercury.picoctf.net/static/325a52d249be0bd3811421eacd2c877a/flag.txt.en
* ls
* clear
* cat ende.py
* cat pw.txt
* ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
* python3 ende.py -d flag.txt.en ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
* picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}

## Notas:
* descargue los 3 archivos
* vi como era el archivo python
* se utilizaria el cat pw.txt para ver la contraseña
* codigo con -d y la contraseña para ver la bandera
* bandera

## Referencias: