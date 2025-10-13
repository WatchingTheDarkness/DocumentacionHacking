# 3 - matryoshka doll

## Descripcion:
* Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this
* Wait, you can hide files inside files? But how do you find them?
* Make sure to submit the flag as picoCTF{XXXXX}

## Solucion:
*  wget https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg
*  file dolls.jpg
*  binwalk dolls.jpg
*  unzip dolls.jpg
*  cd base_images/
*  binwalk 2_c.jpg
*  rm -rf base_images/
*  binwalk dolls.jpg
*  for i in {0..100}; do unzip *.jpg; cd base_images; done
*  ls
*  picoCTF{336cf6d51c9d9774fd37196c1d7320ff}

## Notas:

## Referencias:
