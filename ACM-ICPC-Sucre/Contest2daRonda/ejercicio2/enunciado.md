Considera lo siguiente:
* Una cadena, s, de longitud n donde s=c0c1...cn-1.
* Un número entero, k, donde k es un factor de n.
Podemos dividir s en n/k subsegmentos donde cada subsegmento, 'ti', consta de un bloque contiguo de k caracteres en s. Luego, use cada 'ti' para crear una cadena 'ui' tal que:
* Los caracteres en 'ui' son una subsecuencia de los caracteres en 'ti'.
* Cualquier aparición repetida de un carácter se elimina de la cadena, de modo que cada carácter en 'ui' aparece exactamente una vez. En otras palabras, si el carácter en algún índice 'j' en 'ti' ocurre en un índice anterior < 'j' en 'ti', entonces no incluya el carácter en la cadena 'ui'.
Dados s y k, imprima n/k líneas donde cada línea i denota una cadena 'ui'
## Ejemplo
s = 'AAABCADDE'
k = 3
Hay tres subcadenas de longitud 3 para considerar 'AAA', 'BCA' y 'DDE'. La primera subcadena son todos los caracteres 'A', por lo que u1 = 'A'. La segunda subcadena tiene todos los caracteres distintos, por lo que u2 = 'BCA'. La tercera subcadena tiene 2 caracteres diferentes, por lo que u3 = 'DE'. Tenga en cuenta que una subsecuencia mantiene el orden original de los caracteres encontrados. El orden de los caracteres en cada subsecuencia mostrada es importante.
## Impresiones
Imprime cada subsecuencia en una nueva línea. Habrá n/k de ellos. No se espera ningún valor de retorno.
## Formato de entrada
La primera línea contiene una sola cadena que denota s.
La segunda línea contiene un número entero, k, que indica la longitud de cada subsecuencia.
## Restricciones
* 1 <= n <= 10^4, donde n es la longitud de s
* 1 <= k <= norte
* Se garantiza que n es múltiplo de k.
## Entrada de muestra
     ```
     AABCAAADA
     3
     ```
## Salida de muestra
     ```
     AB
     California
     ANUNCIO
```
## Explicación
Dividimos s en n/k = 9/3 = 3 subsegmentos de longitud k = 3. Convertimos cada 'ti' a 'ui' eliminamos las apariciones posteriores de caracteres no distintos en 'ti':
1. t0 = 'AAB' -> u0 = 'AB'
2. t1 = 'CAA' -> u1 = 'CA'
3. t2 = 'ADA' -> u2 = 'AD'
Imprimimos cada ui en una nueva línea.