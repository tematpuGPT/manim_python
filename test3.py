from manim import *

class LoveScene(Scene):
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

        # Заставляем буквы танцевать
        for letter in letters:
            self.play(letter.animate.rotate(PI/2).scale(1.5), run_time=0.5)
            self.play(letter.animate.rotate(-PI/2).scale(0.67), run_time=0.5)

        # Собираем буквы в одну точку
        self.play(letters.animate.arrange_in_grid(rows=1, buff=0.1))
        self.wait()

        # Показываем большое сердечко
        heart = Heart(color=RED)
        heart.scale(2)
        self.play(FadeOut(letters), FadeIn(heart))
        self.wait()