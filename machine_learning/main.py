from manim import *
import numpy as np

class SupervisedLearning(Scene):
    def construct(self):


        hackwhiz_pose7 = ImageMobject("media/images/main/pose7.png")
        hackwhiz_pose7.scale(0.5)
        hackwhiz_pose7.z_index = -1
        # Create the supervised learning text
        supervised_text = Text("Supervised Learning", font_size=72)

        # Create the regression and classification texts
        regression_text = Text("Регресія", font_size=48)
        regression_text.next_to(supervised_text, DOWN + LEFT, buff=-1)

        classification_text = Text("Класифікація", font_size=48)
        classification_text.next_to(supervised_text, DOWN + RIGHT, buff=-2)

        # Create arrows to connect the texts
        arrow_width = 2  # Desired arrow thickness

        # Дані для точок
        x_vals = np.linspace(-4, 4, 8)
        y_vals = 2.4 * x_vals + 4 + np.random.normal(0, 1, size=x_vals.shape)  # шум

        # Створюємо координатну сітку
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 10, 2],
            x_length=10,
            y_length=5,
            tips=False,
        ).set_opacity(0.2).scale(1.2).to_edge(DOWN, buff=1)

        # Основна лінія регресії
        regression_line = axes.plot(
            lambda x: 1.2 * x + 2,
            x_range=[-5, 5],
            color=BLUE,
            stroke_width=8,
        ).set_opacity(0.5)

        # Точки
        dots = VGroup(*[
            Dot(axes.c2p(x, y), color=YELLOW, radius=0.15).set_opacity(0.7)
            for x, y in zip(x_vals, y_vals)
        ])

        # Лінії від точок до регресійної лінії
        error_lines = VGroup()
        for x, y in zip(x_vals, y_vals):
            y_pred = 1.2 * x + 2
            line = DashedLine(
                axes.c2p(x, y), axes.c2p(x, y_pred),
                color=RED, stroke_width=4, dash_length=0.15
            ).set_opacity(0.5)
            error_lines.add(line)

        mse_plot_group = VGroup(axes, regression_line, dots, error_lines).scale(1.2).set_z_index(-1)
        mse_plot_group.move_to(ORIGIN)


        hackwhiz_pose7.set_opacity(0.2)
        # Add all elements to the scene
        self.play(Write(supervised_text), FadeIn(hackwhiz_pose7, shift=UP))
        self.play(hackwhiz_pose7.animate.scale(0.5).set_opacity(1).to_edge(DOWN).shift(DOWN*1.5))
        self.play(supervised_text.animate.to_edge(UP))

        regression_arrow = Arrow(supervised_text.get_bottom(), regression_text.get_top(), buff=0.3, stroke_width=arrow_width)
        classification_arrow = Arrow(supervised_text.get_bottom(), classification_text.get_top(), buff=0.3, stroke_width=arrow_width)

        self.play(Create(regression_arrow), Write(regression_text))
        self.play(Create(classification_arrow), Write(classification_text))

        self.wait(1)

        # Position the main text at the top
        self.play(FadeOut(supervised_text, regression_arrow, classification_arrow, classification_text), hackwhiz_pose7.animate.shift(DOWN * 8), FadeOut(hackwhiz_pose7))

        self.play(regression_text.animate.move_to(ORIGIN))

        self.play(regression_text.animate.to_edge(UP))

        linear_regression_formula = MathTex("\\hat{y} = w \\times x + b", font_size=72)

        linear_regression_text = Text("Лінійна регресія", font_size=36)
        linear_regression_text.next_to(linear_regression_formula, DOWN, buff=0.5)

        self.play(Write(linear_regression_formula), Write(axes), Write(regression_line))
        self.play(Write(linear_regression_text))

        self.wait(2)

        self.play(FadeOut(linear_regression_formula))
        self.play(FadeOut(regression_text), linear_regression_text.animate.to_edge(UP))

        mse_loss_formula = MathTex("MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2", font_size=72)
        mse_loss_text = Text("MSE Loss - основна функція втрат", font_size=36)

        # --- Додаємо великий напівпрозорий plot на фон ---

        mse_loss_text.next_to(mse_loss_formula, DOWN, buff=0.5)
        
        self.play(Write(mse_loss_formula), Write(dots), Write(error_lines))
        self.play(Write(mse_loss_text))

        self.wait(2)

        self.play(FadeOut(mse_loss_formula, mse_loss_text, linear_regression_text, mse_plot_group))

        classification_text2 = Text("Класифікація", font_size=72)

        self.play(Write(classification_text2))

        self.play(classification_text2.animate.scale(0.5))
        self.play(classification_text2.animate.to_edge(UP))


        logistic_regression_text = Text("Логістична регресія", font_size=36)
        logistic_regression_formula = MathTex("P(y=1|x) = \\sigma(w^T x + b)", font_size=72)

        logistic_regression_text.next_to(logistic_regression_formula, DOWN, buff=0.5)

        # Додаємо напівпрозорий sigmoid plot на фон
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=5,
            tips=False,
        ).set_opacity(0.2).scale(1.2).to_edge(DOWN, buff=1)

        sigmoid_curve = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            x_range=[-6, 6],
            color=rgba_to_color((0.2, 0.6, 0.8, 0.1)),
            stroke_width=10,
        )
        # Групуємо для зручності
        sigmoid_group = VGroup(axes, sigmoid_curve).scale(1.5).set_z_index(-1)
        sigmoid_group.move_to(ORIGIN)

        logistic_regression_text.next_to(logistic_regression_formula, DOWN, buff=0.5)

        self.play(Write(logistic_regression_formula), Write(sigmoid_group))
        self.play(Write(logistic_regression_text))

        self.wait(16)

        self.play(FadeOut(classification_text2, logistic_regression_formula, sigmoid_group), logistic_regression_text.animate.to_edge(UP))

        log_loss_formula = MathTex("L(y, \\hat{y}) = -y [\\log(\\hat{y}) - (1-y) \\log(1-\\hat{y})]", font_size=72)
        log_loss_text = Text("Log Loss - основна функція втрат", font_size=36)
        log_loss_text.next_to(log_loss_formula, DOWN, buff=0.5)

        self.play(Write(log_loss_formula))
        self.play(Write(log_loss_text))

        self.wait(2)

        self.play(FadeOut(log_loss_formula, log_loss_text, logistic_regression_text))

