# MÓDULO 1: Lógica Proposicional - Plan de Animación Ordenado
**Estilo:** First-principles + Whiteboard minimalista (papel claro, tinta negra, acentos azul/naranja)
**Fuente:** `logica_proposicional` (Subtemas 1-15)

## Estructura: 1 Módulo = 6 Videos Cortos (2-3 min c/u) = Serie en orden

Cada video sigue el prompt de 4 fases internamente:
1. Problema Original -> 2. Evolución Intuitiva -> 3. Aha! -> 4. Relevancia

---

### VIDEO 1.1: ¿Qué es una Proposición? (Subtema 1 - line 6)
**Guion first-principles:**
1. Problema: Antes de Boole, ¿cómo decidir si una frase es discutible? Ambigüedad del lenguaje natural.
2. Evolución: Necesidad de clasificar frases en V/F. Ejemplo: "Colombia está en Sudamérica" vs "¿Cómo estás?" vs "x+3=10"
3. Aha!: Definición formal + Atómica vs Molecular. Es el bit 0/1 del pensamiento.
4. Relevancia: Todo `if` en código es una proposición. Base de la computación.

**Visual:** Frases que caen y se sellan con V/F o se tachan (no proposición). Whiteboard.

### VIDEO 1.2: Los Ladrillos - NOT, AND, OR (Subtema 2 - line 20)
**Guion:**
1. Problema: Una sola proposición no basta. Necesitamos combinar ideas: "Tengo dinero Y tengo tiempo"
2. Evolución: Inventamos conectores como interruptores físicos. AND = dos interruptores en serie, OR = en paralelo.
3. Aha!: Tabla de 4 filas no es para memorizar, es enumerar todas las realidades posibles.
4. Relevancia: Circuitos lógicos, compuertas AND/OR en tu CPU.

**Visual:** 2 interruptores + bombilla. Animación del circuito que se cierra.

### VIDEO 1.3: La Tabla de Verdad como Máquina (Subtema 4 - line 64)
**Guion:**
1. Problema: ¿Cómo no olvidar ningún caso con 3 variables (p,q,r)?
2. Evolución: Método binario V=1 F=0, contar VVV -> FFF. Jerarquía de evaluación.
3. Aha!: La tabla es un algoritmo mecánico, no magia.
4. Relevancia: Tablas de verdad = tests unitarios exhaustivos.

**Visual:** Construcción de tabla fila por fila como contador binario.

### VIDEO 1.4: El Villano - La Implicación → (Subtema 3 - line 46) *VIDEO CLAVE*
**Guion:**
1. Problema: "Si terminas el proyecto, te doy bono" - ¿cuándo miente el jefe?
2. Evolución: Analizar los 4 casos de la promesa.
3. Aha!: Solo es falsa en V->F. F->V es veracidad vacua (no mintió porque no se activó la promesa). `p->q ≡ ¬p ∨ q`
4. Relevancia: `if (p) { q }` en código. Si p es falso, el bloque no se ejecuta, no es error.

**Visual:** 4 viñetas de la promesa. Tabla p->q con único rojo. Ya tenemos prototipo `ImplicacionTablaVerdad`.

### VIDEO 1.5: El Kit de Herramientas - Leyes y Familia (Subtemas 5,6,7 - line 83,102,117)
**Guion:**
1. Problema: Las tablas son lentas. ¿Cómo simplificar sin recalcular todo?
2. Evolución: Descubrimos equivalencias `≡` como atajos algebraicos. De Morgan, contrapositiva.
3. Aha!: Negar no es poner un "no" delante. `¬(p∧q) → ¬p∨¬q` se ve como romper paréntesis. `¬(p→q) = p∧¬q`
4. Relevancia: Refactorizar condiciones: `if (!(a && b))` -> `if (!a || !b)` (De Morgan en código real). Contrapositiva = demostrar lo contrario.

**Visual:** Fórmulas que se transforman morfoseando, resaltando el cambio ∧<->∨.

### VIDEO 1.6: El Salto a lo Infinito - Cuantificadores (Parte II - line 190-256)
**Guion:**
1. Problema: "2+2=5 es falso" sirve, pero "Todos los humanos son mortales" no cabe en p,q.
2. Evolución: Necesitamos hablar de colecciones: ∀ (para todo) y ∃ (existe). Dominio de discurso.
3. Aha!: `∀x (A(x)->B(x))` vs `∃x (A(x)∧B(x))` - el error de usar ∧ con ∀. Negación `¬∀ = ∃¬`. Orden `∀x∃y` vs `∃y∀x`.
4. Relevancia: SQL `SELECT * WHERE`, bucles `forAll` / `exists` en programación. Puente directo a Módulo 2: Conjunto = {x | P(x)}.

**Visual:** Puntos en un universo que se iluminan. ∀ = barnido sobre todos, ∃ = encontrar uno que brilla.

---
**Orden de producción:** 1.1 -> 1.2 -> 1.3 -> 1.4 -> 1.5 -> 1.6
**Estética global:** Fondo #FDF6E3 (papel), tinta #2C3E50, acentos #2980B9/#E67E22, mucho espacio negativo, Write() lento.
