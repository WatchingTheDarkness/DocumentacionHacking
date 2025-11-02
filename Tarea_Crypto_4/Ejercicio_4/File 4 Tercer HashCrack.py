import hashlib
import socket
import requests
import os

def download_rockyou():
    """Descargar rockyou.txt si no existe"""
    if not os.path.exists('rockyou.txt'):
        print("Descargando rockyou.txt...")
        url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
        try:
            response = requests.get(url, stream=True)
            with open('rockyou.txt', 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Descarga completada")
        except:
            print("Error descargando rockyou.txt")
            return False
    return True

def crack_with_rockyou(target_hash):
    """Usar rockyou.txt para crackear el hash"""
    try:
        with open('rockyou.txt', 'r', encoding='latin-1') as f:
            for i, line in enumerate(f):
                password = line.strip()
                if hashlib.sha256(password.encode('latin-1')).hexdigest() == target_hash:
                    print(f"🎯 ¡ENCONTRADA en línea {i}: {password}")
                    return password
                if i % 10000 == 0:
                    print(f"Probadas {i} contraseñas...")
    except Exception as e:
        print(f"Error: {e}")
    return None

def solve_with_dictionary():
    host = "verbal-sleep.picoctf.net"
    port = 57223
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    # Primer hash
    s.recv(1024)
    s.send(b"password123\n")
    
    # Segundo hash
    s.recv(1024)
    s.send(b"letmein\n")
    
    # Tercer hash
    s.recv(1024)
    
    target_hash = "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745"
    
    if download_rockyou():
        print("Buscando en rockyou.txt...")
        password = crack_with_rockyou(target_hash)
        
        if password:
            s.send(f"{password}\n".encode())
            response = s.recv(4096).decode()
            print("🎯 RESULTADO:")
            print(response)
        else:
            print("No se encontró en rockyou.txt")
    else:
        print("No se pudo obtener rockyou.txt")
    
    s.close()

# Ejecutar
solve_with_dictionary()