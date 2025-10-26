import gmpy2
from Crypto.Util.number import long_to_bytes

# Valores del problema
c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

# Factorizar n (como n es pequeño, esto es factible)
# Usando factordb.com o alguna herramienta de factorización
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

# Verificar que p * q = n
assert p * q == n

# Calcular phi(n)
phi = (p - 1) * (q - 1)

# Calcular la clave privada d
d = gmpy2.invert(e, phi)

# Descifrar el mensaje
m = pow(c, d, n)

# Convertir a texto
flag = long_to_bytes(m)
print(flag.decode())