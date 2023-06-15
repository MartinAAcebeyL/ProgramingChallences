La secuencia de Fibonacci se crea sumando los dos términos anteriores para obtener el nuevo termino.

Matemáticamente significa fn = fn−1 + fn−2. Si comenzamos a construir esta serie a partir de los números 1, 1 obtenemos 1, 1, 2, 3, 5, 8, 13, 21, 34...

Escribiendo esta serie de forma continua tenemos 112358132134... Se ha decidido establecer el día de Fibonacci, marcando un día del calendario cuyos números formen parte de la serie. Por ejemplo noviembre 23 seria 11 - 23 que representa los primeros números de la serie. Otro ejemplo es febrero 13 que será 213 que que es posible hallar en la cadena obtenida.

Dada una fecha se quiere conocer si es un posible día que se pueda asignar al famoso matemático Fibonacci. Para ser considerada una posible fecha, deben existe por lo menos tres números consecutivamente en la serie, así como por ejemplo agosto 13 .

Para este problema considere solamente los primeros 30 números de la serie.

## Entrada
La entrada consiste de dos números M, D (1 ≤ M ≤ 12, 1 ≤ D ≤ 31) representando el mes y el día respectivamente.

## Salida
Por cada caso de prueba en la entrada imprima SI, si este día puede ser un día de Fibonacci y ”NO” en otros casos.