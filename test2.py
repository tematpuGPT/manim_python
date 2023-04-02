
from manim import *

class Multiplication(Scene):
    def construct(self):
        # Создаем два четырехзначных числа
        num1 = 1234
        num2 = 5678

        # Преобразуем их в строки для удобства
        num1_str = str(num1)
        num2_str = str(num2)

        # Создаем группу из цифр первого числа
        digits1 = VGroup(*[Text(digit) for digit in num1_str])
        # Располагаем их горизонтально с небольшим отступом
        digits1.arrange(buff=0.2)
        # Перемещаем их в верхнюю часть сцены
        digits1.to_edge(UP)

        # Создаем группу из цифр второго числа
        digits2 = VGroup(*[Text(digit) for digit in num2_str])
        # Располагаем их горизонтально с небольшим отступом
        digits2.arrange(buff=0.2)
        # Перемещаем их под первым числом
        digits2.next_to(digits1, DOWN, aligned_edge=RIGHT)

        # Создаем знак умножения
        sign = Text("×")
        # Перемещаем его под вторым числом
        sign.next_to(digits2, LEFT)

        # Создаем горизонтальную линию под знаком умножения
        line = Line(start=sign.get_left(), end=digits2.get_right())
        # Сдвигаем ее немного вниз
        line.shift(DOWN * 0.2)

        # Добавляем все элементы на сцену
        self.add(digits1, digits2, sign, line)

        # Создаем список для хранения промежуточных результатов
        partial_results = []

        # Для каждой цифры второго числа (начиная с последней)
        for i in range(len(num2_str) - 1, -1, -1):
            # Получаем цифру как число
            digit = int(num2_str[i])
            # Умножаем ее на первое число
            partial_result = digit * num1
            # Преобразуем результат в строку для удобства
            partial_result_str = str(partial_result)
            # Создаем группу из цифр результата
            partial_result_digits = VGroup(*[Text(d) for d in partial_result_str])
            # Располагаем их горизонтально с небольшим отступом
            partial_result_digits.arrange(buff=0.2)
            # Перемещаем их под линией с соответствующим сдвигом вправо
            partial_result_digits.next_to(line, DOWN, aligned_edge=RIGHT, buff=0.5)
            partial_result_digits.shift(RIGHT * 0.5 * i)
            # Добавляем результат в список промежуточных результатов
            partial_results.append(partial_result_digits)

            # Для каждой цифры результата (начиная с последней)
            for j in range(len(partial_result_str) - 1, -1, -1):
                # Получаем цифру как текст
                result_digit = partial_result_digits[j]
                # Получаем соответствующие цифры первого и второго числа как тексты
                num1_digit = digits1[-(j + 1) - i]
                num2_digit = digits2[i]
                # Создаем копии этих цифр для анимации перемещения
                num1_digit_copy = num1_digit.copy()
                num2_digit_copy = num2_digit.copy()
                # Добавляем копии на сцену поверх оригинальных цифр
                self.add(num1_digit_copy, num2_digit_copy)
                # Подсвечиваем копии зеленым цветом
                self.play(ApplyMethod(num1_digit_copy.set_color, GREEN), ApplyMethod(num2_digit_copy.set_color, GREEN))
                # Перемещаем копии к цифре результата
                self.play(Transform(num1_digit_copy, result_digit), Transform(num2_digit_copy, result_digit))
                # Удаляем копии с сцены
                self.remove(num1_digit_copy, num2_digit_copy)
                # Показываем цифру результата
                self.play(FadeIn(result_digit))
                # Ждем немного
                self.wait(0.5)

                # Добавляем промежуточный результат на сцену
                self.add(partial_result_digits)
                # Ждем немного
                self.wait(0.5)

                # Если это не последний промежуточный результат
                if i > 0:
                    # Создаем вертикальную линию под промежуточным результатом
                    vertical_line = Line(start=partial_result_digits.get_left(), end=partial_result_digits.get_right())
                    vertical_line.shift(DOWN * 0.2)
                    # Добавляем линию на сцену
                    self.play(Create(vertical_line))
                    # Ждем немного
                    self.wait(0.5)

                # Если это последний промежуточный результат
                else:
                    # Создаем двойную горизонтальную линию под промежуточным результатом
                    double_line = DoubleLine(start=partial_result_digits.get_left(), end=partial_result_digits.get_right())
                    double_line.shift(DOWN * 0.2)
                    # Добавляем линию на сцену
                    self.play(Create(double_line))
                    # Ждем немного
                    self.wait(0.5)

                # Складываем все промежуточные результаты в одно число
                final_result = sum(partial_results)
                # Преобразуем его в строку для удобства
                final_result_str = str(final_result)
                # Создаем группу из цифр итогового результата
                final_result_digits = VGroup(*[Text(d) for d in final_result_str])
                # Располагаем их горизонтально с небольшим отступом
                final_result_digits.arrange(buff=0.2)
                # Перемещаем их под двойной линией с выравниванием по правому краю
                final_result_digits.next_to(double_line, DOWN, aligned_edge=RIGHT, buff=0.5)

                # Для каждой цифры итогового результата (начиная с последней)
                for k in range(len(final_result_str) - 1, -1, -1):
                    # Получаем цифру как текст
                    final_digit = final_result_digits[k]
                    # Получаем соответствующие цифры всех промежуточных результатов как тексты
                    partial_digits = [partial[k] for partial in partial_results]
                    # Создаем копии этих цифр для анимации перемещения
                    partial_digits_copies = [digit.copy() for digit in partial_digits]
                    # Добавляем копии на сцену поверх оригинальных цифр
                    self.add(*partial_digits_copies)
                    # Подсвечиваем копии зеленым цветом
                    self.play(*[ApplyMethod(digit.set_color, GREEN) for digit in partial_digits_copies])
                    # Перемещаем копии к цифре итогового результата
                    self.play(*[Transform(digit, final_digit) for digit in partial_digits_copies])
                    # Удаляем копии с сцены
                    self.remove(*partial_digits_copies)
                    # Показываем цифру итогового результата
                    # Показываем цифру итогового результата
                    self.play(FadeIn(final_digit))
                    # Ждем немного
                    self.wait(0.5)

                    # Добавляем итоговый результат на сцену
                    self.add(final_result_digits)
                    # Ждем немного
                    self.wait(0.5)

                    # Заканчиваем сцену
                    self.play(FadeOut(VGroup(*self.mobjects)))