from manim import *

class TelegramAd(Scene):
    def construct(self):
        tg = SVGMobject("Telegram_logo.svg")
        tg.scale(2)
        tg.set_stroke("#1d93d2", 2)

        text = Text("Підписуйтесь на Telegram", font_size=36, font="Arial")
        text.next_to(tg, DOWN, buff=0.5)

        text2 = Text("@chE_pUhaaa",font_size = 48)
        text2.next_to(text, UP, buff=0.35)

        # Додаємо зображення
        pose4 = ImageMobject("pose4_left.png").scale(1.2)
        pose8 = ImageMobject("pose8.png").scale(1.2)

        # Початкові позиції: під логотипом, зменшена прозорість, трохи повернуті
        pose4.move_to(tg.get_center() + UP * 1.4)
        pose4.set_z_index(tg.z_index - 1)
        pose4.set_opacity(0)
        pose4.scale(0.18)

        pose8.move_to(tg.get_center() + UP * 1.4)
        pose8.set_z_index(tg.z_index - 1)
        pose8.set_opacity(0)
        pose8.scale(0.18)

        self.add(pose4, pose8)
        # Анімація виходу з-під логотипа

        self.play(DrawBorderThenFill(tg, run_time=0.5))
        self.play(tg.animate.shift(UP * 1), run_time=0.2)
        self.play(
            Write(text),
            Write(text2),            
            pose4.animate.shift(LEFT * 2.5).rotate(45 * DEGREES).set_opacity(1),
            pose8.animate.shift(RIGHT * 2.5).rotate(-45 * DEGREES).set_opacity(1),
            run_time=0.5
        )

        self.wait(2)


