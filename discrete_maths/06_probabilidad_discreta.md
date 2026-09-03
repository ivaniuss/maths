# MATEMÁTICA DISCRETA - MÓDULO 6: PROBABILIDAD DISCRETA
**Versión Auto-Estudio | Explicaciones + Ejemplos + Ejercicios**

---

## 1. ¿Qué es la Probabilidad? (La Ciencia de la Incertidumbre)

**Definición:** La probabilidad es una medida numérica que cuantifica qué tan seguro es que ocurra un evento. Va de **0 a 1** (o de 0% a 100%).

- **Probabilidad = 0:** El evento es **imposible**. (Ej: Que un dado normal caiga en 7).
- **Probabilidad = 1:** El evento es **seguro**. (Ej: Que un dado normal caiga en un número del 1 al 6).
- **Probabilidad = 0.5:** El evento es **tan probable como improbable**. (Ej: Que una moneda caiga en cara).

**¿Por qué "Discreta"?** Porque trabajamos con conjuntos finitos o contables (dados, cartas, personas), no con mediciones continuas (como la temperatura exacta). Aquí los resultados son "saltos" (1, 2, 3...).

---

## 2. Espacio Muestral (`Ω`) y Eventos (`E`)

- **Espacio Muestral (`Ω`):** Es el conjunto de **todos los resultados posibles** de un experimento.
  - *Ejemplo:* Lanzar un dado → `Ω = {1, 2, 3, 4, 5, 6}`.
- **Evento (`E`):** Es cualquier **subconjunto** del espacio muestral. Es un resultado o grupo de resultados que nos interesa.
  - *Ejemplo:* Que salga un número par → `E = {2, 4, 6}`.
  - *Ejemplo:* Que salga un 5 → `E = {5}` (Evento elemental).

**Regla de oro:** La probabilidad de un evento es la suma de las probabilidades de los resultados elementales que lo componen.

---

## 3. La Regla de Laplace (El "Corazón" de la Probabilidad Clásica)

Si todos los resultados en el espacio muestral son **igualmente probables** (como un dado justo o una moneda sin truco), entonces la probabilidad de un evento `E` es:

> **`P(E) = (Número de casos favorables a E) / (Número de casos totales en Ω)`**

**Ejemplo clásico:** ¿Cuál es la probabilidad de obtener un número par al lanzar un dado?
- Casos favorables: `{2, 4, 6}` → 3 casos.
- Casos totales: `{1, 2, 3, 4, 5, 6}` → 6 casos.
- `P(par) = 3 / 6 = 1 / 2 = 0.5` (50%).

**¡Cuidado!** Esta regla solo aplica si los resultados son equiprobables. Si el dado está cargado, no sirve.

---

## 4. Axiomas de la Probabilidad (Las Reglas del Juego)

Son las tres leyes fundamentales que toda probabilidad debe cumplir. Las inventó Kolmogorov, el papá de la probabilidad moderna.

1. **Axioma 1 (No negatividad):** La probabilidad de cualquier evento `E` es mayor o igual a 0: `P(E) ≥ 0`.
2. **Axioma 2 (Certexa):** La probabilidad de todo el espacio muestral es 1: `P(Ω) = 1`.
3. **Axioma 3 (Aditividad):** Si dos eventos `A` y `B` son **mutuamente excluyentes** (no pueden ocurrir al mismo tiempo), entonces la probabilidad de que ocurra `A` o `B` es `P(A ∪ B) = P(A) + P(B)`.
   - *Ejemplo:* Lanzar un dado. `P(salga 1) = 1/6`, `P(salga 2) = 1/6`. Como no puede salir 1 y 2 a la vez, `P(1 o 2) = 1/6 + 1/6 = 1/3`.

---

## 5. Propiedades Derivadas (Lo que se deduce de los Axiomas)

Estas propiedades son súper útiles para resolver problemas:

- **Probabilidad del complemento:** `P(E') = 1 - P(E)`.
  - *Ejemplo:* Si la probabilidad de que llueva es 0.3, la de que NO llueva es 0.7.
- **Probabilidad de la unión de dos eventos (Regla de la Adición General):** 
  > **`P(A ∪ B) = P(A) + P(B) - P(A ∩ B)`**
  - *¿Por qué se resta?* Porque si sumamos `P(A) + P(B)`, los elementos que están en ambos (intersección) los contamos dos veces, y hay que restarlos una vez.
  - *Ejemplo:* ¿Probabilidad de que al sacar una carta de una baraja sea un As o una carta de Tréboles?
    - `P(As) = 4/52`, `P(Trébol) = 13/52`, `P(As ∩ Trébol) = 1/52` (el As de Tréboles).
    - `P(As ∪ Trébol) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13`.

---

## 6. Probabilidad Condicional (`P(A|B)`) - "Si ya pasó B, ¿qué pasa con A?"

La probabilidad de que ocurra `A` **dado que** ya ocurrió `B`. Es una de las herramientas más poderosas.

**Fórmula:** `P(A | B) = P(A ∩ B) / P(B)` (siempre que `P(B) > 0`).

**Analogía:** Imagina que tienes una bolsa con 5 canicas rojas y 5 azules. Sacas una canica al azar sin mirar.
- ¿Cuál es la probabilidad de que sea roja? `5/10 = 1/2`.
- **Ahora condicional:** ¿Cuál es la probabilidad de que sea roja **dado que** te dijeron que no es azul? (Sabemos que es roja segura). `P(Roja | No Azul) = 1`. Porque la condición reduce el espacio muestral solo a las rojas.

**Regla de la Multiplicación (para eventos dependientes):**
De la fórmula anterior se desprende: 
> **`P(A ∩ B) = P(A) * P(B | A)`** (o también `P(A ∩ B) = P(B) * P(A | B)`).

---

## 7. Eventos Independientes (Sin Efectos entre ellos)

Dos eventos `A` y `B` son **independientes** si la ocurrencia de uno **no afecta** la probabilidad del otro. 

**Definición formal:** `A` y `B` son independientes si `P(A | B) = P(A)` (o `P(B | A) = P(B)`).

**Consecuencia (Regla de la Multiplicación para independientes):**
> **`P(A ∩ B) = P(A) * P(B)`**

**Ejemplo clásico:** Lanzas un dado y una moneda.
- `A` = "El dado sale 6" → `P(A)=1/6`.
- `B` = "La moneda sale Cara" → `P(B)=1/2`.
- Son independientes porque lo que pase en el dado no afecta a la moneda.
- `P(A ∩ B) = (1/6) * (1/2) = 1/12`.

---

## 8. Teorema de Bayes (El Santo Grial de la Actualización de Creencias)

**¿Qué hace?** Te permite **invertir** probabilidades condicionales. Si sabes `P(A|B)`, este teorema te dice cómo calcular `P(B|A)`. Es la base de los filtros de spam, los diagnósticos médicos y la inteligencia artificial.

**Fórmula:** 
> **`P(A | B) = [P(B | A) * P(A)] / P(B)`**

**Analogía (El problema del médico):**
- Una enfermedad afecta al 1% de la población: `P(Enfermo) = 0.01`.
- La prueba detecta al 99% de los enfermos (sensibilidad): `P(PruebaPositiva | Enfermo) = 0.99`.
- La prueba da falsos positivos en el 2% de los sanos: `P(PruebaPositiva | Sano) = 0.02`.

**Pregunta:** Si una persona da positivo, ¿qué probabilidad hay de que realmente esté enferma? `P(Enfermo | Positivo)`.

**Solución con Bayes:**
- `P(Enfermo) = 0.01`, `P(Sano) = 0.99`.
- `P(Positivo | Enfermo) = 0.99`.
- `P(Positivo | Sano) = 0.02`.
- `P(Positivo) = P(Positivo|Enfermo)*P(Enfermo) + P(Positivo|Sano)*P(Sano) = (0.99*0.01) + (0.02*0.99) = 0.0099 + 0.0198 = 0.0297`.

Aplicamos Bayes:
`P(Enfermo | Positivo) = [0.99 * 0.01] / 0.0297 = 0.0099 / 0.0297 ≈ 0.333` ≈ **33.3%**.

**Conclusión alucinante:** Aunque la prueba es muy buena, un positivo solo da un 33% de probabilidad real de estar enfermo. ¡Porque la enfermedad es muy rara y hay muchos falsos positivos! Esto es un clásico que se usa en medicina y estadística.

---

## 9. Ejercicios Resueltos (Paso a Paso)

**Ejercicio 1:** Se lanzan dos dados justos. ¿Cuál es la probabilidad de que la suma sea 7?

**Solución:**
1. Espacio muestral total: `6 * 6 = 36` combinaciones equiprobables.
2. Casos favorables (suma 7): `(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)` → 6 casos.
3. `P(suma 7) = 6/36 = 1/6`.
**Respuesta:** `1/6`.

---

**Ejercicio 2:** En una bolsa hay 3 bolas rojas y 2 azules. Se sacan dos bolas **sin reemplazo**. ¿Cuál es la probabilidad de que ambas sean rojas?

**Solución:**
- `A` = "Primera roja", `B` = "Segunda roja".
- `P(A) = 3/5`.
- Si la primera fue roja, quedan 2 rojas y 2 azules (total 4). `P(B | A) = 2/4 = 1/2`.
- Usamos la regla de la multiplicación: `P(A ∩ B) = P(A) * P(B|A) = (3/5) * (1/2) = 3/10`.
**Respuesta:** `3/10 = 0.3`.

---

## 10. Ejercicios para Practicar (RESPONDE TÚ PRIMERO)

**Intenta resolver estos. Las soluciones están al final (no hagas trampa).**

1. **Probabilidad Simple:** Al lanzar un dado de 6 caras, ¿cuál es la probabilidad de obtener un número mayor que 4?

2. **Regla de la Adición:** En un mazo de 52 cartas, ¿cuál es la probabilidad de sacar una carta que sea un Rey o una carta de Corazones?

3. **Condicional:** En una clase hay 60% de chicos y 40% de chicas. El 50% de los chicos juega fútbol, y el 20% de las chicas juega fútbol. Si se elige un estudiante al azar y juega fútbol, ¿cuál es la probabilidad de que sea chico?

4. **Independencia:** Se lanzan dos monedas. ¿Cuál es la probabilidad de que ambas caigan en cara?

5. **Teorema de Bayes (Desafío):** En una fábrica, la máquina A produce el 40% de las piezas y tiene un 5% de defectuosas. La máquina B produce el 60% y tiene un 2% de defectuosas. Si se encuentra una pieza defectuosa, ¿cuál es la probabilidad de que venga de la máquina A?

---

<details>
<summary>RESPUESTAS (Solo mira después de intentarlo)</summary>

1. **Respuesta:** Los números mayores que 4 son `{5, 6}` (2 casos). Total 6 casos. `P = 2/6 = 1/3`.

2. **Respuesta:** 
   - `P(Rey) = 4/52`.
   - `P(Corazones) = 13/52`.
   - `P(Rey ∩ Corazones) = 1/52` (el Rey de Corazones).
   - `P(Rey ∪ Corazones) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13`.

3. **Solución:**
   - Definimos: `P(Chico) = 0.6`, `P(Chica) = 0.4`.
   - `P(Fútbol | Chico) = 0.5`, `P(Fútbol | Chica) = 0.2`.
   - Queremos `P(Chico | Fútbol)`.
   - Calculamos `P(Fútbol) = (0.6*0.5) + (0.4*0.2) = 0.3 + 0.08 = 0.38`.
   - Bayes: `P(Chico | Fútbol) = [P(Fútbol|Chico)*P(Chico)] / P(Fútbol) = (0.5 * 0.6) / 0.38 = 0.3 / 0.38 ≈ 0.789`.
   **Respuesta:** `78.9%`.

4. **Respuesta:** 
   - Eventos independientes: `P(Cara) = 1/2` para cada moneda.
   - `P(Cara y Cara) = (1/2) * (1/2) = 1/4 = 0.25`.

5. **Solución:**
   - `P(A) = 0.4`, `P(Defectuoso|A) = 0.05`.
   - `P(B) = 0.6`, `P(Defectuoso|B) = 0.02`.
   - `P(Defectuoso) = (0.4*0.05) + (0.6*0.02) = 0.02 + 0.012 = 0.032`.
   - Bayes: `P(A | Defectuoso) = [0.05 * 0.4] / 0.032 = 0.02 / 0.032 = 0.625 = 62.5%`.
   **Respuesta:** `62.5%` (A pesar de que A produce menos piezas, sus defectos son más probables que los de B).

</details>

---

## 11. Conclusión del Módulo 6 (Probabilidad Discreta)

¡Acabas de dominar la lógica del azar!

- Distingues entre Espacio Muestral y Evento.
- Aplicas la Regla de Laplace para casos equiprobables.
- Usas la Regla de la Adición (para `A o B`) y la Multiplicación (para `A y B`).
- Calculas probabilidades condicionales y entiendes la independencia.
- Y lo más importante: **has dominado el Teorema de Bayes**, que te permite actualizar tus creencias cuando llega nueva información. ¡Eso es lo que usan los científicos de datos a diario!

**La conexión con tu siguiente tema (Recursión):** La recursión no está directamente relacionada con la probabilidad, pero es el siguiente paso lógico en tu ruta porque es la base de todos los algoritmos que estudiaremos después. La probabilidad nos da las herramientas para analizar algoritmos aleatorios, pero la recursión es la herramienta para **construirlos**.

**Guardar cambios:** Reemplaza el contenido de este archivo con el texto de este bloque.

¿Listo para el **Módulo 7: Recursión**? 🔁🚀