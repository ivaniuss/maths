# MATEMÁTICA DISCRETA - MÓDULO 4: FUNCIONES
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. ¿Qué es una Función? (La Relación Estricta)

**Definición formal:** Una función `f` de un conjunto `A` (dominio) a un conjunto `B` (codominio) es una **relación binaria** `f ⊆ A × B` que cumple dos condiciones:

1. **Existencia:** Para todo `a ∈ A`, existe **al menos** un `b ∈ B` tal que `(a, b) ∈ f`.
2. **Unicidad:** Para todo `a ∈ A`, si `(a, b) ∈ f` y `(a, c) ∈ f`, entonces `b = c`.

En español: **"Cada elemento del dominio tiene UNA y solo UNA imagen en el codominio"**.

**Notación:** `f: A → B` se lee *"f es una función de A en B"*. 
- `A` es el **dominio** (los valores de entrada).
- `B` es el **codominio** (los valores de salida posibles).
- Si `(a, b) ∈ f`, escribimos `f(a) = b` (se lee "f de a es igual a b").

**Analogía:** Una función es como una **máquina expendedora**. 
- El dominio son los botones que puedes presionar.
- El codominio son todos los productos que tiene la máquina.
- La función es la regla que asigna a cada botón **un solo producto**. Si presionas el botón, siempre cae lo mismo. ¡Nunca dos cosas diferentes!

**Diferencia clave con Relaciones:**
- En una **relación**, un elemento de `A` puede estar relacionado con varios de `B` (ej: Ana practica Fútbol y Natación).
- En una **función**, un elemento de `A` solo puede tener **una** flecha (ej: Ana tiene **una** edad).

---

## 2. Partes de una Función (Dominio, Codominio, Rango/Imagen)

- **Dominio (`Dom(f)`):** Es el conjunto `A`. Todos los valores de entrada que tienen una flecha.
- **Codominio (`Cod(f)`):** Es el conjunto `B`. El conjunto donde *pueden* caer las flechas.
- **Rango o Imagen (`Im(f)` o `f(A)`):** Es el conjunto de los elementos de `B` que **realmente** reciben al menos una flecha. Siempre es un subconjunto del codominio.

**Ejemplo:** `f: {1, 2, 3} → {a, b, c, d}` definida por `f(1)=a`, `f(2)=a`, `f(3)=b`.
- Dominio: `{1, 2, 3}`.
- Codominio: `{a, b, c, d}`.
- Rango/Imagen: `{a, b}` (porque `c` y `d` no reciben ninguna flecha).

**Regla de oro:** ¡El rango puede ser más pequeño que el codominio! Eso es normal. Si el rango es igual al codominio, tenemos una función especial (sobreyectiva, que veremos después).

---

## 3. Tipos de Funciones (Inyectiva, Sobreyectiva, Biyectiva)

Estas son las tres propiedades que clasifican a las funciones. Son fundamentales para entender si una función tiene inversa.

### a) Función Inyectiva (Uno a uno)
**Definición:** Una función `f: A → B` es **inyectiva** si elementos distintos del dominio siempre van a elementos distintos del codominio. Es decir, no hay dos `a` diferentes que tengan la misma imagen.

- **Fórmula:** `∀x, y ∈ A, f(x) = f(y) → x = y`.
- **Traducción:** Si la salida es la misma, es porque la entrada era la misma.
- **Analogía:** Es como un **DNI**. Cada persona tiene un número único, y cada número único pertenece a una sola persona. No hay dos personas con el mismo DNI.

### b) Función Sobreyectiva (Sobre / Onto)
**Definición:** Una función `f: A → B` es **sobreyectiva** si **todo** elemento del codominio `B` es imagen de al menos un elemento del dominio `A`. Es decir, el rango es igual al codominio.

- **Fórmula:** `∀y ∈ B, ∃x ∈ A tal que f(x) = y`.
- **Traducción:** No sobra ningún elemento en el codominio; todos reciben alguna flecha.
- **Analogía:** Es como un **reparto de pizzas**. Si hay 10 casas (B) y 10 repartidores (A), y cada casa recibe al menos una pizza, la función es sobreyectiva (todas las casas tienen pizza). Si una casa se queda sin pizza, no es sobreyectiva.

### c) Función Biyectiva (Correspondencia uno a uno)
**Definición:** Una función `f: A → B` es **biyectiva** si es **inyectiva Y sobreyectiva** al mismo tiempo.

- **Consecuencia:** Cada elemento de `A` se empareja con **exactamente uno** de `B`, y viceversa. No hay empates (inyectiva) y no sobran elementos (sobreyectiva).
- **Analogía:** Es un **matrimonio perfecto** entre dos conjuntos del mismo tamaño. Cada persona del conjunto A tiene una pareja única en el conjunto B, y todos en B tienen pareja.

---

## 4. Composición de Funciones (Funciones de Funciones)

**Definición:** Si tenemos dos funciones, `f: A → B` y `g: B → C`, podemos **componerlas** para crear una nueva función `g ∘ f: A → C`.

- **Fórmula:** `(g ∘ f)(x) = g(f(x))`.
- **Orden (¡Cuidado!):** Se lee "g compuesta con f". Primero se aplica `f` a `x`, y luego se aplica `g` al resultado de `f`.
- **Analogía:** Es como hacer dos pasos en una fábrica. Primero la máquina `f` transforma la materia prima, y luego la máquina `g` transforma el producto semiacabado.

**Ejemplo:** 
- `f: ℕ → ℕ`, `f(x) = x + 1`.
- `g: ℕ → ℕ`, `g(x) = 2x`.
- `(g ∘ f)(x) = g(f(x)) = g(x + 1) = 2(x + 1) = 2x + 2`.
- **¡Ojo!** `(f ∘ g)(x) = f(g(x)) = f(2x) = 2x + 1`. El orden cambia totalmente el resultado.

**Propiedad clave:** La composición de funciones **no es conmutativa** (el orden importa). Pero sí es **asociativa**: `(h ∘ g) ∘ f = h ∘ (g ∘ f)`.

---

## 5. Función Inversa (Deshacer lo hecho)

**Definición:** Si `f: A → B` es **biyectiva**, entonces existe su función inversa `f^{-1}: B → A` que "deshace" lo que hizo `f`.

- **Propiedad:** `f^{-1}(f(x)) = x` para todo `x ∈ A`, y `f(f^{-1}(y)) = y` para todo `y ∈ B`.
- **¿Cuándo existe inversa?** **SOLO** cuando la función es **biyectiva** (inyectiva + sobreyectiva). Si no es biyectiva, no tiene inversa.
- **Analogía:** Si `f` es "multiplicar por 2", su inversa `f^{-1}` es "dividir por 2". Pero si `f` es "elevar al cuadrado", no tiene inversa en los reales porque no es inyectiva (`2^2 = (-2)^2`).

**Regla para calcularla:** 
1. Escribe `y = f(x)`.
2. Despeja `x` en función de `y`.
3. Cambia `x` por `f^{-1}(y)`.
4. Si quieres, cambia la variable `y` por `x` al final para que quede más legible.

---

## 6. Funciones Especiales (Las que aparecen siempre)

| Función | Notación | Definición | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Función Identidad** | `id_A` o `I_A` | `id_A: A → A`, `id_A(x) = x` | Devuelve lo mismo que entró. Es la "función neutra" para la composición. |
| **Función Constante** | `k` | `f: A → B`, `f(x) = c` (siempre el mismo valor fijo) | `f(x) = 5` para todo `x`. |
| **Función Proyección** | `π_i` | Toma una tupla y devuelve su i-ésimo componente. | `π_1(x, y) = x`. |

---

## 7. Cardinalidad y Funciones (El tamaño importa)

Las funciones nos permiten comparar el **tamaño** de conjuntos (incluso infinitos).

- **Dos conjuntos `A` y `B` tienen el mismo tamaño (misma cardinalidad)** si existe una **función biyectiva** `f: A → B`.
- **Ejemplo:** El conjunto de los números naturales `ℕ` y el de los números pares `P = {2, 4, 6, ...}` tienen el mismo tamaño. ¿Por qué? Porque la función `f(n) = 2n` es una biyección entre ellos. Aunque parezca que los pares son "la mitad", son igual de infinitos. (¡Esto es la locura de los infinitos de Cantor!).

---

## 8. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Determina si `f: ℤ → ℤ` definida por `f(x) = 2x` es inyectiva, sobreyectiva o biyectiva.

**Solución:**
1. **Inyectiva:** Supongamos `f(a) = f(b)`. Entonces `2a = 2b → a = b`. ✅ **Cumple**.
2. **Sobreyectiva:** ¿Todo entero `y` tiene un `x` tal que `2x = y`? Si `y = 3`, necesitamos `x = 1.5`, que no es entero. ❌ **No cumple**.
**Respuesta final:** Es **inyectiva pero no sobreyectiva**. Por lo tanto, **no es biyectiva** y no tiene inversa en los enteros.

---

**Ejercicio 2:** Dadas `f(x) = x^2` y `g(x) = x + 1`, calcula `(f ∘ g)(x)` y `(g ∘ f)(x)`.

**Solución:**
- `(f ∘ g)(x) = f(g(x)) = f(x + 1) = (x + 1)^2 = x^2 + 2x + 1`.
- `(g ∘ f)(x) = g(f(x)) = g(x^2) = x^2 + 1`.
**Conclusión:** Son diferentes, así que la composición no es conmutativa.

---

**Ejercicio 3:** Encuentra la inversa de `f: ℝ → ℝ` definida por `f(x) = 3x - 2`.

**Solución:**
1. Verificamos que es biyectiva: es una recta, claramente inyectiva y sobreyectiva en los reales. ✅
2. Escribimos `y = 3x - 2`.
3. Despejamos `x`: `3x = y + 2 → x = (y + 2) / 3`.
4. Cambiamos notación: `f^{-1}(y) = (y + 2) / 3`.
5. Si queremos con variable `x`: `f^{-1}(x) = (x + 2) / 3`.
**Respuesta:** `f^{-1}(x) = (x + 2) / 3`.

---

## 9. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos. Las soluciones están al final (no hagas trampa).**

1. **Clasifica** la función `f: ℕ → ℕ` definida por `f(x) = x + 1`. ¿Es inyectiva? ¿Sobreyectiva? ¿Biyectiva? (Recuerda que ℕ = {1, 2, 3, ...}).

2. **Composición:** Si `f(x) = x/2` y `g(x) = 2x + 3`, calcula `(f ∘ g)(x)` y `(g ∘ f)(x)`.

3. **Inversa:** Encuentra la inversa de `f(x) = (x - 1) / 2` (con dominio y codominio en ℝ).

4. **Desafío:** ¿Existe una función inyectiva de `A = {1, 2}` a `B = {a, b, c}`? Si existe, da un ejemplo. ¿Y una sobreyectiva? Justifica.

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

1. **Solución:**
   - **Inyectiva:** `f(a) = f(b) → a+1 = b+1 → a = b`. ✅
   - **Sobreyectiva:** ¿Todo natural `y` tiene un `x` tal que `x+1 = y`? Si `y = 1`, necesitamos `x = 0`, pero 0 no está en ℕ (empezamos en 1). ❌ **No es sobreyectiva** porque el 1 nunca es alcanzado.
   - **Biyectiva:** No, porque no es sobreyectiva.
   **Respuesta:** Solo inyectiva.

2. **Solución:**
   - `(f ∘ g)(x) = f(g(x)) = f(2x+3) = (2x+3)/2 = x + 1.5`.
   - `(g ∘ f)(x) = g(f(x)) = g(x/2) = 2*(x/2) + 3 = x + 3`.
   **Conclusión:** `x + 1.5 ≠ x + 3`, así que no son iguales.

3. **Solución:**
   - Escribimos `y = (x - 1) / 2`.
   - Despejamos: `2y = x - 1 → x = 2y + 1`.
   - Cambiamos notación: `f^{-1}(x) = 2x + 1`.

4. **Solución:**
   - **Inyectiva:** Sí. Ejemplo: `f(1) = a`, `f(2) = b`. (Cada uno va a un elemento distinto). Es posible porque `B` tiene más elementos que `A`.
   - **Sobreyectiva:** **No**, porque `B` tiene 3 elementos y `A` solo 2. Una función solo puede generar como máximo 2 salidas diferentes (una por cada elemento de A). Como `|B| = 3 > 2`, al menos un elemento de B se queda sin flecha. **No puede ser sobreyectiva**.

</details>

---

## 10. Conclusión del Módulo 4 (Funciones)

¡Ya dominas el concepto más importante de las matemáticas aplicadas!

- Aprendiste que una función es una relación con **existencia y unicidad**.
- Sabes distinguir si es **inyectiva** (uno a uno), **sobreyectiva** (cubre todo el codominio) o **biyectiva** (ambas).
- Compones funciones y sabes que el orden importa.
- Sabes calcular la función inversa **solo si es biyectiva**.

**La conexión con tu siguiente tema (Combinatoria):** La combinatoria es el arte de contar. Y para contar bien, necesitamos entender cuántas funciones hay entre dos conjuntos. Por ejemplo, ¿cuántas funciones inyectivas hay de `A` en `B` si `|A|=3` y `|B|=5`? Eso es **Combinatoria**, y lo veremos en el Módulo 5.

**Guardar cambios:** Crea un nuevo archivo con este contenido y nómbralo `04_Funciones.txt` o `.md`.

¿Listo para el **Módulo 5: Combinatoria**? 🚀