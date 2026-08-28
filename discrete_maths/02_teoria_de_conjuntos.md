# MATEMÁTICA DISCRETA - MÓDULO 2: TEORÍA DE CONJUNTOS
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. ¿Qué es un Conjunto?
**Definición:** Un conjunto es una **colección bien definida** de objetos distintos. Estos objetos se llaman **elementos** o **miembros** del conjunto.

- **"Bien definida"** significa que debemos poder decir con certeza si un objeto pertenece o no al conjunto. Nada de ambigüedades.
- **Ejemplo válido:** El conjunto de los números pares positivos menores a 10: `{2, 4, 6, 8}`.
- **NO es conjunto:** "El conjunto de personas altas" (¿qué es "alto"? es subjetivo, no está bien definido).

**Notación:**
- Los conjuntos se denotan con **letras mayúsculas**: `A`, `B`, `C`.
- Los elementos se escriben entre **llaves `{}`** y se separan con comas.
- **Pertenencia:** `a ∈ A` significa "el elemento `a` pertenece al conjunto `A`".
- **No pertenencia:** `a ∉ A` significa "el elemento `a` no pertenece al conjunto `A`".

---

## 2. Dos formas de definir un Conjunto

### a) Por Extensión (Lista explícita)
Escribes **todos** los elementos del conjunto entre llaves.
- `A = {1, 2, 3, 4, 5}` → El conjunto de los números del 1 al 5.
- `B = {lunes, martes, miércoles}` → El conjunto de tres días de la semana.

**Regla de oro:** El orden no importa. `{1, 2}` es el **mismo conjunto** que `{2, 1}`. Tampoco se repiten elementos: `{1, 1, 2}` es simplemente `{1, 2}`.

### b) Por Comprensión (Descripción de una propiedad)
Escribes una variable representativa y una condición (predicado) que deben cumplir los elementos.
- `A = { x | x es un número natural y x < 5 }` → Se lee: "El conjunto de todas las `x` tal que `x` es un número natural y `x` es menor a 5". Esto da `{1, 2, 3, 4}`.
- `B = { x ∈ ℕ | x es par }` → El conjunto de los números naturales pares.

**Formato estándar:** `{ variable | condición( variable ) }` (La barra `|` se lee "tal que").

---

## 3. Conjuntos Especiales (Los más importantes)

| Nombre | Símbolo | Definición | Ejemplo / Nota |
| :--- | :--- | :--- | :--- |
| **Conjunto Vacío** | `∅` o `{}` | El conjunto que no tiene ningún elemento. | No confundir con `{∅}` que es un conjunto que contiene al vacío (tiene 1 elemento). |
| **Conjunto Universal** | `U` | El conjunto que contiene **todos** los elementos posibles en un contexto dado. | Si hablamos de números enteros, `U = ℤ`. Si hablamos de animales, `U` son todos los animales. |
| **Números Naturales** | `ℕ` | `{1, 2, 3, 4, ...}` | Algunos libros incluyen el 0. Siempre aclara qué convención usas. |
| **Números Enteros** | `ℤ` | `{..., -2, -1, 0, 1, 2, ...}` | Viene del alemán *Zahlen*. |
| **Números Racionales** | `ℚ` | Números que se escriben como `a/b` con `a` y `b` enteros, `b ≠ 0`. | Ej: 1/2, -3/4, 5. |
| **Números Reales** | `ℝ` | Todos los números en la recta numérica (incluye π, √2, etc.). | Es el conjunto más grande que usaremos. |

---

## 4. Subconjuntos (`⊆`) y Subconjuntos Propios (`⊂`)

### a) Subconjunto (`A ⊆ B`)
**Definición:** `A` es subconjunto de `B` si **todos** los elementos de `A` están también en `B`.
- **Fórmula lógica:** `∀x (x ∈ A → x ∈ B)`.
- **Ejemplo:** `{1, 2} ⊆ {1, 2, 3}` → Verdadero.
- **Propiedad clave:** El conjunto vacío `∅` es subconjunto de **cualquier** conjunto. Siempre. `∅ ⊆ B` para todo `B`.

### b) Subconjunto Propio (`A ⊂ B`)
**Definición:** `A` es subconjunto propio de `B` si `A ⊆ B` **pero** `A ≠ B` (es decir, B tiene al menos un elemento que A no tiene).
- **Ejemplo:** `{1, 2} ⊂ {1, 2, 3}` → Verdadero.
- **Contraejemplo:** `{1, 2} ⊂ {1, 2}` → Falso (porque son iguales, no es propio).

**Diferencia crucial entre `∈` y `⊆`:**
- `∈` significa "es **un elemento** de". Ej: `2 ∈ {1, 2, 3}`.
- `⊆` significa "es **un subconjunto** de". Ej: `{2} ⊆ {1, 2, 3}`.
- **ERROR TÍPICO:** Decir `2 ⊆ {1, 2, 3}` es FALSO porque `2` no es un conjunto (es un número). Solo los conjuntos pueden ser subconjuntos.

---

## 5. Igualdad de Conjuntos
Dos conjuntos `A` y `B` son **iguales** (`A = B`) si tienen exactamente los mismos elementos.

**Definición formal:** `A = B` si `A ⊆ B` y `B ⊆ A` (es decir, se contienen mutuamente).
- **Ejemplo:** `{1, 2, 3} = {3, 2, 1}` → Verdadero (el orden no importa).

---

## 6. Operaciones entre Conjuntos (La "Aritmética" de Conjuntos)

| Operación | Símbolo | Definición (en lógica) | Diagrama de Venn (mental) | Ejemplo (A={1,2,3}, B={3,4,5}) |
| :--- | :--- | :--- | :--- | :--- |
| **Unión** | `A ∪ B` | `{ x | x ∈ A ∨ x ∈ B }` | Todo lo que está en A o en B (o ambos). | `{1,2,3,4,5}` |
| **Intersección** | `A ∩ B` | `{ x | x ∈ A ∧ x ∈ B }` | Solo lo que está en A y en B a la vez. | `{3}` |
| **Diferencia** | `A \ B` | `{ x | x ∈ A ∧ x ∉ B }` | Lo que está en A pero no en B. | `{1,2}` |
| **Complemento** | `A'` o `A^c` o `¬A` | `{ x ∈ U | x ∉ A }` | Todo lo que está en el universo `U` pero no en A. | Si `U={1,2,3,4,5,6}`, `A'={4,5,6}`. |
| **Diferencia Simétrica** | `A △ B` | `{ x | (x ∈ A ∨ x ∈ B) ∧ ¬(x ∈ A ∧ x ∈ B) }` | Está en A o en B, pero NO en ambos (OR exclusivo). | `{1,2,4,5}` |

**Analogía para recordar:**
- **Unión (∪):** Es el OR lógico (`∨`).
- **Intersección (∩):** Es el AND lógico (`∧`).
- **Complemento (`'`):** Es la Negación (`¬`).
- **Diferencia (`\`):** Es "A y no B" = `A ∧ ¬B`.

---

## 7. Leyes del Álgebra de Conjuntos (Espejo de la Lógica)

Aquí viene la magia. Las leyes de los conjuntos son **idénticas** a las leyes lógicas que ya aprendiste, solo que cambias los símbolos:
- `∨` (OR) se convierte en `∪` (Unión)
- `∧` (AND) se convierte en `∩` (Intersección)
- `¬` (Negación) se convierte en Complemento (`'`)
- `V` (Verdadero) se convierte en `U` (Universal)
- `F` (Falso) se convierte en `∅` (Vacío)

| Ley | Lógica (lo sabes) | Conjuntos (nuevo) |
| :--- | :--- | :--- |
| **Doble Negación / Complemento** | `¬(¬p) ≡ p` | `(A')' = A` |
| **Idempotencia** | `p ∧ p ≡ p` , `p ∨ p ≡ p` | `A ∩ A = A` , `A ∪ A = A` |
| **Conmutativa** | `p ∧ q ≡ q ∧ p` | `A ∩ B = B ∩ A` , `A ∪ B = B ∪ A` |
| **Asociativa** | `(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)` | `(A ∩ B) ∩ C = A ∩ (B ∩ C)` |
| **Distributiva** | `p ∧ (q ∨ r) ≡ (p∧q) ∨ (p∧r)` | `A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)` |
| **De Morgan** | `¬(p∧q) ≡ ¬p∨¬q` | `(A ∩ B)' = A' ∪ B'` |
| | `¬(p∨q) ≡ ¬p∧¬q` | `(A ∪ B)' = A' ∩ B'` |
| **Identidad (Cero/Uno)** | `p ∧ V ≡ p` , `p ∨ F ≡ p` | `A ∩ U = A` , `A ∪ ∅ = A` |
| | `p ∧ F ≡ F` , `p ∨ V ≡ V` | `A ∩ ∅ = ∅` , `A ∪ U = U` |
| **Complemento** | `p ∧ ¬p ≡ F` , `p ∨ ¬p ≡ V` | `A ∩ A' = ∅` , `A ∪ A' = U` |

**Conclusión clave:** Si te sabes las leyes lógicas, **ya te sabes las leyes de conjuntos**. Solo cambia la notación.

---

## 8. Cardinalidad (Tamaño de un Conjunto)

**Definición:** La cardinalidad de un conjunto `A` es el número de elementos que contiene. Se denota `|A|`.

- **Ejemplo:** Si `A = {a, b, c}`, entonces `|A| = 3`.
- **Conjunto vacío:** `|∅| = 0`.

### Principio de Inclusión-Exclusión (Para dos conjuntos):
Esta fórmula permite contar cuántos elementos hay en la unión sin contar dos veces los que están en la intersección:

> **`|A ∪ B| = |A| + |B| - |A ∩ B|`**

**Analogía:** Si tienes 10 personas que comen pizza, 8 que comen hamburguesa, y 3 que comen ambas. ¿Cuántas personas comen pizza o hamburguesa? 
`10 + 8 - 3 = 15`. No sumes 10+8 porque los 3 que comen ambas los estarías contando dos veces.

### Para tres conjuntos (Fórmula extendida):
> `|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|`

(Siempre se suman los de a 3 al final, porque al restarlos 3 veces, los quitamos de más).

---

## 9. Conjunto Potencia (Partes de un Conjunto)

**Definición:** El conjunto potencia de `A`, denotado `P(A)` o `2^A`, es el conjunto de **todos los subconjuntos** de `A` (incluyendo el vacío y el propio `A`).

- **Ejemplo:** Si `A = {1, 2}`.
  - Subconjuntos: `∅`, `{1}`, `{2}`, `{1, 2}`.
  - Entonces `P(A) = { ∅, {1}, {2}, {1, 2} }`.
- **Cardinalidad del conjunto potencia:** Si `|A| = n`, entonces `|P(A)| = 2^n`. 
  - En el ejemplo, `n=2`, entonces `2^2 = 4`. (De ahí viene la notación `2^A`).

**¿Por qué importa?** En computación, el conjunto potencia representa todas las combinaciones posibles de elementos.

---

## 10. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Dado el universo `U = {1, 2, 3, 4, 5, 6, 7}`, `A = {1, 2, 3, 4}` y `B = {3, 4, 5, 6}`. Calcula:
a) `A ∪ B`
b) `A ∩ B`
c) `A \ B`
d) `A'` (Complemento de A)
e) `A △ B`

**Solución:**
a) `A ∪ B = {1, 2, 3, 4, 5, 6}` (todos los que están en alguno).
b) `A ∩ B = {3, 4}` (los que están en ambos).
c) `A \ B = {1, 2}` (los que están en A pero NO en B).
d) `A' = U \ A = {5, 6, 7}` (los que están en U pero no en A).
e) `A △ B = (A ∪ B) \ (A ∩ B) = {1, 2, 5, 6}` (están en uno solo de los dos).

---

**Ejercicio 2:** Simplifica la expresión de conjuntos: `(A ∩ B) ∪ (A ∩ B')`.
**Solución:**
1. Aplicamos la ley distributiva al revés (factor común `A`): `A ∩ (B ∪ B')`.
2. `B ∪ B' = U` (Complemento: un conjunto y su contrario dan el Universal).
3. `A ∩ U = A` (Identidad).
**Resultado final:** `A`. 
*(Esto tiene sentido lógico: "Los elementos que están en A y B, o en A y no en B" son simplemente los que están en A).*

---

**Ejercicio 3:** En una encuesta a 100 personas:
- 50 ven fútbol.
- 40 ven baloncesto.
- 20 ven ambos deportes.
¿Cuántas personas ven **al menos uno** de los dos deportes?

**Solución:**
Usamos el principio de inclusión-exclusión:
`|Fútbol ∪ Baloncesto| = |Fútbol| + |Baloncesto| - |Fútbol ∩ Baloncesto|`
`= 50 + 40 - 20 = 70`.
**Respuesta final:** 70 personas ven al menos uno.

---

## 11. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos. Las soluciones están al final (no hagas trampa).**

1. **Dado `A = {x ∈ ℕ | x < 5}` y `B = {x ∈ ℕ | x es par y x ≤ 6}`**, escribe por extensión: `A ∩ B` y `A ∪ B`.

2. **¿Verdadero o Falso?** Justifica brevemente:
   a) `∅ ∈ {1, 2, 3}`
   b) `∅ ⊆ {1, 2, 3}`
   c) `{1} ∈ {1, 2, 3}`
   d) `{1} ⊆ {1, 2, 3}`

3. **Simplifica** la siguiente expresión de conjuntos usando las leyes: `(A ∩ B) ∪ (A ∩ B ∩ C)`.
   *(Pista: factoriza `A ∩ B` y usa la ley de absorción o la de identidad).*

4. **Cardinalidad:** Si `|A| = 10`, `|B| = 7` y `|A ∩ B| = 3`, ¿cuánto vale `|A △ B|` (diferencia simétrica)?

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

1. **Solución:**
   - `A = {1, 2, 3, 4}` (naturales menores que 5).
   - `B = {2, 4, 6}` (pares menores o iguales a 6).
   - `A ∩ B = {2, 4}`.
   - `A ∪ B = {1, 2, 3, 4, 6}`.

2. **Soluciones:**
   a) **Falso.** `∅` es un conjunto, no un número. `{1,2,3}` solo tiene números como elementos.
   b) **Verdadero.** El vacío es subconjunto de **todo** conjunto.
   c) **Falso.** `{1}` es un conjunto, no es un elemento de `{1,2,3}` (los elementos son 1, 2 y 3). Ojo: `{1} ∈ {1, {2}, 3}` sería verdadero si el conjunto contiene a `{1}`, pero no en este caso.
   d) **Verdadero.** El elemento `1` está dentro, por lo que el conjunto `{1}` es subconjunto.

3. **Solución:**
   - `(A ∩ B) ∪ (A ∩ B ∩ C)`.
   - Factorizamos `(A ∩ B)`: `(A ∩ B) ∪ [(A ∩ B) ∩ C]`.
   - Aplicamos la ley de absorción (que dice que `X ∪ (X ∩ C) = X`).
   - Esto se reduce a **`A ∩ B`**.
   *(Interpretación: Si un elemento está en A y B, ya sea que esté o no en C, no importa; la condición fuerte es estar en A y en B).*

4. **Solución:**
   - La diferencia simétrica son los elementos que están en A o en B, pero no en ambos.
   - Fórmula: `|A △ B| = |A ∪ B| - |A ∩ B|`.
   - Primero, `|A ∪ B| = 10 + 7 - 3 = 14`.
   - Entonces, `|A △ B| = 14 - 3 = 11`.
   **Respuesta:** 11.

</details>

---

## 12. Conclusión del Módulo 2 (Teoría de Conjuntos)

¡Felicidades! Ya dominas el lenguaje de las colecciones.

- Aprendiste a definir conjuntos por extensión y comprensión.
- Manejas las operaciones (Unión, Intersección, Diferencia, Complemento) y sus leyes, que son un calco de la lógica proposicional.
- Sabes contar elementos usando el Principio de Inclusión-Exclusión.
- Entiendes el concepto de subconjunto y conjunto potencia.

**La conexión con tu siguiente tema (Relaciones):** Una relación no es más que un **subconjunto del producto cartesiano** entre dos conjuntos. Por ejemplo, si tenemos el conjunto de estudiantes y el de materias, la relación "está inscrito en" es un conjunto de pares ordenados `(estudiante, materia)`. Para definir eso, necesitamos primero entender el **Producto Cartesiano**, que es la primera parte del Módulo 3.

**Guardar cambios:** Crea un nuevo archivo con este contenido y nómbralo `02_Teoria_de_Conjuntos.txt` o `.md`.

¿Listo para el **Módulo 3: Relaciones**? 🚀