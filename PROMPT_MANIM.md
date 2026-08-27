# PROMPT MAESTRO - Generación de Videos Animados con Manim
**Proyecto:** Animación de Módulos de Matemática Discreta (versión first-principles)
**Autor:** Ivaniuss | Fecha: 2026-08-27 (actualizado con voz sincronizada)
**Para:** Cualquier agente futuro que retome el proyecto

---

## 1. CONTEXTO DEL PROYECTO

**Objetivo:** Convertir los apuntes de texto de Matemática Discreta en serie de videos animados estilo 3Blue1Brown minimalista, priorizando comprensión sobre memorización, con voz sincronizada.

**Fuentes (NO inventar, leer):**
- `discrete_maths/logica_proposicional` (Módulo 1: 343 líneas)
- `discrete_maths/teoria_de_conjuntos.md` (Módulo 2: 267 líneas)
- Repo original: `https://github.com/3b1b/manim` (92.1k stars) pero **usamos Manim Community** `pip install manim`

---

## 2. SETUP TÉCNICO VERIFICADO 2026-08-27

**Entorno:**
- Python 3.12.11 (pyenv), ffmpeg 7.1, TeX Live 2023, sox 14.4.2
- `pip install manim==0.21.0` + `pip install manim-voiceover` + `pip install edge-tts`
- Voz: `es-CO-GonzaloNeural` (male, friendly) o `es-CO-SalomeNeural` (female)
- `manim --version` = 0.21.0

**Estructura:**
```
discrete_maths/
├── logica_proposicional
├── teoria_de_conjuntos.md
├── PROMPT_MANIM.md (este archivo)
├── animaciones/
│   ├── escenas.py (demos dark, obsoletas)
│   └── modulo1/
│       ├── 00_PLAN.md (6 videos ordenados)
│       ├── escenas_modulo1.py (versión sin voz, 30s)
│       ├── escenas_modulo1_vo.py (BUG: add_sound por segmento -> audio pisado)
│       ├── escenas_modulo1_sync.py (CORRECTA: single combined audio, 79s)
│       ├── generar_voz.py (genera s01..s07 con edge-tts)
│       ├── voiceovers/s01_*.mp3 + combined_11.mp3 (75.88s)
│       └── media/videos/...
```

**Comandos:**
```bash
# 1. Generar voz
python3 animaciones/modulo1/generar_voz.py
edge-tts --voice es-CO-GonzaloNeural --rate +0% --text "Hola" --write-media out.mp3
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp3

# 2. Concatenar audios
ffmpeg -f concat -safe 0 -i concat.txt -c copy combined_11.mp3

# 3. Render video SIN audio por segmentos (o con single add_sound)
manim -ql animaciones/modulo1/escenas_modulo1_sync.py Escena11_Proposicion_SYNC

# 4. Video tiene audio ya via self.add_sound(COMBINED) al inicio
# Si se genera sin audio, muxear: ffmpeg -i video_only.mp4 -i combined.mp3 -c:v copy -c:a aac FIXED.mp4
```

**Videos verificados:**
- `media/videos/escenas_modulo1/480p15/Escena11_Proposicion.mp4` (30.5s, sin voz, dark->light, obsoleto)
- `media/videos/escenas_modulo1_vo/480p15/Escena11_Proposicion_VO.mp4` (75.3s, BUG audio pisado)
- `media/videos/escenas_modulo1_vo/480p15/Escena11_Proposicion_VO_FIXED.mp4` (75.8s, FIX tpad pero aún desync en s05->s06)
- `media/videos/escenas_modulo1_sync/480p15/Escena11_Proposicion_SYNC.mp4` (79.26s video + 75.90 audio, SYNC correcto) ✅ CANÓNICO

---

## 3. PROMPT PEDAGÓGICO (CORE)

> "Actúa como divulgador científico experto en pedagogía. Escribe guion para video explicativo sobre **[TEMA]**.
> 1. **El Problema Original:** Época antigua/cotidiano antes de solución moderna.
> 2. **La Evolución Intuitiva:** Construcción paso a paso sin fórmulas inmediatas.
> 3. **El 'Aha!' Moment:** Conexión necesidad básica -> solución elegante.
> 4. **Relevancia Actual:** Conexión con tecnología/ciencia moderna.
> **Tono:** Conversacional, humilde, curioso, centrado en espectador. Evita tecnicismos hasta analogía."

Cada video corto (1 subtema) sigue las 4 fases internamente.

---

## 4. ESTILO VISUAL MINIMALISTA

```python
config.background_color = "#FDF6E3" # papel crema
INK = "#2C3E50"; ACCENT_BLUE="#2980B9"; ACCENT_ORANGE="#E67E22"
ACCENT_GREEN="#27AE60"; ACCENT_RED="#C0392B"; GRAY_SOFT="#7F8C8D"
```
- Whiteboard: `Write()` 1.5-2s, `Create()`, `FadeIn(shift=...)`
- Analogías tangibles: interruptores/bombilla, tarjetas V/F, Venn, etc.
- 1 idea por pantalla, mucho espacio negativo, `RoundedRectangle` blanca
- Ritmo pausado: waits calibrados a duración exacta de audio (ver sección 5)
- Tipografía: `Text` para español, `MathTex` para fórmulas

---

## 5. SINCRONIZACIÓN VOZ-VIDEO (CRÍTICO - LEER BUGFIX 2026-08-27)

**BUG anterior:** Llamar `self.add_sound(s01)`, `self.add_sound(s02)` sin `time_offset` pone todos en t=0, se pisan y queda mute. Además, hacer `FadeOut` entre audios genera silent gap no presente en `combined.mp3`, causando desfase acumulativo (ej: s05 "ninguna de las dos es proposición" ya mostraba s06 "Dos tipos").

**SOLUCIÓN CORRECTA (workflow canónico usado en `escenas_modulo1_sync.py:1`):**

1. **Generar audios por segmento** con `generar_voz.py` (edge-tts, voz `es-CO-GonzaloNeural`, rate `+0%`). Medir duración con `ffprobe`:
   ```
   s01 9.096, s02 9.696, s03 11.064, s04 11.88, s05 12.672, s06 13.2, s07 8.28 = 75.888s
   ```

2. **Concatenar** en UN solo archivo:
   ```bash
   ffmpeg -f concat -safe 0 -i concat.txt -c copy voiceovers/combined_11.mp3
   ```

3. **En Scene, UNA sola llamada al inicio:**
   ```python
   COMBINED = str(VOICE_DIR / "combined_11.mp3")
   class Escena11_SYNC(Scene):
       def construct(self):
           self.add_sound(COMBINED)  # t=0, dura 75.88s
           # luego animaciones con waits que suman EXACTO cada D_Sxx
   ```

4. **Calibrar waits** para que cada bloque dure `D_Sxx`:
   ```python
   D_S01 = 9.096
   self.play(Write(title), run_time=2.0)
   self.play(FadeIn(problema), run_time=1.0)
   self.wait(D_S01 - 2.0 - 1.0)  # 6.096

   # Transiciones (FadeOut) DEBEN estar DENTRO del siguiente bloque, no entre bloques
   # Ej: FadeOut de s02->s03 se hace en los primeros 0.6s de s03:
   self.play(FadeOut(prev), run_time=0.6) # parte de D_S03
   self.play(Write(definicion), run_time=1.5)
   self.wait(D_S03 - 0.6 - 1.5)  # 8.964
   ```
   **NO hacer `wait` silencioso entre `add_sound`. Todo FadeOut cuenta dentro del siguiente D_Sxx.**

5. **Timeline canónico 1.1:**
   ```
   0.000-9.096   s01 Intro
   9.096-18.792  s02 Problema
   18.792-29.856 s03 Definición
   29.856-41.736 s04 Ejemplos SÍ (Colombia V / 2+2=5 F)
   41.736-54.408 s05 Ejemplos NO (¿Cómo estás? / x+3=10) <- aquí estaba el desfase bug
   54.408-67.608 s06 Clasificación Simple vs Compuesta
   67.608-75.888 s07 Relevancia if(true)
   75.888-79.26  Cierre silencioso (3.3s)
   ```
   Verificado: `ffprobe` da 79.26 video, 75.90 audio, cierre 3.3s.

**Para próximos videos (1.2, 1.3...):** Repetir 1-5. Generar nuevos s08.. con `generar_voz.py`, concatenar a `combined_12.mp3`, usar `self.add_sound(COMBINED_12)` y calibrar `D_Sxx`.

---

## 6. ESTRUCTURA ORDENADA

| Video | Subtema | Archivo | Estado |
|-------|---------|---------|--------|
| 1.1 | ¿Qué es proposición? `logica:6` | `escenas_modulo1_sync.py:Escene11_SYNC` | ✅ 79s SYNC |
| 1.2 | NOT, AND, OR `logica:20` | pendiente | ⏳ |
| 1.3 | Implicación `logica:46` | pendiente | ⏳ |
| 1.4 | Leyes/Familia/Negación `logica:83` | pendiente | ⏳ |
| 1.5 | Cuantificadores `logica:190` | pendiente | ⏳ |

**NO saltar.** Hacer 1.2 solo tras validar 1.1 SYNC con usuario.

---

## 7. INSTRUCCIONES SIGUIENTE AGENTE

1. Leer este PROMPT + `00_PLAN.md` + fuentes `.md` + `escenas_modulo1_sync.py`
2. Verificar `ffprobe` durations vs `D_Sxx` en código
3. Reproducir `media/videos/escenas_modulo1_sync/480p15/Escena11_Proposicion_SYNC.mp4` y validar que al decir "ninguna de las dos es proposición" aún están las 4 tarjetas visibles, y "Hay dos tipos" aparece JUSTO después.
4. Si OK, generar 1.2 con mismo workflow single-combined-audio.
5. Si el usuario pide cambio de voz/velocidad: editar `generar_voz.py:VOICE` y `RATE`, regenerar.

## 8. REVISIÓN 2026-08-27

- Bug reportado: audio cortado y mute, desync s05->s06
- Root cause: múltiples `add_sound` en t=0 + FadeOut silencioso entre segmentos
- Fix: single `combined_11.mp3` + waits calibrados
- Documentado en `animaciones/modulo1/README_VOZ.md` y aquí sección 5
