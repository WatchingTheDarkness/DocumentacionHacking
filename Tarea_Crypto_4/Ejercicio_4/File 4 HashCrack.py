import hashlib
import socket

def solve_hashcrack():
    host = "verbal-sleep.picoctf.net"
    port = 57223
    
    # Conectar al servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Leer el mensaje de bienvenida y el hash
    welcome = s.recv(1024).decode()
    print("Servidor:")
    print(welcome)
    
    # Extraer el hash (ya lo sabemos: 482c811da5d5b4bc6d497ffa98491e38)
    target_hash = "482c811da5d5b4bc6d497ffa98491e38"
    
    # Este es un hash MD5 conocido - es "password123"
    # Verificación:
    test_hash = hashlib.md5("password123".encode()).hexdigest()
    if test_hash == target_hash:
        print(f"✅ Hash verificado: 'password123' -> {test_hash}")
        password = "password123"
    else:
        # Si no es password123, probamos otras
        passwords_to_try = [
            "password123", "password", "123456", "admin", 
            "Password123", "P@ssw0rd", "picoctf"
        ]
        
        for pwd in passwords_to_try:
            if hashlib.md5(pwd.encode()).hexdigest() == target_hash:
                password = pwd
                print(f"✅ Contraseña encontrada: {password}")
                break
        else:
            print("❌ No se pudo encontrar la contraseña")
            return
    
    # Enviar la contraseña
    print(f"Enviando contraseña: {password}")
    s.send(f"{password}\n".encode())
    
    # Recibir respuesta
    response = s.recv(4096).decode()
    print("Respuesta del servidor:")
    print(response)
    
    # Continuar recibiendo datos si hay más
    while True:
        try:
            more_data = s.recv(1024).decode()
            if not more_data:
                break
            print(more_data)
        except:
            break
    
    s.close()

# Ejecutar
solve_hashcrack()