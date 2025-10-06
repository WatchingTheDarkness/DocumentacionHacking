# 4 - like1000

## Descripcion:
* This .tar file got tarred a lot.
* Try and script this, it'll save you a lot of time

## Solucion:
* wget https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar
* for i in {1000..1}; do tar -xf $i.tar && rm $i.tar ; done
* picoCTF{l0t5_0f_TAR5}

## Notas:

## Referencias: