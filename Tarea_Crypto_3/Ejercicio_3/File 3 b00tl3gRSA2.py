from Crypto.Util.number import long_to_bytes
import gmpy2

c = 52497954820732785916694430709381989585222734861621810312044158352841984853316193833257902203639983869401699990309731097449568092397200809915830344986135466893943301638624435431369866092474264520437169918529123920338758561450844244523671868671753302122215275875947625584390267895380512862079082197376624985979
n = 98157075702365631976978960236087576496176915233236631553220393020774789603921213070680144195499821718799205640375982930161348699575782333453716884967853381496651368799077607386792815882960473399697734164959530631522267171905389225069473489609672676589724488900920415051516373739715131856868427118639695340029
e_large = 81655028613108196740053953234222783816700020470891678222225957964197640331662734263094294541929822547373451520631982137868174767721624075523188288319001440660669364584432049266584646553831861040893951380883603664101937287445180652269653454577910144512569920455020241194915050329982009265026372131827383560193

print("=== ENFOQUE ALTERNATIVO ===")
print("Probando si e_large podría ser φ(n) o relacionado con φ(n)")

# El valor e_large es extremadamente grande - podría ser φ(n) o d
# Si e_large = φ(n), entonces podemos encontrar d fácilmente

common_es = [3, 17, 65537]

for e_real in common_es:
    print(f"\nProbando con e_real = {e_real}")
    
    try:
        # Si e_large es φ(n), entonces d = e_real^-1 mod e_large
        d_real = gmpy2.invert(e_real, e_large)
        
        # Descifrar
        m = pow(c, d_real, n)
        flag_bytes = long_to_bytes(m)
        
        # Verificar si es texto legible
        try:
            flag_text = flag_bytes.decode('utf-8')
            print(f"Texto decodificado: {flag_text[:100]}")  # Mostrar primeros 100 caracteres
            
            # Buscar patrones de flag
            if 'pico' in flag_text.lower() or 'ctf' in flag_text.lower():
                print(f"¡FLAG ENCONTRADA!: {flag_text}")
                break
        except:
            # Si no es UTF-8, mostrar hex
            print(f"No es UTF-8, hex: {flag_bytes.hex()[:100]}")
            
    except Exception as e:
        print(f"Error con e={e_real}: {e}")

print("\n=== OTRA POSIBILIDAD: e_large podría ser el mensaje original ===")
# ¿Y si el "ciphertext" que nos dieron no es realmente el ciphertext?
# Podría ser que e_large sea el mensaje y necesitemos encontrar la verdadera relación

# Probemos calcular m = c^d mod n con d pequeños
for d_small in [65537, 17, 3]:
    try:
        m = pow(c, d_small, n)
        flag_bytes = long_to_bytes(m)
        try:
            flag_text = flag_bytes.decode('utf-8')
            print(f"Con d={d_small}: {flag_text[:100]}")
            if 'pico' in flag_text.lower():
                print(f"¡FLAG!: {flag_text}")
        except:
            pass
    except:
        pass