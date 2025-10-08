import tarfile
import os

# Cambiar al directorio donde están los archivos .tar
directorio = r"C:\Users\watch\Downloads\NotasHacking\DocumentacionHacking\Tarea_Forensic_2\Ejercicio_4"
os.chdir(directorio)

for i in range(999, 0, -1):
    filename = str(i) + '.tar'
    
    # Verificar si el archivo existe
    if not os.path.exists(filename):
        print(f"Archivo {filename} no encontrado, continuando...")
        continue
    
    print(f"Extrayendo {filename}...")
    try:
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()
    except Exception as e:
        print(f"Error al procesar {filename}: {e}")