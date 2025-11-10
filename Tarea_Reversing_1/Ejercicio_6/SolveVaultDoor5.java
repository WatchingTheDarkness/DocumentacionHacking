import java.util.Base64;
import java.net.URLDecoder;
import java.io.UnsupportedEncodingException;

public class SolveVaultDoor5 {
    public static void main(String[] args) {
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTM0JTMyJTYzJTM2JTM0JTMwJTM5JTYy";
        
        try {
            // Paso 1: Decode Base64
            byte[] base64DecodedBytes = Base64.getDecoder().decode(expected);
            String urlEncoded = new String(base64DecodedBytes, "UTF-8");
            System.out.println("URL encoded: " + urlEncoded);
            
            // Paso 2: Decode URL
            String password = URLDecoder.decode(urlEncoded, "UTF-8");
            System.out.println("Password: " + password);
            System.out.println("Flag: picoCTF{" + password + "}");
            
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
}