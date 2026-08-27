# MATEMÁTICA DISCRETA - MÓDULO 1: LÓGICA PROPOSICIONAL Y CUANTIFICADORES
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. ¿Qué es una Proposición?
**Definición:** Es una oración declarativa que **necesariamente** debe ser o Verdadera (V) o Falsa (F), pero nunca ambas al mismo tiempo.

- **Ejemplo válido:** *"Colombia está en Sudamérica"* (Verdadero).
- **Ejemplo válido:** *"2 + 2 = 5"* (Falso).
- **NO es proposición:** *"¿Cómo estás?"* (no es declarativa).
- **NO es proposición:** *"x + 3 = 10"* (no sabemos cuánto vale x, no tiene valor fijo).

**Clasificación:**
- **Simples (Atómicas):** Una sola idea. Ej: `p = "Está lloviendo"`.
- **Compuestas (Moleculares):** Unión de dos o más simples mediante conectores lógicos. Ej: *"Está lloviendo Y hace frío"*.

---

## 2. Conectores Básicos: NOT, AND, OR

### a) Negación (NOT) - `¬p`
Invierte el valor de verdad. 
- Si `p` es Verdadero, `¬p` es Falso.
- **Ejemplo:** `p = "Soy mayor de edad"`. `¬p = "NO soy mayor de edad"`.

### b) Conjunción (AND) - `p ∧ q`
Solo es **Verdadero** si **ambas** proposiciones son verdaderas. Basta con que una sea falsa para que todo sea falso.
- **Ejemplo:** *"Tengo dinero Y tengo tiempo"*. Si no tengo dinero, toda la frase es falsa, aunque tenga tiempo.

### c) Disyunción (OR) - `p ∨ q`
Es **Falso** solo si **ambas** son falsas. En matemáticas y computación, el OR siempre es **inclusivo** (significa "una o la otra o ambas").
- **Ejemplo:** *"Aprobaré estudiando O aprobaré haciendo trampa"*. Es verdad si estudio, si hago trampa, o si hago ambas.

**Tabla de verdad de los 3 básicos:**

| p | q | ¬p | p ∧ q | p ∨ q |
| :---: | :---: | :---: | :---: | :---: |
| V | V | F | V | V |
| V | F | F | F | V |
| F | V | V | F | V |
| F | F | V | F | F |

---

## 3. El Gran Problema: La Implicación (→) - "Si... entonces..."
Es el conector más difícil de entender porque choca con el español cotidiano. 

**Definición formal:** `p → q` (Si p, entonces q). Solo es **FALSA** en **UN ÚNICO CASO**: cuando `p` es Verdadera y `q` es Falsa. En todos los demás casos, es Verdadera.

**La "Promesa" (La mejor analogía):**
Imagina que tu jefe te dice: *"Si terminas el proyecto (p), entonces te daré un bono (q)"*. 
Analicemos las 4 opciones:

1. **Terminas (V) y te da el bono (V):** El jefe cumplió → **Verdadero**.
2. **Terminas (V) y NO te da el bono (F):** El jefe mintió → **Falso** (el único caso).
3. **NO terminas (F) y te da el bono (V):** El jefe es un loco generoso, pero **NO mintió** (nunca dijo que pasaría si no terminabas). Como no rompió su palabra → **Verdadero**.
4. **NO terminas (F) y NO te da el bono (F):** El jefe no hizo nada, pero tampoco mintió → **Verdadero**.

**Conclusión clave:** La implicación solo se preocupa por **no ser falsa**. Si el "Si" no se cumple, la promesa no se activa y automáticamente es verdadera (esto se llama *"Veracidad Vacua"*).

---

## 4. Construcción de Tablas de Verdad (Método Sistemático)
Para construir tablas de más de 2 variables (ej: `(p → q) ∨ ¬r`), debes seguir un orden jerárquico:
1. **Paréntesis** (de adentro hacia afuera).
2. **Negaciones (¬)**.
3. **AND (∧) y OR (∨)**.
4. **Implicación (→)** (se evalúa al final, o cuando esté entre paréntesis).

**Orden para escribir las combinaciones:** Si tienes 3 variables (p, q, r), escribe las filas como si contaras en binario (V=1, F=0), para no repetir ni olvidar ninguna:
- Fila 1: V V V
- Fila 2: V V F
- Fila 3: V F V
- Fila 4: V F F
- Fila 5: F V V
- Fila 6: F V F
- Fila 7: F F V
- Fila 8: F F F

---

## 5. Leyes de Equivalencia Lógica (El Álgebra de la Lógica)
Dos proposiciones son **equivalentes (`≡`)** cuando, al hacer sus tablas de verdad, les da **exactamente la misma columna final** (fila por fila).

Aquí tienes las leyes agrupadas por "utilidad". No las memorices de golpe, entiéndelas:

| Categoría | Leyes (p, q, r son variables; V = Verdadero, F = Falso) |
| :--- | :--- |
| **Doble Negación** | `¬(¬p) ≡ p` (Decir "no es falso que..." es afirmar) |
| **Idempotencia** | `p ∧ p ≡ p` (Verde Y Verde es Verde) <br> `p ∨ p ≡ p` |
| **Conmutativa** | `p ∧ q ≡ q ∧ p` (El orden da igual) <br> `p ∨ q ≡ q ∨ p` |
| **Asociativa** | `(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)` (Da igual cómo agrupes) |
| **Distributiva** | `p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)` (El AND se distribuye) |
| **De Morgan (CRUCIAL)** | **`¬(p ∧ q) ≡ ¬p ∨ ¬q`** <br> **`¬(p ∨ q) ≡ ¬p ∧ ¬q`** <br> *Traducción: La negación rompe el paréntesis, y el AND se convierte en OR (y viceversa).* |
| **Identidad (Cero/Uno)** | `p ∧ V ≡ p` , `p ∨ F ≡ p` <br> `p ∧ F ≡ F` , `p ∨ V ≡ V` |
| **Complemento (Tercio excluido)** | `p ∧ ¬p ≡ F` (Algo no puede ser y no ser a la vez) <br> `p ∨ ¬p ≡ V` (Algo ES o NO ES, no hay término medio) |
| **Implicación (LA MÁS USADA)** | **`p → q ≡ ¬p ∨ q`** <br> *Traducción: "Si llueve, me mojo" es lo mismo que "NO llueve O me mojo".* |

---

## 6. La Familia de la Implicación: Converse, Inverse y Contrapositive
Cuando tienes una implicación `p → q`, puedes formar 3 nuevas proposiciones moviendo y negando sus partes. 

**BASE:** `p → q` (Si eres bomberos, entonces apagas fuegos).

| Nombre | Fórmula | ¿Es equivalente a la Base? | Explicación / Contraejemplo |
| :--- | :--- | :--- | :--- |
| **Converse (Recíproca)** | `q → p` | **NO** ❌ | *Si apagas fuegos, entonces eres bombero*. (Falso, porque un agricultor también apaga fuegos para quemar rastrojos). |
| **Inverse (Inversa)** | `¬p → ¬q` | **NO** ❌ | *Si NO eres bombero, entonces NO apagas fuegos*. (Falso, porque puedes ser voluntario y apagar fuegos). |
| **Contrapositive (Contrarrecíproca)** | `¬q → ¬p` | **SÍ ✅ (EQUIVALENTE)** | *Si NO apagas fuegos, entonces NO eres bombero*. (Verdadero, porque todo bombero apaga fuegos). |

**Regla de ORO para toda la vida:** `p → q` **SIEMPRE** es equivalente a `¬q → ¬p`. 
Si un día necesitas demostrar algo en matemáticas y es muy difícil, intenta demostrar su **Contrarrecíproca**. Es una estrategia de demostración llamada *"Demostración por Contraposición"*.

---

## 7. Cómo Negar Correctamente (Lo que más falla en exámenes)

- **Negar una conjunción (AND):** `¬(p ∧ q)` → Se convierte en **`¬p ∨ ¬q`**. 
  - *Ejemplo práctico:* *"No es cierto que tenga hambre Y tenga sueño"* significa *"O NO tengo hambre O NO tengo sueño"*.
- **Negar una disyunción (OR):** `¬(p ∨ q)` → Se convierte en **`¬p ∧ ¬q`**.
  - *Ejemplo práctico:* *"No es cierto que sea español O francés"* significa *"NO soy español Y NO soy francés"*.
- **Negar una implicación (→):** `¬(p → q)` → Recuerda que `p → q` es `¬p ∨ q`. Al negarlo: `¬(¬p ∨ q)` = `p ∧ ¬q`.
  - **FÓRMULA MÁGICA:** `¬(p → q) ≡ p ∧ ¬q`.
  - *Ejemplo:* La negación de *"Si estudio, apruebo"* es *"Estudio Y NO apruebo"*. ¡Es la única forma de demostrar que la promesa era mentira!

---

## 8. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Simplifica la expresión `¬(¬p ∧ q)` usando leyes lógicas.
**Solución:**
1. Aplicamos De Morgan: `¬(¬p) ∨ ¬q`.
2. Aplicamos Doble Negación: `p ∨ ¬q`.
**Resultado final:** `p ∨ ¬q`.

---

**Ejercicio 2:** Simplifica `(p → q) ∧ ¬q`.
**Solución:**
1. Sustituimos la implicación: `(¬p ∨ q) ∧ ¬q`.
2. Aplicamos distributiva (o razonamos): `(¬p ∧ ¬q) ∨ (q ∧ ¬q)`.
3. `q ∧ ¬q` es `Falso (F)`.
4. `(¬p ∧ ¬q) ∨ F` → eliminar el Falso, queda `¬p ∧ ¬q`.
**Resultado final:** `¬p ∧ ¬q`. 
*(Interpretación: Si "Si p entonces q" y además "no q", entonces forzosamente "no p" - esto es el razonamiento lógico de "Modus Tollens").*

---

**Ejercicio 3:** Encuentra la Contrarrecíproca de `¬p → q`.
**Solución:**
La receta para la contrarrecíproca es: **Negar ambos lados e invertir el orden**.
1. Negamos el consecuente (la parte de la derecha) y lo ponemos a la izquierda: `¬q`.
2. Negamos el antecedente (la parte de la izquierda) y lo ponemos a la derecha: `¬(¬p)` = `p`.
**Resultado final:** `¬q → p`.

---

## 9. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos 3 ejercicios en un papel. Las respuestas están al final (no hagas trampa).**

1. **Simplifica** la siguiente expresión usando las leyes: `¬(p ∨ ¬q)`.
2. **Simplifica** la siguiente expresión: `(p → q) ∧ (q → p)`. *(Pista: ¿Cómo se llama esto en lógica?)*.
3. **Nega** esta proposición compuesta: `(¬p ∧ q) → r`.

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>


1. **Respuesta:** `¬p ∧ q`. (Aplicas De Morgan: `¬p ∧ ¬(¬q)` → `¬p ∧ q`).
2. **Respuesta:** `p ↔ q` (Bicondicional: "p si y solo si q"). Si simplificas: `(¬p ∨ q) ∧ (¬q ∨ p)`. Esto solo es verdad cuando p y q tienen el mismo valor de verdad.
3. **Respuesta:** `(¬p ∧ q) ∧ ¬r`. (Recuerda la regla de negar implicación: `¬(A → r)` es `A ∧ ¬r`. Aquí `A` es `¬p ∧ q`, así que queda `(¬p ∧ q) ∧ ¬r`).

</details>

---

## 10. Cierre de la Parte I: Lógica Proposicional
Con esto tienes las bases de la lógica proposicional. Esta primera parte reúne los conceptos, las leyes y los ejercicios fundamentales. La lógica proposicional es el "código binario" de tu cerebro: cada vez que uses un `if (condicion)` en programación, estarás aplicando estas tablas de verdad.

Antes de pasar a la siguiente parte, asegúrate de que la negación de implicaciones y las leyes de De Morgan te salgan dormido.


---

## Parte II: Cuantificadores

### 11. Cuantificadores: ∀ (Para todo) y ∃ (Existe)

Hasta ahora trabajamos con proposiciones fijas (`p = "Llueve"`). Pero en matemáticas necesitamos hablar de **colecciones enteras**. 
Por ejemplo: *"Todos los humanos son mortales"*. No podemos asignarle una sola variable `p` a eso, porque se refiere a *cada* humano. Para eso nacen los cuantificadores.

### a) Cuantificador Universal: `∀` (Para todo / Para cada)
- **Símbolo:** `∀` (Una "A" al revés, de *All*).
- **Significado:** La proposición es **verdadera** para **todos** los elementos de un conjunto (dominio).
- **Ejemplo:** `∀x (Humano(x) → Mortal(x))`. 
  - *Traducción:* "Para todo x, si x es Humano, entonces x es Mortal". 
  - En español coloquial: "Todos los humanos son mortales".

### b) Cuantificador Existencial: `∃` (Existe / Al menos uno)
- **Símbolo:** `∃` (Una "E" al revés, de *Exists*).
- **Significado:** La proposición es **verdadera** si **al menos un elemento** del dominio la cumple.
- **Ejemplo:** `∃x (Humano(x) ∧ Sabe_Nadar(x))`.
  - *Traducción:* "Existe al menos un x tal que x es Humano y x sabe nadar".
  - En español coloquial: "Algún humano sabe nadar".

---

## 12. El Dominio de Discurso (El "Universo" de lo que hablamos)
Es el conjunto de todos los elementos que estamos considerando. Si no defines el dominio, los cuantificadores no tienen sentido.

- Si el dominio es **"Todos los animales"**, la frase `∀x (Tiene_Plumas(x))` significa *"Todos los animales tienen plumas"* → Falso (las vacas no).
- Si el dominio es **"Todas las aves"**, la frase `∀x (Tiene_Plumas(x))` significa *"Todas las aves tienen plumas"* → Verdadero.

**Regla de oro:** Siempre debes saber de qué "grupo" estás hablando antes de cuantificar.

---

## 13. La Traducción del Español a la Lógica (El gran dolor de cabeza)

El español es ambiguo. Aquí tienes la guía de traducción:

| Frase en Español | Traducción Lógica | Explicación |
| :--- | :--- | :--- |
| **"Todos los A son B"** | `∀x (A(x) → B(x))` | Usamos **IMPLICACIÓN**. No uses AND aquí, porque sería "Todo x es A y es B", lo cual es demasiado restrictivo. |
| **"Algún A es B"** | `∃x (A(x) ∧ B(x))` | Usamos **AND**. Si usáramos `→` aquí, sería muy débil y casi siempre sería verdadero sin sentido. |
| **"Ningún A es B"** | `¬∃x (A(x) ∧ B(x))` o `∀x (A(x) → ¬B(x))` | Ambas son equivalentes. |

**Ejemplo clave (el que más falla):**
- *"Todas las manzanas son rojas"* se escribe `∀x (Manzana(x) → Roja(x))`. 
- **NUNCA** se escribe `∀x (Manzana(x) ∧ Roja(x))` porque eso diría que *"Todas las cosas del universo son manzanas y son rojas"*. ¡Cuidado!

---

## 14. Negación de Cuantificadores (Las Leyes de De Morgan Gigantes)

Aquí ocurre la magia. Negar un "Para todo" es convertirlo en un "Existe", y viceversa. Es exactamente igual que De Morgan, pero aplicado a conjuntos infinitos.

| Regla | Fórmula | Traducción al Español |
| :--- | :--- | :--- |
| **Negación del Universal** | `¬∀x P(x) ≡ ∃x ¬P(x)` | *"No es cierto que todos cumplan P"* es igual a *"Existe al menos uno que NO cumple P"*. |
| **Negación del Existencial** | `¬∃x P(x) ≡ ∀x ¬P(x)` | *"No es cierto que exista uno que cumpla P"* es igual a *"Todos NO cumplen P"*. |

**Analogía para recordarlo:**
- *"No todos los estudiantes aprobaron"* es equivalente a *"Al menos un estudiante NO aprobó"*.
- *"No hay ningún estudiante que aprobó"* es equivalente a *"Todos los estudiantes NO aprobaron"*.

**Regla práctica para exámenes:** Cuando niegues una frase con cuantificadores, **cambia ∀ por ∃ (o viceversa) y niega la propiedad interior**.

---

## 15. Cuantificadores Anidados (Dos variables)
A veces necesitamos dos cuantificadores para hablar de relaciones entre dos cosas (ej: "Todo el mundo quiere a alguien"). El **orden importa muchísimo**.

**Caso 1:** `∀x ∃y (Ama(x, y))` 
- *Traducción:* "Para toda persona x, existe al menos una persona y tal que x ama a y".
- Español: **"Todo el mundo ama a alguien"** (cada persona tiene a su propio alguien, puede ser diferente).

**Caso 2:** `∃y ∀x (Ama(x, y))`
- *Traducción:* "Existe una persona y, tal que para toda persona x, x ama a y".
- Español: **"Hay alguien a quien todo el mundo ama"** (es la misma persona para todos, como un famoso).

**Conclusión:** El orden de los cuantificadores **NO es conmutativo**. Cambia totalmente el significado.

---

## 16. Ejemplos Resueltos con Cuantificadores (Paso a Paso)

**Ejercicio 4:** Traduce a lógica: *"Todos los perros son leales, pero algunos perros son agresivos"*.
**Solución:**
1. Definimos dominio: Perros.
2. Definimos propiedades: `L(x)` = "x es leal", `A(x)` = "x es agresivo".
3. Traducimos:
   - "Todos los perros son leales": `∀x L(x)`.
   - "Algunos perros son agresivos": `∃x A(x)`.
4. Unimos con "pero" (que es un AND): **`∀x L(x) ∧ ∃x A(x)`**.

---

**Ejercicio 5:** Niega la siguiente proposición: `∀x (Estudiante(x) → Estudia(x))`.
**Solución:**
1. Aplicamos la negación del universal: `¬∀x (Estudiante(x) → Estudia(x)) ≡ ∃x ¬(Estudiante(x) → Estudia(x))`.
2. Negamos la implicación interior (recordando que `¬(p → q) ≡ p ∧ ¬q`): 
   `∃x (Estudiante(x) ∧ ¬Estudia(x))`.
3. Traducción al español: *"Existe un estudiante que NO estudia"*.

---

**Ejercicio 6:** ¿Es `∃x ∀y (x < y)` verdadero si el dominio son los **Números Naturales (1, 2, 3...)**?
**Solución:**
- Traducción: *"Existe un número x que es menor que todos los demás números y"*. 
- En los naturales, si x es 1, no es menor que sí mismo (porque 1 < 1 es falso). Si x es 0, no existe en los naturales. 
- **Respuesta:** Falso. No hay un número natural que sea menor que todos, incluido él mismo.

---

## 17. Ejercicios para Practicar (Cuantificadores) - RESPONDE TÚ PRIMERO

**Intenta resolver estos (las soluciones están al final).**

4. **Traduce a lógica:** *"Ningún pez sabe volar"*. (Dominio: todos los animales. Propiedades: `Pez(x)`, `Vuela(x)`).

5. **Traduce al español:** `∀x ∃y (Amigo(x, y) ∧ ¬(x = y))`. (Donde `Amigo(x,y)` = "x es amigo de y").

6. **Niega la siguiente proposición:** `∃x (Perro(x) ∧ ¬Ladra(x))`. Da el resultado simplificado y su traducción al español.

7. **Verdadero o Falso (con dominio = Números Enteros):** `∀x ∃y (x + y = 0)`. Justifica.

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

4. **Respuesta:** `∀x (Pez(x) → ¬Vuela(x))` o también `¬∃x (Pez(x) ∧ Vuela(x))`. (La primera es la más natural: "Para todo x, si es pez, entonces no vuela").

5. **Traducción:** *"Para toda persona x, existe una persona y tal que x es amigo de y y x NO es igual a y"*. 
   Español coloquial: *"Todo el mundo tiene al menos un amigo que no es él mismo"* (nadie es amigo solo de sí mismo).

6. **Solución:** 
   - Negamos: `¬∃x (Perro(x) ∧ ¬Ladra(x)) ≡ ∀x ¬(Perro(x) ∧ ¬Ladra(x))`.
   - Aplicamos De Morgan al interior: `∀x (¬Perro(x) ∨ Ladra(x))`.
   - Traducción: *"Todos los animales o no son perros o ladran"*, que coloquialmente es *"Todos los perros ladran"* (porque si es perro, forzosamente tiene que ladrar).

7. **Verdadero.** `∀x ∃y (x + y = 0)` dice: *"Para cualquier número entero x, existe un número entero y que es su inverso aditivo"*. Si x=5, y=-5; si x=-3, y=3. Como los enteros tienen negativos, es **Verdadero**.

</details>

---

## 18. Conclusión FINAL del Módulo 1 (Lógica Proposicional + Cuantificadores)

¡Felicidades! Ahora sí has terminado la base de todo el razonamiento lógico-matemático. 

- La **Lógica Proposicional** (`∧`, `∨`, `→`, `¬`) es para verdades exactas y fijas.
- Los **Cuantificadores** (`∀`, `∃`) son para verdades que dependen de elementos de un conjunto.

**La conexión con tu siguiente tema (Conjuntos):** Un conjunto no es más que una colección de elementos que comparten una propiedad. Por ejemplo, el conjunto `A = { x | x es un número par }` se lee *"El conjunto de todas las x tal que x es par"*, y eso usa justamente los cuantificadores que acabas de aprender.

**¡Cierra este archivo y guarda los cambios!** Tu Módulo 1 ahora está COMPLETO al 100%. En el próximo archivo (`02_Teoria_de_Conjuntos.md`) empezaremos con el Tema 2 de tu índice. 🚀