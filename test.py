from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        
class ColumnMultiplication(Scene):
    def construct(self):
        # Создаем объекты для чисел и знака умножения
        num1 = Integer(1032).set_color(YELLOW)
        num2 = Integer(2323).set_color(BLUE)
        mul = MathTex("\\times").set_color(WHITE)
        # Располагаем их на сцене
        num1.next_to(mul, LEFT, buff=0.5)
        num2.next_to(mul, RIGHT, buff=0.5)
        group = VGroup(num1, mul, num2).move_to(UP * 2)
        # Показываем числа и знак умножения
        self.play(Write(group))
        self.wait()
        
        # # Создаем объекты для промежуточных результатов
        # res1 = Integer(num1.get_value() * (num2.get_value() % 10)).set_color(GREEN) # 1032 * 3
        # res2 = Integer(num1.get_value() * ((num2.get_value() // 10) % 10)).set_color(GREEN) # 1032 * 20
        # res3 = Integer(num1.get_value() * ((num2.get_value() // 100) % 10)).set_color(GREEN) # 1032 * 200
        # res4 = Integer(num1.get_value() * (num2.get_value() // 1000)).set_color(GREEN) # 1032 * 2000
        # # Располагаем их на сцене под числами
        # res1.next_to(num2, DOWN, buff=0.5).align_to(num1, RIGHT)
        # res2.next_to(res1, DOWN, buff=0.5).shift(RIGHT * 0.5)
        # res3.next_to(res2, DOWN, buff=0.5).shift(RIGHT * 0.5)
        # res4.next_to(res3, DOWN, buff=0.5).shift(RIGHT * 0.5)
        
        # # Показываем промежуточные результаты по одному с анимацией перемножения цифр
        # for i in range(4):
            # digit = num2[i] # цифра из второго числа
            # line = Line(digit.get_center(), num1.get_center(), color=RED) # линия от цифры к первому числу
            # self.play(Create(line)) # показываем линию
            # self.play(TransformMatchingShapes(line.copy(), res4[i])) # превращаем копию линии в соответствующий результат
            # self.play(FadeOut(line), Write(res4[i])) # убираем линию и показываем результат
            # self.wait()
            
        # # Показываем знак плюс между промежуточными результатами
        # plus1 = MathTex("+").next_to(res1, LEFT, buff=0.2)
        # plus2 = MathTex("+").next_to(res2, LEFT, buff=0.2)
        # plus3 = MathTex("+").next_to(res3, LEFT, buff=0.2)
        # self.play(Write(plus1), Write(plus2), Write(plus3))
        # self.wait()
        
        # # Создаем объект для окончательного результата
        # final = Integer(num1.get_value() * num2.get_value()).set_color(ORANGE) # 1032 * 2323
        # final.next_to(res4, DOWN, buff=0.5).align_to(num1, LEFT)
        
        # # Показываем горизонтальную линию под промежуточными результатами
        # hline = Line(num1.get_left(), res4.get_right(), color=WHITE)
        # hline.next_to(res4, DOWN, buff=0.2)
        # self.play(Create(hline))
        # self.wait()
        
        # # Показываем окончательный результат с анимацией сложения промежуточных результатов
        # self.play(
            # TransformMatchingShapes(res1.copy(), final[0:4]), # превращаем копию первого результата в первые четыре цифры окончательного
            # TransformMatchingShapes(res2.copy(), final[1:5]), # превращаем копию второго результата в вторые четыре цифры окончательного
            # TransformMatchingShapes(res3.copy(), final[2:6]), # превращаем копию третьего результата в третьи четыре цифры окончательного
            # TransformMatchingShapes(res4.copy(), final[3:7]), # превращаем копию четвертого результата в четвертые четыре цифры окончательного
            # run_time=2 # устанавливаем время анимации в 2 секунды
        # )
        # self.play(Write(final)) # показываем окончательный результат
        # self.wait()