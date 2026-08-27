# Workflow VOZ - Corregido 2026-08-27

**Problema detectado:** `Scene.add_sound()` sin `time_offset` pone todos los audios en t=0, se pisan y luego queda mute.

**Solución correcta (usada para FIXED):**
1. Generar audios con edge-tts: `generar_voz.py` -> `voiceovers/s01_*.mp3` (es-CO-GonzaloNeural)
2. Concatenar: `ffmpeg -f concat -i concat.txt -c copy combined_11.mp3` (75.88s)
3. Renderizar video SIN audio (solo animación con waits calibrados a duración de voz)
4. Muxear al final: `ffmpeg -i video_only.mp4 -i combined_11.mp3 -filter:v tpad... -c:v libx264 -c:a aac FIXED.mp4`

**Videos:**
- `Escena11_Proposicion_VO.mp4` (BUG: audio pisado, 72s)
- `Escena11_Proposicion_VO_FIXED.mp4` (OK: 75.8s, audio continuo, sin cortes)

**Para el próximo agente:** NO usar `self.add_sound()` por segmento. Usar workflow de concatenación + mux final.
