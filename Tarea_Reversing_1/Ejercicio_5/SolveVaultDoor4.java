import java.util.*;

public class SolveVaultDoor4 {
    public static void main(String[] args) {
        byte[] myBytes = {
            // Primera fila - decimal
            106, 85, 53, 116, 95, 52, 95, 98,
            // Segunda fila - hexadecimal  
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            // Tercera fila - octal
            0142, 0131, 0164, 063, 0163, 0137, 0142, 064,
            // Cuarta fila - caracteres directos
            'e', '9', '4', '3', 'c', '3', 'a', '0'
        };
        
        StringBuilder password = new StringBuilder();
        
        for (int i = 0; i < myBytes.length; i++) {
            password.append((char) myBytes[i]);
        }
        
        System.out.println("Password: " + password.toString());
        System.out.println("Flag: picoCTF{" + password.toString() + "}");
        
        // Mostrar por grupos para verificación
        System.out.println("\nDesglose:");
        System.out.println("Decimal: " + new String(myBytes, 0, 8));
        System.out.println("Hex: " + new String(myBytes, 8, 8));
        System.out.println("Octal: " + new String(myBytes, 16, 8));
        System.out.println("Chars: " + new String(myBytes, 24, 8));
    }
}