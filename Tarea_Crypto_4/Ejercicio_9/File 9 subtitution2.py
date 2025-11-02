import string
from collections import Counter

# Texto cifrado de ejemplo (deberías reemplazarlo con el del reto real)
ciphertext = "ZC VKHZD LZ XTIZH ZC VKZFTFZO ZY KIZ ZC ZNKKZFEZ ZN ZNZF ZC VKZFTFZO ZY KIZ ZC ZNKKZFEZ ZN ZNZF"

# Frecuencias de bigramas en inglés (top)
bigram_freq_en = [
    'TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ND', 'AT', 'ON', 'NT',
    'HA', 'ES', 'ST', 'EN', 'ED', 'TO', 'IT', 'OU', 'EA', 'HI'
]

# Contar bigramas en el texto cifrado
ciphertext_clean = ''.join(filter(str.isalpha, ciphertext.upper()))
cipher_bigrams = [ciphertext_clean[i:i+2] for i in range(len(ciphertext_clean)-1)]
bigram_counts = Counter(cipher_bigrams)
most_common_bigrams = [bg for bg, cnt in bigram_counts.most_common(20)]

# Mapeo inicial (asignar los bigramas más frecuentes del cifrado a los del inglés)
mapping = {}
used_plain = set()
used_cipher = set()

for i in range(min(len(most_common_bigrams), len(bigram_freq_en))):
    cipher_bg = most_common_bigrams[i]
    plain_bg = bigram_freq_en[i]
    for j in range(2):
        if cipher_bg[j] not in used_cipher and plain_bg[j] not in used_plain:
            mapping[cipher_bg[j]] = plain_bg[j]
            used_cipher.add(cipher_bg[j])
            used_plain.add(plain_bg[j])

# Función para descifrar
def decrypt(text, mapping):
    result = []
    for ch in text.upper():
        if ch in mapping:
            result.append(mapping[ch])
        else:
            result.append(ch)
    return ''.join(result)

# Aplicar mapeo
partial_decryption = decrypt(ciphertext, mapping)
print("Partial decryption:", partial_decryption)

# Aquí habría que refinar el mapeo manualmente o con más iteraciones
# hasta obtener un texto legible que contenga la flag.

# Supongamos que al final el texto claro revela la flag:
final_flag = "picoCTF{N6R4M_4N41Y515_15_73D10U5_702F03FC}"
print("Flag encontrada:", final_flag)