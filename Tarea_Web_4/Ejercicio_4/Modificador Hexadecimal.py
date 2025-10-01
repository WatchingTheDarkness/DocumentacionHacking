class AnalizadorBytesPython:
    def analizar_bytes(self):
        print("🔍 ANALIZADOR DE BYTES PYTHON")
        print("=" * 50)
        
        bytes_input = input("📋 Pega aquí tu dato (formato \\x1a6\\x84...): ").strip()
        
        if not bytes_input:
            print("❌ No se ingresó ningún dato")
            return
        
        print("\n" + "=" * 50)
        print("📊 RESULTADOS DEL ANÁLISIS")
        print("=" * 50)
        
        # Procesar el dato
        self.procesar_bytes_python(bytes_input)
    
    def procesar_bytes_python(self, bytes_string):
        try:
            bytes_data = eval(f'b"{bytes_string}"')
            
            print(f"✅ Conversión exitosa!")
            print(f"📏 Longitud: {len(bytes_data)} bytes")
            print(f"💾 Bytes crudos: {bytes_data}")
            print(f"🔢 Hexadecimal: {bytes_data.hex()}")
            
            print("\n--- 📝 DECODIFICACIÓN COMO TEXTO ---")
            
            codificaciones = ['utf-8', 'latin-1', 'ascii', 'utf-16', 'iso-8859-1']
            
            texto_encontrado = False
            for codificacion in codificaciones:
                try:
                    texto = bytes_data.decode(codificacion)
                    if any(c.isprintable() for c in texto):
                        print(f"🔤 {codificacion.upper()}: {texto}")
                        texto_encontrado = True
                except:
                    continue
            
            if not texto_encontrado:
                print("❌ No se pudo decodificar como texto legible")
            
            print("\n--- 🔍 ANÁLISIS DETALLADO ---")
            
            print(f"📋 Bytes (decimal): {list(bytes_data)}")
            
            print(f"📖 Representación mixta: {self.bytes_a_representacion_mixta(bytes_data)}")
            
            print(f"\n--- 📈 ESTADÍSTICAS ---")
            print(f"🔢 Rango de valores: {min(bytes_data)} - {max(bytes_data)}")
            print(f"🎯 Bytes únicos: {len(set(bytes_data))}")
            print(f"📊 Primeros bytes: {list(bytes_data[:8])}")
            print(f"📊 Últimos bytes: {list(bytes_data[-8:])}")
            
        except Exception as e:
            print(f"❌ Error procesando los bytes: {e}")
            print("💡 Asegúrate de que el formato sea correcto: \\x1a6\\x84\\x88...")
    
    def bytes_a_representacion_mixta(self, bytes_data):
        """Convierte bytes a representación mixta (texto + hex)"""
        resultado = []
        for byte in bytes_data:
            if 32 <= byte <= 126: 
                resultado.append(chr(byte))
            else:
                resultado.append(f'[\\x{byte:02x}]')
        return ''.join(resultado)

if __name__ == "__main__":
    analizador = AnalizadorBytesPython()
    analizador.analizar_bytes()