import hashlib
import socket

def solve_hashcrack():
    host = "verbal-sleep.picoctf.net"
    port = 57223
    
    # Conectar al servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Leer el primer mensaje y responder
    welcome = s.recv(1024).decode()
    print("Primer hash:")
    print(welcome)
    
    # Primer hash: MD5 de "password123"
    s.send(b"password123\n")
    
    # Recibir segundo hash
    second_response = s.recv(1024).decode()
    print("Segundo hash:")
    print(second_response)
    
    # Extraer el segundo hash
    second_hash = "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3"
    
    # Probar contraseñas comunes para SHA-1
    passwords_to_try = [
        "letmein", "michael", "monkey", "shadow", "master",
        "qwerty", "dragon", "mustang", "baseball", "iloveyou",
        "trustno1", "jordan", "harley", "password", "password1",
        "password123", "admin", "picoctf", "secret", "hello"
    ]
    
    password_found = None
    for pwd in passwords_to_try:
        sha1_hash = hashlib.sha1(pwd.encode()).hexdigest()
        if sha1_hash == second_hash:
            password_found = pwd
            print(f"✅ Segundo hash crackeado: '{pwd}'")
            break
        else:
            print(f"❌ {pwd} -> {sha1_hash}")
    
    if password_found:
        # Enviar segunda contraseña
        s.send(f"{password_found}\n".encode())
        
        # Recibir la flag
        final_response = s.recv(4096).decode()
        print("Respuesta final:")
        print(final_response)
    else:
        print("❌ No se pudo crackear el segundo hash")
    
    s.close()

# Ejecutar
solve_hashcrack()