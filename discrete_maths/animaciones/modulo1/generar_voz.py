#!/usr/bin/env python3
import subprocess, pathlib, json

VOICE = "es-CO-GonzaloNeural"  # Voz colombiana masculina, friendly
RATE = "+0%"  # puedes poner -5% para más pausado
VOICE_DIR = pathlib.Path(__file__).parent / "voiceovers"
VOICE_DIR.mkdir(exist_ok=True)

# Guion Escena 1.1 - first-principles, 7 segmentos
segmentos = [
    ("s01_intro", "¿Qué es una proposición? Antes de la lógica formal, el lenguaje humano era ambiguo. No podíamos ponernos de acuerdo sobre qué era verdad."),
    ("s02_problema", "Frases como ¡Qué alto es!, o ¿Cómo estás?, suenan bien, pero no puedes decir si son verdaderas o falsas. No sirven para razonar con precisión."),
    ("s03_definicion", "Por eso, necesitamos un filtro. Una proposición es una oración declarativa que es, necesariamente, verdadera o falsa. Nunca ambas al mismo tiempo."),
    ("s04_ejemplos_si", "Por ejemplo, Colombia está en Sudamérica, es verdadera. Y dos más dos igual cinco, es falsa. Pero ambas son proposiciones. Ser falsa no la descalifica."),
    ("s05_ejemplos_no", "En cambio, ¿Cómo estás? no es declarativa, es una pregunta. Y equis más tres igual diez, no tiene valor fijo, depende de cuánto vale equis. Ninguna de las dos es proposición."),
    ("s06_clasificacion", "Hay dos tipos. Las simples, o atómicas, son una sola idea, como p: está lloviendo. Las compuestas, o moleculares, unen ideas con conectores, como llueve y hace frío."),
    ("s07_relevancia", "Y esto es el bit cero y uno de tu código. Cada if en programación es una proposición que la computadora evalúa como verdadera o falsa."),
]

for name, text in segmentos:
    out = VOICE_DIR / f"{name}.mp3"
    # Usamos edge-tts CLI
    cmd = ["edge-tts", "--voice", VOICE, "--rate", RATE, "--text", text, "--write-media", str(out)]
    print(f"Generando {name}...")
    subprocess.run(cmd, check=True)
    # medir duración
    dur = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)],
        capture_output=True, text=True
    ).stdout.strip()
    print(f"  -> {out} ({dur}s)")

print("Listo. Archivos en", VOICE_DIR)
