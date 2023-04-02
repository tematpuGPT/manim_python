from manim import *

class HeartScene(Scene):
    def construct(self):
        # Создаем два слова
        artem = Text("Артём")
        yulia = Text("Юля")

        # Располагаем их на сцене
        artem.to_edge(LEFT)
        yulia.to_edge(RIGHT)

        # Показываем слова
        self.play(Write(artem), Write(yulia))
        self.wait()

        # Приближаем их друг к другу
        self.play(artem.animate.shift(RIGHT*3), yulia.animate.shift(LEFT*3))
        self.wait()

        # Распадаем их на буквы
        letters = VGroup(*artem, *yulia)
        self.play(letters.animate.space_out_submobjects(0.5))
        self.wait()

        # Заставляем буквы танцевать в хороводе
        self.play(Rotate(letters, angle=PI/2, about_point=ORIGIN), run_time=1)
        self.play(Rotate(letters, angle=-PI/2, about_point=ORIGIN), run_time=1)

        # Собираем буквы в одну точку
        self.play(letters.animate.arrange_in_grid(rows=1, buff=0.1))
        self.wait()

        # Создаем две квадратичные кривые Безье
        curve1 = QuadraticBezier([UP*2 + LEFT*2, UP*3 + RIGHT*2, DOWN*2 + RIGHT*2])
        curve2 = QuadraticBezier([DOWN*2 + RIGHT*2, DOWN*3 + LEFT*2, UP*2 + LEFT*2])

        # Объединяем их в один объект
        heart = VGroup(curve1, curve2)

        # Заливаем его красным цветом
        heart.set_fill(color=RED, opacity=1)

        # Показываем сердце
        self.play(FadeOut(letters), FadeIn(heart))
        self.wait()
