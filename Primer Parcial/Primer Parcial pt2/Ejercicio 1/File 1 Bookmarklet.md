# 1 - Bookmarklet

## Descripcion:
* Why search for the flag when I can make a bookmarklet to print it for me?
Additional details will be available after launching your challenge instance.
* A bookmarklet is a bookmark that runs JavaScript instead of loading a webpage.
* What happens when you click a bookmarklet?
* Web browsers have other ways to run JavaScript too.

## Solucion:
* http://titan.picoctf.net:54535
* consola de comandos
*         javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£Ö�ÓÚåÛÑ¢ÕÓ�¨Í�ÕÄ¦�í";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
* picoCTF{p@g3_turn3r_18d2fa20}

## Notas:
* entramos a la pagina,
* despues copiamos el codigo que viene en la pagina
* entramos a la consola de comandos
* pegamos el codigo
* nos da la bandera

## Referencias: