#!/usr/bin/env python3
import base64
import re

data = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg=="

def try_b64_decode(s):
    """Intenta decodificar s como Base64; devuelve bytes o None si falla."""
    try:
        # base64.b64decode aceptará str o bytes; pero rechazará si no es base64 válido.
        return base64.b64decode(s, validate=True)
    except Exception:
        return None

def clean_repr_bytes(s):
    """
    Si s es la representación 'b'...'' (incluye la letra b y comillas),
    extrae el contenido interno. También elimina saltos de línea y comillas.
    """
    # s puede venir con \n al final
    s = s.strip()
    # patrón para b'...'
    m = re.match(r"^b['\"](.*)['\"]$", s)
    if m:
        return m.group(1)
    # si no, quitar comillas exteriores si las hubiera
    return s.strip("'\"")

# empezamos con la cadena original
current = data
layers = 0
# intentamos hasta 10 capas por seguridad
for i in range(10):
    # limpiamos espacios y saltos
    candidate = current.strip()
    # Si candidate parece la representación b'...'
    candidate = clean_repr_bytes(candidate)

    decoded = try_b64_decode(candidate)
    if decoded is None:
        break

    layers += 1
    # intentamos decodificar a texto utf-8; si falla, lo mostramos en latin1
    try:
        text = decoded.decode('utf-8')
    except Exception:
        text = decoded.decode('latin1')

    print(f"[layer {layers}] decoded => {repr(text)}")
    current = text

print("\nCAPAS DECODIFICADAS:", layers)
print("RESULTADO FINAL (raw):")
print(current)
