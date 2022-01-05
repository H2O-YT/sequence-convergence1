#All image, except the logo, are renderized with Manim
from manim import *


class GeometricGraph(Scene):
    def construct(self):
        ax = NumberPlane(x_range = [-1.0, config.frame_width-1.0, 1],
        y_range = [-0.1, 1.1, 0.1], y_length=config.frame_height)
        x_labels = VGroup(*[MathTex(str(x)).next_to(ax.c2p(x, 0), DOWN) for x in range(1, int(np.ceil(config.frame_width-1.0)))])
        y_labels = VGroup(*[MathTex(str(y/10)).next_to(ax.c2p(0, y/10), LEFT) for y in range(1, 10)], MathTex(str(1)).next_to(ax.c2p(0, 1), LEFT))
        x_values = [x for x in range(1, int(np.ceil(config.frame_width-1.0)))]
        y_values = [(1/2)**x for x in x_values]
        dots = VGroup(*[Dot(ax.c2p(x_value, y_value), color = YELLOW) for x_value, y_value in zip(x_values, y_values)])
        text = Tex("It seems the sequence converges to 0")
        ellipse = Ellipse(color = BLUE_D, width = text.width+1.5, height = text.height+1.5, fill_color = BLACK, fill_opacity = 1.0)
        self.add(ax, dots, x_labels, y_labels, ellipse, text)