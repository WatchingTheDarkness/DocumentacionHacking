# 8 - SQL Direct

## Descripcion:
* Connect to this PostgreSQL server and find the flag!
Additional details will be available after launching your challenge instance.
* What does a SQL database contain?

## Solucion:
* psql -h saturn.picoctf.net -p 59135 -U postgres pico
* postgres
* \dt
* select * from flags;
* picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}

## Notas:
* entramos a la tabla sql
* ponemos la contraseña
* generamos una tabla
* le decimos que queremos que seleccione todas las banderas
* bandera

## Referencias: