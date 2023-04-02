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

        # Заставляем буквы танцевать в хороводе
        self.play(Rotate(letters, angle=PI/2, about_point=ORIGIN), run_time=1)
        self.play(Rotate(letters, angle=-PI/2, about_point=ORIGIN), run_time=1)

        # Собираем буквы в одну точку
        self.play(letters.animate.arrange_in_grid(rows=1, buff=0.1))
        self.wait()

        # Создаем два круга и треугольник
        circle1 = Circle(color=RED, fill_opacity=1)
        circle2 = Circle(color=RED, fill_opacity=1)
        triangle = Triangle(color=RED, fill_opacity=1)

        # Сдвигаем их так чтобы они образовывали сердце
        circle1.shift(UP*0.5 + LEFT*0.5)
        circle2.shift(UP*0.5 + RIGHT*0.5)
        triangle.rotate(-PI/2 + PI/6)
        triangle.shift(DOWN*0.8)
        #triangle.shift(RIGHT*(np.sqrt(3)/2 - np.cos(PI/6)))
        #triangle.shift(RIGHT*0.2)
        triangle.shift(RIGHT*(np.sqrt(3)/2 - np.cos(PI/6) - triangle.get_critical_point(ORIGIN)[0]))
        # Объединяем их в один объект
        heart = VGroup(circle1, circle2, triangle)

        # Показываем сердце
        self.play(FadeOut(letters), FadeIn(heart))
        self.wait()