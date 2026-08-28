# MATEMÁTICA DISCRETA - MÓDULO 3: RELACIONES
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. Producto Cartesiano (El "Súper Poder" previo a las Relaciones)

Antes de entender una relación, debemos entender cómo se combinan dos conjuntos.

**Definición:** El producto cartesiano de dos conjuntos `A` y `B` (se escribe `A × B`) es el conjunto de **todos los pares ordenados** `(a, b)` donde `a ∈ A` y `b ∈ B`.

- **Fórmula:** `A × B = { (a, b) | a ∈ A ∧ b ∈ B }`.
- **"Ordenado"** significa que `(a, b)` es diferente de `(b, a)` a menos que `a = b`.

**Ejemplo:** 
Si `A = {1, 2}` y `B = {x, y, z}`.
`A × B = { (1,x), (1,y), (1,z), (2,x), (2,y), (2,z) }`.

**Cardinalidad del producto cartesiano:** 
`|A × B| = |A| * |B|`. 
En el ejemplo: `2 * 3 = 6` pares.

**Ojo al dato:** El producto cartesiano de un conjunto consigo mismo, `A × A`, genera todas las combinaciones posibles de elementos de `A` consigo mismos.

---

## 2. ¿Qué es una Relación Binaria?

**Definición:** Una relación binaria `R` entre un conjunto `A` y un conjunto `B` es **cualquier subconjunto** del producto cartesiano `A × B`.

- Es decir, `R ⊆ A × B`.
- Si `(a, b) ∈ R`, decimos que "`a` está relacionado con `b`", y lo escribimos `a R b`.
- Si `(a, b) ∉ R`, decimos que "`a` NO está relacionado con `b`", y lo escribimos `a R̸ b`.

**Ejemplo cotidiano:**
- `A = {Ana, Luis}` (Personas).
- `B = {Fútbol, Natación}` (Deportes).
- `R` = "Practica el deporte".
- Si Ana practica fútbol, entonces `(Ana, Fútbol) ∈ R`.
- Si Luis no practica nada, no hay pares con Luis.
- `R ⊆ A × B`.

---

## 3. Relación de un Conjunto en sí mismo (Relación Homogénea)

Es el caso especial más importante: `R ⊆ A × A`. Aquí relacionamos elementos de un conjunto con otros elementos del **mismo** conjunto.

**Ejemplo:** `A = {1, 2, 3, 4}`. 
Definimos `R` como "es menor que" (`<`).
Entonces: `R = { (1,2), (1,3), (1,4), (2,3), (2,4), (3,4) }`.

---

## 4. Representación de Relaciones (3 formas de verlas)

Las relaciones se pueden dibujar o representar de varias maneras. Todas dicen lo mismo, pero cada una es útil para algo distinto.

### a) Conjunto de pares ordenados (Forma explícita)
Es la que hemos estado usando. Ej: `R = {(1,1), (1,2), (2,2)}`.

### b) Matriz booleana (Muy usado en computación)
Si `A` tiene `m` elementos y `B` tiene `n` elementos, dibujamos una matriz de `m` filas x `n` columnas. Ponemos un **1** si el par está en la relación, y un **0** si no.

- **Ejemplo:** `A = {1, 2}`, `B = {x, y}`. `R = { (1,x), (2,x), (2,y) }`.
  - Matriz (filas = A, columnas = B):
  > |   | x | y |
  > |---|---|---|
  > | 1 | 1 | 0 |
  > | 2 | 1 | 1 |

### c) Grafo Dirigido (Dibujo de flechas)
Si la relación es de `A` en `A` (homogénea), dibujamos círculos (vértices) para cada elemento de `A` y flechas (arcos) para cada par relacionado.

- Si `a R a` (un elemento relacionado consigo mismo), dibujamos un **lazo** (flecha que sale y vuelve al mismo círculo).

---

## 5. Propiedades de las Relaciones Homogéneas (Las "Reglas de Comportamiento")

Cuando una relación es de un conjunto en sí mismo (`R ⊆ A × A`), puede cumplir ciertas propiedades que la clasifican. Son fundamentales para entender bases de datos y lenguajes de programación.

| Propiedad | Definición formal | ¿Qué significa en español? | Ejemplo en `A = {1, 2, 3}` |
| :--- | :--- | :--- | :--- |
| **Reflexiva** | `∀x ∈ A, (x, x) ∈ R` | Cada elemento está relacionado consigo mismo. | `R = {(1,1), (2,2), (3,3), (1,2)}` es reflexiva (tiene los 3 lazos). |
| **Simétrica** | `∀x,y ∈ A, (x,y) ∈ R → (y,x) ∈ R` | Si `x` se relaciona con `y`, entonces `y` se relaciona con `x`. | `R = {(1,2), (2,1), (3,3)}` es simétrica. |
| **Antisimétrica** | `∀x,y ∈ A, (x,y)∈R ∧ (y,x)∈R → x = y` | Nunca puede haber flechas en ambos sentidos entre elementos distintos. | `R = {(1,1), (1,2), (2,3)}` es antisimétrica (no hay doble flecha). |
| **Transitiva** | `∀x,y,z ∈ A, (x,y)∈R ∧ (y,z)∈R → (x,z)∈R` | Si `x` va a `y`, y `y` va a `z`, entonces `x` tiene que ir a `z`. | `R = {(1,2), (2,3), (1,3)}` es transitiva. |

---

## 6. Tipos Especiales de Relaciones (Las Más Importantes)

### a) Relación de Equivalencia
Una relación es de **equivalencia** si cumple **tres propiedades a la vez**: **Reflexiva**, **Simétrica** y **Transitiva**.

- **Ejemplo clásico:** La relación "Ser igual en edad" entre personas.
- *Reflexiva:* Yo tengo mi misma edad (V).
- *Simétrica:* Si Ana tiene la edad de Luis, entonces Luis tiene la edad de Ana (V).
- *Transitiva:* Si Ana tiene la edad de Luis, y Luis la de Carlos, entonces Ana tiene la edad de Carlos (V).
- **¿Para qué sirve?** Una relación de equivalencia **particiona** (divide) el conjunto en grupos llamados **clases de equivalencia**. Todos los elementos dentro de una misma clase son equivalentes entre sí.

### b) Relación de Orden Parcial
Una relación es de **orden parcial** si cumple **Reflexiva**, **Antisimétrica** y **Transitiva**.

- **Ejemplo clásico:** La relación "Menor o igual que" (`≤`) en los números enteros.
- *Reflexiva:* `5 ≤ 5` (V).
- *Antisimétrica:* Si `a ≤ b` y `b ≤ a`, entonces `a = b` (V).
- *Transitiva:* Si `a ≤ b` y `b ≤ c`, entonces `a ≤ c` (V).
- **¿Para qué sirve?** Para ordenar elementos (como en una pila de tareas pendientes donde una depende de otra).

---

## 7. Clases de Equivalencia y Particiones (El Tesoro Oculto)

Cuando tienes una relación de equivalencia `R` sobre un conjunto `A`, puedes agrupar los elementos en **clases de equivalencia**.

**Definición de Clase de Equivalencia:** Dado un elemento `a ∈ A`, su clase de equivalencia `[a]` es el conjunto de todos los elementos que están relacionados con `a`.
`[a] = { x ∈ A | x R a }`.

**Propiedad mágica:** Estas clases **no se solapan** (son disjuntas) y **cubren todo** `A`. Es decir, forman una **partición** de `A`.

**Ejemplo:** `A = {1, 2, 3, 4, 5}`. Relación `R` = "Tener la misma paridad" (ser ambos pares o ambos impares).
- Clase del 1: `[1] = {1, 3, 5}` (todos los impares).
- Clase del 2: `[2] = {2, 4}` (todos los pares).
- Las clases `{1,3,5}` y `{2,4}` dividen a `A` en dos grupos sin mezclarse. ¡Eso es una partición!

---

## 8. Cierre de Relaciones (Rellenar los huecos)

A veces una relación no es transitiva o reflexiva, pero queremos **forzarla** a serlo añadiendo los pares mínimos necesarios.

- **Cierre reflexivo:** Añadir `(x, x)` para todo `x` que no lo tenga.
- **Cierre simétrico:** Añadir `(y, x)` por cada `(x, y)` que no tenga su inverso.
- **Cierre transitivo (El más usado en grafos):** Añadir todas las conexiones indirectas necesarias. *Ejemplo: Si tenemos (1,2) y (2,3), añadir (1,3).* 
- En computación, el cierre transitivo se usa para calcular "¿a qué nodos puedo llegar desde este nodo?" en un grafo.

---

## 9. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Dado `A = {1, 2, 3}` y la relación `R = { (1,1), (1,2), (2,1), (2,2), (3,3) }`. 
¿Es reflexiva? ¿Es simétrica? ¿Es transitiva? ¿Es de equivalencia?

**Solución:**
1. **Reflexiva:** ¿Están `(1,1)`, `(2,2)` y `(3,3)`? Sí, todos están → **Cumple**.
2. **Simétrica:** Revisamos cada par:
- `(1,2)` está, y su inverso `(2,1)` está ✅.
- `(2,1)` está, y su inverso `(1,2)` está ✅.
- Los lazos `(1,1)`, `(2,2)`, `(3,3)` son simétricos consigo mismos.
→ **Cumple**.
3. **Transitiva:** Revisamos todas las combinaciones:
- `(1,2)` y `(2,1)` exigen `(1,1)` (está) ✅.
- `(2,1)` y `(1,2)` exigen `(2,2)` (está) ✅.
- El resto son lazos, que no exigen nada nuevo.
→ **Cumple**.
**Respuesta final:** Es reflexiva, simétrica y transitiva, por lo tanto **es una Relación de Equivalencia**. Sus clases son `[1] = {1,2}` y `[3] = {3}`.

---

**Ejercicio 2:** Representa la relación `R = { (1,2), (2,3), (1,3) }` en una matriz booleana (A = {1,2,3}) y di qué propiedad famosa cumple.

**Solución:**
- Matriz (filas = origen, columnas = destino):

> |   | 1 | 2 | 3 |
> |---|---|---|---|
> | 1 | 0 | 1 | 1 |
> | 2 | 0 | 0 | 1 |
> | 3 | 0 | 0 | 0 |

- **Propiedad:** Si `(1,2)` y `(2,3)` están, entonces `(1,3)` está. No tiene pares sueltos que la rompan. Además no tiene lazos (no es reflexiva) y no tiene flechas inversas (es antisimétrica). 
**Respuesta:** Es **Transitiva** y **Antisimétrica**.

---

**Ejercicio 3:** Encuentra el cierre transitivo de `R = { (1,2), (2,3) }` sobre `A = {1, 2, 3}`.

**Solución:**
1. Partimos de la base: `(1,2)` y `(2,3)`.
2. Para que sea transitiva, necesitamos `(1,3)` porque `1→2` y `2→3` obligan a `1→3`.
3. Añadimos `(1,3)`.
**Respuesta final:** El cierre transitivo es `R* = { (1,2), (2,3), (1,3) }`. (Si existiera el 4, seguiríamos añadiendo, pero aquí termina).

---

## 10. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos. Las soluciones están al final (no hagas trampa).**

1. **Producto Cartesiano:** Si `A = {a, b}` y `B = {1, 2, 3}`, escribe `A × B` y calcula su cardinalidad.

2. **Propiedades:** Dado `A = {1, 2, 3, 4}` y `R = { (1,1), (2,2), (3,3), (4,4), (1,2), (2,1) }`.
 - ¿Es reflexiva? ¿Es simétrica? ¿Es transitiva? (Justifica tu respuesta en transitiva).

3. **Identificación:** ¿Qué tipo de relación es "Ser hijo de" en el conjunto de todas las personas? (¿Reflexiva, simétrica, antisimétrica, transitiva?). 

4. **Partición:** Sea `A = {1, 2, 3, 4, 5, 6}`. La relación `R` agrupa a los números que dejan el **mismo residuo** al dividirlos por 3 (es decir, misma clase módulo 3). Escribe las clases de equivalencia.

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

1. **Solución:**
 `A × B = { (a,1), (a,2), (a,3), (b,1), (b,2), (b,3) }`.
 Cardinalidad: `|A| * |B| = 2 * 3 = 6`.

2. **Solución:**
 - **Reflexiva:** Sí, porque contiene `(1,1), (2,2), (3,3), (4,4)`.
 - **Simétrica:** Sí, porque tiene `(1,2)` y su inverso `(2,1)`; los lazos son simétricos consigo mismos.
 - **Transitiva:** **Sí**. Revisamos: `(1,2)` y `(2,1)` exigen `(1,1)` (está). `(2,1)` y `(1,2)` exigen `(2,2)` (está). Los lazos no exigen nada. Por lo tanto, sí es transitiva.
 (Conclusión: Es una relación de equivalencia, divide a A en dos clases: `{1,2}` y `{3}`, `{4}`).

3. **Solución:**
 - **Reflexiva:** No, nadie es hijo de sí mismo.
 - **Simétrica:** No, si Juan es hijo de Pedro, Pedro no es hijo de Juan.
 - **Antisimétrica:** Sí, porque no pueden existir dos flechas inversas (sería una paradoja temporal).
 - **Transitiva:** No, si Juan es hijo de Pedro, y Pedro es hijo de Carlos, Juan NO es hijo de Carlos (es nieto).
 **Clasificación:** Es una relación **Antisimétrica** (y no cumple las demás).

4. **Solución:**
 - Números que divididos por 3 dan residuo 0: `{3, 6}`.
 - Números que divididos por 3 dan residuo 1: `{1, 4}`.
 - Números que divididos por 3 dan residuo 2: `{2, 5}`.
 **Clases de equivalencia:** `[0] = {3,6}`, `[1] = {1,4}`, `[2] = {2,5}`.
 (Estas tres clases forman una partición de `A`).

</details>

---

## 11. Conclusión del Módulo 3 (Relaciones)

¡Ya dominas las conexiones entre elementos! Has aprendido:

- A crear el producto cartesiano y extraer relaciones de él.
- A representar relaciones como matrices o grafos dirigidos.
- A clasificar relaciones por sus propiedades (Reflexiva, Simétrica, Antisimétrica, Transitiva).
- A identificar las poderosas **Relaciones de Equivalencia** (que dividen conjuntos en grupos) y las **Relaciones de Orden** (que los organizan jerárquicamente).
- A calcular el cierre transitivo (esencial para encontrar caminos en grafos).

**La conexión con tu siguiente tema (Funciones):** Una **Función** es un tipo **muy estricto** de relación. En una relación normal, un elemento `a` puede estar relacionado con varios `b` (como Ana practicando Fútbol y Natación). En una función, **cada `a` está relacionado con EXACTAMENTE UN `b`**. Es una relación con una "regla de oro" extra. ¡Eso lo veremos en el Módulo 4!

**Guardar cambios:** Crea un nuevo archivo con este contenido y nómbralo `03_Relaciones.txt` o `.md`.

¿Listo para el **Módulo 4: Funciones**? 🚀