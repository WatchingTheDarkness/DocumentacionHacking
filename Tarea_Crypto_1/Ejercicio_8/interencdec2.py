def caesar_shift(s, shift):
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch)-97+shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch)-65+shift) % 26 + 65))
        else:
            res.append(ch)
    return ''.join(res)

s = "wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}"
# aplicamos shift -7
decoded = caesar_shift(s, -7)
print("After Caesar -7:", decoded)

# opcional: reemplazos leet comunes
leet_map = str.maketrans({'3':'e','4':'a','1':'i','0':'o','5':'s','7':'t','9':'y','6':'g'})
print("Leet->letters :", decoded.translate(leet_map))
