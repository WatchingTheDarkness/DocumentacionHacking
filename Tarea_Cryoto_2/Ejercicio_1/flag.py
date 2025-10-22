m = 14311663942709674867122208214901970650496788151239520971623411712977120586163535880168563325

# Convertir a hexadecimal y luego a texto
hex_string = hex(m)[2:]  # [2:] para quitar el '0x'
flag = bytes.fromhex(hex_string).decode('ascii')

print("Flag:", flag)