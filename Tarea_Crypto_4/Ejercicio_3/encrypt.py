import socket
import re
from Crypto.Util.number import long_to_bytes
import math

# Tus valores iniciales
n1 = 26755116905035262789998904594091972243604809855247642478209157702796475822930601924102479258823213629004473638710091609419186372592588113105462135907092786
e = 65537
c1 = 20729061661321475017889337504644962651717398577008157971448147558025240474917653212836209529733103892407060983650238824381980372177530238133212988984320877

def get_rsa_values(host, port):
    """Conectar al servicio y obtener N, e, c"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(4096).decode()
        s.close()
        
        # Extraer N, e, c del output
        n_match = re.search(r'N: (\d+)', data)
        e_match = re.search(r'e: (\d+)', data)  
        c_match = re.search(r'cyphertext: (\d+)', data)
        
        if n_match and e_match and c_match:
            n = int(n_match.group(1))
            e = int(e_match.group(1))
            c = int(c_match.group(1))
            return n, e, c
    except Exception as e:
        print(f"Error: {e}")
    return None, None, None

def break_with_common_factor():
    host = "verbal-sleep.picoctf.net"
    port = 50206
    
    print("Tus valores iniciales:")
    print(f"N1 = {n1}")
    print(f"e = {e}")
    print(f"c1 = {c1}")
    print()
    
    # Obtener varios N más del servicio
    other_ns = []
    for i in range(5):
        print(f"Obteniendo N adicional {i+1}/5...")
        n, e_new, c = get_rsa_values(host, port)
        if n and n != n1:  # Solo si es diferente al que ya tenemos
            other_ns.append(n)
            print(f"  N{i+2} = {n}")
            
            # Verificar GCD con nuestro N1
            gcd_val = math.gcd(n1, n)
            print(f"  GCD(N1, N{i+2}) = {gcd_val}")
            
            if gcd_val > 1 and gcd_val < n1:
                print("🎯 ¡FACTOR COMÚN ENCONTRADO!")
                p = gcd_val
                q = n1 // p
                
                # Verificar factorización
                if p * q == n1:
                    print("✓ Factorización correcta")
                    
                    # Calcular clave privada
                    phi = (p - 1) * (q - 1)
                    d = pow(e, -1, phi)
                    
                    # Descifrar
                    m = pow(c1, d, n1)
                    flag = long_to_bytes(m)
                    
                    print(f"\n🚩 FLAG: {flag.decode()}")
                    return flag.decode()
    
    print("\nNo se encontró factor común con estos N. Probando más...")
    
    # Si no encontramos, probar con más conexiones
    for i in range(10):
        print(f"Obteniendo N adicional {i+6}/15...")
        n, e_new, c = get_rsa_values(host, port)
        if n and n != n1:
            gcd_val = math.gcd(n1, n)
            if gcd_val > 1 and gcd_val < n1:
                print("🎯 ¡FACTOR COMÚN ENCONTRADO!")
                p = gcd_val
                q = n1 // p
                
                if p * q == n1:
                    phi = (p - 1) * (q - 1)
                    d = pow(e, -1, phi)
                    m = pow(c1, d, n1)
                    flag = long_to_bytes(m)
                    print(f"\n🚩 FLAG: {flag.decode()}")
                    return flag.decode()
    
    return None

# Ejecutar
if __name__ == "__main__":
    flag = break_with_common_factor()
    
    if not flag:
        print("No se pudo encontrar la flag. El servicio podría estar generando N únicos.")