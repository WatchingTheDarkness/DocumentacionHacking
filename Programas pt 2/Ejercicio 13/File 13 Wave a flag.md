# 13 - Wave a flag

## Descripcion:
* Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...
* This program will only work in the webshell or another Linux computer.
* To get the file accessible in your shell, enter the following in the Terminal prompt: $ wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm
* Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm
* -h and --help are the most common arguments to give to programs to get more information from them!
* Not every program implements help features like -h and --help.

## Solucion:
* wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm
* file warm
* chmod +x warm
* ./warm  
* ./warm -h
* picoCTF{b1scu1ts_4nd_gr4vy_30e77291}

## Notas:
* primero tenemos que descargar el archivo que resulta que es warm
* despues tenemos que ver que archivos tenemos en el archivo
* despues tenemos que darle permisos para revisar los archivos
* buscamos lo que se esta resaltando
* finalizamos teniendo los datos

## Referencias: