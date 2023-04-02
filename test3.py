from manim import *
from manim.mobject.geometry import QuadraticBezier
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
        
        # Создаем кардиоиду с помощью параметрических уравнений
        cardioid = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t) - np.cos(2 * t),
                2 * np.sin(t) - np.sin(2 * t),
                0
            ]), t_min=0, t_max=TAU, color=RED
        )
        # Заливаем кардиоиду красным цветом
        cardioid.set_fill(color=RED, opacity=1)
        
        # Масштабируем и перемещаем кардиоиду над буквами
        cardioid.scale(0.5).shift(UP*2)

        # Показываем сердце на экране
        self.play(FadeIn(cardioid))
