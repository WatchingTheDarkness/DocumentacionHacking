def atbash_decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(155 - ord(char))  # A(65) ↔ Z(90)
            else:
                result += chr(219 - ord(char))  # a(97) ↔ z(122)
        else:
            result += char
    return result

encrypted = "krxlXGU{zgyzhs_xizxp_zx751vx6}"
decrypted = atbash_decrypt(encrypted)

print("Texto cifrado:", encrypted)
print("Texto descifrado:", decrypted)