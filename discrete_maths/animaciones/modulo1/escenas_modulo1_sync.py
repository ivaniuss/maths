from manim import *
import pathlib

config.background_color = "#FDF6E3"
INK = "#2C3E50"
ACCENT_BLUE = "#2980B9"
ACCENT_ORANGE = "#E67E22"
ACCENT_GREEN = "#27AE60"
ACCENT_RED = "#C0392B"
GRAY_SOFT = "#7F8C8D"

VOICE_DIR = pathlib.Path(__file__).parent / "voiceovers"
COMBINED = str(VOICE_DIR / "combined_11.mp3")

# Duraciones medidas con ffprobe
D_S01 = 9.096
D_S02 = 9.696
D_S03 = 11.064
D_S04 = 11.88
D_S05 = 12.672
D_S06 = 13.2
D_S07 = 8.28

class Escena11_Proposicion_SYNC(Scene):
    """
    VIDEO 1.1 SINCRONIZADO - single combined audio
    Timeline exacto: s01 0-9.09, s02 9.09-18.79, s03 18.79-29.85, s04 29.85-41.73, s05 41.73-54.40, s06 54.40-67.60, s07 67.60-75.88
    """
    def construct(self):
        # Añadir audio combinado UNA sola vez al inicio - sin cortes
        self.add_sound(COMBINED)

        title = Text("¿Qué es una proposición?", font_size=44, color=INK, weight=BOLD).to_edge(UP, buff=0.5)
        underline = Line(LEFT*3.5, RIGHT*3.5, color=ACCENT_BLUE, stroke_width=4).next_to(title, DOWN, buff=0.15)

        # --- S01 (0.0 - 9.096): Intro ---
        # Animaciones dentro de S01: title 2.0 + problema 1.0 = 3.0, resto espera
        self.play(Write(title), Create(underline), run_time=2.0)
        problema = VGroup(
            Text("Antes de la lógica formal,", font_size=22, color=GRAY_SOFT),
            Text("el lenguaje era ambiguo.", font_size=22, color=GRAY_SOFT),
            Text("¿Cómo ponerse de acuerdo", font_size=20, color=INK),
            Text("sobre qué es verdad?", font_size=20, color=INK),
        ).arrange(DOWN, buff=0.08).to_edge(LEFT, buff=1).shift(UP*1.4)
        self.play(FadeIn(problema, shift=DOWN*0.2), run_time=1.0)
        self.wait(D_S01 - 2.0 - 1.0)  # 6.096

        # --- S02 (9.096 - 18.792 = 9.696): Frases ambiguas ---
        ambiguas = VGroup(
            Text('"¡Qué alto es!"', font_size=18, color=GRAY_SOFT, slant=ITALIC),
            Text('"Ojalá llueva"', font_size=18, color=GRAY_SOFT, slant=ITALIC),
            Text('"¿Cómo estás?"', font_size=18, color=GRAY_SOFT, slant=ITALIC),
        ).arrange(DOWN, buff=0.12).next_to(problema, DOWN, buff=0.35)
        ambiguas_box = SurroundingRectangle(ambiguas, color=ACCENT_RED, buff=0.25, corner_radius=0.2, stroke_width=2, stroke_opacity=0.6)
        ambiguas_label = Text("¿Verdadero o falso?  No se puede saber", font_size=14, color=ACCENT_RED).next_to(ambiguas_box, DOWN, buff=0.15)
        filtro = Text("Necesitamos un filtro: solo frases con valor fijo V / F", font_size=18, color=ACCENT_BLUE, weight=BOLD).to_edge(DOWN, buff=0.7)
        arrow = Arrow(ambiguas_box.get_bottom(), filtro.get_top(), color=ACCENT_BLUE, buff=0.2, stroke_width=4)

        # Dentro de S02: ambiguas 1.2 + label 0.5 + arrow/filtro 0.8 = 2.5
        self.play(Write(ambiguas), Create(ambiguas_box), run_time=1.2)
        self.play(FadeIn(ambiguas_label, shift=UP*0.05), run_time=0.5)
        self.wait(1.5)
        self.play(Create(arrow), Write(filtro), run_time=0.8)
        self.wait(D_S02 - 1.2 - 0.5 - 1.5 - 0.8)  # 5.696

        # Transición a S03: limpiar DURANTE el inicio de S03 no aquí, sino que el wait de S02 ya consumió todo s02
        # Hacemos fadeout rápido que se solapa con inicio de s03 pero lo contamos dentro de s03
        # Para mantener sync, el fadeout debe estar DENTRO de s03, no entre medias
        # Así que lo hacemos justo antes de s03 pero sin wait extra: lo animamos en 0.6s al inicio de s03

        # --- S03 (18.792 - 29.856 = 11.064): Definición ---
        # Fadeout previo + definicion
        self.play(
            FadeOut(ambiguas), FadeOut(ambiguas_box), FadeOut(ambiguas_label),
            FadeOut(arrow), FadeOut(problema), FadeOut(filtro),
            run_time=0.6
        )
        definicion = VGroup(
            Text("Definición:", font_size=26, color=ACCENT_BLUE, weight=BOLD),
            Text("Oración declarativa que ES", font_size=20, color=INK),
            Text("necesariamente V o F,", font_size=20, color=INK),
            Text("nunca ambas al mismo tiempo.", font_size=16, color=GRAY_SOFT),
        ).arrange(DOWN, buff=0.08).move_to(UP*1.5)
        self.play(Write(definicion), run_time=1.5)
        # Resto de s03
        self.wait(D_S03 - 0.6 - 1.5)  # 8.964

        # --- S04 (29.856 - 41.736 = 11.88): Ejemplos SÍ ---
        card1 = RoundedRectangle(width=3.4, height=1.1, corner_radius=0.15, stroke_color=INK, stroke_width=2, fill_color=WHITE, fill_opacity=1).move_to(LEFT*3.2 + UP*0.3)
        txt1 = Text('"Colombia está en Sudamérica"', font_size=13, color=INK).move_to(card1.get_center()+UP*0.22)
        sello1 = VGroup(Circle(radius=0.26, color=ACCENT_GREEN, fill_opacity=0.15, stroke_width=3), Text("V", font_size=20, color=ACCENT_GREEN, weight=BOLD))
        sello1.move_to(card1.get_center()+DOWN*0.25)
        lbl1 = Text("✓ Proposición (Verdadera)", font_size=11, color=ACCENT_GREEN).next_to(card1, DOWN, buff=0.08)
        g1 = VGroup(card1, txt1, sello1, lbl1)

        card2 = RoundedRectangle(width=3.4, height=1.1, corner_radius=0.15, stroke_color=INK, stroke_width=2, fill_color=WHITE, fill_opacity=1).move_to(RIGHT*3.2 + UP*0.3)
        txt2 = Text('"2 + 2 = 5"', font_size=15, color=INK).move_to(card2.get_center()+UP*0.22)
        sello2 = VGroup(Circle(radius=0.26, color=ACCENT_ORANGE, fill_opacity=0.15, stroke_width=3), Text("F", font_size=20, color=ACCENT_ORANGE, weight=BOLD))
        sello2.move_to(card2.get_center()+DOWN*0.25)
        lbl2 = Text("✓ Proposición (Falsa)", font_size=11, color=ACCENT_ORANGE).next_to(card2, DOWN, buff=0.08)
        g2 = VGroup(card2, txt2, sello2, lbl2)

        nota = Text("¡Ser falsa no la descalifica!", font_size=13, color=ACCENT_ORANGE, weight=BOLD).next_to(card2, UP, buff=0.12)

        # s04 desglose: g1 0.8+0.5=1.3, wait 1.0, g2 0.8+0.5=1.3, nota 0.4, wait 1.2, resto
        self.play(FadeIn(g1[0], shift=UP*0.1), Write(g1[1]), run_time=0.8)
        self.play(FadeIn(g1[2]), FadeIn(g1[3]), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(g2[0], shift=UP*0.1), Write(g2[1]), run_time=0.8)
        self.play(FadeIn(g2[2]), FadeIn(g2[3]), run_time=0.5)
        self.play(FadeIn(nota, shift=DOWN*0.05), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(nota), run_time=0.3)
        # Resto de s04
        self.wait(D_S04 - 0.8 -0.5 -1.0 -0.8 -0.5 -0.4 -1.2 -0.3)  # 11.88-5.5=6.38

        # --- S05 (41.736 - 54.408 = 12.672): Ejemplos NO ---
        card3 = RoundedRectangle(width=3.4, height=1.1, corner_radius=0.15, stroke_color=INK, stroke_width=2, fill_color=WHITE, fill_opacity=1).move_to(LEFT*3.2 + DOWN*1.8)
        txt3 = Text('"¿Cómo estás?"', font_size=15, color=INK).move_to(card3.get_center()+UP*0.22)
        sello3 = Text("✗", font_size=28, color=ACCENT_RED, weight=BOLD).move_to(card3.get_center()+DOWN*0.25)
        lbl3 = Text("✗ NO es proposición", font_size=11, color=ACCENT_RED).next_to(card3, DOWN, buff=0.08)
        g3 = VGroup(card3, txt3, sello3, lbl3)

        card4 = RoundedRectangle(width=3.4, height=1.1, corner_radius=0.15, stroke_color=INK, stroke_width=2, fill_color=WHITE, fill_opacity=1).move_to(RIGHT*3.2 + DOWN*1.8)
        txt4 = Text('"x + 3 = 10"', font_size=15, color=INK).move_to(card4.get_center()+UP*0.22)
        sello4 = Text("✗", font_size=28, color=ACCENT_RED, weight=BOLD).move_to(card4.get_center()+DOWN*0.25)
        lbl4 = Text("✗ NO es proposición", font_size=11, color=ACCENT_RED).next_to(card4, DOWN, buff=0.08)
        g4 = VGroup(card4, txt4, sello4, lbl4)

        expl = VGroup(
            Text('"¿Cómo estás?" es pregunta, no declarativa', font_size=12, color=INK),
            Text('"x+3=10" depende de x → sin valor fijo', font_size=12, color=INK),
        ).arrange(DOWN, buff=0.05).to_edge(DOWN, buff=0.35)
        expl_box = SurroundingRectangle(expl, color=ACCENT_RED, buff=0.15, corner_radius=0.1, stroke_width=1.2, stroke_opacity=0.5)

        self.play(FadeIn(g3[0], shift=UP*0.1), Write(g3[1]), run_time=0.7)
        self.play(FadeIn(g3[2]), FadeIn(g3[3]), run_time=0.4)
        self.wait(1.2)
        self.play(FadeIn(g4[0], shift=UP*0.1), Write(g4[1]), run_time=0.7)
        self.play(FadeIn(g4[2]), FadeIn(g4[3]), run_time=0.4)
        self.play(Create(expl_box), Write(expl), run_time=0.6)
        # Aquí es donde decías que se descuadra: este wait debe mantener las tarjetas visibles
        # mientras dice "ninguna de las dos es proposición" (final de s05)
        self.wait(D_S05 - 0.7 -0.4 -1.2 -0.7 -0.4 -0.6)  # 12.672-4.0=8.672

        # --- S06 (54.408 - 67.608 = 13.2): Clasificación ---
        # Transición: limpiar tarjetas pero DURANTE s06, no antes
        self.play(
            FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(g4),
            FadeOut(expl), FadeOut(expl_box), FadeOut(definicion),
            run_time=0.6
        )
        clasif_title = Text("Dos tipos:", font_size=26, color=INK, weight=BOLD).to_edge(UP, buff=1.2)
        self.play(Write(clasif_title), run_time=0.8)

        simple = VGroup(
            RoundedRectangle(width=3.8, height=1.6, corner_radius=0.12, stroke_color=ACCENT_BLUE, stroke_width=3, fill_color=WHITE, fill_opacity=1),
            Text("SIMPLE (Atómica)", font_size=15, color=ACCENT_BLUE, weight=BOLD),
            Text('p = "Está lloviendo"', font_size=14, color=INK),
            Text("Una sola idea", font_size=11, color=GRAY_SOFT),
        )
        simple[1].move_to(simple[0].get_center()+UP*0.38)
        simple[2].move_to(simple[0].get_center()+DOWN*0.02)
        simple[3].move_to(simple[0].get_center()+DOWN*0.42)
        simple.move_to(LEFT*3 + DOWN*0.2)

        compuesta = VGroup(
            RoundedRectangle(width=3.8, height=1.6, corner_radius=0.12, stroke_color=ACCENT_ORANGE, stroke_width=3, fill_color=WHITE, fill_opacity=1),
            Text("COMPUESTA (Molecular)", font_size=14, color=ACCENT_ORANGE, weight=BOLD),
            Text('"Llueve Y hace frío"', font_size=13, color=INK),
            Text("p  ∧  q", font_size=20, color=INK),
        )
        compuesta[1].move_to(compuesta[0].get_center()+UP*0.38)
        compuesta[2].move_to(compuesta[0].get_center()+DOWN*0.02)
        compuesta[3].move_to(compuesta[0].get_center()+DOWN*0.42)
        compuesta.move_to(RIGHT*3 + DOWN*0.2)

        arrow2 = Arrow(simple.get_right(), compuesta.get_left(), color=GRAY_SOFT, buff=0.2, stroke_width=3)
        conector = Text("+ conectores →", font_size=14, color=GRAY_SOFT).next_to(arrow2, UP, buff=0.05)

        self.play(FadeIn(simple, shift=RIGHT*0.15), run_time=0.7)
        self.wait(1.2)
        self.play(Create(arrow2), Write(conector), run_time=0.5)
        self.play(FadeIn(compuesta, shift=LEFT*0.15), run_time=0.7)
        # Resto de s06
        self.wait(D_S06 - 0.6 -0.8 -0.7 -1.2 -0.5 -0.7)  # 13.2-4.5=8.7

        self.play(FadeOut(clasif_title), FadeOut(simple), FadeOut(compuesta), FadeOut(arrow2), FadeOut(conector), run_time=0.5)
        # Este fadeout de 0.5 lo restamos de s07, por eso s07 wait será menor

        # --- S07 (67.608 - 75.888 = 8.28): Relevancia ---
        # Ya consumimos 0.5 del fadeout, quedan 7.78
        relevancia = VGroup(
            Text("Relevancia hoy:", font_size=16, color=GRAY_SOFT),
            Text("Esto es el bit 0 / 1 de tu código", font_size=22, color=INK, weight=BOLD),
            VGroup(
                RoundedRectangle(width=5.8, height=1.0, corner_radius=0.08, stroke_color=INK, stroke_width=2, fill_color="#2C3E50", fill_opacity=1),
                Text('if (proposicion == true) { ... }', font_size=16, color=WHITE, font="Monospace"),
            )
        ).arrange(DOWN, buff=0.2).move_to(DOWN*0.8)
        relevancia[2][1].move_to(relevancia[2][0].get_center())

        self.play(Write(relevancia[0]), Write(relevancia[1]), run_time=0.8)
        self.play(FadeIn(relevancia[2], shift=UP*0.05), run_time=0.6)
        self.wait(D_S07 - 0.5 - 0.8 - 0.6)  # 8.28-1.9=6.38

        # Cierre post-narración
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        cierre = VGroup(
            Text("Módulo 1.1 completo", font_size=18, color=GRAY_SOFT),
            Text("Siguiente: ¿Cómo combinarlas?", font_size=26, color=ACCENT_BLUE, weight=BOLD),
            Text("NOT, AND, OR  →  los ladrillos", font_size=16, color=INK),
        ).arrange(DOWN, buff=0.12).move_to(ORIGIN)
        self.play(Write(cierre), run_time=1.2)
        self.wait(1.5)
