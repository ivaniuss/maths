# MATEMÁTICA DISCRETA - MÓDULO 5: COMBINATORIA
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. ¿Qué es la Combinatoria? (El Arte de Contar sin Contar)

**Definición:** La Combinatoria es la rama de las matemáticas que se encarga de **contar** el número de formas en que se pueden ordenar, agrupar o seleccionar elementos de un conjunto, sin necesidad de enumerarlos uno por uno.

**¿Por qué es útil?**
- Para calcular probabilidades (¿cuántos casos favorables hay sobre el total?).
- Para analizar la complejidad de algoritmos (¿cuántas operaciones hará mi programa?).
- Para diseñar contraseñas o códigos (¿cuántas combinaciones seguras existen?).

**Los dos principios fundamentales:** Todo en combinatoria se reduce a dos reglas básicas: **La Regla de la Suma (O)** y **La Regla del Producto (Y)**. Domina estas dos y lo demás es pura aplicación.

---

## 2. Principio de la Suma (Regla del "O")

**Definición:** Si una tarea se puede realizar de `m` maneras diferentes **O** de `n` maneras diferentes, y ambas opciones son mutuamente excluyentes (no se pueden hacer al mismo tiempo), entonces el número total de maneras de realizar la tarea es **`m + n`**.

- **Analogía:** Tienes 3 camisas azules y 4 camisas rojas. ¿De cuántas formas puedes elegir UNA camisa? `3 + 4 = 7` formas. (O eliges una azul, o eliges una roja, no ambas).

---

## 3. Principio del Producto (Regla del "Y")

**Definición:** Si una tarea se puede dividir en dos pasos secuenciales, donde el primer paso se puede hacer de `m` maneras, y el segundo paso se puede hacer de `n` maneras (independientemente del primero), entonces el número total de maneras de realizar la tarea completa es **`m * n`**.

- **Analogía:** Tienes 3 camisas y 4 pantalones. ¿De cuántas formas puedes elegir un atuendo (una camisa Y un pantalón)? `3 * 4 = 12` conjuntos.

**Combinando ambas:** 
Si para ir al trabajo puedes ir en 2 autobuses (suma) y luego en 3 líneas de metro (producto), pero también puedes ir en 4 trenes directos (suma), el total sería: `(2 * 3) + 4 = 10` caminos posibles.

---

## 4. Factorial (`!`) - El Ladrillo de la Combinatoria

Antes de permutar o combinar, necesitamos entender el **factorial**. 

**Definición:** El factorial de un número entero positivo `n` (se escribe `n!`) es el producto de todos los enteros desde `n` hasta 1.

- **Fórmula:** `n! = n * (n-1) * (n-2) * ... * 1`.
- **Casos especiales:** `0! = 1` (por convención, para que las fórmulas funcionen).

**Ejemplos:**
- `5! = 5 * 4 * 3 * 2 * 1 = 120`.
- `3! = 3 * 2 * 1 = 6`.

**Interpretación clave:** `n!` es el número de formas de **ordenar** `n` elementos distintos en una fila. 
(Ej: ¿De cuántas formas puedes ordenar 3 libros en un estante? `3! = 6` formas).

---

## 5. Permutaciones (Importa el Orden)

Una **permutación** es un arreglo u ordenamiento de elementos donde **el orden SÍ importa**. 
*Ejemplo: La contraseña "123" no es lo mismo que "321".*

### a) Permutaciones sin repetición (Todos los elementos son distintos)
Se escribe `P(n) = n!`. Son todas las formas de ordenar los `n` elementos disponibles, usando **todos** ellos.

**Fórmula general (tomar `r` elementos de un total de `n`):** 
`P(n, r) = n! / (n - r)!` 
*(Se lee: "Permutaciones de n tomados de r en r").*

- **Ejemplo:** ¿Cuántas formas hay de elegir al presidente, vicepresidente y tesorero (3 cargos distintos) de un grupo de 10 personas?
  - Aquí importa el orden (quién es presidente y quién vice no es lo mismo).
  - `P(10, 3) = 10! / (10 - 3)! = 10! / 7! = 10 * 9 * 8 = 720` formas.

### b) Permutaciones con repetición (Hay elementos iguales)
Si tienes elementos repetidos (ej: la palabra "MESA" tiene todas letras distintas; "CASA" tiene la 'A' repetida), la fórmula cambia para no contar los ordenamientos idénticos.

**Fórmula:** `n! / (k1! * k2! * ... * km!)`, donde `k1, k2...` son las cantidades de veces que se repite cada elemento.

- **Ejemplo:** ¿Cuántas palabras diferentes (con o sin sentido) puedes formar con las letras de **"CASA"**?
  - Total de letras: `n = 4`. La 'A' se repite `2` veces. El resto (C, S) van 1 vez.
  - Cálculo: `4! / 2! = 24 / 2 = 12` palabras únicas.

### c) Permutaciones Circulares (Orden en círculo)
Cuando los elementos se ordenan en círculo (como alrededor de una mesa), los giros no cuentan como arreglos distintos.

**Fórmula:** `(n - 1)!`.

- **Ejemplo:** ¿De cuántas formas puedes sentar a 5 personas alrededor de una mesa redonda?
  - `(5 - 1)! = 4! = 24` formas.

---

## 6. Combinaciones (NO Importa el Orden)

Una **combinación** es una selección de elementos donde **el orden NO importa**. 
*Ejemplo: Elegir 3 frutas para un batido. Da igual que elijas manzana, pera y banana que banana, pera y manzana; el batido es el mismo.*

**Fórmula (coeficiente binomial):** 
`C(n, r) = n! / (r! * (n - r)!)`
*(Se lee "Combinaciones de n tomados de r en r" o "n choose r").*

- **Ejemplo:** ¿De cuántas formas puedes elegir un comité de 3 personas de un grupo de 10?
  - `C(10, 3) = 10! / (3! * 7!) = (10 * 9 * 8) / (3 * 2 * 1) = 720 / 6 = 120` formas.

**La gran diferencia:** 
- Si te preguntan por **cargos** (presidente, secretario) → Usa **Permutaciones** (orden importa).
- Si te preguntan por **comités** o **manos de cartas** → Usa **Combinaciones** (orden no importa).

---

## 7. Combinaciones con Repetición (Las "Cajas" o "Estrellas y Barras")

A veces puedes elegir elementos **permitiendo repetirlos**. 
*Ejemplo: ¿De cuántas formas puedo comprar 4 donas si hay 3 sabores disponibles y puedo repetir sabores? (No importa el orden).*

**Fórmula:** `C(n + r - 1, r)`, donde `n` es el número de tipos de elementos y `r` es cuántos eliges.

- **Ejemplo:** En una heladería hay 5 sabores. ¿De cuántas formas puedes elegir 3 bolas de helado (pueden ser del mismo sabor y no importa el orden)?
  - `n = 5`, `r = 3`.
  - `C(5 + 3 - 1, 3) = C(7, 3) = 7! / (3! * 4!) = 35` formas.

---

## 8. Principio del Palomar (El Principio de la Galera)

Es un principio de conteo súper simple pero con consecuencias alucinantes.

**Definición:** Si tienes `n` palomas y `m` palomares, y `n > m`, entonces **al menos un palomar tendrá más de una paloma**. Es decir, si hay más objetos que cajas, forzosamente alguna caja se repite.

**Aplicación práctica:** En un grupo de 13 personas, al menos 2 cumplen años en el mismo mes. (12 meses, 13 personas → forzosamente se repite un mes).

---

## 9. Números Binomiales y el Triángulo de Pascal

El coeficiente `C(n, r)` (combinaciones) aparece en el **Triángulo de Pascal**. Cada número es la suma de los dos que tiene encima.

```
Fila 0: 1
Fila 1: 1 1
Fila 2: 1 2 1
Fila 3: 1 3 3 1
Fila 4: 1 4 6 4 1
```

**Teorema del Binomio:** 

$$(a + b)^n = \sum_{k=0}^{n} C(n, k) \cdot a^{n-k} \cdot b^k$$

- *Ejemplo:* $(x + y)^3 = C(3,0)x^3 + C(3,1)x^2 y + C(3,2)x y^2 + C(3,3)y^3 = x^3 + 3x^2 y + 3x y^2 + y^3$.

---

## 10. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Un código de acceso está formado por 3 letras (del alfabeto de 26) seguidas de 2 dígitos (0-9). ¿Cuántos códigos distintos hay si se permiten repeticiones?

**Solución:**
1. Paso 1 (Letras): 3 posiciones, 26 opciones cada una → `26 * 26 * 26 = 26^3`.
2. Paso 2 (Dígitos): 2 posiciones, 10 opciones cada una → `10 * 10 = 10^2`.
3. Principio del producto (letras Y dígitos): `26^3 * 10^2 = 17576 * 100 = 1,757,600` códigos.

---

**Ejercicio 2:** ¿De cuántas formas se pueden ordenar las letras de la palabra **"MATEMATICAS"**?

**Solución:**
1. Contamos letras totales: `M(2)`, `A(3)`, `T(2)`, `E(1)`, `I(1)`, `C(1)`, `S(1)`. Total = 11 letras.
2. Es una permutación con repetición: `11! / (2! * 3! * 2!)`.
3. `11! = 39916800`. Dividimos: `2! = 2`, `3! = 6`, `2! = 2`. Denominador = `2 * 6 * 2 = 24`.
4. `39916800 / 24 = 1,663,200`.
**Respuesta:** 1,663,200 formas.

---

**Ejercicio 3:** En una clase de 30 alumnos, se quiere elegir un delegado y un subdelegado (cargos distintos). ¿De cuántas formas se puede hacer?

**Solución:**
- Aquí el orden importa (ser delegado no es lo mismo que subdelegado). Son permutaciones.
- `P(30, 2) = 30 * 29 = 870` formas.

---

**Ejercicio 4:** En una baraja de 52 cartas, ¿de cuántas formas se pueden repartir 5 cartas a un jugador (sin importar el orden)?

**Solución:**
- Orden no importa (una mano de póker es una combinación).
- `C(52, 5) = 52! / (5! * 47!) = (52 * 51 * 50 * 49 * 48) / (5 * 4 * 3 * 2 * 1) = 2,598,960` manos posibles.

---

## 11. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos. Las soluciones están al final (no hagas trampa).**

1. **Principio del Producto:** En un restaurante ofrecen 3 tipos de sopa, 5 platos principales y 4 postres. ¿Cuántas comidas completas (sopa + plato + postre) se pueden pedir?

2. **Permutación sin repetición:** ¿De cuántas formas pueden terminar los 8 primeros puestos (oro, plata, bronce, y 4to a 8vo) en una carrera de 8 atletas?

3. **Combinación:** En una liga de 10 equipos, ¿cuántos partidos diferentes se juegan si cada pareja de equipos se enfrenta una sola vez?

4. **Permutación con repetición:** ¿Cuántas palabras únicas (con o sin sentido) se pueden formar con las letras de la palabra "ANANA"?

5. **Desafío (Principio del Palomar):** En un salón de 367 personas, ¿por qué es seguro afirmar que al menos dos personas cumplen años el mismo día?

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

1. **Respuesta:** `3 * 5 * 4 = 60` comidas completas.

2. **Respuesta:** Son permutaciones de 8 en 8: `8! = 40320` formas de terminar la carrera.

3. **Respuesta:** El orden de los equipos no importa (juego A vs B es lo mismo que B vs A). Usamos combinaciones: `C(10, 2) = 10! / (2! * 8!) = 45` partidos.

4. **Respuesta:** "ANANA" tiene 5 letras. A aparece 3 veces, N aparece 2 veces.  
   `5! / (3! * 2!) = 120 / (6 * 2) = 120 / 12 = 10` palabras únicas.

5. **Respuesta:** Hay 367 personas y solo 366 días posibles en un año (contando el 29 de febrero). Como hay más personas que días (367 > 366), forzosamente al menos dos personas comparten el mismo día de cumpleaños. **Este es el principio del palomar en acción.**

</details>

---

## 12. Conclusión del Módulo 5 (Combinatoria)

¡Ya eres un contador profesional! Has aprendido:

- Los principios de la **Suma (O)** y el **Producto (Y)**.
- El poder del **Factorial (`n!`)**.
- A diferenciar entre **Permutaciones** (orden importa) y **Combinaciones** (orden no importa).
- A manejar casos con repetición.
- El engañosamente simple **Principio del Palomar**, que permite hacer afirmaciones sorprendentes sin saber los detalles.

**La conexión con tu siguiente tema (Probabilidad Discreta):** Ahora que sabes contar el número total de casos posibles y el número de casos favorables, puedes calcular probabilidades con la Regla de Laplace: **Probabilidad = (Casos Favorables) / (Casos Totales)**. ¡La combinatoria es el motor de la probabilidad!

**Guardar cambios:** Crea un nuevo archivo con este contenido y nómbralo `05_Combinatoria.txt` o `.md`.

¿Listo para el **Módulo 6: Probabilidad Discreta**? 🚀🎲